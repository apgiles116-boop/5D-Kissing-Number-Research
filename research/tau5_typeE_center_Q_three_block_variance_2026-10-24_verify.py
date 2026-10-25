#!/usr/bin/env python3
"""Exact symbolic verification for Type-E center/Q three-block variance.
The analytic block Cauchy-Schwarz argument is in the companion markdown note.
"""
import sympy as s

rho,d=s.symbols("rho d",real=True)
mu=s.Rational(8,7)
b=s.Rational(32,5)+s.Rational(6,5)*d-s.Rational(8,5)*rho
c=16-rho-b
lhs=(rho-mu)**2+(b-4*mu)**2/4+(c-9*mu)**2/9
rhs=s.Rational(42,25)*(mu-rho+d/3)**2+d**2/3
assert s.simplify(lhs-rhs)==0

S1=4+d
S2=s.Rational(4,5)+s.Rational(2,5)*d+s.Rational(4,5)*rho
assert s.simplify(2*(S1-S2)-b)==0

B=s.Rational(383,504)
r=B-s.Rational(3,4)
H=s.Rational(3,36)+r/(16*(1-r)**2)
assert H==s.Rational(250891,2988012)
cB=s.Rational(25,28)-s.Rational(5,4)*H
assert cB==s.Rational(65919115,83664336)

Etight=s.factor((s.Rational(42,25)*cB**2-s.Rational(5,7))/2)
assert Etight==s.Rational(7824330390487,47617150464768)

D=s.sqrt(s.Rational(8,125))
assert s.simplify((s.Rational(112,101)*cB)**2-D**2)>0
vertex=s.Rational(28,125)*s.sqrt(10)*cB
assert s.simplify(vertex**2-s.Rational(1,25))>0

T=s.Rational(1,25)
Enear=s.simplify((s.Rational(42,25)*(cB-s.Rational(25,48)*D)**2
                 +D**2/3+s.Rational(3,10)*T-s.Rational(5,7))/2)
assert s.simplify(Enear-(s.Rational(9312366342511,47617150464768)
                   -s.Rational(13183823,239040960)*s.sqrt(10)))==0
z=s.expand(Enear-s.Rational(1,50))
R=z.coeff(s.sqrt(10),0)
S=-z.coeff(s.sqrt(10))
assert R>0 and S>0
assert s.factor(R**2-10*S**2)==s.Rational(
    63836833008778530901655209,157457848498913566556200960000)
print("PASS: exact block identity and near-tight defect certificates")
print("T=0: Eplus-Lminus >=",Etight,"~",float(Etight))
print("T<=1/25: Eplus-Lminus >=",Enear,"~",float(Enear),">1/50")
