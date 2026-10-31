#!/usr/bin/env python3
"""Exact rational checks for the sharp two-plane Walsh theorem.
The general inequality is proved via Bessel in the companion note.
"""
from fractions import Fraction as F
from itertools import combinations

x=F(1,250)
for a,b in [(F(0),F(0)),(F(1,100),F(1,16)),(F(1,4),F(1,4)),(x,F(0))]:
    w,v=1-a,1-b
    B=a*v+b*w
    c=(B-a*b)/(w*v)
    k=(1-2*a)*(1-2*b)/(w*v)
    assert c+k==1 and c>=a+b and B==a+b-2*a*b
    for rho2 in [F(0),F(1,16),F(1,4),F(1)]:
        d2=w*v*rho2
        P=a*b*rho2
        BB=w*b*(1-rho2)
        CC=a*v*(1-rho2)
        T=P+BB+CC
        assert T==B-(B-a*b)*rho2
        assert T<=B-c*d2
        assert T+d2==B+k*d2

thresholds={F(1,4):F(22877,124500),
            F(3,8):F(8793,83000),
            F(7,16):F(55141,996000)}
for r,claimed in thresholds.items():
    c2=x*(1-r*r/(1-x))
    margin=(F(1,2)-r)**2-c2
    assert margin>0
    s=F(1,4)-x-(1-2*x)/(1-x)*r*r
    assert s==claimed
    print('sharp safe r=',r,'slack=',s,'margin=',margin)
assert F(3,4)/(1-x)**2<2
assert F(1,4)/(1-x)**2<1

supports=list(combinations(range(5),2))
slots=[(sup,sign) for sup in supports for sign in (+1,-1)]
core={i for i,(sup,sign) in enumerate(slots) if sup[0]==0 and sign==1}
iso=set(range(20))-core
RII=[];NII=[];R114=[]
for i,j in combinations(range(20),2):
    meeting=len(set(slots[i][0])&set(slots[j][0]))==1
    if meeting and not (i in core and j in core): R114.append((i,j))
    if i in iso and j in iso:
        (RII if meeting else NII).append((i,j))
assert (len(core),len(iso),len(RII),len(NII),len(R114))==(4,16,78,42,114)
deg={i:0 for i in iso}
for i,j in RII: deg[i]+=1;deg[j]+=1
star=[i for i in iso if slots[i][0][0]==0]
nonstar=[i for i in iso if slots[i][0][0]!=0]
assert len(star)==4 and len(nonstar)==12
assert all(deg[i]==9 for i in star)
assert all(deg[i]==10 for i in nonstar)
print('K5 counts 78/42/114 and degrees 9x4,10x12: PASS')
print('ALL EXACT CHECKS PASSED')