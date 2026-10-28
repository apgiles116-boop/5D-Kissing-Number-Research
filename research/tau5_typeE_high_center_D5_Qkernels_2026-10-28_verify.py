#!/usr/bin/env python3
"""Exact D5 Q-kernel 17-line rank classification and support identities.

Uses integer arithmetic, a modular rank check for all 1140 omitted triples,
and exact SymPy rational ranks for representatives of both cases.
"""
from itertools import combinations
from collections import Counter
import numpy as np
import sympy as sp

roots, supports = [], []
for i,j in combinations(range(5),2):
    for s in (-1,1):
        x = np.zeros(5,dtype=int)
        x[i] = 1
        x[j] = s
        roots.append(x)
        supports.append((i,j))
X = np.array(roots,dtype=int)
assert len(X) == 20
assert np.array_equal(X.T @ X,8*np.eye(5,dtype=int))

# Integer 10*Q(unit) = 5*x*x^T - 2*I; use upper-triangle coordinates.
Q = []
for x in X:
    T = 5*np.outer(x,x)-2*np.eye(5,dtype=int)
    Q.append([int(T[i,j]) for i in range(5) for j in range(i,5)])
Q = np.array(Q,dtype=int)

def rankmod(A,p=1009):
    A = A.copy()%p
    m,n = A.shape
    r = 0
    for c in range(n):
        k = next((i for i in range(r,m) if A[i,c]),None)
        if k is None:
            continue
        A[[r,k]] = A[[k,r]]
        A[r] = A[r]*pow(int(A[r,c]),-1,p)%p
        for i in range(r+1,m):
            if A[i,c]:
                A[i] = (A[i]-A[i,c]*A[r])%p
        r += 1
        if r == m:
            break
    return r

assert rankmod(Q.T) == 14
counts = Counter()
for missing in combinations(range(20),3):
    kept = [i for i in range(20) if i not in missing]
    full_missing = (supports[missing[0]] == supports[missing[1]]
                    or supports[missing[0]] == supports[missing[2]]
                    or supports[missing[1]] == supports[missing[2]])
    expected = 13 if full_missing else 14
    rank = rankmod(Q[kept].T)
    assert rank == expected,(missing,rank,expected)
    counts[rank] += 1
assert counts == {13:180,14:960}

# Rational checks, independent of the modular enumeration.
for missing,expected in [((0,1,2),13),((0,2,4),14)]:
    kept = [i for i in range(20) if i not in missing]
    assert sp.Matrix(Q[kept].T).rank() == expected

# Q^+ + Q^- = S_ij, Q^+ - Q^- = O_ij, with exact integer scaling.
for k,(i,j) in enumerate(combinations(range(5),2)):
    xp = X[2*k+1]
    xm = X[2*k]
    Qp = 5*np.outer(xp,xp)-2*np.eye(5,dtype=int)
    Qm = 5*np.outer(xm,xm)-2*np.eye(5,dtype=int)
    S = np.zeros((5,5),dtype=int)
    S[i,i] = S[j,j] = 5
    S -= 2*np.eye(5,dtype=int)
    O = np.zeros((5,5),dtype=int)
    O[i,j] = O[j,i] = 5
    assert np.array_equal(Qp+Qm,2*S)
    assert np.array_equal(Qp-Qm,2*O)

# The sharp frame gap >=2 follows from the 3x3 omitted-line Gram:
# each diagonal =1 and each off-diagonal has absolute value <=1/2,
# hence its operator norm is <=2 by Gershgorin.
print('PASS: 960 Q-rank-14 subsets, 180 Q-rank-13 subsets')
print('PASS: exact support-sum identities, full D5 frame 4I')
print('PASS: analytic rounded 17-line frame gap >=2')
print('CONDITIONAL: true/rounded Gram kernel angles <1/17 and <1/18')
print('GLOBAL PROVED RANGE UNCHANGED: 40 <= tau_5 <= 44')
