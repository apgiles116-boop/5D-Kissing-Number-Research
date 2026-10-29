#!/usr/bin/env python3
"""Exact SymPy verification: D5 weighted Q-spectrum and sharp cap witness."""
from itertools import combinations
import sympy as s

edges=list(combinations(range(5),2))
labels=[(e,sgn) for e in edges for sgn in (1,-1)]
roots=[]
for (i,j),sgn in labels:
    v=s.zeros(5,1);v[i]=1;v[j]=sgn;roots.append(v)
I=s.eye(5)
P=[v*v.T/2 for v in roots]
R=[p-I/5 for p in P]
G=s.Matrix(20,20,lambda i,j:s.trace(R[i]*R[j]))
assert G.eigenvals()=={s.Rational(3,2):4,s.Integer(1):10,s.Integer(0):6}
assert sum(P,s.zeros(5))==4*I
assert sum(R,s.zeros(5))==s.zeros(5)
print("PASS exact D5 spectrum and tight frame")

cycles=[
    ((0,1),(2,3),(0,2),(1,3)),
    ((0,1),(2,3),(0,3),(1,2)),
    ((0,1),(2,4),(0,2),(1,4)),
    ((0,1),(2,4),(0,4),(1,2)),
    ((0,1),(3,4),(0,3),(1,4)),
]
kernel=[]
for ab,cd,ac,bd in cycles:
    v=s.zeros(20,1)
    for e,sgn in ((ab,1),(cd,1),(ac,-1),(bd,-1)):
        k=edges.index(e);v[2*k]+=sgn;v[2*k+1]+=sgn
    assert G*v==s.zeros(20,1)
    kernel.append(v)
kernel.append(s.ones(20,1))
assert s.Matrix.hstack(*kernel).rank()==6
print("PASS five independent cycles and global kernel")

contacts=[(i,j) for i,j in combinations(range(20),2)
          if s.trace(P[i]*P[j])==s.Rational(1,4)]
assert len(contacts)==120
assert all(sum(k in pair for pair in contacts)==12 for k in range(20))

def verify(a):
    A=sum(a);U=sum(x*x for x in a)
    w=[1-x for x in a]
    T=sum((w[i]*P[i] for i in range(20)),s.zeros(5))
    V=s.trace((T-(20-A)*I/5)**2)
    Q=sum(w[i]*w[j]*s.trace(P[i]*P[j])
          for i,j in combinations(range(20),2))
    J=sum(a[i]*a[j] for i,j in contacts)
    assert s.simplify(Q-(30-3*A+J/4))==0
    assert s.simplify(V-(U-A*A/5+J/2))==0
    assert s.simplify(Q-(30-3*A+A*A/10-U/2+V/2))==0

verify([s.Rational((i*i+3*i+2)%7,40) for i in range(20)])
a=[s.Integer(0)]*20
idx=[labels.index(((0,1),1)),labels.index(((0,1),-1)),
     labels.index(((2,3),1)),labels.index(((2,3),-1))]
assert all(s.trace(P[i]*P[j])==0 for i,j in combinations(idx,2))
for k in idx[:3]:a[k]=s.Rational(1,4)
a[idx[3]]=s.Rational(5,504)
verify(a)
B=s.Rational(383,504);U=sum(x*x for x in a)
assert sum(a)==B
assert U-B**2/5==s.Rational(11447,158760)
assert 30-3*B==s.Rational(4657,168)
assert s.Rational(4657,168)-s.Rational(8790283,317520)==s.Rational(11447,317520)
print("PASS weighted identities, rational cap values and sharp orthogonal witness")
print("ALL EXACT CHECKS PASSED")
