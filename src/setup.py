
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import toml

if os.path.isfile('./pyproject.toml'):
    project = toml.load('./pyproject.toml')
else:
    project = toml.load('../pyproject.toml')

setup(
    long_description='',
    name=project['tool']['poetry']['name'],
    version=project['tool']['poetry']['version'],
    description=project['tool']['poetry']['description'],
    python_requires='==3.*,>=3.7.0',
    author='Vikash Kothary',
    author_email='kothary.vikash@gmail.com',
    install_requires=['flask==1.*,>=1.1.2']
)
