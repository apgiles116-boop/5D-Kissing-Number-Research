#!/usr/bin/env python3
"""Exact SymPy verifier for Type-E Q-kernel dimension and fourth-moment note."""
from itertools import combinations
import sympy as s

E=s.eye(5)
edges=list(combinations(range(5),2))
v=[(E[:,i]+t*E[:,j])/s.sqrt(2) for i,j in edges for t in (1,-1)]
P=[x*x.T for x in v]
Q=[p-E/5 for p in P]
K=s.Matrix(20,20,lambda i,j:s.trace(Q[i]*Q[j]))
assert K.eigenvals()=={s.Integer(0):6,s.Integer(1):10,s.Rational(3,2):4}
assert sum(Q,s.zeros(5))==s.zeros(5)
flat=lambda m:s.Matrix([m[i,j] for i in range(5) for j in range(i,5)])
L=s.Matrix.hstack(*map(flat,P))
assert L.rank()==15
U=s.Matrix(5,10,lambda i,j:int(i in edges[j]))
assert U.rank()==5
cycles=[]
for a,b,c,d in combinations(range(5),4):
    for cyc in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
        t=s.zeros(10,1)
        for k in range(4):
            t[edges.index(tuple(sorted((cyc[k],cyc[(k+1)%4]))))]=(-1)**k
        cycles.append(t)
        assert U*t==s.zeros(5,1)
        c20=s.Matrix([t[k//2] for k in range(20)])
        assert L*c20==s.zeros(15,1)
        assert sum(x!=0 for x in c20)==8
assert len(cycles)==15 and s.Matrix.hstack(*cycles).rank()==5
B=s.Matrix(10,10,lambda i,j:int(i!=j and len(set(edges[i])&set(edges[j]))==1))
assert B.eigenvals()=={s.Integer(6):1,s.Integer(1):4,s.Integer(-2):5}
assert K==s.eye(20)-s.ones(20,20)/5+s.kronecker_product(B,s.ones(2,2))/4
assert s.trace(K)==16 and s.trace(K*K)==19
assert s.trace(K*K)-s.trace(K)**2/14==s.Rational(5,7)
S=sum(v[i].dot(v[j])**2 for i in range(20) for j in range(i+1,20))
T=sum(v[i].dot(v[j])**4 for i in range(20) for j in range(i+1,20))
assert S==30 and T==s.Rational(15,2)
off=sum(K[i,j]**2 for i in range(20) for j in range(i+1,20))
assert off==s.Rational(31,10)
assert off-(s.Rational(4,175)*400-s.Rational(8,25)*20)==s.Rational(5,14)
assert T-(s.Rational(2,5)*S+s.Rational(1,350)*400-s.Rational(3,10)*20)==s.Rational(5,14)
print("PASS: exact D5 spectrum, 15 cycles spanning rank 5, and fourth moments.")
