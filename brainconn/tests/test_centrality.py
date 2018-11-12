# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import os.path as op

import pytest
import numpy as np
from brainconn import centrality
from brainconn.tests.utils import (load_sample, MAT_DIR)


@pytest.fixture(scope='module')
def testdata1():
    """
    Undirected data.
    """
    n_nodes = 200
    corr = np.random.random((n_nodes, n_nodes))
    corr += corr.T  # Make symmetric
    wei = corr - np.eye(n_nodes)
    bin_ = (wei > np.mean(wei)).astype(int)
    data_dict = {'corr': corr,
                 'wei': wei,
                 'bin': bin_,
                 }
    return data_dict


@pytest.fixture(scope='module')
def testdata2():
    """
    Directed data.
    """
    n_nodes = 200
    corr = np.random.random((n_nodes, n_nodes))
    wei = corr - np.eye(n_nodes)
    bin_ = (wei > np.mean(wei)).astype(int)
    data_dict = {'corr': corr,
                 'wei': wei,
                 'bin': bin_,
                 }
    return data_dict


def test_node_betweenness_bin(testdata1):
    """
    Smoke test for brainconn.centrality.betweenness_bin.
    """
    node_betw = centrality.betweenness_bin(testdata1['bin'])
    assert node_betw.shape == testdata1['bin'].shape[:1]


def test_node_betweenness_wei(testdata1):
    """
    Smoke test for brainconn.centrality.betweenness_wei.
    """
    node_betw = centrality.betweenness_wei(testdata1['wei'])
    assert node_betw.shape == testdata1['wei'].shape[:1]


def test_edge_betweenness_bin(testdata1):
    """
    Smoke test for brainconn.centrality.edge_betweenness_wei.
    """
    edge_betw, node_betw = centrality.edge_betweenness_wei(testdata1['bin'])
    assert edge_betw.shape == testdata1['bin'].shape
    assert node_betw.shape == testdata1['bin'].shape[:1]


def test_edge_betweenness_wei(testdata1):
    """
    Smoke test for brainconn.centrality.edge_betweenness_wei.
    """
    edge_betw, node_betw = centrality.edge_betweenness_wei(testdata1['wei'])
    assert edge_betw.shape == testdata1['wei'].shape
    assert node_betw.shape == testdata1['wei'].shape[:1]


def test_erange(testdata2):
    """
    Smoke test for brainconn.centrality.erange.
    """
    erange, eta, eshort, fs = centrality.erange(testdata2['bin'])
    assert erange.shape == testdata2['bin'].shape
    assert isinstance(eta, float)
    assert eshort.shape == testdata2['bin'].shape
    assert isinstance(fs, float)


def test_kcoreness_centrality_bd(testdata2):
    """
    Smoke test for brainconn.centrality.kcoreness_centrality_bd.
    """
    coreness, kn = centrality.kcoreness_centrality_bd(testdata2['bin'])
    assert coreness.shape == testdata2['bin'].shape[:1]
    assert kn.shape == testdata2['bin'].shape[:1]


def test_kcoreness_centrality_bu(testdata1):
    """
    Smoke test for brainconn.centrality.kcoreness_centrality_bu.
    """
    coreness, kn = centrality.kcoreness_centrality_bu(testdata1['bin'])
    assert coreness.shape == testdata1['bin'].shape[:1]
    assert kn.shape == testdata1['bin'].shape[:1]


def test_pc():
    x = load_sample(thres=.4)
    # ci,q = bc.modularity_und(x)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    pc = np.load(op.join(MAT_DIR, 'sample_pc.npy'))

    pc_ = centrality.participation_coef(x, ci)
    print(list(zip(pc, pc_)))

    assert np.allclose(pc, pc_, atol=0.02)


def test_participation():
    W = np.eye(3)
    ci = np.array([1, 1, 2])

    assert np.allclose(centrality.participation_coef(W, ci), [0, 0, 0])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0, 0, 0])

    W = np.ones((3, 3))
    assert np.allclose(centrality.participation_coef(W, ci), [
        0.44444444, 0.44444444, 0.44444444])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0], [
        0.44444444, 0.44444444, 0.44444444])

    W = np.eye(3)
    W[0, 1] = 1
    W[0, 2] = 1
    assert np.allclose(centrality.participation_coef(W, ci),
                       [0.44444444, 0, 0])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0.44444444, 0, 0])

    W = np.eye(3)
    W[0, 1] = -1
    W[0, 2] = -1
    W[1, 2] = 1
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0., 0.5, 0.])


def test_gateway():
    x = load_sample(thres=.1)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    g_pos, _ = centrality.gateway_coef_sign(x, ci)

    print(np.sum(g_pos), 43.4382)
    assert np.allclose(np.sum(g_pos), 43.4382, atol=.001)

    gpb, _ = centrality.gateway_coef_sign(x, ci, centrality_type='betweenness')

    print(np.sum(gpb), 43.4026)
    assert np.allclose(np.sum(gpb), 43.4026, atol=.001)


def test_zi():
    x = load_sample(thres=.4)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    zi = np.load(op.join(MAT_DIR, 'sample_zi.npy'))

    zi_ = centrality.module_degree_zscore(x, ci)
    print(list(zip(zi, zi_)))

    assert np.allclose(zi, zi_, atol=0.05)
    # this function does the same operations but varies by a modest quantity
    # because of the matlab and numpy differences in population versus
    # sample standard deviation. i tend to think that using the population
    # estimator is acceptable in this case so i will allow the higher
    # tolerance.

# TODO this test does not give the same results, why not


def test_shannon_entropy():
    x = load_sample(thres=0.4)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))
    hpos, _ = centrality.diversity_coef_sign(x, ci)
    print(np.sum(hpos))
    print(hpos[-1])
    assert np.allclose(np.sum(hpos), 102.6402, atol=.01)
