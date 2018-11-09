# setup.py

from setuptools import setup

setup(
   name='eventropy',
   version='1.0.1',
   description='Events Management',
   license="Mozilla Public License 2.0 (MPL 2.0)",
   long_description='A configurable events registry for Python. It assumes that you will be using PostgreSQL as the backing store.',
   author='Phenicle',
   author_email='pheniclebeefheart@gmail.com',
   url="https://github.com/phenicle/eventropy",
   packages=['eventropy',],  #same as name
   install_requires=['cfgpy','psycopg2'], #external packages as dependencies
)
