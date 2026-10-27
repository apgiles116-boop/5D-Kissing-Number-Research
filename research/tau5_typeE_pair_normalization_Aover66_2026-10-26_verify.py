#!/usr/bin/env python3
"""Exact rational certificate checker. Analytic inequalities are in the companion note."""
from fractions import Fraction as F
import sympy as sp

def g(c,lam,eta):
    t=max((eta-lam)/2,min((eta+lam)/2,c))
    return t*t-eta*t+lam*abs(t-c)

def U(k,a):
    return ((k+4)*a+9*a*a+5*a**3+a**4)/(16*(1-a)**2)

def vcap(K,p):
    return (F(3,13) if K==134 else F(3,7))*(24*p-(F(1,5) if K==134 else F(3,10)))

def check(K,p,lam,eta,require14=False):
    patterns=[(n12,n13,21-n12-n13)
        for n12 in range(22) for n13 in range(22-n12)
        if 12*n12+13*n13+14*(21-n12-n13)==2*K
        and (not require14 or 21-n12-n13>=1)]
    costs=[(n12*g(F(-1,5),lam,eta)+n13*g(F(1,20),lam,eta)
            +n14*g(F(3,10),lam,eta),(n12,n13,n14))
            for n12,n13,n14 in patterns]
    C,pat=min(costs)
    v=vcap(K,p)
    B=3+12*p-F(10,3)*lam-eta
    assert v>=0 and -B+F(10,3)*v<0
    margin=C-24*lam*p-B*v+F(5,3)*v*v
    assert margin>0
    return C,pat,v,margin

d=sp.symbols('d')
x=(sp.Rational(1,2)+d)**2
assert sp.expand(x*(x-sp.Rational(1,4))-(d/4+sp.Rational(5,4)*d*d+2*d**3+d**4))==0
ai,aj=sp.symbols('ai aj')
D=(1-ai)*(1-aj)
assert sp.expand(x*(x-D/4)-x*(x-sp.Rational(1,4))-(1-D)*x/4)==0

p=F(1,59)
assert check(134,p,F(3,10),F(0))==(F(91,400),(5,16,0),F(183,3835),F(969259,235315600))
assert check(135,p,F(1,2),F(-3,7))==(F(2841,9800),(3,18,0),F(27,590),F(2091,34113800))

a=F(1,66)
assert U(20,a)==F(533803,22651200)<F(7,240)
assert U(14,a)==F(5214463,294465600)
assert U(13,a)==F(4926967,294465600)
assert F(9,20)-12*U(20,a)-F(3,25)==F(17821,377520)>0
C,pat,v,m=check(134,U(14,a),F(3,10),F(0),True)
assert (C,pat,m)==(F(131,400),(6,14,1),F(506645887636151,5653544845520000))
C,pat,v,m=check(135,U(14,a),F(1,5),F(-1,10),True)
assert (C,pat,m)==(F(99,400),(4,16,1),F(41873920448669,1639193475920000))
assert F(1,59)-U(13,a)==F(3774547,17373470400)>0
print("PASS: quartic identities, universal P>1/59, degree-14 exclusions, Type-E A>1/66")
