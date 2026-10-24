#!/usr/bin/env python3
"""Exact rational checks for Type E capped Welch / six-exception theorem.

Analytic ingredients: frame trace identity, capped-simplex concentration,
and endpoint defect inequality. This script checks exact constants,
piecewise monotonicity, and contact-density arithmetic.
"""
from fractions import Fraction as F

B = F(383, 504)
D0 = F(1780062775, 4032758016)
old = F(17456771, 635040)

def g(A):
    assert 0 <= A <= B
    k = (4*A).numerator // (4*A).denominator
    r = A-F(k, 4)
    assert 0 <= r <= F(1, 4)
    return F(k, 16)+r*r

def f(A):
    return 30-3*A+A*A/10-g(A)/2

assert B == F(3, 4)+F(5, 504)
assert g(B) == F(3, 16)+F(5, 504)**2
L = f(B)
assert L == F(8790283, 317520)
assert L-old == F(131, 672)
K = L-F(3, 2)-F(5, 4)*D0
assert K == F(2067388216673, 80655160320)

# On each interval, f'=-3+A/5-(A-k/4), decreasing in A.
for k in range(4):
    left = F(k, 4)
    right = min(F(k+1, 4), B)
    if right <= left:
        continue
    assert -3+left/F(5) <= -F(57, 20)
    for j in range(101):
        A = left+(right-left)*F(j, 100)
        assert f(A) >= L+F(57, 20)*(B-A)

upper75 = 75*F(1, 4)+109*F(1, 16)
upper37 = 37*F(1, 4)+147*F(1, 9)
assert upper75 == F(409, 16)
assert upper37 == F(307, 12)
assert K > upper75 and K > upper37

# Within-part K2,2 bound for 0<=p<=1/4.
for j in range(101):
    p = F(j, 400)
    assert (F(1, 2)-p)**2 <= F(1, 4)-F(3, 4)*p

print("PASS: exact capped frame floor", L)
print("PASS: exact improvement", L-old)
print("PASS: safe squared-correlation floor", K)
print("PASS: >=76 safe pairs >1/4, >=38 safe pairs >1/3")
print("PASS: K2,2 within-part quadratic bound")
