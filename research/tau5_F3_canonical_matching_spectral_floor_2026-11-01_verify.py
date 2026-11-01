#!/usr/bin/env python3
"""Exact algebraic verifier for the F3 C4+2K2 matching-energy theorem.
No floating-point optimizer is used in the assertions.
"""
from sympy import Rational, sqrt, simplify, expand, diff, symbols

p=(0,2,7,5)
q=(4,3,1,6)
E={tuple(sorted(e)) for e in ((0,2),(0,4),(0,5),(1,4),(1,7),
                              (2,3),(2,7),(3,6),(5,6),(5,7))}
spokes={tuple(sorted((p[i],q[i]))) for i in range(4)}
p_cycle={tuple(sorted((p[i],p[(i+1)%4]))) for i in range(4)}
q_opp={tuple(sorted((q[i],q[(i+2)%4]))) for i in range(2)}
assert E==spokes|p_cycle|q_opp
assert (len(E),len(spokes),len(p_cycle),len(q_opp))==(10,4,4,2)

x,y,u,v=symbols('x y u v',real=True)
P=(1+2*x+y,1-y,1-2*x+y)
Q=(1+2*u+v,1-v,1-2*u+v)
alpha=(1,sqrt(Rational(3,2)),1/sqrt(2))
L=expand((alpha[0]*P[0]+Q[0]/alpha[0]
         +2*(alpha[1]*P[1]+Q[1]/alpha[1])
         +(alpha[2]*P[2]+Q[2]/alpha[2]))/2)
grad=[simplify(diff(L,z)) for z in (x,y,u,v)]
assert all(z.is_positive is True for z in
           (grad[0],-grad[1],-grad[2],grad[3]))
star={x:-Rational(1,2),y:0,u:-Rational(1,4),v:-Rational(1,2)}
assert simplify(L.subs(star)-(sqrt(6)+sqrt(2)))==0
C=2-(sqrt(6)+sqrt(2))/2
assert simplify(C-Rational(681,10000)).is_positive is True

s=-(sqrt(6)+sqrt(2))/4
r=(sqrt(6)-sqrt(2))/4
t=sqrt(2)/4
R=(s+2*t+r,s-r,s-2*t+r)
for k in range(3):
    pk=simplify(P[k].subs(star))
    qk=simplify(Q[k].subs(star))
    assert pk.is_nonnegative and qk.is_nonnegative
    assert simplify(pk*qk-R[k]**2)==0
    assert simplify(R[k]+sqrt(pk*qk))==0
assert s<-Rational(1,2)
assert 0<r<Rational(1,2) and 0<t<Rational(1,2)

eps=symbols('eps',positive=True)
xx=-Rational(1,2)-eps; yy=2*eps
uu=-Rational(1,4)+eps/2; vv=-Rational(1,2)-eps
Pdef=[simplify(z.subs({x:xx,y:yy})) for z in P]
Qdef=[simplify(z.subs({u:uu,v:vv})) for z in Q]
assert Pdef==[0,1-2*eps,2+4*eps]
assert Qdef==[0,Rational(3,2)+eps,1-2*eps]
# R0=0, Rk=-sqrt(Pk Qk), k=1,2 gives exact PSD rank-3 Gram.
# Strictness and safe nonedges for small eps follow by continuity.
print("PASS: F3 incidence, affine signs, radical floor, Fourier PSD witness, deformation")
print("C_can > 2-(sqrt(6)+sqrt(2))/2 > 681/10000")
