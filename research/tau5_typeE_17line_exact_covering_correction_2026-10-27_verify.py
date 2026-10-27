#!/usr/bin/env python3
"""Exact finite certificate for the 17-line D16+center covering radius.

Requires sympy. No floating-point hull, optimization or SDP.
Enumerates all C(32,5)=201376 base active-facet systems exactly.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
from math import comb
import sympy as sp

S=sp.sqrt(2)
facets=[]
for i,j in combinations(range(1,5),2):
    for sign in (-1,1):
        f=[0]*5; f[i]=1; f[j]=sign
        facets.extend([tuple(f),tuple(-t for t in f)])
for i in range(1,5):
    f=[0]*5; f[0]=f[i]=1
    facets.extend([tuple(f),tuple(-t for t in f)])
assert len(facets)==32

def solve_exact(rows):
    M=[list(row)+[1] for row in rows]
    prev=1
    for k in range(5):
        pivot=next((i for i in range(k,5) if M[i][k]),None)
        if pivot is None: return None
        if pivot!=k: M[k],M[pivot]=M[pivot],M[k]
        pk=M[k][k]
        for i in range(k+1,5):
            multiplier=M[i][k]
            for j in range(k+1,6):
                numerator=M[i][j]*pk-multiplier*M[k][j]
                assert numerator%prev==0
                M[i][j]=numerator//prev
            M[i][k]=0
        prev=pk
    w=[None]*5
    for k in range(4,-1,-1):
        w[k]=(F(M[k][5])-sum((M[k][j]*w[j] for j in range(k+1,5)),F(0)))/M[k][k]
    return tuple(w)

vertices=set()
count=0
for indices in combinations(range(32),5):
    count+=1
    w=solve_exact([facets[i] for i in indices])
    if w is not None and all(sum(a*b for a,b in zip(f,w))<=1 for f in facets):
        vertices.add(w)
assert count==comb(32,5)==201376
assert len(vertices)==48

base=[]
for i in range(4):
    for sign in (-1,1):
        v=[F(0)]*4; v[i]=F(sign); base.append(tuple(v))
for signs in product((-1,1),repeat=4):
    base.append(tuple(F(s,2) for s in signs))
expected=set()
for v in base:
    for T in (-1-min(v),1-max(v)):
        expected.add((T,)+v)
assert vertices==expected

ordered=sorted(vertices)
active=[]
for w in ordered:
    active.append({i for i,f in enumerate(facets) if sum(a*b for a,b in zip(f,w))==1})
edges=[]
for i,j in combinations(range(len(ordered)),2):
    common=active[i]&active[j]
    if len(common)>=4 and sp.Matrix([facets[k] for k in common]).rank()==4:
        edges.append((i,j))
assert len(edges)==218

def L(w): return 8*w[0]-3*sum(w[1:])
threshold=5*S
final=set()
for w in ordered:
    if sp.simplify(threshold-abs(L(w))).is_nonnegative:
        final.add(tuple(sp.Rational(z) for z in w))
for i,j in edges:
    p,q=ordered[i],ordered[j]
    lp,lq=L(p),L(q)
    for side in (-1,1):
        boundary=side*threshold
        if min(lp,lq)<boundary<max(lp,lq):
            t=(boundary-lp)/sp.Rational(lq-lp)
            w=tuple(sp.expand(sp.Rational(p[k])+t*sp.Rational(q[k]-p[k])) for k in range(5))
            assert all(sp.simplify(1-sum(a*b for a,b in zip(f,w))).is_nonnegative for f in facets)
            assert sp.simplify(threshold-abs(L(w))).is_nonnegative
            final.add(w)
assert len(final)==114

norms=Counter(sp.expand(2*sum(z*z for z in w)) for w in final)
assert norms=={
    sp.Rational(31,8)-3*S/4:8,
    sp.Rational(631,98)-135*S/49:24,
    sp.Rational(123,32)-15*S/16:8,
    sp.Rational(127,22)-280*S/121:8,
    sp.Rational(5,2):30,
    sp.Rational(631,32)-195*S/16:24,
    sp.Rational(75,16)-15*S/8:2,
    sp.Integer(2):8,
    sp.Rational(13,4)-S:2,
}
R2=sp.Rational(31,8)-3*S/4
assert all(sp.simplify(R2-n).is_nonnegative for n in norms)
assert sum(norms.values())==114
rho2=sp.simplify(1/R2)
assert sp.simplify(rho2-sp.Rational(1,3)).is_positive
b_star=sp.simplify(1-1/(3*rho2))
assert b_star==(6*S-7)/24
assert b_star.is_positive
print('PASS: 201376 exact facet systems; 48 base vertices; 218 edges')
print('PASS: 114 clipped vertices; nine exact norm classes')
print('rho^2 =',rho2,'rho =',sp.N(sp.sqrt(rho2),16))
print('rho^2 > 1/3: PASS')
print('conditional outside energy b >=',b_star,'=',sp.N(b_star,16))
