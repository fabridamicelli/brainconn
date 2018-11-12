# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import load_sample


def test_assortativity_wu_sign():
    x = load_sample(thres=.1)
    ass_pos, _ = bc.core.local_assortativity_wu_sign(x)

    print(ass_pos, .2939)
    assert np.allclose(np.sum(ass_pos), .2939, atol=.0001)


def test_core_periphery_dir():
    x = load_sample(thres=.1)
    c, q = bc.core.core_periphery_dir(x)
    assert np.sum(c) == 57
    assert np.sum(np.cumsum(c)) == 4170
    assert np.allclose(q, .3086, atol=.0001)
