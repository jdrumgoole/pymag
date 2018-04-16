
'''
Created on 30 Sep 2016

@author: jdrumgoole
'''
from setuptools import setup
import os
from codecs import open
from pymongo_aggregation.version import __VERSION__
def read(f):
    return open(f, 'r').read()
    
setup(
    name = "pymongo_aggregation",
    version = "0.1a5", #__VERSION__,
    author = "Joe Drumgoole",
    author_email = "joe@joedrumgoole.com",
    description = "A set of convenience classes for using the Pymongo MongoDB aggregation framework",
    long_description = read('README.md'),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    keywords = "MongoDB API Aggregation",
    url = "https://github.com/jdrumgoole/mongodb_utils",
    
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6' ],
   
    install_requires = [ "pymongo", "nose" ],
       
    packages = [ "pymongo_aggregation", "test"],
    test_suite='nose.collector',
    tests_require=['nose'],
)