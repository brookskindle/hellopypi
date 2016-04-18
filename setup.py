#!/usr/bin/env python

from setuptools import setup
#from distutils.core import setup

setup(
    name="HelloPyPi",
    packages=["hellopypi"],
    version="0.0.1dev",
    description="A test package upload.",
    long_description=("Importing the 'hellopypi' module will cause a greeting "
                      "message to be displayed to stdout."),
    author="Brooks Kindle",
    author_email="brookskindle@gmail.com",
    url="https://github.com/brookskindle/hellopypi",
    keywords=["test", "hello"],
)
