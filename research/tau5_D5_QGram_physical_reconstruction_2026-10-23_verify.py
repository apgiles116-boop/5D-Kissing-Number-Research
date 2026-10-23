#!/usr/bin/env python3
"""Exact rational checks for D5 physical Q-Gram reconstruction.

The simultaneous-diagonalization and compactness arguments are analytic,
not consequences of the finite computation.
"""
from itertools import combinations
from sympy import Matrix, Rational, eye, zeros

n = 5
edges = list(combinations(range(n), 2))
I = eye(n)
P, S = {}, {}
for a, b in edges:
    va, vb = I[:, a], I[:, b]
    P[a, b, '+'] = (va + vb) * (va + vb).T / 2
    P[a, b, '-'] = (va - vb) * (va - vb).T / 2
    S[a, b] = P[a, b, '+'] + P[a, b, '-']

assert all(X*X == X and X.trace() == 2 for X in S.values())
assert sum(S.values(), zeros(n)) == 4*I
for e, f in combinations(edges, 2):
    common = len(set(e) & set(f))
    assert (S[e]*S[f]).trace() == common
    assert S[e]*S[f] == S[f]*S[e]
    for a in ('+', '-'):
        for b in ('+', '-'):
            assert (P[e[0],e[1],a]*P[f[0],f[1],b]).trace() == Rational(common,4)
for e in edges:
    assert (P[e[0],e[1],'+']*P[e[0],e[1],'-']).trace() == 0

labels = list(P)
Q = {k: P[k]-I/5 for k in labels}
G = Matrix([[(Q[k]*Q[j]).trace() for j in labels] for k in labels])
assert G.rank() == 14
assert all(G[i,i] == Rational(4,5) for i in range(20))
assert all(G[i,j] == (P[labels[i]]*P[labels[j]]).trace()-Rational(1,5)
           for i in range(20) for j in range(20))
assert sum((P[k]*P[j]).trace() for k in labels for j in labels) == 80

# Four pairwise-intersecting edges in K5 must be a vertex star.
families = [c for c in combinations(edges, 4)
            if all(set(e)&set(f) for e,f in combinations(c,2))]
stars = [frozenset(e for e in edges if a in e) for a in range(n)]
assert len(families) == 5
assert {frozenset(c) for c in families} == set(stars)

# One support's +/- labels can be swapped without changing the Q-Gram.
swapped = list(labels)
i, j = swapped.index((0,1,'+')), swapped.index((0,1,'-'))
swapped[i], swapped[j] = swapped[j], swapped[i]
assert Matrix([[(Q[k]*Q[l]).trace() for l in swapped] for k in swapped]) == G

# An explicit rational orthogonal conjugation preserves the Q-Gram.
v = Matrix([1,2,3,4,5])
U = I-2*v*v.T/v.dot(v)
assert U.T*U == I
R = {k: U*P[k]*U.T-I/5 for k in labels}
assert Matrix([[(R[k]*R[l]).trace() for l in labels] for k in labels]) == G
print("PASS: rational 20-line D5 Q-Gram, rank 14, frame 4I")
print("PASS: all ten support-projector overlap and commutation identities")
print("PASS: all K5 four-edge intersecting families are the five stars")
print("PASS: within-support swap ambiguity and rational O(5) invariance")
print("Analytic steps: 3D projector lemma, simultaneous diagonalization, compactness")
