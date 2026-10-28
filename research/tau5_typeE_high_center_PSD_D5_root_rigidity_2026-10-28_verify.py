#!/usr/bin/env python3
"""Exact integral signed-Gram PSD rigidity certificate, ranks <= 5.

No floating-point calculations. Dependencies: networkx, numpy, sympy.
Enumerates every unlabeled support and switching-normalized signing,
then uses integer Schur complements and exact bitset clique bounds.
"""
from collections import Counter
from itertools import product, combinations
from math import comb
import networkx as nx
import numpy as np
import sympy as sp

def charpoly_int(A):
    n = A.shape[0]
    B = np.eye(n, dtype=np.int64)
    I = B.copy()
    out = [1]
    for k in range(1, n+1):
        P = A @ B
        tr = int(np.trace(P))
        assert tr % k == 0
        c = -(tr // k)
        out.append(c)
        B = P + c*I
    return tuple(out)

def roots_above(poly, p, q):
    """Exact real-root count above rational p/q."""
    n = len(poly)-1
    asc = poly[::-1]
    signs = []
    for j in range(n,-1,-1):
        val = sum(asc[k]*comb(k,j)*p**(k-j)*q**(n-k+j)
                  for k in range(j,n+1))
        if val:
            signs.append(val > 0)
    return sum(a != b for a,b in zip(signs,signs[1:]))

def has_clique(adj, target):
    n = len(adj)
    def color_bound(mask):
        colors = 0
        while mask:
            colors += 1
            available = mask
            while available:
                bit = available & -available
                v = bit.bit_length()-1
                mask ^= bit
                available ^= bit
                available &= ~adj[v]
        return colors
    def rec(mask, size):
        if size >= target:
            return True
        if size+mask.bit_count() < target:
            return False
        if size+color_bound(mask) < target:
            return False
        while mask:
            bit = mask & -mask
            v = bit.bit_length()-1
            mask ^= bit
            if rec(mask & adj[v],size+1):
                return True
            if size+mask.bit_count() < target:
                return False
        return False
    return rec((1<<n)-1,0)

def classify(rank, indefinite_only=False):
    atlas = [g for g in nx.graph_atlas_g() if len(g) == rank]
    cols = np.array(list(product((-1,0,1), repeat=rank)),dtype=np.int64)
    signings = eligible = max_clique = 0
    histogram = Counter()
    for g in atlas:
        edges = sorted(tuple(sorted(e)) for e in g.edges())
        fixed = set(tuple(sorted(e)) for e in nx.minimum_spanning_tree(g).edges())
        free = [e for e in edges if e not in fixed]
        B = 2*np.eye(rank,dtype=np.int64)
        for i,j in fixed:
            B[i,j] = B[j,i] = 1
        for signs in product((-1,1), repeat=len(free)):
            for (i,j),s in zip(free,signs):
                B[i,j] = B[j,i] = s
            signings += 1
            poly = charpoly_int(B)
            if poly[-1] == 0:
                continue
            if indefinite_only and roots_above(poly,0,1) == rank:
                continue
            eligible += 1
            mat = sp.Matrix(B.tolist())
            det = int(mat.det())
            assert det == (-1)**rank*poly[-1]
            adj = np.array(mat.adjugate()).astype(np.int64)
            q = np.einsum('ij,jk,ik->i',cols,adj,cols)
            selected = cols[q == 2*det]
            if len(selected) == 0:
                histogram[0] += 1
                continue
            cross = selected @ adj @ selected.T
            adjacency = [0]*len(selected)
            for i in range(len(selected)):
                for j in range(i+1,len(selected)):
                    num = int(cross[i,j])
                    if num%det == 0 and abs(num) <= abs(det):
                        adjacency[i] |= 1<<j
                        adjacency[j] |= 1<<i
            omega = next(k for k in range(len(selected),0,-1)
                         if has_clique(adjacency,k))
            if omega >= 5:
                check = nx.Graph()
                check.add_nodes_from(range(len(selected)))
                check.add_edges_from((i,j) for i in range(len(selected))
                    for j in range(i+1,len(selected)) if (adjacency[i]>>j)&1)
                assert max(map(len,nx.find_cliques(check))) == omega
            max_clique = max(max_clique,omega)
            histogram[omega] += 1
    assert sum(histogram.values()) == eligible
    return (len(atlas),signings,eligible,max_clique)

def check_D5():
    roots = []
    for i,j in combinations(range(5),2):
        for s in (-1,1):
            v = np.zeros(5,dtype=np.int64)
            v[i] = 1
            v[j] = s
            roots.append(v)
    assert len(roots) == 20
    X = np.array(roots,dtype=np.int64)
    H = X @ X.T
    assert np.all(np.diag(H) == 2)
    degrees = [sum(abs(int(H[i,j])) == 1 for j in range(20) if j != i)
               for i in range(20)]
    assert degrees == [12]*20
    assert sum(degrees)//2 == 120
    # Unit-vector frame: sum (r/sqrt(2))(r/sqrt(2))^T = 4I.
    assert np.array_equal(X.T@X,8*np.eye(5,dtype=np.int64))
    print('PASS: D5 has 20 lines, 12 neighbors per line, 120 edges, frame 4I')

def main():
    expected = {
        1:(1,1,1,0),
        2:(2,2,2,1),
        3:(4,5,4,3),
        4:(11,24,20,8),
        5:(34,220,164,5),
    }
    for r in range(1,6):
        got = classify(r,indefinite_only=(r==5))
        assert got == expected[r],(r,got)
        print('PASS: rank',r,'atlas/signings/eligible/max clique =',got)
    check_D5()
    print('PASS: order >=13 and rank <=5 forces PSD rank exactly five')
    print('CONDITIONAL TYPE E: rounded high-center 17-line system is D5')
    print('GLOBAL PROVED RANGE UNCHANGED: 40 <= tau_5 <= 44')

if __name__ == '__main__':
    main()
