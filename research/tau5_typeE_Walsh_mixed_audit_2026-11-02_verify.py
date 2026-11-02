#!/usr/bin/env python3
"""Exact checks: singleton mixed-Walsh signs, endpoint-average error, Q floor."""
import sympy as s
from fractions import Fraction as F

c,d,p,q=s.symbols("c d p q",real=True)
def contact(si,sj):
    return c+si*sj*d+sj*p+si*q
assert s.expand(contact(1,1)-(c+d+p+q))==0
assert s.expand(contact(-1,-1)-(c+d-p-q))==0
assert s.expand(contact(1,-1)-(c-d-p+q))==0
assert s.expand(contact(-1,1)-(c-d+p-q))==0

t=s.symbols("t",positive=True)
a=t/2
D=t*(1-t)/2
G=s.Matrix([[a,0,-D,-D],
            [0,1-a,-D,-s.Rational(1,2)-D],
            [-D,-D,a,0],
            [-D,-s.Rational(1,2)-D,0,1-a]])
X=G[:2,:2];Y=G[:2,2:4]
Bp=s.simplify(X+Y);Bm=s.simplify(X-Y)
assert s.factor(Bp.det())==0
assert s.simplify(Bp[0,0]-t*t/2)==0
assert s.simplify(Bm.det()-t*(3-2*t)/2)==0
assert s.simplify(Bm[0,0]-t*(2-t)/2)==0
sub={c:-D,d:-s.Rational(1,2)-D,p:-D,q:-D}
assert s.simplify(contact(1,1).subs(sub)+s.Rational(1,2)+4*D)==0
assert s.simplify(contact(-1,-1).subs(sub)+s.Rational(1,2))==0
for si,sj in [(1,-1),(-1,1)]:
    assert s.simplify(contact(si,sj).subs(sub)-s.Rational(1,2))==0
print("PASS sharp singleton witness and endpoint constraints")

G0=s.Matrix([[s.Rational(1,10),0,0,s.Rational(1,10)],
             [0,s.Rational(9,10),s.Rational(1,10),0],
             [0,s.Rational(1,10),s.Rational(1,10),0],
             [s.Rational(1,10),0,0,s.Rational(9,10)]])
assert all(v>0 for v in G0.eigenvals())
vals=[contact(si,sj).subs({c:0,d:0,p:s.Rational(1,10),q:s.Rational(1,10)})
      for si,sj in [(1,1),(-1,-1),(1,-1),(-1,1)]]
assert vals==[s.Rational(1,5),-s.Rational(1,5),0,0]
assert (vals[0]+vals[1])/2==0 and vals[0]>0
print("PASS exact local counterexample to endpoint-average substitution")

G2=s.Matrix([[s.Rational(1,5),0,-s.Rational(1,10),0],
             [0,s.Rational(4,5),0,-s.Rational(3,5)],
             [-s.Rational(1,10),0,s.Rational(1,5),0],
             [0,-s.Rational(3,5),0,s.Rational(4,5)]])
assert all(v>0 for v in G2.eigenvals())
vals2=[contact(si,sj).subs({c:-s.Rational(1,10),d:-s.Rational(3,5),p:0,q:0})
       for si,sj in [(1,1),(-1,-1),(1,-1),(-1,1)]]
assert vals2==[-s.Rational(7,10),-s.Rational(7,10),s.Rational(1,2),s.Rational(1,2)]
print("PASS double-contact exception witness")

A=F(383,504)
assert F(3,4)<A<F(1,1)
r=A-F(3,4)
L=F(30)-3*A+A*A/F(10)-F(1,2)*(F(3,16)+r*r)
assert L==F(8790283,317520)
old=F(17456771,635040)
assert L-old==F(131,672) and L>old
print("PASS refined global Q floor:",L,"=",float(L),"increase:",L-old)
