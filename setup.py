from setuptools import setup, find_packages
import os
import sys
import re
import shutil


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def read_all(f):
    with open(f) as I:
        return I.read()

requirements = map(str.strip, open("requirements.txt").readlines())

version = get_version('oandapyV20')

if sys.argv[-1] == 'publish':
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('oandapyV20.egg-info')
    sys.exit()

setup(name='oandapyV20',
      version=version,
      description="Python wrapper for the OANDA REST-V20 API",
      long_description=read_all("README.rst"),
      classifiers=[
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Intended Audience :: Financial and Insurance Industry',
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],  # Get from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='OANDA FOREX/CFD wrapper REST-V20 API',
      author='F. Brekeveld',
      author_email='f.brekeveld@gmail.com',
      url='http://github.com/hootnot/oanda-api-v20',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
