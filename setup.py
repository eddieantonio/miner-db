from setuptools import setup
from miner_db import __version__ as version, __doc__ as description

setup(name='miner-db',
      version=version,
      license='Apache',
      description=description,
      url='http://github.com/eddieantonio/miner-db',
      author='Eddie Antonio Santos',
      author_email='easantos@ualberta.ca',
      include_package_data=True,
      packages=['miner_db'])
