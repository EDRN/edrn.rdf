# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Site
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import ISite
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

SiteSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'titleURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Title URI'),
            description=_(u'Uniform Resource Identifier for the title predicate.'),
        ),
    ),
    atapi.StringField(
        'abbrevNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abbreviated Name URI'),
            description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        ),
    ),
    atapi.StringField(
        'assocMemberSponsorURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Associate Members Sponsor URI'),
            description=_(u'Uniform Resource Identifier fo the predicate that identifies the sponsor for a site.'),
        ),
    ),
    atapi.StringField(
        'fundingDateStartURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Funding Start Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding started for the site.'),
        ),
    ),
    atapi.StringField(
        'fundingDateFinishURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Funding Finish Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding ended for the site.'),
        ),
    ),
    atapi.StringField(
        'fwaNumberURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'FWA Number URI'),
            description=_(u'Uniform Resource Identifier for the FWA number predicate.'),
        ),
    ),
    atapi.StringField(
        'piURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'PI URI'),
            description=_(u'Uniform Resource Identifier for the Primary Investigator predicate.'),
        ),
    ),
    atapi.StringField(
        'coIURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Co-I URI'),
            description=_(u'Uniform Resource Identifier for the Co-Investigator predicate.'),
        ),
    ),
    atapi.StringField(
        'staffURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Staff URI'),
            description=_(u'Uniform Resource Identifier for the staff predicate.'),
        ),
    ),
    atapi.StringField(
        'mailAddr1URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Line 1 URI'),
            description=_(u'Uniform Resource Identifier for line 1 of the mailing address.'),
        ),
    ),
    atapi.StringField(
        'mailAddr2URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Line 2 URI'),
            description=_(u'Uniform Resource Identifier for line 2 of the mailing address.'),
        ),
    ),
    atapi.StringField(
        'mailAddrCityURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address City URI'),
            description=_(u'Uniform Resource Identifier for the city of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'mailAddrStateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address State URI'),
            description=_(u'Uniform Resource Identifier for the state of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'mailAddrZipURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Post Code URI'),
            description=_(u'Uniform Resource Identifier for the post code (zip code) of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'mailAddrCountryURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Country URI'),
            description=_(u'Uniform Resource Identifier for the country of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'physAddr1URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address Line 1 URI'),
            description=_(u'Uniform Resource Identifier for line 1 of the physical address.'),
        ),
    ),
    atapi.StringField(
        'physAddr2URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address Line 2 URI'),
            description=_(u'Uniform Resource Identifier for line 2 of the physical address.'),
        ),
    ),
    atapi.StringField(
        'physAddrCityURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address City URI'),
            description=_(u'Uniform Resource Identifier for the city of the physical address predicate.'),
        ),
    ),
    atapi.StringField(
        'physAddrStateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address State URI'),
            description=_(u'Uniform Resource Identifier for the state of the physical address predicate.'),
        ),
    ),
    atapi.StringField(
        'physAddrZipURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address Post Code URI'),
            description=_(u'Uniform Resource Identifier for the post code (zip code) of the physical address predicate.'),
        ),
    ),
    atapi.StringField(
        'physAddrCountryURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Physical Address Country URI'),
            description=_(u'Uniform Resource Identifier for the country of the physical address predicate.'),
        ),
    ),
    atapi.StringField(
        'shipAddr1URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address Line 1 URI'),
            description=_(u'Uniform Resource Identifier for line 1 of the shipping address.'),
        ),
    ),
    atapi.StringField(
        'shipAddr2URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address Line 2 URI'),
            description=_(u'Uniform Resource Identifier for line 2 of the shipping address.'),
        ),
    ),
    atapi.StringField(
        'shipAddrCityURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address City URI'),
            description=_(u'Uniform Resource Identifier for the city of the shipping address predicate.'),
        ),
    ),
    atapi.StringField(
        'shipAddrStateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address State URI'),
            description=_(u'Uniform Resource Identifier for the state of the shipping address predicate.'),
        ),
    ),
    atapi.StringField(
        'shipAddrZipURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address Post Code URI'),
            description=_(u'Uniform Resource Identifier for the post code (zip code) of the shipping address predicate.'),
        ),
    ),
    atapi.StringField(
        'shipAddrCountryURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Shipping Address Country URI'),
            description=_(u'Uniform Resource Identifier for the country of the shipping address predicate.'),
        ),
    ),
    atapi.StringField(
        'specialityURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Speciality URI'),
            description=_(u'Uniform Resource Identifier for predicate identifying the site speciality.'),
        ),
    ),
    atapi.StringField(
        'urlURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'URL URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying the site home page.'),
        ),
    ),
    atapi.StringField(
        'memberTypeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Member Type URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying the type of the EDRN member site.'),
        ),
    ),
    atapi.StringField(
        'histNotesURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Hisorical Notes URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying historical notes.'),
        ),
    ),
))

