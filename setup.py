
import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='syntaxnet-python',
    version=version,
    url='http://github.com/algorithmiaio/syntaxnet-python/',
    license='MIT',
    author='James Sutton',
    author_email='james@algorithmia.com',
    description='A python library for syntaxnet & parsey mcparseface ',
    packages=['syntaxnet', 'syntaxnet.ext'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'numpy>=0.10',
        'protobuf==3.0.0b2.post1',
    ]
)
