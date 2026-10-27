#!/usr/bin/env python3
"""Exact rational certificate checks: rank-14 Q-spectrum, P>23/1000, Type-E A>1/49."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

def g(c, lam, eta):
    t=max((eta-lam)/2,min((eta+lam)/2,c))
    return t*t-eta*t+lam*abs(t-c)

def pats(K,lo=12,hi=14,req=None):
    for ns in product(range(22),repeat=hi-lo+1):
        if sum(ns)==21 and sum((lo+i)*ns[i] for i in range(len(ns)))==2*K:
            if req is None or ns[req-lo]>=1:
                yield ns

def cost(K,lam,eta,req=None):
    return min((sum(n*g(F(k,4)-F(16,5),lam,eta)
                    for k,n in zip(range(12,15),ns)),ns)
               for ns in pats(K,req=req))

def vcap(K,p):
    return F(3,13)*(24*p-F(1,5)) if K==134 else F(3,7)*(24*p-F(3,10))

def tangent(K,p,lam,eta,r):
    C,ns=cost(K,lam,eta)
    v=vcap(K,p)
    L=F(6,5)+r/2+F(13,14)*p/r
    q=F(39,560)/r
    B=L-F(10,3)*lam-eta
    assert B>2*q*v
    return C,ns,v,C-24*lam*p-B*v+q*v*v

def U(k,a):
    return ((k+4)*a+9*a*a+5*a**3+a**4)/(16*(1-a)**2)

def degree14(K,p,lam,eta):
    C,ns=cost(K,lam,eta,req=14)
    B=F(3,2)-F(10,3)*lam-eta
    assert B>=0
    return C,ns,C-24*lam*p-B*vcap(K,p)

def main():
    S,V,P,E=sp.symbols("S V P E")
    raw=21*sp.Rational(16,25)+2*(P-E+S/4-sp.Rational(2,5)*S+sp.Rational(210,25))
    assert sp.simplify(raw.subs(S,sp.Rational(168,5)+V/2)
        -(sp.Rational(504,25)+2*(P-E)-3*V/20))==0

    p=F(23,1000)
    assert p<F(7,240) and 12*p+F(3,25)<F(9,20)
    assert tangent(134,p,F(3,10),F(0),F(1,5))==(
        F(91,400),(5,16,0),F(132,1625),F(101251,3250000))
    assert tangent(135,p,F(19,50),-F(3,10),F(1,6))==(
        F(633,2500),(3,18,0),F(27,250),F(4803,17500000))

    a=F(1,49)
    p0,p14,p13=U(20,a),U(14,a),U(13,a)
    assert (p0,p14,p13)==(
        F(316159,9834496),F(713179,29503488),F(3949,172872))
    assert F(11,20)-(12*p0+F(3,25))==F(2718283,61465600)>0
    assert F(7,240)-p14==F(736697,147517440)>0
    assert F(9,20)-(12*p14+F(3,25))==F(2454173,61465600)>0
    assert F(9,100)-F(13,7)*p14==F(232896761,5163110400)>0
    assert degree14(134,p14,F(2,5),F(1,10))==(
        F(147,400),(6,14,1),F(51776099,399526400))
    assert degree14(135,p14,F(1,2),-F(3,10))==(
        F(17,50),(4,16,1),F(2918819,86051840))
    assert p-p13==F(1691,10804500)>0
    print("PASS: exact rank-14 identity, universal P>23/1000, conditional A>1/49")

if __name__=="__main__":
    main()
