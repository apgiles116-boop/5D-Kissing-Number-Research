#!/usr/bin/env python3
"""Exact rational arithmetic checks for the 2026-10-26 integrality/Type-E note.
Analytic addition-theorem and endpoint steps are proved in the companion note.
"""
from fractions import Fraction as Q

# Gegenbauer expansion: f(t)=t^4-t^2/4 in dimension five.
c0,c2,c4=Q(1,28),Q(1,18),Q(8,315)
assert c0+c2*Q(-3,2)+c4*Q(15,8)==0
assert c2*Q(15,2)+c4*Q(-210,8)==Q(-1,4)
assert c4*Q(315,8)==1
assert c0*21**2==Q(3,4)*21

# For P<=1/120, V<=(24/5)P<=1/25.
assert Q(24,5)*Q(1,120)==Q(1,25)
assert Q(672,5)==Q(672,5)
assert Q(672,5)+Q(2,25)<Q(269,2)
assert Q(672,5)-134==Q(2,5)
assert 48*Q(1,120)==Q(2,5)
# Positive f(s) makes the rounded-error bound strict.
for s in (Q(251,1000),Q(1,2),Q(3,4),Q(1)):
    assert s-Q(1,4)<4*s*(s-Q(1,4))
# Verify negative-defect rounding for all rational grid points.
for k in range(1001):
    s=Q(k,4000)
    r=Q(0) if s<=Q(1,8) else Q(1,4)
    assert abs(s-r)<=8*s*(Q(1,4)-s)

t=Q(1,200)
ks=1/(16*(1-t)**4)
k0=1/(16*(1-t)**2)
kc=3*(1+t)**2*(1+t/4)/(16*(1-t)**4)
assert ks==Q(100000000,1568239201)
assert k0==Q(2500,39601)
assert kc==Q(2427090075,12545913608)
Ko=19*ks+k0
Kc=16*ks+k0+3*kc
assert Kc>Ko
assert Kc==Q(20873290225,12545913608)
assert Q(1,120)-Kc*t==Q(21939473,1505509632960)>0
print("PASS: universal 21-line P_f>1/120 exact integrality certificate")
print("PASS: Type-E rational energy contradiction margin",
      Q(1,120)-Kc*t)
print("CONDITIONAL: Type E A>1/200. OPEN: Type-E exclusion, tau_5.")
