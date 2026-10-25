#!/usr/bin/env python3
"""Exact symbolic audit for the Type-E D5 ten-active-line / 1/10 orbit gap note.

The geometric counting proof and Cauchy--Schwarz proof are in the .md file.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import sympy as sp

q=sp.sqrt(2)/2
s=sp.symbols("s",real=True)
assert sp.simplify(s**2+2*(2*q-s)**2-(3*(s-4*q/3)**2+sp.Rational(4,3)))==0
assert 2*(1-q)<q
assert [4+2*k+comb(4-k,2) for k in range(4)]==[10,9,9,10]
assert 4+4==8

U,W=sp.symbols("U W",real=True)
S2=4
S4=sp.Rational(3,2)+U/2
S6=(15*U-11*W)/4
assert sp.simplify(S4-S2/4-(1+U)/2)==0
assert sp.simplify((sp.Rational(5,3)*S6+sp.Rational(5,8)*S4).subs(W,U**2)-((15+105*U)/16-sp.Rational(55,12)*U**2))==0
assert sp.simplify(160*(1+U)**2-27*((15+105*U)/4-sp.Rational(55,3)*U**2)-sp.Rational(5,4)*(524*U**2-311*U+47))==0
assert sp.discriminant(524*U**2-311*U+47,U)==-1791

assert sp.Rational(383,504)<sp.Rational(19,25)
assert 3*231**2-400**2==83
C=4/sp.sqrt(3)-2
assert sp.simplify(sp.Rational(31,100)-C)>0
eps=F(1,10); AA=F(19,25); CC=F(31,100)
upper=10*eps**2+2*CC*AA*eps+CC**2*AA/4
assert upper==F(165379,1000000)
assert F(27,160)-upper==F(3371,1000000)

lines=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=sp.zeros(5,1); v[i]=q; v[j]=sign*q
        lines.append(v)
assert len(lines)==20
centers=[sp.ones(5,1)/sp.sqrt(5),
         sp.Matrix([1,0,0,0,0]),
         sp.Matrix([1,1,0,0,0])/sp.sqrt(2),
         sp.Matrix([1,1,1,0,0])/sp.sqrt(3)]
for x in centers:
    assert sp.simplify((x.T*x)[0]-1)==0
    t2=[sp.simplify((x.dot(v))**2) for v in lines]
    qq=[sp.simplify(y**2) for y in x]
    uval=sum(y**2 for y in qq); wval=sum(y**3 for y in qq)
    assert sp.simplify(sum(t2)-4)==0
    assert sp.simplify(sum(y**2 for y in t2)-(sp.Rational(3,2)+uval/2))==0
    assert sp.simplify(sum(y**3 for y in t2)-(15*uval-11*wval)/4)==0
    assert sum(bool(sp.simplify(y-sp.Rational(1,4))>0) for y in t2)<=10

print("PASS: exact D5 counting, moment, and rational 1/10 orbit-gap checks.")
print("Contradiction margin:",F(27,160)-upper)
