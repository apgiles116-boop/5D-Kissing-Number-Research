#!/usr/bin/env python3
"""Exact Fraction/SymPy checks for the Type-E safe-subframe rank-defect lemma.

The general theorem is proved by rank-14 and Eckart--Young, not by sampling.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational

B = F(383, 504)
assert 0 < B < 1

# Sharp positive normalized-defect coefficient.
a = b = F(1, 4)
W = (1-a)*(1-b)
assert (1-W)/(4*W) == F(7, 18)*(a+b)
assert a/(4*(1-a)) == a/3

# n=16 isolated-line floor.
gap16 = F(9,16) - F(49,324)*(F(7,2)*B+B*B)
H16 = (1-B)**2*gap16
assert gap16 == F(122483, 1679616) > 0
assert H16 == F(1793273603, 426649337856) > 0

# n=17 isolated + center, improved positive-defect coefficient.
gap17 = F(27,32) - F(361,162)*(B/4) - F(49,324)*B*B
H17 = (1-B)**2*gap17
assert gap17 == F(3915941, 11757312) > 0
assert H17 == F(57333292181, 2986545364992) > 0

def f16(t):
    return (1-t)**2*(F(9,16)-F(49,324)*(F(7,2)*t+t*t))

def f17(t):
    return (1-t)**2*(F(27,32)-F(361,648)*t-F(49,324)*t*t)

assert f16(B-F(1,4)) > F(608,10000)
assert f17(B-F(1,4)) > F(1249,10000)

# D5 exact rational regression: 20 root lines, no sqrt needed for squares.
roots=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[i]=1
        v[j]=sign
        roots.append(v)
assert len(roots)==20

def dot(v,w):
    return sum(x*y for x,y in zip(v,w))

for n in (16,17):
    rs=roots[:n]
    sq=[]
    for i,j in combinations(range(n),2):
        q=F(dot(rs[i],rs[j])**2,4)
        assert q in (F(0),F(1,4))
        sq.append((q-F(1,4))**2)
    K=Matrix([[Rational(dot(rs[i],rs[j])**2,4)-Rational(1,5)
               for j in range(n)] for i in range(n)])
    assert K.rank()<=14
    assert sum(sq)>=F(9,32)*(n-14)
    print(f"D5 n={n}: Q-rank {K.rank()}, squared defect {sum(sq)}")

print("H120 lower:", H16, float(H16))
print("H136 lower:", H17, float(H17))
print("All exact rational checks passed.")
