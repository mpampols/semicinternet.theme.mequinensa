from setuptools import setup, find_packages
import os

version = '1.0.20111026'

setup(name='semicinternet.theme.mequinensa',
      version=version,
      description="A free Plone theme from SEMIC Internet for Plone 4",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='semic internet plone theme mequinensa',
      author='Marc Pampols',
      author_email='mpampols@semicinternet.com',
      url='https://github.com/mpampols/semicinternet.theme.mequinensa',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['semicinternet', 'semicinternet.theme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.registry',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
