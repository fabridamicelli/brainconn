# brainconn (brain connectivity) library

The `brainconn` Python library is a fork of `bctpy`, which in turn is a Python implementation of the `BCT` MATLAB toolbox. `bctpy` was written by [Roan LaPlante](https://github.com/aestrivex) and is a wonderful tool. However, there were certain elements of the implementation that we wanted to change, so we chose to develop independently on a fork, which we renamed to `brainconn` to allow separate releases on PyPi and the like.

[![License: GPL v3](https://img.shields.io/badge/license-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/FIU-Neuro/brainconn.svg?branch=master)](https://travis-ci.org/FIU-Neuro/brainconn)
[![Codecov](https://codecov.io/gh/FIU-Neuro/brainconn/branch/master/graph/badge.svg)](https://codecov.io/gh/FIU-Neuro/brainconn)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1e2340c0a02d45c1b21e22e8f92f2a35)](https://www.codacy.com/project/tsalo/brainconn/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=FIU-Neuro/brainconn&amp;utm_campaign=Badge_Grade_Dashboard)
[![Documentation Status](https://readthedocs.org/projects/brainconn/badge/?version=latest)](http://brainconn.readthedocs.io/en/latest/?badge=latest)

## About

`brainconn` implements graph theoretic measures in Python.

### Why graph theory?



## Copyright information

`bctpy` was released with the [GNU GPLv3+ license](https://www.gnu.org/licenses/gpl-3.0), which we adhere to as well. Changes made since splitting `brainconn` from `bctpy` are tracked in the [CHANGELOG](CHANGELOG.md).

## Citing brainconn

We eventually plan to publish `brainconn` releases on Zenodo, which will make specific versions citable. Moreover, the algorithms employed in `brainconn` (as well as the `BCT` MATLAB toolbox) should also be cited when used. We use [duecredit](https://github.com/duecredit/duecredit) to make compiling and annotating these citations easier. If you use `brainconn`, please make sure to run your code with `duecredit` before publication to make sure you have a comprehensive list of the software and papers that should be cited. You can do this by running your Python script (e.g., `run_brainconn.py`) from the command line like so: `python -m duecredit run_brainconn.py`.

## Dependencies

At minimum, `brainconn` requires `numpy`, `scipy`, and `networkx`. While `bctpy` has limited dependencies to these three packages, `brainconn` is open to additional dependencies, as long as they are relatively stable and well-tested.

`pytest` is used for the test suite. The test suite is not complete.

## About `bctpy` and other authors

BCT is a matlab toolbox with many graph theoretical measures off of which `bctpy`
is based.  I did not write BCT (apart from small bugfixes I have submitted)
and a quality of life improvements that I have taken liberties to add.
With few exceptions, `bctpy` is a direct translation of matlab code to python.

`bctpy` should be considered beta software, with BCT being the gold standard by
comparison. I did my best to test all functionality in `bctpy`, but much of it is
arcane math that flies over the head of this humble programmer. There *are*
bugs lurking in `bctpy`, the question is not whether but how many. If you locate
bugs, please submit them to me at rlaplant@nmr.mgh.harvard.edu.

Many thanks to Stefan Fuertinger for his assistance tracking down a number of
bugs. Stefan Fuertinger has a similar software package dealing with brain
network functionality at http://research.mssm.edu/simonyanlab/analytical-tools/

Many thanks to Chris Barnes for his assistance in documenting a number of issues and facilitating a number of test cases.

Credit for writing BCT (the matlab version) goes to the following list of
authors, especially Olaf Sporns and Mika Rubinov.

- Olaf Sporns
- Mikail Rubinov
- Yusuke Adachi
- Andrea Avena
- Danielle Bassett
- Richard Betzel
- Joaquin Goni
- Alexandros Goulas
- Patric Hagmann
- Christopher Honey
- Martijn van den Heuvel
- Rolf Kotter
- Jonathan Power
- Murray Shanahan
- Andrew Zalesky

In order to be a bit more compact I have removed the accreditations from the
docstrings each functions. This does not in any way mean that I wish to take
credit from the individual contributions. I have moved these accreditations
to the credits file.


[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
