#!/usr/bin/env python3
"""Exact algebra checks for isolated-center/D5 covering and 3/40 orbit gap.

The accompanying mathematical note contains the geometric proof.
"""
from itertools import combinations
import sympy as s

s1,s2,t,U=s.symbols("s1 s2 t U", real=True)
assert s.expand(5*(s1+s2)**2-4*(s1*s1+4*s2*s2)
                -(s1-s2)*(s1+11*s2)) == 0
assert s.Rational(2,5)>s.Rational(1,3)
assert 1-s.Rational(1,4)/s.Rational(2,5)==s.Rational(3,8)
assert s.expand(s.Rational(5,3)*t**2+s.Rational(5,8)
                -(t+s.Rational(1,2))**2
                -s.Rational(2,3)*(t-s.Rational(3,4))**2)==0

x=s.symbols("x0:5", real=True)
V=[(x[i]+sign*x[j])/s.sqrt(2)
   for i,j in combinations(range(5),2) for sign in (1,-1)]
X2=sum(y*y for y in x)
U4=sum(y**4 for y in x)
W6=sum(y**6 for y in x)
assert s.expand(sum(v**2 for v in V)-4*X2)==0
assert s.expand(sum(v**4 for v in V)
                -s.Rational(3,2)*X2**2-s.Rational(1,2)*U4)==0
assert s.expand(sum(v**6 for v in V)
                -s.Rational(15,4)*X2*U4+s.Rational(11,4)*W6)==0

den=(15+105*U)/4-s.Rational(55,3)*U**2
assert s.expand(160*(1+U)**2-27*den
                -s.Rational(5,4)*(524*U**2-311*U+47))==0
assert 311**2-4*524*47 == -1791

C=4/s.sqrt(3)-2
A=s.Rational(383,504)
eps=s.Rational(3,40)
upper=s.simplify(20*eps**2+2*C*A*eps+C**2*A/4)
assert s.simplify(upper-(s.Rational(3133,1890)
                         -s.Rational(6511,7560)*s.sqrt(3)))==0
assert 3-s.Rational(45025,26044)**2==s.Rational(7619183,678289936)
assert upper<s.Rational(27,160)

print("PASS: exact D5 moment identities and discriminant -1791")
print("PASS: exact 27/160 D5 defect bound and Type-E epsilon>3/40 gap")
print("Unconditional isolated-center D5 orbit gap:", s.sqrt(s.Rational(2,5))-1/s.sqrt(3))
print("Status: Type E exclusion remains OPEN.")
