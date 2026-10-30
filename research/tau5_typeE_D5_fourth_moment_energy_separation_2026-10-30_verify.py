#!/usr/bin/env python3
"""Exact symbolic/rational checks; the universal inequality is proved in the note."""
from fractions import Fraction as F
from itertools import combinations
from sympy import symbols, expand, factor
B=F(383,504)
c=F(3,20)-B/F(30)-B*B/F(60)
assert c==F(1753391,15240960) and c>F(1,15)
a=symbols('a', real=True)
assert factor(F(1,4)+a/F(3)-1/(4*(1-a))-a*(1-4*a)/(12*(1-a)))==0
v=symbols('v0:5', real=True)
second=fourth=0
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        s=(v[i]+sign*v[j])**2/F(2)
        second+=s
        fourth+=s*s
N=sum(x*x for x in v)
assert expand(second-4*N)==0
assert expand(fourth-(F(3,2)*N*N+F(1,2)*sum(x**4 for x in v)))==0
t,A=symbols('t A', real=True)
q=t*t/F(2)+(1-t)**2/F(3)
lhs=F(1,8)+q/F(8)-A*t/F(12)
rhs=F(3,20)-A/F(30)-A*A/F(60)+F(5,48)*(t-F(2,5)*(1+A))**2
assert expand(lhs-rhs)==0
print("PASSED: D5 moments, energy chord, completed square, exact cap")
print("d >= sqrt(2) *", c, "=", float(c)*2**0.5)
