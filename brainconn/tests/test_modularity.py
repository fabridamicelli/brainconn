# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample, load_signed_sample,
                                   load_directed_low_modularity_sample,
                                   load_directed_sample)


def test_modularity_und():
    x = load_sample(thres=.4)
    _, q = bc.modularity.modularity_und(x)
    assert np.allclose(q, 0.24097717)
    # matlab and bctpy appear to return different results due to the cross-
    # package numerical instability of eigendecompositions


def test_modularity_louvain_und():
    x = load_sample(thres=.4)

    seed = 38429004
    _, q = bc.modularity.modularity_louvain_und(x, seed=seed)
    assert np.allclose(q, 0.25892588)

    fails = 0
    for i in range(100):
        ci, q = bc.modularity.modularity_louvain_und(x)
        try:
            assert np.allclose(q, .25, atol=0.01)
        except AssertionError:
            if fails >= 5:
                raise
            else:
                fails += 1

    seed = 94885236
    _, q = bc.modularity.modularity_finetune_und(x, seed=seed)
    assert np.allclose(q, .25879794)


def test_modularity_finetune_und():
    x = load_sample(thres=.4)

    seed = 94885236
    _, q = bc.modularity.modularity_finetune_und(x, seed=seed)
    assert np.allclose(q, .25879794)

    fails = 0
    for i in range(100):
        _, q = bc.modularity.modularity_finetune_und(x)
        try:
            assert np.allclose(q, .25, atol=0.03)
        except AssertionError:
            if fails >= 5:
                raise
            else:
                fails += 1

    seed = 71040925
    ci, oq = bc.modularity.modularity_louvain_und(x, seed=seed)
    _, q = bc.modularity.modularity_finetune_und(x, ci=ci, seed=seed)
    print(q, oq)
    # assert np.allclose(q, .25892588)
    assert np.allclose(q, .25856714)
    assert q - oq >= -1e6

    ci, oq = bc.modularity.modularity_und(x)
    for i in range(100):
        _, q = bc.modularity.modularity_finetune_und(x, ci=ci)
        assert np.allclose(q, .25, atol=0.002)
        assert q - oq >= -1e6

    # modularity_finetune_und appears to be very stable when given a stable ci
    # in thousands of test runs on the sample data (using the deterministic
    # modularity maximization algorithm), only two states appeared;
    # both improved the optimal modularity. a basic increase -- modules that
    # always benefited from switching -- always occurred. on top of that, a
    # slightly larger increase dependent on order occurred in both matlab and
    # bctpy around ~0.6% of the time. Due to numerical instability arising
    # from something different between matlab and scipy, these values were not
    # the same across languages, but both languages showed bistable transitions
    # they were extremely stable. The values were about .0015 apart.

    # also the matlab and python versions of modularity_und return slightly
    # different modular structure, but the instability is present despite this
    # (i.e. it is unstable both when the modular structure is identical and
    # not)


def test_modularity_louvain_und_sign_seed():
    # performance is same as matlab if randomness is quashed
    x = load_signed_sample()
    seed = 90772777
    _, q = bc.modularity.modularity_louvain_und_sign(x, seed=seed)
    print(q)
    assert np.allclose(q, .46605515)


def test_modularity_finetune_und_sign_actually_finetune():
    x = load_signed_sample()
    seed = 34908314
    ci, oq = bc.modularity.modularity_louvain_und_sign(x, seed=seed)
    _, q = bc.modularity.modularity_finetune_und_sign(x, seed=seed, ci=ci)
    print(q)
    assert np.allclose(q, .47282924)
    assert q >= oq

    seed = 88215881
    np.random.seed(seed)
    randomized_sample = np.random.random(size=(len(x), len(x)))
    randomized_sample = randomized_sample + randomized_sample.T
    x[np.where(bc.utils.threshold_proportional(randomized_sample, .2))] = 0

    ci, oq = bc.modularity.modularity_louvain_und_sign(x, seed=seed)
    print(oq)
    assert np.allclose(oq, .45254522)
    for i in range(100):
        _, q = bc.modularity.modularity_finetune_und_sign(x, ci=ci)
        assert q >= oq


def test_modularity_probtune_und_sign():
    x = load_signed_sample()
    seed = 59468096
    ci, q = bc.modularity.modularity_probtune_und_sign(x, seed=seed)
    print(q)
    assert np.allclose(q, .07885327)

    seed = 1742447
    ci, _ = bc.modularity.modularity_louvain_und_sign(x, seed=seed)
    _, oq = bc.modularity.modularity_finetune_und_sign(x, seed=seed, ci=ci)

    for i in np.arange(.05, .5, .02):
        fails = 0
        for j in range(100):
            _, q = bc.modularity.modularity_probtune_und_sign(x, ci=ci, p=i)
            try:
                assert q < oq
            except AssertionError:
                if fails > 5:
                    raise
                else:
                    fails += 1


def test_modularity_dir_low_modularity():
    x = load_directed_low_modularity_sample(thres=.67)
    _, q = bc.modularity.modularity_dir(x)
    assert np.allclose(q, .06450290)


def test_modularity_louvain_dir_low_modularity():
    x = load_directed_low_modularity_sample(thres=.67)
    seed = 28917147
    _, q = bc.modularity.modularity_louvain_dir(x, seed=seed)
    assert np.allclose(q, .06934894)


def test_modularity_dir():
    x = load_directed_sample()
    _, q = bc.modularity.modularity_dir(x)
    print(q, .32742787)
    assert np.allclose(q, .32742787)


def test_modularity_louvain_dir():
    x = load_directed_sample()
    seed = 43938304
    _, q = bc.modularity.modularity_louvain_dir(x, seed=seed)
    assert np.allclose(q, .32697921)


def test_community_louvain():
    x = load_sample(thres=0.4)
    seed = 39185
    ci, q = bc.modularity.community_louvain(x, seed=seed)
    print(q)
    assert np.allclose(q, 0.2583, atol=0.015)
