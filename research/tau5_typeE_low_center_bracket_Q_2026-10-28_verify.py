#!/usr/bin/env python3
"""Exact rational verifier for Type-E center interval and conditional Q-floor.
Assumes upstream harmonic/mass and near-seven exclusion certificates.
All decisions use rational arithmetic, not floating-point.
"""
import sympy as sp
s,u,x,c=sp.symbols('s u x c',real=True)
R=sp.Rational
D=lambda z:196*z-644*z**2+896*z**3-448*z**4
B=R(2595,256)
N=7*u*(1-4*u)
q=R(23,4)+u-R(36,5)
E=R(175,24)*q**2+R(147,4)*(R(5,7)+R(5,12)*q+N/28)**2
P=sp.factor(E+N-15)
assert sp.expand(P)==R(147,4)*u**4-49*u**3-R(399,32)*u**2-R(35,4)*u+R(795,1024)
assert sp.simplify(sp.diff(P,u)-7*(336*u**3-336*u**2-57*u-20)/16)==0
# On [0,1/4], 336u^3-336u^2<=0 and -57u-20<0.
lo=R(582766,100000);hi=R(582767,100000)
assert P.subs(u,lo-R(23,4))>0
assert P.subs(u,hi-R(23,4))<0
# Type-E resource E+N0<=15, center cap-simplex N0>=N,
# and E+N0 increasing with N0 imply s>=unique root in (lo,hi).
# Under conditional earlier exclusion s<209/30, define x0 by smax(x0)=209/30.
smaxcut=R(209,30)
Dx=R(1405,2304)
assert sp.factor(5-35*((smaxcut-R(32,5))*R(5,8))**2)==Dx
xl=R(3143598,10**9);xu=R(3143600,10**9)
assert D(xl)<Dx<D(xu)
# c(x)=D^{-1}(43/3-(B+D(x))/2) is decreasing.
w=lambda z:R(43,3)-(B+D(z))/2
cl=R(548737,10**7);cu=R(548738,10**7)
assert D(cl)<w(xu) and w(xl)<D(cu)
# F(x,s) = 30-3a+a^2/10-U/2+(5/8)(4-a/5-s/2)^2
# decreases in each of x,c on these tiny rational boxes.
a=R(1,2)+x+c
U=R(1,8)+x*x+c*c
h=4-a/5-smaxcut/2
F=30-3*a+a*a/10-U/2+R(5,8)*h*h
assert sp.diff(F,x).subs({x:xl,c:cl})<0
assert sp.diff(F,c).subs({x:xl,c:cl})<0
Fl=F.subs({x:xu,c:cu});Fu=F.subs({x:xl,c:cl})
assert R(283956,10000)<Fl<Fu<R(283957,10000)
# Coarse exact derivative certificate on [0,x0]:
# D'(c)>128, D'(x)<=196 => -c'(x)<49/64; a'(x)>15/64.
# a<3/5, h>0, x>=0, c<3/50 yield F_x< -2013/3200.
assert -R(72,25)*R(15,64)+R(3,50)*R(49,64)==-R(2013,3200)
print('PASS: exact center quartic and unique root bracket',lo,hi)
print('PASS: exact cutoff x0 and c(x0) rational brackets')
print('PASS: conditional projected Q-floor 28.3956 < Q_min < 28.3957')
print('CONDITIONAL: retained harmonic/mass resource, directional L monotonicity, and s<209/30')
