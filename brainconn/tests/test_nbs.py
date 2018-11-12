# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample_group_qball,
                                   load_sample_group_dsi,
                                   load_sample_group_fmri)


def test_nbs_dsi_qbi():
    q = load_sample_group_qball()
    d = load_sample_group_dsi()
    _nbs_helper(q, d, .5, atol=0.3)


def test_nbs_dsi_fmri():
    d = load_sample_group_dsi()
    f = load_sample_group_fmri()
    assert f.shape == (219, 219, 8)
    _nbs_helper(d, f, .03, atol=0.03)


def _nbs_helper(x, y, expected_pval, atol=.05, thresh=.1, ntrials=25,
                paired=False):
    # comment
    pval, _, _ = bc.nbs.nbs_bct(x, y, thresh, k=ntrials, paired=paired)
    print(pval, expected_pval)
    assert np.allclose(pval, expected_pval, atol=atol)
