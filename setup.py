from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='tdesvenain.templates',
      version=version,
      description="A set of skels for Plone dev",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        ],
      keywords='paster Plone zopeskel',
      author='Thomas Desvenain',
      author_email='thomas.desvenain@gmail.com',
      url='https://github.com/tdesvenain/tdesvenain.zopeskel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tdesvenain'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel<3.0',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [paste.paster_create_template]
      tdesvenain_edm = tdesvenain.templates.edm:EDM
      """,
      )
