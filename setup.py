from setuptools import setup

setup(
    name='appengine-pipeline',
    version='0.1',
    description='The Google App Engine Pipeline API',
    url='http://code.google.com/p/appengine-pipeline',
    packages=['appengine-pipeline'],
	package_dir={'appengine-pipeline': 'src/pipeline'},
    package_data={'appengine-pipeline': ['simplejson/*.*','ui/*.*']},
)
