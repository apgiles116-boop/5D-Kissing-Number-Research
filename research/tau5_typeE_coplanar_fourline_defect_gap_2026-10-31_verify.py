#!/usr/bin/env python3
"""Exact certificate for Type-E coplanar four-line defect theorem.
Analytic concavity and cyclic-gap proofs are in the companion .md file.
"""
from fractions import Fraction as F
import math
import random
import sympy as s

# Machin identity: (5+i)^4(239-i) has equal positive real/imag parts.
assert 476*239+480 == 480*239-476
# Five alternating terms: upper bound on atan(1/5).
a_upper=sum((-1)**k*F(1,(2*k+1)*5**(2*k+1)) for k in range(5))
# Two alternating terms: lower bound on atan(1/239).
b_lower=F(1,239)-F(1,3*239**3)
pi_upper=16*a_upper-4*b_lower
assert pi_upper<F(355,113)

x=F(257*355,960*113)
assert x<1
cos_lower=F(1)-x*x/2+x**4/24-x**6/720
assert cos_lower>F(2,3)
print("Exact cos Taylor margin over 2/3:",cos_lower-F(2,3))

# Verify geometric-mean affine minorant at square corners.
c0=2*s.sqrt(3)-3
for b,c in [(s.Rational(0),s.Rational(0)),
            (s.Rational(1,4),s.Rational(0)),
            (s.Rational(0),s.Rational(1,4)),
            (s.Rational(1,4),s.Rational(1,4))]:
    p=s.sqrt((s.Rational(3,4)+b)*(s.Rational(3,4)+c))
    assert s.simplify(p-(s.Rational(3,4)+c0*(b+c)))>=0
assert 4-s.sqrt(15)>0

theta=math.acos(2/3)
Delta=math.pi/3-theta
k=1/(4*theta)
h=Delta/(2*theta)
floor=k*(4*theta-math.pi)+2*h*F(121,504)
assert floor>1/8
assert abs(floor-(383/504-257*math.pi/(1512*theta)))<1e-13
print("Coplanar Type-E raw defect floor:",floor)
print("Margin over 1/8:",floor-1/8)

def defect(angles,a):
    return sum(max(math.sqrt((1-a[i])*(1-a[j]))*
                   abs(math.cos(angles[i]-angles[j]))-.5,0)
               for i in range(4) for j in range(i+1,4))

angles=[0,theta,2*theta,3*theta]
assert abs(defect(angles,[.25]*4)-1/9)<1e-13

rng=random.Random(20261031)
for _ in range(70000):
    b,c=rng.random()/4,rng.random()/4
    g=rng.random()*math.pi
    p=math.sqrt((.75+b)*(.75+c))
    assert max(p*abs(math.cos(g))-.5,0)>=k*(theta-g)+h*(b+c)-1e-12
    a=[rng.random()/4 for i in range(4)]
    if sum(a)>383/504:
        fac=(383/504)/sum(a)
        a=[fac*v for v in a]
    phi=[0]+[rng.random()*math.pi for i in range(3)]
    assert defect(phi,a)>=k*(4*theta-math.pi)+2*h*(1-sum(a))-1e-12
print("All exact checks and 70,000 deterministic sanity tests passed.")
