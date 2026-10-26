#!/usr/bin/env python3
"""Exact rational coefficient checks for the Type-E Q-rank S upper bound."""
import sympy as s
A=s.symbols("A")
p=A/4+s.Rational(5,16)*A**2+A**3/4+A**4/16
expr=(s.Rational(19,10)*A+s.Rational(3,5)*A**2+s.Rational(3,10)*A**3+
      s.Rational(3,10)*(20-4*A+6*A**2)-(20-2*A)**2/350+p)
expected=(s.Rational(34,7)+s.Rational(33,28)*A+
          s.Rational(7563,2800)*A**2+s.Rational(11,20)*A**3+A**4/16)
assert s.expand(expr-expected)==0
U=s.Rational(20,3)*expected
assert U.subs(A,0)==s.Rational(680,21)
assert U.subs(A,s.Rational(1,40))==s.Rational(66741643,2048000)
assert U.subs(A,s.Rational(1,40))-s.Rational(3001691,100000)==s.Rational(131675283,51200000)
print("PASS: exact polynomial upper bound and low-energy gap")
