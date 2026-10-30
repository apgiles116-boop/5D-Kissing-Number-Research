#!/usr/bin/env python3
"""Exact rational terminal checks for the Type-E tight-frame separation theorem.

Analytic inequalities are proved in the accompanying Markdown note; this
verifies the three rational thresholds and D5's unit-norm tight-frame identity.
"""
from fractions import Fraction as F
from itertools import combinations

assert F(99,70)**2 > 2
L_historical = F(35017,10000)+F(383,1512)
L_harmonic = F(35017,10000)+F(189,1000)
L_atlas = F(209,60)+F(189,1000)
assert L_historical == F(7096963,1890000)
assert L_harmonic == F(36907,10000)
assert L_atlas == F(11017,3000)

for n, L in [(46,L_historical),(37,L_harmonic),(34,L_atlas)]:
    x=F(1,2*n*n)
    assert 0 < x < F(1,2)
    # (1-x) - (1-x/2-x^2)^2 = x^2*(7/4-x-x^2) >= 0
    assert F(7,4)-x-x*x > 0
    bracket=1-x/F(2)-x*x-F(99,70*n)
    assert bracket>0
    lower=4*bracket*bracket
    margin=lower-L
    assert margin>0, (n,margin)
    print(f"n={n}: Lcap={L}; lower={lower}; exact margin={margin}")

D=4-L_atlas
V=F(5,4)*D*D
assert D==F(983,3000)
assert V==F(966289,7200000)
print(f"normalized Q variance > {V} ({float(V):.12f})")

# Exact D5 20-projective-line tight-frame check: sum of the +/- root
# outer products for each support equals the support-plane projector.
frame=[[F(0) for _ in range(5)] for __ in range(5)]
for p,q in combinations(range(5),2):
    for sign in (-1,1):
        frame[p][p]+=F(1,2)
        frame[q][q]+=F(1,2)
        frame[p][q]+=F(sign,2)
        frame[q][p]+=F(sign,2)
assert frame == [[F(4) if p==q else F(0) for q in range(5)] for p in range(5)]
print("PASS: exact rational thresholds, variance floor, D5 tight-frame identity")
