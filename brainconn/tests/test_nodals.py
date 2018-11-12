# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample)


def test_glob_eff():
    x = load_sample(thres=.4)
    geff = bc.distance.efficiency_wei(x)
    print(geff, 1.8784)
    assert np.allclose(geff, 1.8784, atol=1e-4)


def test_loc_eff():
    x = load_sample(thres=.4)
    leff = bc.distance.efficiency_wei(x, local=True)
    print(np.sum(leff), 315.6225)
    assert np.allclose(np.sum(leff), 315.6225, atol=0.1)


def test_glob_eff_bin():
    x = load_sample(thres=.4)
    geff = bc.distance.efficiency_bin(x)

    y = bc.utils.binarize(x)
    geff2 = bc.distance.efficiency_bin(y)

    print(geff, geff2, 0.6999)
    assert np.allclose(geff, 0.6999, atol=1e-4)
    assert np.allclose(geff2, 0.6999, atol=1e-4)


def test_loc_eff_bin():
    x = load_sample(thres=.4)
    leff = bc.distance.efficiency_bin(x, local=True)

    y = bc.utils.binarize(x)
    leff2 = bc.distance.efficiency_bin(y, local=True)

    print(np.sum(leff), np.sum(leff2), 105.5111)
    assert np.allclose(np.sum(leff), 105.5111, atol=0.1)
    assert np.allclose(np.sum(leff2), 105.5111, atol=0.1)
