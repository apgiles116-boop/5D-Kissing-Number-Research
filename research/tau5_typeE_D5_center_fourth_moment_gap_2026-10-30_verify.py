#!/usr/bin/env python3
"""Exact SymPy regression for D5 isolated-center covering and moment gap.

The accompanying note supplies the universal proofs; this script checks
the identities symbolically and 3124 nonzero integer test directions.
"""
from itertools import combinations, product
import sympy as S

v = S.symbols("v0:5", real=True)
roots = []
for p, q in combinations(range(5), 2):
    for sign in (1, -1):
        r = S.zeros(5, 1)
        r[p] = 1/S.sqrt(2)
        r[q] = sign/S.sqrt(2)
        roots.append(r)
assert len(roots) == 20
V = S.Matrix(v)
s = [S.expand((V.dot(r))**2) for r in roots]
R = sum(x*x for x in v)
assert S.simplify(sum(s) - 4*R) == 0
assert S.simplify(sum(x*x for x in s)
    - (S.Rational(3, 2)*R**2 + S.Rational(1, 2)*sum(x**4 for x in v))) == 0

uniform = S.Matrix([1/S.sqrt(5)]*5)
axis = S.Matrix([1, 0, 0, 0, 0])
for x in (uniform, axis):
    ss = [S.simplify((x.dot(r))**2) for r in roots]
    assert sum(ss) == 4
    assert sum(t*t for t in ss) == S.Rational(3, 2)+sum(t**4 for t in x)/2
    assert max(ss) >= S.Rational(2, 5)
assert max(S.simplify((uniform.dot(r))**2) for r in roots) == S.Rational(2, 5)
assert S.Rational(8, 5)-S.Rational(4, 3) == S.Rational(4, 15)
assert S.Rational(2, 5)-S.Rational(1, 3) == S.Rational(1, 15)
assert S.Rational(3, 4)*S.Rational(2, 5)-S.Rational(1, 4) == S.Rational(1, 20)

count = 0
for coords in product(range(-2, 3), repeat=5):
    norm2 = sum(t*t for t in coords)
    if not norm2:
        continue
    t = S.Matrix(coords)
    ss = [S.simplify((t.dot(r))**2/norm2) for r in roots]
    assert max(ss) >= S.Rational(2, 5), coords
    assert sum(x*x-x/S.Integer(3) for x in ss) >= S.Rational(4, 15), coords
    count += 1
assert count == 3124
print("PASS: symbolic D5 second/fourth moment identities")
print("PASS: sharp covering and moment gap for", count, "integer directions")
print("PASS: exact gaps 4/15, 1/15 and 1/20")
