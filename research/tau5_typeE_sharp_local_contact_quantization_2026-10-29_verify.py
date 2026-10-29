#!/usr/bin/env python3
"""Exact symbolic and rational checks; the analytic proof is in the .md note."""
from fractions import Fraction as F
from random import Random
import sympy as sp

rho,d,eps=sp.symbols("rho d eps",real=True)
assert sp.simplify(2*(F(1,2)**2+rho**2-(F(1,2)-d/2)**2-(rho+d/2)**2)-((1-2*rho)*d-d**2))==0
assert sp.simplify((F(1,30)/15-F(1,30)**2)/16-F(1,14400))==0
r=F(1,30)-sp.sqrt(F(1,900)-16*eps)
assert sp.simplify(r/240-r**2/16-eps)==0

def gap(y,rho):
    x=[F(1,2)]*13+[rho]+[F(0)]*6
    y=sorted(y,reverse=True)
    delta=sum(abs(a-b) for a,b in zip(x,y))
    g=lambda t:t*(1-2*t)
    return delta,sum(map(g,y))-sum(map(g,x))

for rr in (F(2,5),F(7,15)):
    for k in range(21):
        dd=(F(1,2)-rr)*F(k,20)
        y=[F(1,2)]*13+[rr]+[F(0)]*6
        y[0]-=dd/2;y[13]+=dd/2
        delta,actual=gap(y,rr)
        assert delta==dd and actual==(1-2*rr)*delta-delta**2

rng=Random(20261029)
for _ in range(2000):
    rr=F(rng.randint(120,140),300)
    y=[F(1,2)]*13+[rr]+[F(0)]*6
    for _ in range(rng.randint(1,20)):
        i,j=rng.sample(range(20),2)
        if y[i]<y[j]:i,j=j,i
        move=min(y[i],F(1,2)-y[j])*F(rng.randint(0,100),100)
        y[i]-=move;y[j]+=move
    delta,actual=gap(y,rr)
    assert actual>=(1-2*rr)*delta-delta**2
print("PASS: symbolic inverse, sharp rational equality family, rational diagnostics")
