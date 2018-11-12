# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample_group_qball,
                                   load_sample_group_dsi)


def test_partition_distance():
    q = load_sample_group_qball()
    d = load_sample_group_dsi()

    q = np.mean(q, axis=2)
    d = np.mean(d, axis=2)

    qi, _ = bc.modularity.modularity_und(q)
    di, _ = bc.modularity.modularity_und(d)

    vi, mi = bc.modularity.partition_distance(qi, di)

    print(vi, mi)
    assert np.allclose(vi, 0.1964, atol=0.01)
    assert np.allclose(mi, 0.6394, atol=0.01)
