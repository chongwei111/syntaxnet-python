
import re
import ast
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='syntaxnet-python',
    version='0.1.1',
    url='http://github.com/algorithmiaio/syntaxnet-python/',
    license='MIT',
    author='James Sutton',
    author_email='james@algorithmia.com',
    description='A python library for syntaxnet & parsey mcparseface ',
    packages=['syntaxnet'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'numpy>=0.10',
        'protobuf==3.0.0b2.post1',
    ]
)
