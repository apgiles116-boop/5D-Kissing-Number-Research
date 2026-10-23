#!/usr/bin/env python3
"""Exact scalar/symbolic checks for the 2026-10-23 degree-counted Type-E note.
Does not independently prove the inherited Type-E graph/mass reductions.
"""
from fractions import Fraction as F
import sympy as s

t=s.symbols("t",real=True)
P2=(5*t*t-1)/4
P4=(21*t**4-14*t*t+1)/8
assert s.simplify(7*t*t*(4*t*t-1)-(1+s.Rational(28,3)*P2+s.Rational(32,3)*P4))==0

p0=(7*s.sqrt(15)-21)/20
d0=s.Rational(1,10)-p0/7
assert s.simplify(7*d0-28*d0*d0-p0)==0
assert s.simplify(2*p0/7-s.Rational(1,8)).is_negative
assert s.simplify(3*p0/35-s.Rational(1,20)).is_negative

A,C,L=s.symbols("A C L",nonnegative=True)
B=s.Rational(7,4)/(1-A)**2*(20*A-3*C+(1+A)**2*(7*C+C*C-L))
f=s.Rational(7,4)*A/(1-A)**2*(17+(1+A)**2*(7+A))
R=s.Rational(7,4)/(1-A)**2*((A-C)*((1+A)**2*(7+A+C)-3)+(1+A)**2*L)
assert s.simplify(f-B-R)==0

a=F(71393,10_000_000)
q=F(7,4)*a/(1-a)**2*(17+(1+a)**2*(7+a))
assert F(735)-(20*q+21)**2>0

al,cl=F(1,125),F(1,350)
b=F(7,4)/(1-al)**2*(20*al-3*cl+(1+al)**2*(7*cl+cl*cl))
assert b==F(23482559,76880000)
assert b<F(611,2000)
print("PASS: exact Gegenbauer identity, irrational 21-line gap,")
print("      degree-counted stability identity, Type-E energy floor,")
print("      and near-zero core localization.")
print("Note: inherited Type-E reductions are assumptions, not verified here.")
