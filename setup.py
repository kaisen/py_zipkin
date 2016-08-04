#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

__version__ = "0.1.0"

setup(
    name='python_zipkin',
    version=__version__,
    provides=["python_zipkin"],
    author='Yelp, Inc.',
    author_email='opensource+python-zipkin@yelp.com',
    license='Copyright Yelp 2016',
    url="https://github.com/Yelp/python_zipkin",
    description='Library for using Zipkin in Python.',
    packages=find_packages(exclude=('tests*', 'testing*', 'tools*')),
    package_data={'': ['*.thrift']},
    install_requires=[
        'six',
        'thriftpy',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)