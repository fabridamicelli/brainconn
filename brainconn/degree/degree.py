"""
Metrics which measure the number of edges connected to nodes.
"""
from __future__ import division, print_function
import numpy as np
from ..utils import binarize


def degrees_dir(CIJ):
    """
    Node degree is the number of links connected to the node. The indegree
    is the number of inward links and the outdegree is the number of
    outward links.

    Parameters
    ----------
    CIJ : NxN :obj:`numpy.ndarray`
        directed binary/weighted connection matrix

    Returns
    -------
    in_degree : Nx1 :obj:`numpy.ndarray`
        node in-degree
    out_degree : Nx1 :obj:`numpy.ndarray`
        node out-degree
    deg : Nx1 :obj:`numpy.ndarray`
        node degree (in-degree + out-degree)

    Notes
    -----
    Inputs are assumed to be on the columns of the CIJ matrix.
           Weight information is discarded.
    """
    CIJ = binarize(CIJ, copy=True)  # ensure CIJ is binary
    in_degree = np.sum(CIJ, axis=0)  # indegree = column sum of CIJ
    out_degree = np.sum(CIJ, axis=1)  # outdegree = row sum of CIJ
    deg = in_degree + out_degree  # degree = indegree+outdegree
    return in_degree, out_degree, deg


def degrees_und(CIJ):
    """
    Node degree is the number of links connected to the node.

    Parameters
    ----------
    CIJ : NxN :obj:`numpy.ndarray`
        undirected binary/weighted connection matrix

    Returns
    -------
    deg : Nx1 :obj:`numpy.ndarray`
        node degree

    Notes
    -----
    Weight information is discarded.
    """
    CIJ = binarize(CIJ, copy=True)  # ensure CIJ is binary
    return np.sum(CIJ, axis=0)


def jdegree(CIJ):
    """
    This function returns a matrix in which the value of each element (u,v)
    corresponds to the number of nodes that have u outgoing connections
    and v incoming connections.

    Parameters
    ----------
    CIJ : NxN :obj:`numpy.ndarray`
        directed binary/weighted connnection matrix

    Returns
    -------
    J : ZxZ :obj:`numpy.ndarray`
        joint degree distribution matrix
        (shifted by one, replicates matlab one-based-indexing)
    J_od : int
        number of vertices with out_degree>in_degree
    J_id : int
        number of vertices with in_degree>out_degree
    J_bl : int
        number of vertices with in_degree==out_degree

    Notes
    -----
    Weights are discarded.
    """
    CIJ = binarize(CIJ, copy=True)  # ensure CIJ is binary
    n_nodes = len(CIJ)
    in_degree = np.sum(CIJ, axis=0)  # indegree = column sum of CIJ
    out_degree = np.sum(CIJ, axis=1)  # outdegree = row sum of CIJ

    # create the joint degree distribution matrix
    # note: the matrix is shifted by one, to accomodate zero in_degree and
    # out_degree in the first row/column
    # upper triangular part of the matrix has vertices with
    # out_degree>in_degree
    # lower triangular part has vertices with in_degree>out_degree
    # main diagonal has units with in_degree=out_degree

    szJ = np.max((in_degree, out_degree)) + 1
    J = np.zeros((szJ, szJ))

    for i in range(n_nodes):
        J[in_degree[i], out_degree[i]] += 1

    J_od = np.sum(np.triu(J, 1))
    J_id = np.sum(np.tril(J, -1))
    J_bl = np.sum(np.diag(J))
    return J, J_od, J_id, J_bl


def strengths_dir(CIJ):
    """
    Node strength is the sum of weights of links connected to the node. The
    instrength is the sum of inward link weights and the outstrength is the
    sum of outward link weights.

    Parameters
    ----------
    CIJ : NxN :obj:`numpy.ndarray`
        directed weighted connection matrix

    Returns
    -------
    is : Nx1 :obj:`numpy.ndarray`
        node in-strength
    os : Nx1 :obj:`numpy.ndarray`
        node out-strength
    str : Nx1 :obj:`numpy.ndarray`
        node strength (in-strength + out-strength)

    Notes
    -----
    Inputs are assumed to be on the columns of the CIJ matrix.
    """
    istr = np.sum(CIJ, axis=0)
    ostr = np.sum(CIJ, axis=1)
    return istr, ostr, istr + ostr


def strengths_und(CIJ):
    """
    Node strength is the sum of weights of links connected to the node.

    Parameters
    ----------
    CIJ : NxN :obj:`numpy.ndarray`
        undirected weighted connection matrix

    Returns
    -------
    str : Nx1 :obj:`numpy.ndarray`
        node strengths
    """
    return np.sum(CIJ, axis=0)


def strengths_und_sign(W):
    """
    Node strength is the sum of weights of links connected to the node.

    Parameters
    ----------
    W : NxN :obj:`numpy.ndarray`
        undirected connection matrix with positive and negative weights

    Returns
    -------
    Spos : Nx1 :obj:`numpy.ndarray`
        nodal strength of positive weights
    Sneg : Nx1 :obj:`numpy.ndarray`
        nodal strength of positive weights
    vpos : float
        total positive weight
    vneg : float
        total negative weight
    """
    W = W.copy()
    np.fill_diagonal(W, 0)  # clear diagonal
    Spos = np.sum(W * (W > 0), axis=0)  # positive strengths
    Sneg = np.sum(W * (W < 0), axis=0)  # negative strengths

    vpos = np.sum(W[W > 0])  # positive weight
    vneg = np.sum(W[W < 0])  # negative weight
    return Spos, Sneg, vpos, vneg
