# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample, load_directed_sample)


def test_threshold_proportional():
    x = load_sample()
    x = bc.utils.threshold_proportional(x, .5, copy=True)
    assert np.allclose(np.sum(x), 22548.51206965)


def test_threshold_proportional_nocopy():
    x = load_sample()
    bc.utils.threshold_proportional(x, .3, copy=False)
    assert np.allclose(np.sum(x), 15253.75425406)


def test_threshold_proportional_directed():
    x = load_directed_sample()
    bc.utils.threshold_proportional(x, .28, copy=False)
    assert np.sum(x) == 3410
    # assert np.allclose( np.sum(x), 32852.72485433 )


def test_threshold_absolute():
    x = load_sample()
    x = bc.utils.threshold_absolute(x, 2.1)
    assert np.allclose(np.sum(x), 13280.17768104)


def test_strengths_und():
    x = load_sample()
    s = bc.degree.strengths_und(x)
    assert np.allclose(np.sum(s), 38967.38702018)


def test_degrees_und():
    x = load_sample()
    s = bc.degree.degrees_und(bc.utils.threshold_proportional(x, .26))
    assert np.sum(s) == 4916


def test_binarize():
    x = load_sample()
    s = bc.utils.binarize(bc.utils.threshold_proportional(x, .41))
    assert np.sum(s) == 7752


def test_normalize():
    x = load_sample()
    s = bc.utils.normalize(bc.utils.threshold_proportional(x, .79))
    assert np.allclose(np.sum(s), 3327.96285964)


def test_invert():
    x = load_sample()
    s = bc.utils.invert(bc.utils.threshold_proportional(x, .13))
    assert np.allclose(np.sum(s), 790.43107587)