finalizeATCTSchema(SiteSchema, folderish=False, moveDiscussion=True)

class Site(base.Source):
    '''Site.'''
    implements(ISite)
    portal_type               = 'Site'
    _at_rename_after_creation = True
    schema                    = SiteSchema
    titleURI                  = atapi.ATFieldProperty('titleURI')
    abbrevNameURI             = atapi.ATFieldProperty('abbrevNameURI')
    assocMemberSponsorURI     = atapi.ATFieldProperty('assocMemberSponsorURI')
    fundingDateStartURI       = atapi.ATFieldProperty('fundingDateStartURI')
    fundingDateFinishURI      = atapi.ATFieldProperty('fundingDateFinishURI')
    fwaNumberURI              = atapi.ATFieldProperty('fwaNumberURI')
    piURI                     = atapi.ATFieldProperty('piURI')
    coIURI                    = atapi.ATFieldProperty('coIURI')
    staffURI                  = atapi.ATFieldProperty('staffURI')
    mailAddr1URI              = atapi.ATFieldProperty('mailAddr1URI')
    mailAddr2URI              = atapi.ATFieldProperty('mailAddr2URI')
    mailAddrCityURI           = atapi.ATFieldProperty('mailAddrCityURI')
    mailAddrStateURI          = atapi.ATFieldProperty('mailAddrStateURI')
    mailAddrZipURI            = atapi.ATFieldProperty('mailAddrZipURI')
    mailAddrCountryURI        = atapi.ATFieldProperty('mailAddrCountryURI')
    physAddr1URI              = atapi.ATFieldProperty('physAddr1URI')
    physAddr2URI              = atapi.ATFieldProperty('physAddr2URI')
    physAddrCityURI           = atapi.ATFieldProperty('physAddrCityURI')
    physAddrStateURI          = atapi.ATFieldProperty('physAddrStateURI')
    physAddrZipURI            = atapi.ATFieldProperty('physAddrZipURI')
    physAddrCountryURI        = atapi.ATFieldProperty('physAddrCountryURI')
    shipAddr1URI              = atapi.ATFieldProperty('shipAddr1URI')
    shipAddr2URI              = atapi.ATFieldProperty('shipAddr2URI')
    shipAddrCityURI           = atapi.ATFieldProperty('shipAddrCityURI')
    shipAddrStateURI          = atapi.ATFieldProperty('shipAddrStateURI')
    shipAddrZipURI            = atapi.ATFieldProperty('shipAddrZipURI')
    shipAddrCountryURI        = atapi.ATFieldProperty('shipAddrCountryURI')
    specialityURI             = atapi.ATFieldProperty('specialityURI')
    urlURI                    = atapi.ATFieldProperty('urlURI')
    memberTypeURI             = atapi.ATFieldProperty('memberTypeURI')
    histNotesURI              = atapi.ATFieldProperty('histNotesURI')

atapi.registerType(Site, PROJECTNAME)
