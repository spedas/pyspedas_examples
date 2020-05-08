"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open

setup(
    name='pyspedas_examples',
    version='0.1.3',
    description='Examples of pySPEDAS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/spedas/pyspedas_examples',
    author='Nick Hatzigeorgiu, Eric Grimes',
    author_email='nikos@berkeley.edu, egrimes@igpp.ucla.edu',
    license='MIT',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 ],
    keywords='examples spedas data tools',
    project_urls={'Information': 'http://spedas.org/wiki/',
                  },
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pyspedas>=0.9.29'],
    python_requires='>=3.5',
    include_package_data=True,
)
