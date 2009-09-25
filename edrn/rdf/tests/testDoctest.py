# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: functional doctests.
'''

import unittest
import doctest
from Testing import ZopeTestCase as ztc
from edrn.rdf.tests import base

def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite('README.txt', package='edrn.rdf',
            test_class=base.EDRNRDFFunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
    ])
    

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
    
