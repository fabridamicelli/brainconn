# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample)


def test_link_communities():
    x = load_sample(thres=0.4)
    M = bc.modularity.link_communities(x)
    assert np.max(M) == 1
