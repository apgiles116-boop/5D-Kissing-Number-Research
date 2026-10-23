#!/usr/bin/env python3
"""Exact rational and polynomial checks for D5 center-covering theorem.

The spectral gap is proved analytically in the accompanying note; this
script checks the exact finite identities used in that proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from sympy import Matrix, Rational, symbols, sqrt, simplify, expand

lines = []
for a,b in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[a]=1
        v[b]=sign
        lines.append(Matrix(v))
assert len(lines)==20

W=Matrix.hstack(*lines)/sqrt(2)
S=sum((v*v.T/2 for v in lines), Matrix.zeros(5))
assert S==4*Matrix.eye(5)
F0=simplify(W.T*W)
assert F0.rank()==5 and F0*F0==4*F0

x=symbols('x0:5', real=True)
quartic=expand(sum((sum(v[i]*x[i] for i in range(5)))**4/4 for v in lines))
norm2=sum(t*t for t in x)
target=Rational(3,2)*norm2**2+Rational(1,2)*sum(t**4 for t in x)
assert simplify(quartic-target)==0

u=Matrix([1/sqrt(5)]*5)
absdots=[abs(simplify((u.T*v)[0]/sqrt(2))) for v in lines]
assert max(absdots)==sqrt(Rational(2,5))
assert sum(F0[i,j]**2 for i in range(20) for j in range(i+1,20))==30
assert sum(F0[i,j]**4 for i in range(20) for j in range(20))==35

eps=Q(1,5)
s=eps/(4-eps)
assert s==Q(1,19)
assert simplify(sqrt(1-Rational(1,19**2))/sqrt(10)-Rational(1,19))==Rational(5,19)
assert Q(5,19)>Q(1,4)
assert simplify(Rational(5,19)*sqrt(Rational(19,5))-sqrt(Rational(5,19)))==0

A,R=symbols('A R')
assert simplify(Rational(8,5)-(1-A/20+R/4)
                -(Rational(3,5)+A/20-R/4))==0
print('PASS: exact 20-line D5 frame and Gram identities')
print('PASS: sharp covering equality and D5 quartic polynomial')
print('PASS: eps=1/5 rational spectral contradiction')
print('PASS: fourth-moment/variance coefficient identity')
print('STATUS: conditional isolated-center theorems; tau_5 remains in [40,44]')
