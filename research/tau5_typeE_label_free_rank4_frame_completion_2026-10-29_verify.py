#!/usr/bin/env python3
"""Exact Fraction verifier for label-free rank-four PSD frame completion.
Proof is in the companion Markdown; random checks are diagnostics only.
"""
from fractions import Fraction as F
from random import Random

def waterfill(s,c):
    s=list(map(F,s)); c=F(c)
    assert len(s)==5 and all(s[i]>=s[i+1] for i in range(4))
    if c==0: return s[-1],[F(0)]*5
    for k in range(1,5):
        theta=(c+sum(s[5-k:]))/k
        if theta>=s[5-k] and (k==4 or theta<=s[4-k]):
            d=[F(0)]+[max(F(0),theta-si) for si in s[1:]]
            assert sum(d)==c
            return theta,d
    raise AssertionError("waterfill")

def variance_diag(s,d,mu):
    return sum((si+di-mu)**2 for si,di in zip(s,d))

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def V(T,mu):
    return sum((T[i][j]-(mu if i==j else 0))**2
               for i in range(5) for j in range(5))

examples=[
 ([F(7,2),F(13,4),F(3),F(3),F(11,4)],F(9,2),F(4),F(5,16)),
 ([F(9,2),F(3),F(3),F(5,2),F(5,2)],F(9,2),F(4),F(5,16)),
 ([F(9,2),F(9,2),F(3),F(3),F(5,2)],F(5,2),F(4),F(5,6)),
]
for s,c,mu,want in examples:
    assert sum(s)+c==5*mu
    theta,d=waterfill(s,c)
    assert variance_diag(s,d,mu)==want
    assert want>=F(5,4)*(s[0]-mu)**2
    print("EXACT",theta,d,want)

rng=Random(20261029)
for trial in range(500):
    s=sorted([F(rng.randrange(0,30),4) for _ in range(5)],reverse=True)
    c=F(rng.randrange(0,45),4)
    mu=(sum(s)+c)/5
    _,d=waterfill(s,c)
    opt=variance_diag(s,d,mu)
    assert opt>=F(5,4)*(s[0]-mu)**2
    weights=[rng.randrange(0,30) for _ in range(4)]
    if sum(weights)==0: weights[0]=1
    comp=[F(0)]+[c*F(w,sum(weights)) for w in weights]
    assert variance_diag(s,comp,mu)>=opt
    W=[[F(rng.randrange(-3,4),4) for _ in range(4)] for _ in range(5)]
    C=mm(W,[list(x) for x in zip(*W)])
    tc=tr(C)
    if tc==0: continue
    C=[[v*c/tc for v in row] for row in C]
    T=[[C[i][j]+(s[i] if i==j else 0) for j in range(5)]
       for i in range(5)]
    assert tr(T)==5*mu
    assert V(T,mu)>=opt
    for k in range(5):
        assert V(T,mu)>=F(5,4)*(T[k][k]-mu)**2
print("PASS: 3 exact rational examples and 500 exact rational PSD rank<=4 diagnostics")
