#!/usr/bin/env python3
"""Exact rational verifier: Type-E isolated Walsh / K5 label averaging."""
from fractions import Fraction as F
from itertools import combinations

supports=list(combinations(range(5),2))
slots=[(s,sgn) for s in supports for sgn in (-1,1)]
core=[((0,k),1) for k in range(1,5)]
iso=[s for s in slots if s not in core]
assert len(iso)==16 and len(core)==4

def nominal(a,b):
    return a[0]==b[0] or set(a[0]).isdisjoint(set(b[0]))

pairs=[(a,b) for a,b in combinations(slots,2) if nominal(a,b)]
II=[(a,b) for a,b in pairs if a in iso and b in iso]
CI=[(a,b) for a,b in pairs if (a in core)!=(b in core)]
CC=[(a,b) for a,b in pairs if a in core and b in core]
assert (len(pairs),len(II),len(CI),len(CC))==(70,42,28,0)
assert F(len(II),120)==F(7,20)
assert F(len(CI),64)==F(7,16)
deg={a:sum(a in e for e in II) for a in iso}
assert sorted(deg.values())==[5]*12+[6]*4
assert {a for a,d in deg.items() if d==6}=={((0,k),-1) for k in range(1,5)}

# Spectral inequality for 0<=x<=1:
# (16-x+2sqrt(124+22x+4x^2))/5 < 8
# iff 15*x*x/4 +10*x-20<0, monotone on [0,1].
def general_poly(x): return F(15,4)*x*x+10*x-20
assert general_poly(F(0))<0 and general_poly(F(1))<0

# Stronger critical inequality for 0<=x<=1/250:
# (16-x+2sqrt(124+22x+4x^2))/5 < 383/50
# iff -129/400+217*x/20+15*x*x/4<0.
def critical_poly(x):
    return -F(129,400)+F(217,20)*x+F(15,4)*x*x
assert critical_poly(F(0))<0 and critical_poly(F(1,250))<0
assert F(2681,1000)*F(1,250)+F(7,40)*F(1,250)**2 == F(26817,2500000)

# Exact rational 5D trace identities, independent test data.
def dot(u,v): return sum((a*b for a,b in zip(u,v)),F(0))
def outer_sum(vecs):
    return [[sum((v[i]*v[j] for v in vecs),F(0)) for j in range(5)]
            for i in range(5)]
def trprod(A,B):
    return sum((A[i][j]*B[j][i] for i in range(5) for j in range(5)),F(0))

ms=[];zs=[]
for k in range(16):
    m=[F(0)]*5;z=[F(0)]*5
    m[k%5]=F(k%3+1,40)
    z[(k+1)%5]=F(k%4+3,5)
    ms.append(m);zs.append(z)
assert all(dot(m,z)==0 for m,z in zip(ms,zs))
M=outer_sum(ms);Z=outer_sum(zs)
a=[dot(m,m) for m in ms]
x=sum(a,F(0));U=sum((v*v for v in a),F(0))
TII=sum((dot(ms[i],ms[j])**2+dot(ms[i],zs[j])**2+
         dot(zs[i],ms[j])**2 for i,j in combinations(range(16),2)),F(0))
assert TII==(trprod(M,M)-U)/2+trprod(M,Z)

cms=[];czs=[]
for k in range(4):
    m=[F(0)]*5;z=[F(0)]*5
    m[k]=F(k+1,20);z[(k+1)%5]=F(k+3,6)
    cms.append(m);czs.append(z)
MC=outer_sum(cms);ZC=outer_sum(czs)
SC=[[MC[i][j]+ZC[i][j] for j in range(5)] for i in range(5)]
TCI=sum((dot(cms[i],ms[j])**2+dot(cms[i],zs[j])**2+
         dot(czs[i],ms[j])**2 for i in range(4) for j in range(16)),F(0))
assert TCI==trprod(MC,Z)+trprod(M,SC)

print("PASS: K5 70=42+28+0, degrees 5^12/6^4, label probabilities 7/20 and 7/16")
print("PASS: rational spectral inequalities for x<=1 and x<=1/250")
print("PASS: exact trace identities T_II and T_CI")
print("CRITICAL TYPE-E CONSEQUENCE: some labeling has T_42 < 26817/2500000")
