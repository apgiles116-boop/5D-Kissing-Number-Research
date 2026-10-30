#!/usr/bin/env python3
"""Exact rational regression for the sharp four-contact Walsh profile.
A verification aid; the universal theorem follows from the convexity proof.
"""
from fractions import Fraction as F
from itertools import product

H=F(1,2); Q=F(1,4)

def tmax(d):
    d=abs(d)
    assert 0<=d<=H
    return Q-d+3*d*d if d<=Q else 3*(H-d)**2

def phi(d):
    d=abs(d)
    assert 0<=d<=H
    return d*(1-4*d) if d<=Q else (2*d-H)*(1-2*d)

def vertex_max(d):
    target=4*d
    best=None
    for free in range(4):
        for signs in product((-H,H),repeat=3):
            y=list(signs); y.insert(free,target-sum(signs))
            if all(-H<=v<=H for v in y):
                val=sum(v*v for v in y)/4-d*d
                best=val if best is None or val>best else best
    return best

for j in range(101):
    d=F(j,200)
    assert vertex_max(d)==tmax(d)
    assert Q-d*d-tmax(d)==phi(d)
    assert phi(d)>=0
    dist=min(abs(d-q) for q in (F(0),Q,H))
    assert phi(d)>=dist/2
    if d>=F(3,8):
        assert tmax(d)<=F(3,4)*phi(d)
    if d>=F(7,16):
        assert tmax(d)<=Q*phi(d)

values=[-H,-Q,F(0),Q,H]
for ts in product(values,repeat=4):
    tpp,tpm,tmp,tmm=ts
    p=(tpp+tpm+tmp+tmm)/4
    b=(tpp+tpm-tmp-tmm)/4
    c=(tpp-tpm+tmp-tmm)/4
    d=(tpp-tpm-tmp+tmm)/4
    T=p*p+b*b+c*c
    W=T+d*d
    assert T<=tmax(d)
    assert Q-W>=phi(d)
    if abs(d)>=Q:
        eps=H-abs(d)
        assert T<=3*eps*eps
        assert max(abs(p),abs(b),abs(c))<=eps

# Rational geometric safe block: m1=(5/13)e3,z1=(12/13)e1;
# m2=(5/13)e1,z2=(12/13)e2.
p=F(0); b=F(60,169); c=F(0); d=F(0)
assert max(abs(p+sg*b+ta*c+sg*ta*d)
           for sg,ta in product((-1,1),repeat=2))<=H
assert p*p+b*b+c*c<=tmax(d)

print("PASS: 101 exact vertex maxima, 625 four-contact tuples,")
print("piecewise sharpness, quantization, absorption and geometric test")
print("At d=3/8: T_max =",tmax(F(3,8)),
      "; forced squared safe slack =",phi(F(3,8)))
