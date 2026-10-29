"""Exact rational verification of Type-E finite-range B coercivity.
This verifies algebra and explicit rational inequalities, not upstream
Type-E harmonic/graph certificates.
"""
from fractions import Fraction as F
from sympy import symbols, expand, Rational, simplify

B, d = symbols('B d', nonnegative=True)
c = Rational(15,172)
hlo = Rational(1,30)-d/2
bound = B/160 + hlo*(B-c*d**2) + d/240-d**2/16
coefficient = Rational(1,240)-d/16-B/2-c*d/30+c*d**2/2
assert simplify(expand(bound)-(Rational(19,480)*B+d*coefficient))==0
lower = F(1,240)-F(1,120)/16-F(1,360)/2-F(15,172)*F(1,120)/30
assert lower == F(553,247680), lower
assert lower>0
assert F(1,30)-F(1,120)/2>0
assert F(1,120)<F(1,30)
assert F(1,360)<F(1,16)
assert F(19,480)==F(1,160)+F(1,30)

# Rational diagnostic tests for the finite-range algebraic step.
for k in range(1001):
    dd = F(k,1000)*F(1,120)
    bb = F(1000-k,1000)*F(1,360)
    bracket = F(1,240)-dd/16-bb/2-F(15,172)*dd/30+F(15,172)*dd*dd/2
    assert bracket>=lower
print('PASS: symbolic expansion, rational constant, domains, and 1001 exact diagnostic cases')
