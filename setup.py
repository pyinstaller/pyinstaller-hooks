#! /usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2005-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

import time
import codecs
import sys, os
from setuptools import setup


# TODO: Use the same mechanisms for adding git commit-is as PyInstaller does
version = time.strftime('%Y%m%d')

REQUIREMENTS = []

# Create long description from README.rst.
# PYPI page will contain complete PyInstaller changelog.
def read(filename):
    try:
        return unicode(codecs.open(filename, encoding='utf-8').read())
    except NameError:
        return open(filename, 'r', encoding='utf-8').read()
long_description = u'\n\n'.join([read('README.rst')])
if sys.version_info < (3,):
    long_description = long_description.encode('utf-8')


CLASSIFIERS = """
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License v2 (GPLv2)
Natural Language :: English
Topic :: Software Development :: Build Tools
Topic :: System :: Software Distribution
""".strip().splitlines()


setup(
    install_requires=REQUIREMENTS,

    name='PyInstaller-Hooks',
    version=version,

    description='PyInstaller bundles a Python application and all its '
                'dependencies into a single package.',
    long_description=long_description,
    keywords='packaging app apps bundle convert standalone executable '
             'pyinstaller macholib cxfreeze freeze py2exe py2app bbfreeze',

    author='PyInstaller Development Team',
    author_email='pyinstaller@googlegroups.com',

    license=('GPL license with a special exception which allows to use '
             'PyInstaller to build and distribute non-free programs '
             '(including commercial ones)'),
    url='http://www.pyinstaller.org',

    classifiers=CLASSIFIERS,
    zip_safe=False,
    packages=['pyinstaller_hooks'],
    package_data={
        '': ['hooks/*'],
        },
    include_package_data=True,

    entry_points={
        'PyInstaller.hooks': ['hooks=true', 'runtime-hooks=true']
    }
)
