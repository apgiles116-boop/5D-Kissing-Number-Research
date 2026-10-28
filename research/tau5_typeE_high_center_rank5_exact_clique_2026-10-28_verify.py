#!/usr/bin/env python3
"""Exact finite certificate: rank-six 17-vertex signed Gram cannot be
within squared Frobenius distance 1/16 of the PSD rank-five cone.

Dependencies: networkx, numpy, sympy.
All matrix arithmetic is exact integer/rational arithmetic; no floating
point eigensolvers are used. Optional NetworkX clique cross-check included.
"""
from collections import Counter
from itertools import product
from math import comb
import networkx as nx
import numpy as np
import sympy as sp

assert 4 * sp.Rational(158205281, 13475000000) < sp.Rational(1, 16)

def charpoly_int(A):
    """Integer Faddeev-LeVerrier recurrence for small matrices."""
    n = A.shape[0]
    B = np.eye(n, dtype=np.int64)
    I = B.copy()
    out = [1]
    for k in range(1, n + 1):
        P = A @ B
        tr = int(np.trace(P))
        assert tr % k == 0
        c = -(tr // k)
        out.append(c)
        B = P + c * I
    return tuple(out)

def roots_above(poly, p, q):
    """Exact roots > p/q, using real-rooted Descartes sign variations."""
    n = len(poly) - 1
    asc = poly[::-1]
    signs = []
    for j in range(n, -1, -1):
        v = sum(asc[k] * comb(k, j) * p ** (k-j) * q ** (n-k+j)
                for k in range(j, n+1))
        if v:
            signs.append(v > 0)
    return sum(a != b for a, b in zip(signs, signs[1:]))

def spectral_screen(poly):
    """Necessary 1/4 screen for six nonzero eigenvalues near PSD rank 5."""
    while poly[-1] == 0:
        poly = poly[:-1]
    assert len(poly) == 7
    return roots_above(poly, -1, 4) == 6 and roots_above(poly, 1, 4) < 6

def has_clique(adj, target):
    """Exact clique existence test with greedy-coloring upper bound."""
    n = len(adj)
    def color_bound(mask):
        colors = 0
        while mask:
            colors += 1
            available = mask
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                mask ^= bit
                available ^= bit
                available &= ~adj[v]
        return colors
    def rec(mask, size):
        if size >= target:
            return True
        if size + mask.bit_count() < target:
            return False
        if size + color_bound(mask) < target:
            return False
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            mask ^= bit
            if rec(mask & adj[v], size+1):
                return True
            if size + mask.bit_count() < target:
                return False
        return False
    return rec((1 << n)-1, 0)

def verify():
    atlas = [g for g in nx.graph_atlas_g() if len(g) == 6]
    assert len(atlas) == 156
    cols = np.array(list(product((-1,0,1), repeat=6)), dtype=np.int64)
    signings = bases = extensions = good7 = tested8 = good8 = 0
    under11 = 0
    clique_counts = Counter()
    for g in atlas:
        edges = sorted(tuple(sorted(e)) for e in g.edges())
        fixed = set(tuple(sorted(e)) for e in nx.minimum_spanning_tree(g).edges())
        free = [e for e in edges if e not in fixed]
        B = 2*np.eye(6, dtype=np.int64)
        for i,j in fixed:
            B[i,j] = B[j,i] = 1
        for signs in product((-1,1), repeat=len(free)):
            for (i,j), s in zip(free, signs):
                B[i,j] = B[j,i] = s
            signings += 1
            p6 = charpoly_int(B)
            if p6[-1] == 0 or not spectral_screen(p6):
                continue
            bases += 1
            mat = sp.Matrix(B.tolist())
            det = int(mat.det())
            assert det == p6[-1]
            adj = np.array(mat.adjugate()).astype(np.int64)
            q = np.einsum('ij,jk,ik->i', cols, adj, cols)
            selected = cols[q == 2*det]
            extensions += len(selected)
            surviving = []
            for c in selected:
                M7 = np.zeros((7,7), dtype=np.int64)
                M7[:6,:6] = B
                M7[:6,6] = c
                M7[6,:6] = c
                M7[6,6] = 2
                p7 = charpoly_int(M7)
                assert p7[-1] == 0 and p7[-2] != 0
                if spectral_screen(p7):
                    surviving.append(c)
            good7 += len(surviving)
            if len(surviving) < 11:
                under11 += 1
                continue
            surviving = np.array(surviving, dtype=np.int64)
            cross = surviving @ adj @ surviving.T
            adjacency = [0] * len(surviving)
            for i in range(len(surviving)):
                for j in range(i+1, len(surviving)):
                    num = int(cross[i,j])
                    if num % det != 0 or abs(num) > abs(det):
                        continue
                    tested8 += 1
                    t = num // det
                    M8 = np.zeros((8,8), dtype=np.int64)
                    M8[:6,:6] = B
                    M8[:6,6] = surviving[i]
                    M8[6,:6] = surviving[i]
                    M8[:6,7] = surviving[j]
                    M8[7,:6] = surviving[j]
                    M8[6,6] = M8[7,7] = 2
                    M8[6,7] = M8[7,6] = t
                    p8 = charpoly_int(M8)
                    assert p8[-1] == p8[-2] == 0 and p8[-3] != 0
                    if not spectral_screen(p8):
                        continue
                    good8 += 1
                    adjacency[i] |= 1 << j
                    adjacency[j] |= 1 << i
            assert not has_clique(adjacency, 11)
            omega = next(k for k in range(10,0,-1) if has_clique(adjacency,k))
            clique_counts[omega] += 1
            if omega >= 9:
                # Independent algorithm for the largest cases.
                check = nx.Graph()
                check.add_nodes_from(range(len(surviving)))
                check.add_edges_from((i,j) for i in range(len(surviving))
                    for j in range(i+1,len(surviving)) if (adjacency[i] >> j) & 1)
                assert max(map(len, nx.find_cliques(check))) == omega
    assert (signings,bases,extensions,good7,tested8,good8,under11) == (
        4562,246,10956,3010,27968,14404,137)
    assert sum(clique_counts.values()) == bases-under11
    assert max(clique_counts) == 10
    assert clique_counts[10] == 3 and clique_counts[9] == 4
    print('PASS: 156 atlas supports, 4562 signings, 246 eligible bases')
    print('PASS: 10956 Schur columns, 3010 seven-block survivors')
    print('PASS: 27968 eight-block tests, 14404 survivors')
    print('PASS: 137 bases too few columns; remaining maximum clique 10')
    print('CONDITIONAL: high-center rounded Gram rank <= 5')
    print('GLOBAL PROVED RANGE UNCHANGED: 40 <= tau_5 <= 44')

if __name__ == '__main__':
    verify()
