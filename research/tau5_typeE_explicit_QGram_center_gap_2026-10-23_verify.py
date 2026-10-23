#!/usr/bin/env python3
"""Exact rational verification of a conditional Type-E Q-Gram spectral gap.

All computations use sympy rational matrices and exact inequalities.
The theorem itself is analytic; this verifies D5 spectral identities and
rational separation at delta=2/7.
"""
from itertools import combinations
from sympy import Matrix, Rational as R, eye, zeros, simplify, sqrt

n=5
# For each D5 line, the rank-one projector is rational despite sqrt(2).
P=[]
for i,j in combinations(range(n),2):
    for s in (1,-1):
        v=zeros(n,1)
        v[i]=1
        v[j]=s
        P.append(v*v.T/2)
Q=[p-eye(n)/5 for p in P]
G=Matrix(20,20,lambda i,j:(Q[i]*Q[j]).trace())
assert G==G.T
assert G*Matrix([1]*20)==zeros(20,1)
assert G.eigenvals()=={R(0):6,R(1):10,R(3,2):4},G.eigenvals()
assert G.rank()==14
assert all(G[i,i]==R(4,5) for i in range(20))

B=R(383,504)
d0=R(2,7)
# The derived necessary inequality is 40*d+30*sqrt(d)>=30-3*B.
# Show it FAILS at d0, and therefore at every d<=d0.
threshold=30-3*B
remaining=threshold-40*d0
assert remaining>0
assert simplify(remaining**2-900*d0)>0

# Exact comparison for improved root.
# root t>0 solves 40t^2+30t=30-3B; d=t^2.
root_t=(-30+sqrt(900+160*threshold))/80
assert simplify(root_t)>0
assert float(root_t**2)>float(d0)
print('PASS: 20-line D5 Q-Gram spectrum:',G.eigenvals())
print('PASS: G0*1=0 and rank 14')
print('PASS: strict delta > 2/7 certified by rational squaring')
print('Exact threshold 30-3B:',threshold)
print('Exact positive squared comparison:',simplify(remaining**2-900*d0))
print('Optimal threshold from derived inequality:',root_t**2,'~',float(root_t**2))
