#!/usr/bin/env python3
"""Exact audit of raw fixed and weighted quartic thresholds."""
from sympy import Matrix, Rational as R, sqrt, simplify, symbols

z1=Matrix([R(1,2),R(1,2),R(1,2),0,0])
z2=Matrix([R(1,2),R(1,2),0,R(1,2),0])
m1=Matrix([0,0,0,0,R(1,2)])
m2=Matrix([1/(2*sqrt(2)),-1/(2*sqrt(2)),0,0,0])
for z,m in [(z1,m1),(z2,m2)]:
    assert simplify(z.dot(z)) == R(3,4)
    assert simplify(m.dot(m)) == R(1,4)
    assert simplify(z.dot(m)) == 0
for si in (-1,1):
    for tj in (-1,1):
        assert abs(simplify((m1+si*z1).dot(m2+tj*z2))) == R(1,2)
r1=z1.dot(z1); r2=z2.dot(z2)
w=(z1.dot(z2))**2
h=1-r1*r2
D=w*(w-r1*r2/4)
F=w*(w-R(1,4))
assert (w,h,D,F)==(R(1,4),R(7,16),R(7,256),0)
assert simplify(D-F-h*w/4)==0

a=symbols('a0:20', real=True)
A=sum(a); U=sum(x*x for x in a)
H=sum(a[i]+a[j]-a[i]*a[j] for i in range(20) for j in range(i+1,20))
assert simplify(H-(19*A-(A*A-U)/2))==0

B,X,Y,Z=symbols('B X Y Z', real=True)
dots=[B+si*X+tj*Y+si*tj*Z for si in (-1,1) for tj in (-1,1)]
assert simplify(sum(v*v for v in dots)-4*(B*B+X*X+Y*Y+Z*Z))==0

Acap=R(383,504)
Phi=3*R(1,16)+(Acap-R(3,4))**2
Pcap=R(5792292955405,4129544208384)
Rcap=R(1780062775,4032758016)
Tcap=19*Acap/16-(Acap**2-Phi)/32+R(7,64)*Pcap
assert simplify(Tcap-R(39403364934925,37755832762368))==0
assert simplify(Rcap+Tcap-R(392481748566875,264290829336576))==0
print('PASS: exact safe-pair counterexample, threshold identity, 20-line energy identity, Walsh identity, rational envelope')
