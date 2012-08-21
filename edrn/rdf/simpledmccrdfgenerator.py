# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Simple DMCC RDF Generator. This generator is used to describe the some of the more simple
sets of data available at the DMCC by accessing their crummy web service.
'''

from edrn.rdf import _
from five import grok
from zope import schema
from interfaces import IGraphGenerator
from rdfgenerator import IRDFGenerator
from utils import validateAccessibleURL
from exceptions import MissingParameterError
from Acquisition import aq_inner
from z3c.suds import get_suds_client
from rdflib.term import URIRef, Literal
from utils import parseTokens
import rdflib

DEFAULT_VERIFICATION_NUM = u'0' * 40960 # Why, why, why? DMCC, you so stupid!

class ISimpleDMCCRDFGenerator(IRDFGenerator):
    '''Simple DMCC RDF Generator.'''
    webServiceURL = schema.TextLine(
        title=_(u'Web Service URL'),
        description=_(u'The Uniform Resource Locator to the DMCC SOAP web service.'),
        required=True,
        constraint=validateAccessibleURL,
    )
    operationName = schema.TextLine(
        title=_(u'Operation Name'),
        description=_(u'Name of the SOAP operation to invoke in order to retrieve data.'),
        required=True,
    )
    verificationNum = schema.TextLine(
        title=_(u'Verification Number String'),
        description=_(u'Stupid, pointless, and needless parameter to pass to the operation. A default will be used if unset.'),
        required=False,
    )
    uriPrefix = schema.TextLine(
        title=_(u'URI Prefix'),
        description=_(u'The Uniform Resource Identifier prepended to all subjects described by this generator.'),
        required=True,
    )
    identifyingKey = schema.TextLine(
        title=_(u'Identifying Key'),
        description=_(u'Key in the DMCC output serves as the discriminant for objects described by this generator.'),
        required=True,
    )
    typeURI = schema.TextLine(
        title=_(u'Type URI'),
        description=_(u'Uniform Resource Identifier naming the type of objects described by this generator.'),
        required=True,
    )
    


class SimpleDMCCGraphGenerator(grok.Adapter):
    '''A statement graph generator that produces statements based on the DMCC's crummy web service.'''
    grok.provides(IGraphGenerator)
    grok.context(ISimpleDMCCRDFGenerator)
    def generateGraph(self):
        context = aq_inner(self.context)
        if not context.webServiceURL: raise MissingParameterError(context, 'webServiceURL')
        if not context.operationName: raise MissingParameterError(context, 'operationName')
        if not context.identifyingKey: raise MissingParameterError(context, 'identifyingKey')
        if not context.uriPrefix: raise MissingParameterError(context, 'uriPrefix')
        if not context.typeURI: raise MissingParameterError(context, 'typeURI')
        verificationNum = context.verificationNum if context.verificationNum else DEFAULT_VERIFICATION_NUM
        predicates = {}
        for objID, item in context.contentItems():
            predicates[item.title] = URIRef(item.predicateURI)
        client = get_suds_client(context.webServiceURL, context)
        function = getattr(client.service, context.operationName)
        horribleString = function(verificationNum)
        graph = rdflib.Graph()
        for row in horribleString.split('!!'):
            subjectURI = None
            statements = []
            for key, value in parseTokens(row):
                if key == context.identifyingKey and not subjectURI:
                    subjectURI = URIRef(context.uriPrefix + value)
                    graph.add((subjectURI, rdflib.RDF.type, context.typeURI))
                elif key in predicates:
                    # Here we should actually adapt to the handler and let it generate a (predicateURI, obj) pair
                    predicateURI = predicates[key]
                    statements.append((predicateURI, Literal(value)))
            for predicate, obj in statements:
                graph.add((subjectURI, predicate, obj))
        return graph

                        