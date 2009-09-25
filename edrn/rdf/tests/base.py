# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN RDF Service: test harness base classes.'''

from edrn.rdf.interfaces import IRDFDatabase
from Globals import package_home
from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc
from zope.component import provideUtility
from zope.interface import implements
import SnakeSQL, os

PACKAGE_HOME = package_home(globals())

class TestDatabase(object):
    implements(IRDFDatabase)
    def connect(self):
        os.chdir(PACKAGE_HOME)
        return SnakeSQL.connect(database='testdata', autoCreate=False)
    
    

# Traditional Products we have to load manually for test cases:
# (none at this time)

@onsetup
def setupEDRNRDF():
    '''Set up additional products required for EDRN RDF Service.'''
    fiveconfigure.debug_mode = True
    import edrn.rdf
    zcml.load_config('configure.zcml', edrn.rdf)
    fiveconfigure.debug_mode = False
    ztc.installPackage('edrn.rdf')

setupEDRNRDF()
ptc.setupPloneSite(products=['edrn.rdf'])

class EDRNRDFTestCase(ptc.PloneTestCase):
    '''Base for unit tests in this package.'''
    pass
    

class EDRNRDFFunctionalTestCase(ptc.FunctionalTestCase):
    '''Base class for functional (doc-)tests.'''
    def afterSetUp(self):
        super(EDRNRDFFunctionalTestCase, self).afterSetUp()
        provideUtility(TestDatabase())
    

