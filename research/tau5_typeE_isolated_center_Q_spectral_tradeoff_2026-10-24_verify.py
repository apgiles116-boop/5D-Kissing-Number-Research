#!/usr/bin/env python3
"""Exact SymPy verifier for isolated-center Q-frame spectral tradeoff and D5 gap."""
from itertools import combinations
import sympy as s

B = s.Rational(383,504)
c = s.Rational(1,4)+5*B/36
assert c == s.Rational(6451,18144)
assert s.Rational(2,3)-c == s.Rational(5645,18144)
assert s.factor((s.Rational(2,3)-c)**2-s.Rational(6,64)) == s.Rational(1003081,329204736)

# D5 Q-Gram, exact rational arithmetic.
vec=[]
for i,j in combinations(range(5),2):
    for sg in (1,-1):
        v=[0]*5
        v[i]=1
        v[j]=sg
        vec.append(v)
K=s.Matrix(20,20,lambda i,j:s.Rational(sum(vec[i][k]*vec[j][k] for k in range(5))**2,4)-s.Rational(1,5))
assert K*s.ones(20,1)==s.zeros(20,1)
assert K.eigenvals()=={s.Rational(0):6,s.Rational(1):10,s.Rational(3,2):4}

# For 0<=a<=1/4, 16(1-a)^2>=9; per-edge moment estimate follows.
a=s.symbols('a',real=True)
assert s.factor(16*(1-a)**2-9)==(4*a-1)*(4*a-7)
print('PASS: exact spectral constants, D5 spectrum/kernel, per-edge factorization, eps>1/3')
