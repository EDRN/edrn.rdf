# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from rdfgenerator import IRDFGenerator
import rdflib

class INullRDFGenerator(IRDFGenerator):
    '''A null RDF generator that produces no statements at all.'''
    def generate(self):
        return rdflib.Graph()
