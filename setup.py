from setuptools import find_packages
from setuptools import setup

setup(
    name='prettylog',
    version='0.1',
    description='Makes your logs pretty!',
    classifiers=[],
    keywords='',
    author='Emerson Matson',
    author_email='emersonn@uw.edu',
    url='',
    packages=['prettylog'],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'colorama',
    ],
    extras_require={
        'test': [
            'mock',
            'nose'
        ]
    }
)
