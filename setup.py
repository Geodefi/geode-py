from os import getenv

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(version=getenv("VERSION"))
