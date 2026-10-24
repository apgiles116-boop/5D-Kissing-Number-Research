#!/usr/bin/env python3
"""Exact symbolic checks for the isolated-center two-sided cap / D5 audit."""
import sympy as s
from itertools import combinations

x = s.symbols('x', real=True)
p = s.Rational(11, 36)*x**2 - s.Rational(1, 9)*x
assert s.simplify(-p - x*(4-11*x)/36) == 0
assert s.simplify((x-s.Rational(1,3))**2-p-(5*x-2)**2/36) == 0

u = s.symbols('u0:5', real=True)
values = []
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        values.append((u[i]+sign*u[j])**2/s.Integer(2))
S1 = s.expand(sum(values))
S2 = s.expand(sum(z*z for z in values))
norm = sum(z*z for z in u)
assert s.expand(S1-4*norm) == 0
assert s.expand(S2-(s.Rational(3,2)*norm**2+s.Rational(1,2)*sum(z**4 for z in u))) == 0
assert s.Rational(11,36)*s.Rational(8,5)-s.Rational(4,9) == s.Rational(2,45)
assert s.Rational(8,5)-s.Rational(4,3) == s.Rational(4,15)
assert 1-1/(4*s.Rational(2,5)) == s.Rational(3,8)

balanced = [s.simplify(z.subs({ui:1/s.sqrt(5) for ui in u})) for z in values]
assert balanced.count(s.Rational(2,5)) == 10
assert balanced.count(s.Integer(0)) == 10
hinge = sum((z-s.Rational(1,3))**2 for z in balanced if z>s.Rational(1,3))
assert s.simplify(hinge) == s.Rational(2,45)

# The earlier one-sided counterexample has a deep center neighbor.
assert s.Rational(-1,4)-s.Rational(3,4) == -1
print('PASS: exact SOS, D5 moments, balanced equality, covering gap, and audit')
