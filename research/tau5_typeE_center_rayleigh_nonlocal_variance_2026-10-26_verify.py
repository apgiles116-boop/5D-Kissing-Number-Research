#!/usr/bin/env python3
"""Exact rational checks for center-Rayleigh / Type-E certificate.
The analytic proof is in the companion Markdown; finite tests are supplementary.
"""
from fractions import Fraction as F
from random import Random

t=F(1,40)
KO=F(20,16*(1-t)**2)
KC=(17+(1+t)**2*(7+t))/(16*(1-t)**2)
Pmax=KC*t
margin=(1-t/2)**2-24*Pmax
assert KO==F(2000,1521)
assert KC==F(1560361,973440)
assert Pmax==F(1560361,38937600)
assert margin==F(8693,648960)>0
assert 30-3*t-F(2,5)*t*t+F(1,10)==F(120099,4000)

rng=Random(20261026)
for _ in range(12):
    z=[[F(rng.randint(-4,4),12) for j in range(5)] for i in range(20)]
    a=[1-sum(c*c for c in zi) for zi in z]
    assert min(a)>0
    A=sum(a)
    T=sum(zi[4]**2 for zi in z)
    q=sum(ai*zi[4]**2/(1-ai) for ai,zi in zip(a,z))
    Fz=[[sum(zi[j]*zi[k] for zi in z) for k in range(5)] for j in range(5)]
    Vz=sum((Fz[j][k]-(F(20)-A)/5*(j==k))**2 for j in range(5) for k in range(5))
    B=[[Fz[j][k] for k in range(4)] for j in range(4)]
    b=[Fz[j][4] for j in range(4)]
    transverse=sum((B[j][k]-(F(20)-A-T)/4*(j==k))**2 for j in range(4) for k in range(4))
    assert Vz==F(5,4)*(T-(F(20)-A)/5)**2+transverse+2*sum(y*y for y in b)
    Sz=sum(sum(z[i][k]*z[j][k] for k in range(5))**2 for i in range(20) for j in range(i+1,20))
    assert Sz==30-3*A+A*A/10-sum(ai*ai for ai in a)/2+Vz/2
    assert (T-4+A/5)**2<=F(4,5)*Vz
    Fu=[[Fz[j][k]+sum(ai*z[i][j]*z[i][k]/(1-ai) for i,ai in enumerate(a))+(1 if j==k==4 else 0)
         for k in range(5)] for j in range(5)]
    Vu=sum((Fu[j][k]-F(21,5)*(j==k))**2 for j in range(5) for k in range(5))
    assert (T+q-F(16,5))**2<=F(4,5)*Vu
    assert (T+q-F(16,5))-(T-4+A/5)==(4-A)/5+q

# Independent rational 21-unit-vector Gegenbauer frame check
eye=[[F(int(i==j)) for j in range(5)] for i in range(5)]
u=eye*3+[[F(3,5),F(4,5),0,0,0],[F(3,5),0,F(4,5),0,0],
         [F(3,5),0,0,F(4,5),0],[F(3,5),0,0,0,F(4,5)],
         [F(4,5),F(3,5),0,0,0],[F(4,5),0,F(3,5),0,0]]
assert len(u)==21
P=sum(max(F(0),sum(u[i][k]*u[j][k] for k in range(5))**4
                   -F(1,4)*sum(u[i][k]*u[j][k] for k in range(5))**2)
      for i in range(21) for j in range(i+1,21))
F21=[[sum(v[j]*v[k] for v in u) for k in range(5)] for j in range(5)]
V21=sum((F21[j][k]-F(21,5)*(j==k))**2 for j in range(5) for k in range(5))
assert V21<=F(24,5)*P

print("PASS: 12 exact rational center-frame examples and 21-line check")
print("KC=",KC,"Pmax=",Pmax,"strict margin=",margin)
print("CONDITIONAL: A<=1/40 => V_z>1/5, S_z>120099/4000")
print("OPEN: Type E; global 40<=tau_5<=44")
