#!/usr/bin/env python3
"""Exact Type-E three-active four-core PSD theorem verifier (SymPy)."""
from itertools import combinations
from collections import Counter
from sympy import Matrix, sqrt, simplify, Rational, symbols

edges = list(combinations(range(4),2))
hist = Counter()
for k in range(4):
    for E in combinations(edges,k):
        B = Matrix(4,4,lambda i,j: int(tuple(sorted((i,j))) in E) if i!=j else 0)
        assert all((lam+sqrt(3)).is_nonnegative for lam in B.eigenvals()), (E,B.eigenvals())
        hist[k] += 1
assert hist == Counter({0:1,1:6,2:15,3:20})

C = symbols('C', positive=True)
v = Matrix([sqrt(3),-1,-1,-1])*sqrt(C/6)
G = v*v.T
assert simplify(sum(G[i,i] for i in range(4))-C)==0
assert simplify(-sum(G[0,j] for j in (1,2,3))-sqrt(3)*C/2)==0

for V in (Matrix([[1,0],[0,1],[1,1],[-1,2]]),
          Matrix([[1,0],[1,0],[-1,0],[-1,0]]),
          Matrix([[0,0],[1,2],[2,-1],[-2,1]])):
    G = V*V.T
    a = [G[i,i] for i in range(4)]
    b = [sqrt(x) for x in a]
    c = sum(a)
    M = sum((V.row(i) for i in range(4)),Matrix([[0,0]]))
    M2 = (M*M.T)[0]
    d = sum(max(-G[i,j],0) for i,j in edges)
    rem = sum((b[i]-b[j])**2/4+(b[i]*b[j]-abs(G[i,j]))/2
              for i,j in edges)
    assert simplify(c-M2/4-d-rem)==0
    W = sum((b[i]*V.row(i) for i in range(4)),Matrix([[0,0]]))
    W2 = (W*W.T)[0]
    d2 = sum(max(-G[i,j],0)**2 for i,j in edges)
    assert simplify((c*c-W2)/4-d2).is_nonnegative

assert ((1-sqrt(3)/2)*Rational(9,1000)-Rational(1,4250)).is_positive
D0=Rational(1780062775,4032758016)
H0=Rational(5792292955405,4129544208384)
def flex(t):
    r=(1+4*t+t*t)/(2+5*t*t)
    return r,6*(r-Rational(1,2)),6*(r*r-Rational(1,4))
r20,d20,h20=flex(Rational(1,20))
r40,d40,h40=flex(Rational(1,40))
assert r20==Rational(481,805) and d20==Rational(471,805)>D0
assert r40==Rational(1761,3205) and d40==Rational(951,3205)<D0
assert h40<H0
print('PASS: all 42 four-vertex active graphs with at most three edges')
print('PASS: exact sharp star witness and centroid identities')
print('PASS: raw-excess slack bound exceeds 1/4250 (distinct from negative-Gram slack)')
print('PASS: flex raw-defect correction t=1/20 -> t=1/40')
