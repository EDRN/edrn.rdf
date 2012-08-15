# encoding: utf-8
# Copyright 2008—2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN RDF Service: interfaces
'''

from zope.interface import Interface

class IRDFDatabase(Interface):
    def query(x):
        '''...'''
        

class IRDFUpdater(Interface):
    '''An object whose RDF may be updated'''
    def updateRDF():
        '''Update this object's RDF graph'''
