#!/usr/bin/env python3
"""Exact rational checks for the outside-sixteen frame-gap proof."""
from fractions import Fraction as Q
import sympy as sp

delta=Q(1,27)
A=Q(383,504)
c=Q(1,4)+delta
D=A+delta
r=D-2*c
bmin=Q(3,4)-delta
vmax=(Q(1,2)+delta/2)/bmin
assert (c,D,r,bmin,vmax)==(Q(31,108),Q(1205,1512),Q(337,1512),Q(77,108),Q(8,11))

def g(d,e):
    d,e=Q(d),Q(e)
    B=(1-d)*(1-e)
    return (1-B)/(16*B*B)

G=g(c,c)+2*g(c,r)+26*g(c,0)+13*g(r,0)
assert G==Q(14734618533396,9706633446125)<Q(38,25)
K=(4*vmax**3-vmax/2)/bmin
assert K==Q(168912,102487)
increment=K*Q(15,2)*delta
assert increment==Q(46920,102487)<Q(23,50)
assert G+increment==Q(1743495708036,882421222375)
assert 2-G-increment==Q(21346736714,882421222375)>0

t=sp.symbols('t')
f=t**4-t**2/sp.Integer(4)
assert sp.expand(f-sp.gegenbauer(0,1,t)/16-sp.gegenbauer(2,1,t)/8-sp.gegenbauer(4,1,t)/16)==0
u,v=sp.symbols('u v',positive=True)
h=(1-u*v)/(16*u**2*v**2)
H=sp.hessian(h,(u,v))
assert sp.simplify(H[0,0]-(3-u*v)/(8*u**4*v**2))==0
assert sp.simplify(H.det()-(u*v-2)*(3*u*v-10)/(256*u**6*v**6))==0
print("PASS: Gegenbauer, convexity, exact simplex vertex, and positive margin")
print("Exact contradiction margin:",2-G-increment)
