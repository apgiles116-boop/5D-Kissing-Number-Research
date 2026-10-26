#!/usr/bin/env python3
"""Exact rational verification of the D5 weighted-mixing gap.

This certifies a D5-template CONDITIONAL result, NOT a Type-E exclusion.
Requires sympy. All PSD checks use integer principal minors.
"""
from itertools import combinations
import sympy as sp

R = sp.Rational
roots = []
labels = []
for i, j in combinations(range(5), 2):
    for sign in (1, -1):
        v = sp.zeros(5, 1)
        v[i] = sp.sqrt(2)/2
        v[j] = sign*sp.sqrt(2)/2
        roots.append(v)
        labels.append((i, j, sign))
assert len(roots) == 20
u = roots[0]
contacts = [j for j in range(1, 20) if sp.simplify(u.dot(roots[j])**2) == R(1, 4)]
assert len(contacts) == 12
W0 = sp.zeros(5)
for j in contacts:
    W0 += R(1, 4) * roots[j] * roots[j].T
assert W0 == sp.diag(R(3,4),R(3,4),R(1,2),R(1,2),R(1,2))

# Three deletions are worst in Loewner order. Signed coordinate
# permutation symmetry allows fixing u=(e1+e2)/sqrt(2).
min_leading = [None]*5
for removed in combinations(contacts, 3):
    W = W0 - sum((R(1,4)*roots[j]*roots[j].T for j in removed), sp.zeros(5))
    T = 32*W - 3*sp.eye(5)
    assert all(x.q == 1 for x in T)
    for k in range(1, 6):
        d = int(T[:k,:k].det(method='domain-ge'))
        assert d > 0, (removed, k, d)
        if min_leading[k-1] is None or d < min_leading[k-1]:
            min_leading[k-1] = d
assert min_leading == [9,189,13,169,2197], min_leading

# A witness demonstrates near-optimality of the rational constant.
removed = (2,3,8)
W = W0 - sum((R(1,4)*roots[j]*roots[j].T for j in removed), sp.zeros(5))
eigs = W.eigenvals()
assert (R(3,8)-sp.sqrt(5)/8) in eigs, eigs
assert R(3,8)-sp.sqrt(5)/8 > R(3,32)

# Optional exact perturbation bound for epsilon <= 1/1000.
e = R(1,1000)
delta = 2*e + e**2
per_pair = delta*(1+delta)*(1+e)**2 + e*(2+e)/4
assert per_pair < R(13,5)*e
assert 19*R(13,5) < 50
assert R(3,32)-50*e == R(7,160)
assert R(1,2)-50*e == R(9,20)
print('PASS: 220 exact five-by-five Sylvester tests, contact counts,')
print('      D5 weighted-mixing gap 3/32, sharpness witness,')
print('      and rational perturbation constants.')
print('Minimum leading principal minors of 32W-3I:', min_leading)
print('Witness minimum eigenvalue:', R(3,8)-sp.sqrt(5)/8)
