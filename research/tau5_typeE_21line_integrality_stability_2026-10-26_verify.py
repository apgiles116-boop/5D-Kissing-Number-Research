"""Exact rational audit of the 21-line integrality-stability certificate.
Universal validity is established by the companion mathematical proof,
not by finite numerical sampling.
"""
import sympy as s

V=s.symbols("V",nonnegative=True)
S=s.Rational(168,5)+V/2
assert s.expand(s.Rational(2,3)*S-14-S/4-s.Rational(5,24)*V)==0
assert s.Rational(24,5)*s.Rational(1,80)==s.Rational(3,50)
assert 24*s.Rational(1,80)==s.Rational(3,10)
for k in range(21):
    assert abs(s.Rational(k,4)-s.Rational(16,5))>=s.Rational(40-3*k,20)
assert s.Rational(840-6*134,20)==s.Rational(9,5)
assert s.Rational(840-6*135,20)==s.Rational(3,2)
assert s.Rational(3,10)-s.Rational(1,5)==s.Rational(1,10)
assert s.Rational(3,13)*s.Rational(1,10)==s.Rational(3,130)
assert s.Rational(24,5)+4*s.Rational(1,80)==s.Rational(97,20)
assert s.expand((s.Rational(3,2)+s.Rational(10,3)*V)**2/21
       -s.Rational(3,28)-s.Rational(10,21)*V)==s.Rational(100,189)*V**2
assert s.Rational(97,20)-s.Rational(10,21)==s.Rational(1837,420)
assert s.Rational(3,28)/s.Rational(1837,420)==s.Rational(45,1837)
assert s.Rational(45,1837)>s.Rational(3,130)
t=s.Rational(1,125)
K=(17+(1+t)**2*(7+t))/(16*(1-t)**2)
assert s.Rational(1,80)-t*K==s.Rational(939499,3844000000)
print("PASS: exact harmonic, integer, spectral, and rational checks")
