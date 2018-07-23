#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='SolidCAD',
    version='0.1',
    description='SolidCAD - OpenSCAD generator (3D/2D CAD)',
    long_description=open('README.md').read(),
    url='https://github.com/alquimista/solidcad/',
    download_url='https://github.com/solidcad/solidcad/archive/master.zip',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic" :: Artistic Software',
        'Topic :: Multimedia',
        'Topic :: Text Processing',
    ],
    author='Roberto Gea',
    author_email='rgea@airmail.cc',
    license='MIT',
    packages=['solidcad'],
    install_requires=[],
    entry_points={
       'console_scripts': ['solidcad=solidcad.cmd_solidcad:main'],
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    keywords="SolidCAD OpenSCAD 3D 2D CAD Sketch Drawing Design stl Printer",
)
