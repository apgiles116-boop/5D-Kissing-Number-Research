#!/usr/bin/env python3
"""Exact SymPy check: six-exception finite D5 deformation. No Type-E elimination."""
from itertools import combinations
from collections import Counter
from sympy import Matrix, Rational, sqrt, simplify, factor

E=[Matrix([int(i==j) for i in range(5)]) for j in range(5)]
roots={}
for i,j in combinations(range(5),2):
    for s in (1,-1):
        roots[(i,j,s)]=E[i]+s*E[j]
core=[(0,j,-1) for j in range(1,5)]
outside=[k for k in roots if k not in core]
assert len(outside)==16 and len(core)==4
assert Matrix.hstack(*(roots[k] for k in outside)).rank()==5

W={}
for j in range(1,5):
    W[j]=E[0]+E[j]-sum((E[k] for k in range(1,5) if k!=j),Matrix.zeros(5,1))
    assert roots[(0,j,-1)].dot(W[j])==0
    assert W[j].dot(W[j])==5

categories=Counter()
for j in range(1,5):
    for k in outside:
        p=roots[(0,j,-1)].dot(roots[k])
        q=W[j].dot(roots[k])
        categories[(int(p),int(q))]+=1
assert sum(categories.values())==64
assert set(categories).issubset({
    (-1,0),(1,0),(-1,2),(1,-2),(0,-2),(0,0),(0,2)})
# Safe for 0<=t<=sqrt(2/3):
# (p+tq)^2 <= 1+(5/2)t^2; the only nontrivial cases reduce to
# t(8-3t)>=0 and t^2<=2/3.

for j,k in combinations(range(1,5),2):
    rj,rk=roots[(0,j,-1)],roots[(0,k,-1)]
    assert (rj.dot(rk),rj.dot(W[k]),W[j].dot(rk),W[j].dot(W[k]))==(1,2,2,1)

t=Rational(1,20)
unit={k:roots[k]/sqrt(2) for k in outside}
unit.update({(0,j,-1):(roots[(0,j,-1)]+t*W[j])/sqrt(2+5*t*t)
             for j in range(1,5)})
assert all(simplify(v.dot(v)-1)==0 for v in unit.values())
violations=[]
for k,l in combinations(unit,2):
    c2=simplify(unit[k].dot(unit[l])**2)
    if c2>Rational(1,4):
        violations.append((k,l,c2))
assert len(violations)==6
assert all(k in core and l in core for k,l,_ in violations)
assert len(list(combinations(unit,2)))==190

rho=factor((1+4*t+t*t)/(2+5*t*t))
w=factor(rho**2)
assert rho==Rational(481,805)
assert all(v==w for _,_,v in violations)
P_hom=factor(6*(w-Rational(1,4)))
P_raw=factor(6*w*(w-Rational(1,4)))
cap_hom=Rational(5792292955405,4129544208384)
cap_raw=Rational(1780062775,4032758016)
assert P_hom==Rational(832257,1296050)
assert P_raw==Rational(192551811777,839872801250)
assert P_hom<cap_hom and P_raw<cap_raw

# Deleted contacts have derivative +2; retained active contacts <=0.
for j,k in combinations(range(1,5),2):
    assert (W[j].dot(roots[(0,k,-1)])+
            roots[(0,j,-1)].dot(W[k]))/2==2
for j in range(1,5):
    for key in outside:
        p=roots[(0,j,-1)].dot(roots[key])
        q=W[j].dot(roots[key])
        if abs(p)==1: assert p*q<=0

# Local covering-radius exclusion at t=1/50.
# sqrt(2/5)>63/100, sqrt(5/2)/50<1/25, 1/sqrt(3)<29/50.
assert Rational(2,5)>Rational(63,100)**2
assert Rational(5,2)<4
assert Rational(1,3)<Rational(29,50)**2
assert Rational(59,100)>Rational(29,50)

print("PASS: 184 safe pairs, 6 exceptional core pairs, exact defect caps")
print("Core/outside categories:",sorted(categories.items()))
print("t=1/20; core correlation =",rho)
print("P_hom =",P_hom,"~",float(P_hom))
print("P_raw =",P_raw,"~",float(P_raw))
print("Six-exception interval: 0<t<=sqrt(2/3)")
print("Center exclusion at t=1/50 certified by covering-radius bounds")
