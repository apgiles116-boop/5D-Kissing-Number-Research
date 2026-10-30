#!/usr/bin/env python3
"""Exact Fraction verification of trace-corrected rank-14 Type-E slack bound."""
from fractions import Fraction as F
from itertools import combinations

B=F(383,504)
c0=F(11,70)
target=F(1,10)

def rank_floor(n):
    return F(9*n*(n-14),448)

assert [rank_floor(n) for n in (16,17,20,21)] == [
    F(9,14), F(459,448), F(135,56), F(189,64)]
assert rank_floor(21)-F(6,16)==F(165,64)
assert F(49,324)*18+F(1,9)==F(17,6)
assert F(9,4)-F(49,324)==F(170,81)

def f17(t):
    return (1-t)**2*(F(459,448)-F(361,648)*t-F(49,324)*t*t)

def g21(c):
    return (1-B)**2*(F(165,64)-F(17,24)*B-F(49,324)*B*B
                     -F(170,81)*(c/2+c*c))

large=f17(B-c0)
small=g21(c0)
assert large==F(3809520955097,38093690880000)
assert small==F(10457848720099,104529087774720)
assert large-target==F(151867097,38093690880000)
assert small-target==F(4939942627,104529087774720)
assert large>target and small>target

# All three F3 perfect matchings: cross deep edges use at most one Walsh parity.
edges={tuple(sorted(e)) for e in [
    (0,2),(0,4),(0,5),(1,4),(1,7),
    (2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[
    [(0,2),(1,4),(3,6),(5,7)],
    [(0,4),(1,7),(2,3),(5,6)],
    [(0,5),(1,4),(2,7),(3,6)]
]
counts=[]
for matching in matchings:
    m=[tuple(sorted(e)) for e in matching]
    assert len(set(sum((list(e) for e in m),[])))==8
    assert all(e in edges for e in m)
    bad=0
    for e1,e2 in combinations(m,2):
        parity=[]
        for i,v in enumerate(e1):
            for j,w in enumerate(e2):
                if tuple(sorted((v,w))) in edges:
                    parity.append((i+j)%2)
        assert len(set(parity))<=1
        bad+=bool(parity)
    counts.append(bad)
assert counts==[5,6,5]

# Optional exact symbolic D5-plus-e1 regression.
try:
    import sympy as s
    roots=[]
    for i,j in combinations(range(5),2):
        for sign in (1,-1):
            v=s.zeros(5,1); v[i]=1; v[j]=sign
            roots.append(v/s.sqrt(2))
    roots.append(s.eye(5)[:,0])
    n=len(roots)
    K=s.Matrix(n,n,lambda i,j:
               (roots[i].dot(roots[j]))**2-s.Rational(1,5))
    M=s.Rational(3,4)*s.eye(n)+s.Rational(1,20)*s.ones(n,n)
    assert K.rank()==14
    assert s.trace((K-M)*(K-M))/2==s.Rational(45,8)
    assert s.Rational(45,8)>s.Rational(189,64)
    print("D5-plus-center regression PASS")
except ImportError:
    print("D5-plus-center regression skipped (SymPy not installed)")

print("Rank floors:",*[str(rank_floor(n)) for n in (16,17,20,21)])
print("F3 exceptional block counts:",counts)
print("Large core:",large,"margin:",large-target)
print("Small core:",small,"margin:",small-target)
print("CONDITIONAL TYPE E: H204 > 1/10")
print("PASS")
