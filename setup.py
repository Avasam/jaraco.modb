#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
from setuptools import find_packages
setup_params = dict(
	name='jaraco.modb',
	use_hg_version=True,
	packages=find_packages(),
	namespace_packages=['jaraco'],
	zip_safe=False,
	install_requires=[
		'jsonpickle',
	],
	setup_requires=[
		'hgtools',
	],
)
if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
