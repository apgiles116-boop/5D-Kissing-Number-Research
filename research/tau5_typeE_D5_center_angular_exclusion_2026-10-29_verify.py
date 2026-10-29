#!/usr/bin/env python3
"""Exact SymPy/Fraction checks for the D5 center angular-exclusion theorem.
The analytic convexity and spherical-angle proof is in the companion note.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

v=sp.symbols('v0:5', real=True)
roots=[]
for i,j in combinations(range(5),2):
    for sign in (-1,1):
        c=[sp.Integer(0)]*5
        c[i]=sp.sqrt(2)/2
        c[j]=sign*sp.sqrt(2)/2
        roots.append(c)
assert len(roots)==20
corr=[sum(v[k]*r[k] for k in range(5)) for r in roots]
V2=sum(x*x for x in v)
assert sp.expand(sum(x*x for x in corr)-4*V2)==0
assert sp.expand(sum(x**4 for x in corr)-sp.Rational(3,2)*V2**2-sp.Rational(1,2)*sum(x**4 for x in v))==0
print('PASS: exact D5 second and fourth moments')

theta=F(2,25)
B=F(383,504)
C=1-theta**2/2+theta**4/24
assert F(17321,10000)**2>3
assert 3*F(577351,1000000)**2>1
assert 3*F(816497,1000000)**2>2
assert C>=F(623,625)
assert F(1,4)*F(623,625)-F(3,10)*theta>0
assert F(3,8)*F(623,625)-F(73,80)*theta>0
assert F(4,5)*F(623,625)-F(3,5)*theta>0
q0=F(1,2)*C+F(17321,20000)*theta
q1=F(577351,1000000)*C+F(816497,1000000)*theta
f=lambda x:x**4-x**2/4
assert q1>q0>=F(1,2)
U=(20-4*B)*f(q0)+4*B*f(q1)
gap=F(3,5)-U
assert gap==F(354233594839339286756640083873782082234484437099,
              79208984971046447753906250000000000000000000000000)
assert gap>0
assert 2*(theta-theta**3/6)**2-F(1,80)==F(9587387,35156250000)
print('PASS: exact trigonometric/radical bounds and derivative margins')
print('PASS: strict terminal gap:',gap)
print('CONDITIONAL THEOREM: maximum projective D5 angular error > 2/25 radians')
print('GLOBAL RANGE UNCHANGED: 40 <= tau_5 <= 44')
