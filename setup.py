from setuptools import setup

setup(
    name='pipeline',
    version='0.1',
    description='The Google App Engine Pipeline API',
    url='http://code.google.com/p/appengine-pipeline',
    packages=['pipeline'],
	package_dir={'pipeline': 'src/pipeline'},
    package_data={'pipeline': ['ui/*.*']},
    requires = ['simplejson']
)
