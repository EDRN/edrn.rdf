# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRNLabcas RDF Generator. An RDF generator that describes EDRN biomarker mutation statistics using Biomuta webservices.
'''

from Acquisition import aq_inner
from edrn.rdf import _
from five import grok
from interfaces import IGraphGenerator
from rdfgenerator import IRDFGenerator
from rdflib.term import URIRef, Literal
from utils import validateAccessibleURL
from zope import schema
from pysolr import Solr
import six

import rdflib

ecasURIPrefix = 'urn:edrn:'
edrnURIPrefix = 'http://edrn.nci.nih.gov/rdf/schema.rdf#'

_edrnlabcasPredicates = {
    u'AnalyticMethods': 'AnalyticMethodsPredicateURI',
    u'AnalyticResults': 'AnalyticResultsPredicateURI',
    u'CollaborativeGroup': 'CollaborativeGroupPredicateURI',
    u'DataCustodian': 'DataCustodianPredicateURI',
    u'DataCustodianEmail': 'DataCustodianEmailPredicateURI',
    u'DataCustodianPhone': 'DataCustodianPhonePredicateURI',
    u'DataDisclaimer': 'DataDisclaimerPredicateURI',
    u'CollectionName': 'DataSetNamePredicateURI',
    u'CollectionDescription': 'DatasetDescriptionPredicateURI',
    u'CollectionId': 'DatasetIdPredicateURI',
    u'sourceurl': 'DatasetURLPredicateURI',
    u'Date': 'DatePredicateURI',
    u'DateDatasetFrozen': 'DateDatasetFrozenPredicateURI',
    u'Description': 'DescriptionPredicateURI',
    u'Discipline': 'DisciplinePredicateURI',
    u'EligibilityCriteria': 'EligibilityCriteriaPredicateURI',
    u'GrantSupport': 'GrantSupportPredicateURI',
    u'InstrumentDetails': 'InstrumentDetailsPredicateURI',
    u'InvestigatorName': 'InvestigatorNamePredicateURI',
    u'LeadPI': 'LeadPIPredicateURI',
    u'LeadPI_fullname': 'LeadPI_fullnamePredicateURI',
    u'MethodDetails': 'MethodDetailsPredicateURI',
    u'PlannedSampleSize': 'PlannedSampleSizePredicateURI',
    u'ProteomicsExperimentType': 'ProteomicsExperimentTypePredicateURI',
    u'ProtocolId': 'ProtocolIDPredicateURI',
    u'PubMedID': 'PubMedIDPredicateURI',
    u'PublishState': 'PublishStatePredicateURI',
    u'RecommendedSoftware': 'RecommendedSoftwarePredicateURI',
    u'ResearchSupport': 'ResearchSupportPredicateURI',
    u'ResultsAndConclusionSummary': 'ResultsAndConclusionSummaryPredicateURI',
    u'InstitutionId': 'SiteIDPredicateURI',
    u'Species': 'SpeciesPredicateURI',
    u'SpecificAims': 'SpecificAimsPredicateURI',
    u'SpecimenType': 'SpecimenTypePredicateURI',
    u'StudyBackground': 'StudyBackgroundPredicateURI',
    u'StudyConclusion': 'StudyConclusionPredicateURI',
    u'StudyDescription': 'StudyDescriptionPredicateURI',
    u'StudyDesign': 'StudyDesignPredicateURI',
    u'StudyId': 'StudyIdPredicateURI',
    u'StudyMethods': 'StudyMethodsPredicateURI',
    u'StudyName': 'StudyNamePredicateURI',
    u'StudyObjective': 'StudyObjectivePredicateURI',
    u'StudyResults': 'StudyResultsPredicateURI',
    u'Technology': 'TechnologyPredicateURI',
    u'Consortium': 'ConsortiumPredicateURI',
    u'AccessGrantedTo': 'AccessGrantedToPredicateURI',
    u'QAState': 'QAStatePredicateURI',
    u'Organ': 'organPredicateURI',
    u'site': 'sitePredicateURI'
}

_graph_obj_mapping = {
    u'ProtocolId': ['protocolPredicateURI', 'http://edrn.nci.nih.gov/data/protocols/'],
    u'InstitutionId': ['sitePredicateURI', 'http://edrn.nci.nih.gov/data/sites/'],
    u'Organ': ['organPredicateURI', 'http://edrn.nci.nih.gov/data/body-systems/']
}


class IEDRNLabcasRDFGenerator(IRDFGenerator):
    '''DMCC Committee RDF Generator.'''
    webServiceURL = schema.TextLine(
        title=_(u'Web Service URL'),
        description=_(u'The Uniform Resource Locator to the DMCC SOAP web service.'),
        required=True,
        constraint=validateAccessibleURL,
        default=u'https://edrn-labcas.jpl.nasa.gov/data-access-api/collections'
    )
    typeURI = schema.TextLine(
        title=_(u'Type URI'),
        description=_(u'Uniform Resource Identifier naming the type of edrnlabcas objects described by this generator.'),
        required=True,
        default=u'urn:edrn:'
    )
    uriPrefix = schema.TextLine(
        title=_(u'URI Prefix'),
        description=_(u'The Uniform Resource Identifier prepended to all edrnlabcas described by this generator.'),
        required=True,
        default=u'https://edrn-labcas.jpl.nasa.gov/labcas-ui/c/index.html?collection_id='
    )
    username = schema.TextLine(
        title=_(u'Username'),
        description=_(u'Username to authenticate with; use a service account if available'),
        required=True,
        default=u'service'
    )
    password = schema.TextLine(
        title=_(u'Password'),
        description=_(u'Password to confirm the identity of the username; this will be visible!'),
        required=True,
    )


class EDRNLabcasGraphGenerator(grok.Adapter):
    '''A graph generator that produces statements about EDRN's science data.'''

    grok.provides(IGraphGenerator)
    grok.context(IEDRNLabcasRDFGenerator)

    def generateGraph(self):
        graph = rdflib.Graph()
        context = aq_inner(self.context)
        solr_conn = Solr(context.webServiceURL, auth=(context.username, context.password))
        solr_response = solr_conn.search('*:*', rows=99999)
        results = {}
        for obj in solr_response:
            if 'sourceurl' not in obj:
                obj['sourceurl'] = context.uriPrefix + obj.get("id")
            results[obj.get("id")] = obj
        graph.bind('edrn', ecasURIPrefix)
        graph.bind('x', edrnURIPrefix)

        # Go through each dataset
        for datasetid in results.keys():
            datasetid_friendly = datasetid.replace("(", "_").replace(")", "_").replace("+", "_").replace(",", "_").replace(".", "").replace("'", "").replace('"', "")
            subjectURI = URIRef(results[datasetid]['sourceurl'])
            graph.add((subjectURI, rdflib.RDF.type, URIRef("{}{}".format(context.typeURI, datasetid_friendly))))
            for key in results[datasetid].keys():
                if key not in _edrnlabcasPredicates.keys():
                    continue
                predicateURI = URIRef(getattr(context, _edrnlabcasPredicates[key]))
                if isinstance(results[datasetid][key], list):
                    graph.add((subjectURI, predicateURI, Literal(results[datasetid][key][0].strip())))
                elif isinstance(results[datasetid][key], six.string_types):
                    graph.add((subjectURI, predicateURI, Literal(results[datasetid][key].strip())))
                else:
                    raise Exception("Not sure what type of data this entry is, please adjust code to ingest this type of data: Datasetid: {}, Key {}, Val {}".format(datasetid, key, str(results[datasetid][key])))
                if key in _graph_obj_mapping.keys():
                    predicateURI = URIRef(getattr(context, _graph_obj_mapping[key][0]))
                    # Watch out for text that isn't equivalent to protocols in labcas
                    if "No Associated Protocol" not in results[datasetid][key][0].strip():
                        for item_split in results[datasetid][key][0].strip().split(","):
                            graph.add((subjectURI, predicateURI, URIRef("{}{}".format(_graph_obj_mapping[key][1], item_split.strip()))))
        # C'est tout.
        return graph
