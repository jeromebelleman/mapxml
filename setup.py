#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='mapxml',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://jeromebelleman.gitlab.io',
    description="Make KML maps canonical and compare them",
    long_description="Make KML maps canonical and compare them with vimdiff.",
    scripts=['mapxml'],
    data_files=[('share/man/man1', ['mapxml.1'])],
)
