# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import load_sample


def test_breadthdist():
    x = load_sample(thres=.02)
    r, d = bc.distance.breadthdist(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(r), np.sum(d))
    assert np.sum(r) == 5804
    assert np.sum(d) == 30762


def test_reachdist():
    x = load_sample(thres=.02)
    r, d = bc.distance.reachdist(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(r), np.sum(d))
    assert np.sum(r) == 5804
    assert np.sum(d) == 30762

    bx = bc.utils.binarize(x, copy=False)
    br, bd = bc.distance.reachdist(bx)
    bd[np.where(np.isinf(bd))] = 0
    print(np.sum(br), np.sum(bd))
    assert np.sum(br) == 5804
    assert np.sum(bd) == 30762


def test_distance_bin():
    x = bc.utils.binarize(load_sample(thres=.02), copy=False)
    d = bc.distance.distance_bin(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(d))
    assert np.sum(d) == 30506  # deals with diagonals differently


def test_distance_wei():
    x = load_sample(thres=.02)
    d, e = bc.distance.distance_wei(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(d), np.sum(e))

    assert np.allclose(np.sum(d), 155650.1, atol=.01)
    assert np.sum(e) == 30570


def test_charpath():
    x = load_sample(thres=.02)
    d, e = bc.distance.distance_wei(x)
    l, eff, ecc, radius, diameter = bc.distance.charpath(d)

    assert np.any(np.isinf(d))
    assert not np.isnan(radius)
    assert not np.isnan(diameter)
