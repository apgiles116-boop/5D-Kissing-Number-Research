#!/usr/bin/env python3
"""Exact rational checker for the Type-E outside-16 deletion-robust frame note.
The analytic proof of Gegenbauer positivity, Jensen and Schur-convexity
is in the companion Markdown note; this verifies its finite certificates.
"""
from fractions import Fraction as Q
import sympy as sp

B = Q(383,504)

def F(c):
    x=[1/(1-t) for t in c]
    return sum(((x[i]*x[j])**2-x[i]*x[j])
               for i in range(len(c)) for j in range(i+1,len(c)))/8

def majorant(n,L):
    p=[Q(0)]
    p += [Q(k,4)+Q(5,2)*L/(1+2*L/k) for k in (1,2,3)]
    p += [B+3*L/(1+2*L/n)]
    v=[p[k]-p[k-1] for k in range(1,5)]+[Q(0)]*(n-4)
    assert all(0<=t<1 for t in v)
    assert all(v[i]>=v[i+1] for i in range(n-1))
    return v

si,sj,a,s=sp.symbols("si sj a s")
assert sp.simplify((1+2*si**2)*(1+2*sj**2)
                   -(1+2*si*sj)**2-2*(si-sj)**2)==0
c=(a+3*s)/(1+2*s)
assert sp.simplify(c-a-(3-2*a)*s/(1+2*s))==0
assert sp.simplify(sp.diff(c,s)-(3-2*a)/(1+2*s)**2)==0
assert sp.simplify(sp.diff(s/(1+2*s),s,2)+4/(1+2*s)**3)==0

for n,L in ((15,Q(1,65)),(16,Q(5,88))):
    low=Q(n*(n-12),16)
    v=majorant(n,L)
    gap=low-F(v)
    assert gap>0
    print(f"n={n}, spectral gap >{L}, exact certificate margin={gap}")

u=sp.symbols("u")
v=[sp.Rational(1,4)]*3+[u]+[sp.Rational(0)]*11
x=[1/(1-t) for t in v]
F15=sp.factor(sum((x[i]*x[j])**2-x[i]*x[j]
                  for i in range(15) for j in range(i+1,15))/8)
assert sp.simplify(sp.Rational(45,16)-F15
                   -(199*u**2-1208*u+127)/(432*(1-u)**2))==0
root=(604-3*sp.sqrt(37727))/199
assert sp.simplify(199*root**2-1208*root+127)==0
assert 0<root<sp.Rational(1,4)
assert sp.Rational(3,4)+root>sp.Rational(383,504)
assert Q(5,88)>Q(1,18)
print("15-vector rank-four necessary energy:",sp.Rational(3,4)+root)
print("PASS: exact rational and symbolic checks.")
