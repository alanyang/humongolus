# coding:utf-8
#

from distutils.core import setup
from setuptools import find_packages

setup(name='Humongolus',
      version='1.1',
      author='Christopher Coté',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['pymongo'],
      include_package_data=True,
      )

#
# setup.py ends here
