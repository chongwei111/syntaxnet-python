
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='syntaxnet',
    version='0.1.0',
    url='http://github.com/algorithmiaio/syntaxnet-python/',
    license='MIT',
    author='James Sutton',
    author_email='james@algorithmia.com',
    description='A python library for syntaxnet & parsey mcparseface ',
    packages=['syntaxnet'],
    install_requires=[
        'numpy>=0.7',
	'protobuf==3.0.0b2',
	'asciitree',
    ],
)
