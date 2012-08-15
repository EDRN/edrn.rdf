# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''RDF Source'''

from five import grok
from zope import schema
from plone.directives import form, dexterity
from edrn.rdf import _
from rdfgenerator import IRDFGenerator
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from Acquisition import aq_inner

class IRDFSource(form.Schema):
    '''A source of RDF data.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this RDF source'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this RDF source.'),
        required=False,
    )
    generator = RelationChoice(
        title=_(u'Generator'),
        description=_(u'Which RDF generator should this source use.'),
        required=False,
        source=ObjPathSourceBinder(object_provides=IRDFGenerator.__identifier__),
    )
    active = RelationChoice(
        title=_(u'Active'),
        description=_(u'Which of the RDF files is the active one.'),
        required=False,
        source=ObjPathSourceBinder(portal_type='File'),
    )
    


class View(grok.View):
    '''RDF output from an RDF source.'''
    grok.context(IRDFSource)
    grok.require('zope2.View')
    grok.name('rdf')
    def render(self):
        context = aq_inner(self.context)
        if context.active and context.active.to_object:
            raise Exception('not yet implemented')
        raise ValueError('The RDF Source at %s does not have an active RDF file to send' % '/'.join(context.getPhysicalPath()))

        
    