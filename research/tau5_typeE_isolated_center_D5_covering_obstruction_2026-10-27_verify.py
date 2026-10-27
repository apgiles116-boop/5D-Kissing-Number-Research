#!/usr/bin/env python3
"""Exact checks for isolated-center/D5 projective covering obstruction."""
import sympy as S

t,b=S.symbols("t b",nonnegative=True)
f=(t-b)**2+4*b**2
assert S.diff(f,b,2)==10
assert S.simplify(f.subs(b,0)-t*t)==0
assert S.simplify(f.subs(b,t/2)-S.Rational(5,4)*t*t)==0

c=S.sqrt(S.Rational(2,5))
cap=1/S.sqrt(3)
assert S.simplify(c*c-cap*cap)==S.Rational(1,15)
assert S.simplify(1-1/(4*c*c))==S.Rational(3,8)
assert S.Rational(3,8)>S.Rational(1,4)

cos_theta=S.sqrt(S.Rational(2,15))+S.sqrt(S.Rational(2,5))
assert S.simplify(c*cap+S.sqrt(1-c*c)*S.sqrt(1-cap*cap)-cos_theta)==0
assert 0<cos_theta<1
chord=S.sqrt(2-2*cos_theta)
assert chord>c-cap

x=S.ones(5,1)/S.sqrt(5)
vals=[]
for p in range(5):
    for q in range(p+1,5):
        for sign in (1,-1):
            d=S.zeros(5,1)
            d[p]=1/S.sqrt(2)
            d[q]=sign/S.sqrt(2)
            vals.append(S.simplify(abs(x.dot(d))))
assert len(vals)==20 and max(vals)==c and vals.count(c)==10

print("PASS exact D5 covering constant",c)
print("PASS isolated-center normalized cap",cap)
print("PASS impossible a_i >= 3/8 > 1/4")
print("PASS angular gap (radians)",S.acos(cos_theta).evalf(15))
print("PASS chord gap",chord.evalf(15))
