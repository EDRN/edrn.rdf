# encoding: utf-8
# Copyright 2008—2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN RDF Service: interfaces
'''

from zope.interface import Interface

class IRDFUpdater(Interface):
    '''An object whose RDF may be updated'''
    def updateRDF():
        '''Update this object's RDF file.'''

class IGraphGenerator(Interface):
    '''An object that creates statement graphs.'''
    def generateGraph():
        '''Generate this object's RDF graph.'''
