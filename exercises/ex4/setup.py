try:
	from setuptools import setup
except:
	from distutils.core import setuptools

config = {
	'description': 'Ex4',
	'author': 'Kota Kondo',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
}