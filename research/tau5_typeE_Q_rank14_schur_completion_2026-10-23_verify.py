#!/usr/bin/env python3
"""Exact rational verification of D5 Q rank-14 Schur completion (2026-10-23)."""
from itertools import combinations
from collections import Counter
import sympy as sp
R=sp.Rational
I=sp.eye
supports=list(combinations(range(5),2))
labels=[(a,b,s) for a,b in supports for s in (1,-1)]
roots=[]
for a,b,s in labels:
    v=sp.zeros(5,1)
    v[a]=1
    v[b]=s
    roots.append(v)
G0=sp.Matrix(20,20,lambda i,j:roots[i].dot(roots[j])**2/4-R(1,5))
assert G0.rank()==14
P=I(20)-R(5,3)*G0+R(2,3)*G0**2
assert P*G0==sp.zeros(20)
# Four diagonal basis vectors E_jj-E_44, ten off-diagonal E_ab+E_ba.
H=I(4)+sp.ones(4)
d=[]
for a,b in supports:
    d.append(sp.Matrix([(int(j in (a,b))-int(4 in (a,b)))*R(1,2)
                        for j in range(4)]))
assert sum((2*v*v.T for v in d),sp.zeros(4))==R(3,2)*H
t=R(1,26)
minors_min=[None]*4
for J in combinations(range(10),4):
    K=sum((d[s]*d[s].T for s in J),sp.zeros(4))
    Schur=(R(3,2)-t)*H-2*(1-t)/(1-2*t)*K
    ms=[Schur[:k,:k].det() for k in range(1,5)]
    assert all(v>0 for v in ms),(J,ms)
    for k in range(4):
        minors_min[k]=ms[k] if minors_min[k] is None else min(minors_min[k],ms[k])
assert minors_min==[R(131,156),R(146969,129792),
                    R(72205331,121485312),R(32734055,1579309056)]
# Signs cancel in the Schur complement, so these 210 tests cover 3360.
worst=sp.Integer(0)
for J in combinations(range(10),4):
    core=[2*j for j in J]
    inv=P.extract(core,core).inv()
    for r,s in combinations(range(4),2):
        worst=max(worst,inv[r,r]*inv[s,s])
assert worst==112
# Repeated-support exact counterexample, rank 14 PSD, R=0, E=1.
newroots=list(roots)
newroots[1]=newroots[0]
Gdup=sp.Matrix(20,20,lambda i,j:
               newroots[i].dot(newroots[j])**2/4-R(1,5))
Edup=Gdup-G0
assert Edup[0,1]==1 and Edup[1,0]==1
assert sum(int(Edup[i,j]!=0) for i in range(20) for j in range(20))==2
assert Gdup.rank()==14
# Independent exact nonlinear identity on a perturbed rational rank-one Q Gram.
J=[0,2,4,6]
O=[i for i in range(20) if i not in J]
Hcore=P.extract(J,J)
Hinv=Hcore.inv()
K=sp.Matrix.hstack(*[
    sum((Hinv[s,r]*P[:,J[s]] for s in range(4)),sp.zeros(20,1))
    for r in range(4)])
assert K.extract(J,list(range(4)))==I(4)
newroots=list(roots)
newroots[0]=roots[0]+R(1,100)*I(5)[:,4]
G=sp.Matrix(20,20,lambda i,j:
    (newroots[i].dot(newroots[j])/2)**2
    -(newroots[i].dot(newroots[i])/2)*
     (newroots[j].dot(newroots[j])/2)/5)
E=sp.zeros(20)
for i,j in combinations(J,2):
    E[i,j]=E[j,i]=G[i,j]-G0[i,j]
RR=G-G0-E
T=K.T*RR*K
piv=G0.extract(O,O).rref()[1]
B=[O[i] for i in piv]
assert len(B)==14
U=RR.extract(B,list(range(20)))*K
assert T+E.extract(J,J)==U.T*G.extract(B,B).inv()*U
print("PASS: D5 Q rank 14, rational frame bound >= 1/26 for 3360 cases")
print("PASS: all 210 four-by-four rational Schur certificates",minors_min)
print("PASS: dual-norm product squared <= 112")
print("PASS: repeated-support rank-14 PSD counterexample with R=0,E=1")
print("PASS: nonlinear Schur equality for perturbed rational rank-one Q Gram")
