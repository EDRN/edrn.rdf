# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Registered Person
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import IRegisteredPerson
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

RegisteredPersonSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'firstNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'First Name URI'),
            description=_(u'Uniform Resource Identifier for the first name predicate.'),
        ),
    ),
    atapi.StringField(
        'middleNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Middle Name URI'),
            description=_(u'Uniform Resource Identifier for the middle name predicate.'),
        ),
    ),
    atapi.StringField(
        'lastNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Last Name URI'),
            description=_(u'Uniform Resource Identifier for the last name predicate.'),
        ),
    ),
    atapi.StringField(
        'phoneURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Phone URI'),
            description=_(u'Uniform Resource Identifier for the phone predicate.'),
        ),
    ),
    atapi.StringField(
        'emailURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Email URI'),
            description=_(u'Uniform Resource Identifier for the email predicate.'),
        ),
    ),
    atapi.StringField(
        'siteURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Site URI'),
            description=_(u'Uniform Resource Identifier for the site predicate.'),
        ),
    ),
))

finalizeATCTSchema(RegisteredPersonSchema, folderish=False, moveDiscussion=True)

class RegisteredPerson(base.Source):
    '''Registered Person generator.'''
    implements(IRegisteredPerson)
    portal_type               = 'Registered Person'
    _at_rename_after_creation = True
    schema                    = RegisteredPersonSchema
    firstNameURI              = atapi.ATFieldProperty('firstNameURI')
    middleNameURI             = atapi.ATFieldProperty('middleNameURI')
    lastNameURI               = atapi.ATFieldProperty('lastNameURI')
    phoneURI                  = atapi.ATFieldProperty('phoneURI')
    emailURI                  = atapi.ATFieldProperty('emailURI')
    siteURI                   = atapi.ATFieldProperty('siteURI')

atapi.registerType(RegisteredPerson, PROJECTNAME)
