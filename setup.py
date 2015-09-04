import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyAnno",
    version = "0.1a",
    author = "Python School",
    author_email = "ann.samoilenko@gmail.com",
    description = ("Code stolen from https://pythonhosted.org/an_example_pypi_project/setuptools.html "
                   "some strange project we were given at school"),
    license = "BSD",
    keywords = "labels voting annottion",
    url = "https://github.com/torrin8/pyanno_voting",
    packages=['pyanno'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)


