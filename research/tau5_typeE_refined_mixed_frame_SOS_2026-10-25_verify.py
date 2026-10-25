#!/usr/bin/env python3
"""Exact SymPy/Fraction checks of the Type-E mixed-frame SOS identity."""
from fractions import Fraction as F
import sympy as s

A, Ac, Ao, sc, so, V = s.symbols("A Ac Ao sc so V", real=True)
Es, Ec, corec, dot, sigR = s.symbols("Es Ec corec dot sigR", real=True)
base = 4*A - A**2/s.Integer(5) - 3*Ac + Ac**2-sc - (V-sc-so)/2
rhs = (A*(1-A/s.Integer(5)) + Ao*(3-Ac-Ao/2)
       +(Ac**2-sc)/2+so/2+(A**2-V)/2)
assert s.simplify((base-rhs).subs(A,Ac+Ao))==0
H_reconstructed = (A*(20-A)/5 + dot
                   -(3*Ac-Ac**2+sc-Ec)
                   -((V-sc-so)/2-corec)+Es)
assert s.simplify((H_reconstructed+sigR-rhs
                   -Es-Ec-corec-(sigR+dot)).subs(A,Ac+Ao))==0
h,c,p,q=s.symbols("h c p q",real=True)
safe=s.Rational(1,2)*((h-c)**2-(p+q)**2+(h+c)**2-(p-q)**2)
assert s.expand(safe-h*h-c*c+p*p+q*q)==0
B=F(383,504)
assert 1-B/F(5)==F(2137,2520)
assert 3-B==F(1129,504)
assert B<1
print("PASS: exact SOS identity and safe-pair decomposition")
print("PASS: coefficients 2137/2520 and 1129/504")
print("No Type-E elimination is asserted.")
