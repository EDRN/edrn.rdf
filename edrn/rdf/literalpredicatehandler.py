# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from predicatehandler import ISimplePredicateHandler

class ILiteralPredicateHandler(ISimplePredicateHandler):
    '''A handler for DMCC web services that maps tokenized keys to literal RDF values.'''
    # No further fields are necessary.
