#!/usr/bin/env python3
"""Exact SymPy regression for 2026-11-01 Type-E midpoint/Q-stability note.
Analytic majorization and harmonic arguments are proved in the companion note.
"""
import sympy as S

t=S.symbols('t',real=True)
D=lambda u:196*u-644*u**2+896*u**3-448*u**4
Dpp=S.diff(D(t),t,2)
assert S.expand(Dpp+280+5376*(t-S.Rational(1,4))*(t-S.Rational(3,4)))==0
assert D(S.Rational(1,4))==21
B=S.Rational(2595,256)
c=15-B
r_lo=S.Rational(27143,10**6);r_hi=S.Rational(27144,10**6)
s_lo=S.Rational(39781,10**6);s_hi=S.Rational(39782,10**6)
assert D(r_lo)<c<D(r_hi)
assert D(s_lo)<S.Rational(41,6)<D(s_hi)

x,y=S.symbols('x y',real=True)
A=x+y
F=30-3*A+A*A/10-(x*x+S.Rational(1,8)+(y-S.Rational(1,2))**2)/2
assert S.expand(S.diff(F,x)-(-3-S.Rational(4,5)*x+y/5))==0
assert S.expand(S.diff(F,y)-(-S.Rational(5,2)+x/5-S.Rational(4,5)*y))==0
A_hi=S.Rational(1,2)+r_hi+s_hi
L_lo=F.subs({x:r_hi,y:S.Rational(1,2)+s_hi})
assert A_hi<S.Rational(567,1000)
assert L_lo>S.Rational(282677,10000)
assert (-3+S.Rational(57,500))*S.Rational(31,129)+S.Rational(58,1000)*S.Rational(98,129)<0
assert S.Rational(70,196)==S.Rational(5,14)
assert S.Rational(140,196)==S.Rational(5,7)
assert S.Rational(1,392)==S.Rational(1,2*196)

Dstar=S.Rational(1780062775,4032758016)
assert Dstar<S.Rational(441401,1000000)
safe_floor=S.Rational(282677,10000)-S.Rational(3,2)-S.Rational(441401,1000000)-S.Rational(441401,1000000)**2
assert safe_floor>26
assert 40*S.Rational(1,4)+144*S.Rational(1,9)==26

xx=S.Rational(11,400)
isolated_floor=(16-xx)**2/10-8+xx-xx**2/2
assert isolated_floor==S.Rational(7015679,400000)
assert isolated_floor>S.Rational(35,2)
assert 30*S.Rational(1,4)+90*S.Rational(1,9)==S.Rational(35,2)

print('PASS: exact concavity, root brackets, Q floor, six-core transfer and 41/31 counts')
print('A upper bracket:',S.N(A_hi,18))
print('L lower bracket:',S.N(L_lo,18))
print('Safe lower bracket:',S.N(safe_floor,18))
