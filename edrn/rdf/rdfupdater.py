# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from edrn.rdf.interfaces import IRDFUpdater
from edrn.rdf.rdfsource import IRDFSource
from five import grok

class RDFUpdater(grok.Adapter):
    '''Update RDF.'''
    grok.provides(IRDFUpdater)
    grok.context(IRDFSource)
    def __init__(self, context):
        self.context = context
    def updateRDF(self):
        raise Exception('not yet implemented')
    
