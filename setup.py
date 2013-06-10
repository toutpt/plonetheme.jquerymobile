from setuptools import setup, find_packages
import os

version = '1.0dev'
extra_requires = {'test': ['plone.app.testing[robot]>=4.2.2']}

setup(name='plonetheme.jquerymobile',
      version=version,
      description="jquerymobile theme",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
      ],
      keywords='plone theme jquery mobile',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/plonetheme.jquerymobile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.browserlayer',
          'plone.app.registry',
          'plone.app.modernizr',
          'collective.js.jquerymobile',
          'collective.fontawesome',
          'collective.monkeypatcher',
          'collective.picturefill',
          'collective.z3cform.html5widgets',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      extras_require=extra_requires,
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
