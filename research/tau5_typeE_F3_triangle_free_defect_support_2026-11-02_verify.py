#!/usr/bin/env python3
"""Exact symbolic checks for F3 exceptional-support triangle obstruction.
The 3-vector PSD contradiction is analytic, not a grid search.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

deep={frozenset(e) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),
                            (2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[[(0,4),(1,7),(2,3),(5,6)],
           [(0,2),(1,4),(3,6),(5,7)],
           [(0,5),(1,4),(2,7),(3,6)]]
expected_g=[[1,-1,1,1],[1,-1,-1,1],[1,-1,1,1]]
for which,B in enumerate(matchings):
    assert all(frozenset(e) in deep for e in B)
    signs={}
    mult={}
    for i,j in combinations(range(4),2):
        hits=[(1-2*si)*(1-2*sj)
              for si,x in enumerate(B[i]) for sj,y in enumerate(B[j])
              if frozenset((x,y)) in deep]
        assert len(set(hits))<=1
        mult[i,j]=len(hits)
        if hits: signs[i,j]=hits[0]
    g=[1]+[signs[0,j] for j in range(1,4)]
    assert g==expected_g[which]
    assert all(signs[i,j]==g[i]*g[j] for i,j in signs)
    if which==0:
        assert sorted(mult.values())==[1]*6
    else:
        assert sorted(mult.values())==[0,1,1,1,1,2]
        singles={ij for ij,v in mult.items() if v==1}
        assert len(singles)==4
        assert [sum(i in ij for ij in singles) for i in range(4)]==[2]*4
        assert len([ij for ij,v in mult.items() if v==2])==1

a=sp.symbols("a0:4",nonnegative=True)
t=[a[0]+a[1],a[1]+a[2],a[2]+a[3],a[3]+a[0]]
C=sum(a)
f=lambda x:x*(1-x)/2
assert sp.simplify(sum(f(x) for x in t)-
    (C*(1-C/2)-((a[0]-a[2])**2+(a[1]-a[3])**2)/2))==0
c,h=sp.symbols("c h",real=True)
q=lambda x:x**2*(1-x)**2/4
assert sp.simplify(2*q(c/2)-q(c/2+h)-q(c/2-h)-
    h**2*(-3*c**2+6*c-2-2*h**2)/4)==0

cstar=F(567,1000)
Dstar=cstar*(1-cstar/F(2))
margin=-3*cstar**2+6*cstar-2-(1-cstar)**2/F(2)
assert margin==F(687577,2000000)>0
assert Dstar==F(812511,2000000)
budget=Dstar+Dstar**2/F(4)
assert budget==F(7160262125121,16000000000000)>F(27,64)

D0=F(1780062775,4032758016)
assert F(3,8)<D0<F(1,2)
alt_budget=D0+F(5,64)+(D0-F(3,8))**2
assert alt_budget==F(8520825355071995281,16263137215612256256)

Q=F(141813,5000)
Qsafe=Q-F(3,2)-budget
assert Qsafe==F(422641337874879,16000000000000)
assert F(184,9)+F(5*42,36)<Qsafe<F(184,9)+F(5*43,36)
needed=F(184,9)+F(5*43,36)+F(3,2)+budget
assert needed==F(1361480786375363,48000000000000)
assert needed-Q==F(75986375363,48000000000000)
print("PASS: F3 switching, C4 polynomial, rational defect budgets and thresholds")
print("Canonical budget:",budget,"alternative double-positive budget:",alt_budget)
print("Conditional safe squared-correlation floor:",Qsafe,float(Qsafe))
print("Q threshold for 44:",needed,float(needed))
