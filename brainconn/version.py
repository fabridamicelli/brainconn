from __future__ import absolute_import, division, print_function

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = ''

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 4 - Beta",
               "Environment :: X11 Applications",
               "Intended Audience :: Science/Research",
               ("License :: OSI Approved :: GNU General Public License v3 or "
                "later (GPLv3+)"),
               "Natural Language :: English",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering :: Information Analysis"]

# Description should be a one-liner:
description = "Brain Connectivity Toolbox for Python"
# Long description will go up on the pypi page
long_description = """

brainconn
======
brainconn is a Python package for performing graph theory analysis for
neuroimaging.

License
=======
``brainconn`` is licensed under the terms of the GNU GPL license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

"""

NAME = "brainconn"
MAINTAINER = "brainconn developers"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/FIU-Neuro/brainconn"
DOWNLOAD_URL = "http://github.com/FIU-Neuro/brainconn.git"
LICENSE = "GPL"
AUTHOR = "brainconn developers"
AUTHOR_EMAIL = "http://github.com/FIU-Neuro/brainconn"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
REQUIRES = ['numpy', 'scipy']
TESTS_REQUIRES = [
    'codecov',
    'pytest',
    'pytest-cov'
]
EXTRA_REQUIRES = {
    'doc': [
        'sphinx>=1.5.3',
        'sphinx_rtd_theme',
        'sphinx-argparse',
        'sphinx_gallery',
        'numpydoc',
        'm2r',
    ],
    'tests': TESTS_REQUIRES,
    'duecredit': ['duecredit'],
    'algorithms': ['networkx', 'mayavi']
}

# Enable a handle to install all extra dependencies at once
EXTRA_REQUIRES['all'] = [val for _, val in list(EXTRA_REQUIRES.items())]
