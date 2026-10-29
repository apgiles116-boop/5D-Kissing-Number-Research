#!/usr/bin/env python3
"""Exact Fraction/SymPy certificate for Type-E D5 shifted fourth-moment exclusion."""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

def check(T, B, left_threshold, right_threshold):
    cup = 1-T*T/2+T**4/24
    clo = 1-T*T/2
    slo = T-T**3/6
    q0up = cup/2+F(866026,1000000)*T
    q0lo = clo/2+F(866025,1000000)*slo
    q1up = F(577351,1000000)*cup+F(816497,1000000)*T
    assert F(1,4)*clo-F(3,10)*T>0
    assert F(3,8)*clo-F(73,80)*T>0
    left = F(8,5)-4*q0up*q0up
    right = 4*B*q1up*q1up*(q1up*q1up-q0lo*q0lo)
    assert left>left_threshold>right_threshold>right
    return left-right

assert F(866025,1000000)**2 < F(3,4) < F(866026,1000000)**2
assert F(577350,1000000)**2 < F(1,3) < F(577351,1000000)**2
assert F(816496,1000000)**2 < F(2,3) < F(816497,1000000)**2

T=F(16,125)
margin=check(T,F(383,504),F(1273,10000),F(1265,10000))
assert 2*(T-T**3/6)**2>F(1,32)

T2=F(27,200)
margin2=check(T2,F(567,1000),F(1,10),F(1,10)-F(1,10**12))
assert 2*(T2-T2**3/6)**2>F(9,250)

x=sp.symbols("x0:5",real=True)
p=sum((x[i]+x[j])**4/4+(x[i]-x[j])**4/4
      for i,j in combinations(range(5),2))
target=sp.Rational(3,2)*sum(t*t for t in x)**2+sp.Rational(1,2)*sum(t**4 for t in x)
assert sp.expand(p-target)==0
print("PASS exact D5 fourth moment and both rational angular exclusions")
print("Baseline positive margin:",margin)
print("Conditional stronger-cap margin:",margin2)
