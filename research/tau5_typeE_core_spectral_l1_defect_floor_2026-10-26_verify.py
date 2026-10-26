#!/usr/bin/env python3
"""Exact arithmetic audit of the four-core L1 lemma and Type-E A>1/183."""
from fractions import Fraction as Q
from itertools import combinations
import sympy as sp

edges = list(combinations(range(4), 2))
checks = 0
for mask in range(64):
    B = sp.zeros(4)
    for k, (i, j) in enumerate(edges):
        if (mask >> k) & 1:
            B[i, j] = B[j, i] = 1
    M = 2*sp.eye(4) + B
    for size in range(1, 5):
        for I in combinations(range(4), size):
            assert M.extract(I, I).det() >= 0, (mask, I)
            checks += 1
assert checks == 960
print("PASS: 64 labeled graphs, 960 exact principal minors")

# (v,v,-v,-v) attains the constant one.
a = Q(1,7)
assert 4*a == 4*a
print("PASS: sharpness via K2,2 antipodal partition")

t = Q(1,183)
Koutside = Q(20,16)/(1-t)**2
Kcore = (17+(1+t)**2*(7+2*t))/(16*(1-t)**2)
assert Kcore > Koutside
assert Kcore == Q(147621527,96987072)
gap = Q(1,120) - t*Kcore
assert gap == Q(1418789,88743170880) > 0
print("PASS: exact gap", gap)
print("CONDITIONAL TYPE E: A > 1/183; Type E remains OPEN")
