# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from setuptools import setup, find_packages
import os

_name = 'edrn.rdf'
_version = '0.0.10'

def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_desc = _read('README.txt')
_longDesc = _header + '\n\n' + _desc + '\n\n' + _read('docs', 'INSTALL.txt') + '\n\n' + _read('docs', 'HISTORY.txt')
open('doc.txt', 'w').write(_longDesc)

setup(
    name=_name,
    version=_version,
    description="EDRN RDF Server",
    long_description=_longDesc,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='EDRN cancer research RDF web Zope Plone',
    author='Sean Kelly',
    author_email='sean.kelly@jpl.nasa.gov',
    url='http://cancer.jpl.nasa.gov/products/rdf-server',
    download_url='http://oodt.jpl.nasa.gov/dist/edrn-rdf',
    license='Proprietary',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edrn'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'rdflib>=2.4,<3.0a',
        'pymssql==1.0.2',
    ],
    entry_points={},
)
