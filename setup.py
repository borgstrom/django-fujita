#!/usr/bin/env python

from setuptools import setup

setup(name='django-fujita',
      packages=['fujita'],
      scripts=['fujita.py'],
      include_package_data=True,
      version='0.3',
      license="Apache License, Version 2.0",
      description='A web based console for Django\'s development server built using Tornado',
      long_description=open('README.rst').read(),
      author='Evan Borgstrom',
      author_email='evan@fatbox.ca',
      url='https://github.com/fatbox/django-fujita',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['setuptools'])
