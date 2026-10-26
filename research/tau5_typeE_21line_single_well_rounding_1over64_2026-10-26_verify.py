#!/usr/bin/env python3
"""Exact rational audit of the 21-line 1/64 gap and conditional Type-E A>1/99.

The analytic convexity, Gegenbauer and PSD arguments are in the .md proof.
"""
from fractions import Fraction as Q
from math import comb

# Normalized dimension-five Gegenbauer coefficients.
assert Q(1,28)+Q(1,3)*Q(-1,4)+Q(8,21)*Q(1,8)==0
assert Q(1,3)*Q(5,4)+Q(8,21)*Q(-14,8)==-Q(1,4)
assert Q(8,21)*Q(21,8)==1
assert Q(441,28)==Q(63,4)
assert (Q(441,5)-21)/2==Q(168,5)

# Under P<=1/64, V<=3/40 and y^2=5V/6<=1/16.
assert Q(24,5)*Q(1,64)==Q(3,40)
assert Q(5,6)*Q(3,40)==Q(1,16)
# E=134 forces y<3/20.
assert 2*Q(3,20)+Q(12,5)*Q(3,20)**2==Q(177,500)>Q(7,20)
assert Q(6,5)*Q(3,20)**2==Q(27,1000)<Q(1,36)
assert 2751<Q(105,2)**2
assert Q(3,8)+Q(19,2)*Q(3,20)==Q(9,5)
# E=135 forces y<=1/12.
assert Q(1,12)-Q(6,5)*Q(1,12)**2==Q(3,40)
assert Q(6,5)*Q(1,12)**2==Q(1,120)<Q(1,36)
assert Q(3,8)+Q(19,2)*Q(1,12)==Q(7,6)<Q(3,2)
for d in range(21):
    assert abs(Q(d)-Q(64,5)) >= 8-Q(3,5)*d
assert 42-Q(3,10)*134==Q(9,5)
assert 42-Q(3,10)*135==Q(3,2)

# Type-E pair counts, coefficient and exact contradiction.
assert comb(16,2)+16*4==184
assert 184+20+comb(4,2)==210
assert 15+4+1==20 and 16+1==17
t=Q(1,99)
ko=20/(16*(1-t)**2)
kc=(17+(1+t)**2*(7+t))/(16*(1-t)**2)
assert kc==Q(478267,310464)>ko
assert Q(1,64)-kc*t==Q(991,15367968)>0
print("PASS: exact rational identities and strict margins")
