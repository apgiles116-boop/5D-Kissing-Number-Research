#!/usr/bin/env python3
"""Exact finite certificate for conditional Type-E high-center rank <= 6.

Dependencies: networkx (graph atlas of all unlabeled graphs on <=7 vertices),
            numpy (ONLY int64 matrix multiplication; no floating-point arithmetic),
            sympy (exact rational inverse for two surviving 7x7 blocks).

All eigenvalue tests use the exact sign-variation count for real-rooted
integer characteristic polynomials evaluated at rational thresholds.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
import networkx as nx
import numpy as np
import sympy as sp

N = 7
E = Fraction(158205281, 13475000000)
TOL = 4 * E
assert Fraction(1, 144) + Fraction(441, 10000) > TOL


def charpoly_int(A):
    """Faddeev-LeVerrier with exact int64 operations for n<=8, |Aij|<=2."""
    n = A.shape[0]
    B = np.eye(n, dtype=np.int64)
    I = B.copy()
    out = [1]
    for k in range(1, n + 1):
        P = A @ B
        trace = int(np.trace(P))
        assert trace % k == 0
        c = -trace // k
        out.append(c)
        B = P + c * I
    return tuple(out)


def roots_above(poly, p, q):
    """Exact number of real roots strictly > p/q via Descartes variations."""
    n = len(poly) - 1
    asc = poly[::-1]
    shifted = []
    for j in range(n, -1, -1):
        numerator = sum(
            asc[k] * comb(k, j) * p ** (k-j) * q ** (n-k+j)
            for k in range(j, n + 1)
        )
        if numerator:
            shifted.append(1 if numerator > 0 else -1)
    return sum(a != b for a, b in zip(shifted, shifted[1:]))


def isolate_roots(poly, q=100000):
    """Seven real roots, increasing order, rational intervals width 1/q."""
    n = len(poly)-1
    intervals = []
    for rank in range(1, n+1):
        lo, hi = -6*q, 10*q
        while hi-lo > 1:
            mid = (lo+hi)//2
            if roots_above(poly, mid, q) <= n-rank:
                hi = mid
            else:
                lo = mid
        intervals.append((lo, hi))
    return intervals


def distance_bounds(poly, q=100000):
    """Bounds on squared Frobenius distance to PSD matrices of rank <=5."""
    intervals = isolate_roots(poly, q)
    assert all(lo >= 0 or hi <= 0 for lo,hi in intervals), (poly, intervals)
    negatives = sum(hi <= 0 for lo,hi in intervals)
    positives = len(intervals) - negatives
    discard = list(range(negatives)) + list(range(negatives, negatives+max(0,positives-5)))
    lower = sum(min(intervals[i][0]**2, intervals[i][1]**2) for i in discard)
    upper = sum(max(intervals[i][0]**2, intervals[i][1]**2) for i in discard)
    return Fraction(lower, q*q), Fraction(upper, q*q)


def normalized_signings(g):
    """One signing per spanning-forest switching assignment."""
    fixed = {tuple(sorted(e)) for e in nx.minimum_spanning_tree(g).edges()}
    edges = sorted(tuple(sorted(e)) for e in g.edges())
    free = [e for e in edges if e not in fixed]
    A = np.eye(7, dtype=np.int64)*2
    for i,j in fixed:
        A[i,j] = A[j,i] = 1
    for signs in product((-1,1), repeat=len(free)):
        for (i,j),sign in zip(free, signs):
            A[i,j] = A[j,i] = sign
        yield A, edges, signs


def exact_seven_basis_classification():
    atlas = [g for g in nx.graph_atlas_g() if len(g) == 7]
    assert len(atlas) == 1044
    poly_count = Counter()
    witnesses = {}
    signings = 0
    for ig,g in enumerate(atlas):
        for A,edges,signs in normalized_signings(g):
            signings += 1
            poly = charpoly_int(A)
            if abs(poly[-1]) not in (2,4):
                continue
            poly_count[poly] += 1
            if poly not in witnesses:
                witnesses[poly] = (ig, edges, signs, A.copy())
    assert signings == 197629
    assert sum(poly_count.values()) == 13812
    assert len(poly_count) == 4802

    survivors = []
    coarse_count = 0
    for poly in poly_count:
        nleft = roots_above(poly,-1,4)
        nright = roots_above(poly,1,4)
        if nleft != 7 or nleft-nright < 2:
            continue
        coarse_count += 1
        lower,upper = distance_bounds(poly)
        if lower > TOL:
            continue
        assert upper < TOL, ('needs finer isolation',poly,lower,upper)
        survivors.append((poly, witnesses[poly], poly_count[poly]))
    assert coarse_count == 111
    assert len(survivors) == 2
    assert sum(x[2] for x in survivors) == 2
    expected = {
        (1,-14,77,-210,292,-186,37,-2),
        (1,-14,76,-202,271,-166,33,-2),
    }
    assert {x[0] for x in survivors} == expected
    print('EXACT 7-basis classification:',signings,'normalized signings;',
          sum(poly_count.values()),'det=+/-2,+/-4;',len(poly_count),
          'distinct polynomials;',coarse_count,'coarse survivors; 2 exact survivors')
    return survivors


def exact_eighth_vertex_obstruction(survivors):
    for poly, (_, _, _, A), count in survivors:
        assert count == 1
        T = sp.Matrix(A.tolist())
        assert all(T[:k,:k].det()>0 for k in range(1,8))
        inv = T.inv()
        denom = sp.ilcm(*[entry.q for entry in inv])
        adj = inv*denom
        candidates = 0
        for values in product((-1,0,1), repeat=7):
            c = sp.Matrix(values)
            if (c.T*adj*c)[0] != 2*denom:
                continue
            candidates += 1
            M8 = np.zeros((8,8), dtype=np.int64)
            M8[:7,:7] = A
            M8[7,:7] = values
            M8[:7,7] = values
            M8[7,7] = 2
            p8 = charpoly_int(M8)
            assert p8[-1] == 0
            assert roots_above(p8,1,12) == 7, (poly,values,p8)
            assert roots_above(p8,21,100) >= 6, (poly,values,p8)
        assert candidates == 112
        print('EXACT extension obstruction:',poly,'has',candidates,
              'possible eighth-vertex columns; all fail the rank-five PSD proximity')


if __name__ == '__main__':
    survivors = exact_seven_basis_classification()
    exact_eighth_vertex_obstruction(survivors)
    print('PASS: conditional high-center rounded Gram has rank at most 6.')
    print('Global proved range unchanged: 40 <= tau_5 <= 44.')
