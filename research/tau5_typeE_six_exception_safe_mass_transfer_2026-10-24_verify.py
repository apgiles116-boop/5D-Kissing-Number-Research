#!/usr/bin/env python3
"""Exact SymPy checks for Type-E six-exception safe-mass transfer (2026-10-24)."""
import sympy as s

B=s.Rational(383,504)
D=s.Rational(1780062775,4032758016)
assert s.Rational(1,4)<D<s.Rational(1,2)
M=s.Rational(3,16)+(B-s.Rational(3,4))**2
assert M==s.Rational(47653,254016)

# Raw frame identity: tr(S_z^2)=(20-A)^2/5+||Delta-W||^2.
A,M2,V=s.symbols("A M2 V")
raw=s.expand(((20-A)**2/5+V-(20-2*A+M2))/2)
assert s.simplify(raw-(30-3*A+A*A/10-M2/2+V/2))==0

# Piecewise capped-simplex floor is decreasing for A<=B.
for k in range(4):
    t=s.symbols("t")
    a=s.Rational(k,4)+t
    f=30-3*a+a*a/10-(s.Rational(k,16)+t*t)/2
    df=s.diff(f,t)
    assert df.subs(t,0)<0 and df.subs(t,s.Rational(1,4))<0
    assert s.diff(df,t)<0

F=s.factor(30-3*B+B*B/10-M/2)
assert F==s.Rational(8790283,317520)
assert F-s.Rational(17456771,635040)==s.Rational(131,672)

# For 6 defects in [0,1/4], total <=D in (1/4,1/2),
# sum squares <= (1/4)^2+(D-1/4)^2 by convexity.
exc=s.factor(s.Rational(3,2)+D+s.Rational(1,16)+(D-s.Rational(1,4))**2)
assert exc==s.Rational(13,8)+D/2+D**2
L=s.factor(F-exc)
assert L==s.Rational(2085231131661776940907,81315686078061281280)
assert L>s.Rational(409,16)  # <=75 raw-safe pairs above 1/4 impossible
assert L>184*s.Rational(1,9)+37*(s.Rational(1,4)-s.Rational(1,9))

# (1+2d)^2<=1+5d for 0<=d<=1/4.
d=s.symbols("d")
assert s.expand(1+5*d-(1+2*d)**2)==d-4*d*d

C=s.factor(s.Rational(11,45)*B*B+s.Rational(5,9)*M+s.Rational(5,18)*D)
assert C==s.Rational(133562881183,362948221440)
assert C<s.Rational(4,5)*B*B

print("PASS: exact frame identity, capped-simplex bound, six-defect mass,")
print("      >=76 raw-safe correlations >1/4, and Q-frame transfer.")
print("F0 =",F,"~",float(F))
print("L0 =",L,"~",float(L))
print("C0 =",C,"~",float(C))
