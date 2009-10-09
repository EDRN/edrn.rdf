# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from setuptools import setup, find_packages
import os

version = '0.0.6'

setup(
    name='edrn.rdf',
    version=version,
    description="EDRN RDF Server",
    long_description=open("README.txt").read() + "\n" + open(os.path.join("docs", "HISTORY.txt")).read(),
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
        'pymssql',
    ],
    entry_points={},
)
