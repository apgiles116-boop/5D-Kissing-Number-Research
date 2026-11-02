"""Exact arithmetic checker: Type E rank-four quartic frame noncollapse, 2026-11-02.

The companion note proves the harmonic addition-theorem positivity and
AM-GM estimates. This script independently checks polynomial expansions,
monotonicity coefficients, and the three rational contradictions.
"""
from fractions import Fraction as F
import sympy as s

x=s.symbols("x")
f=s.Rational(3,8)*x*x*(4*x*x-1)
P0=s.Integer(1)
P2=s.gegenbauer(2,1,x)/3
P4=s.gegenbauer(4,1,x)/5
assert s.expand(f-s.Rational(3,32)*P0-s.Rational(9,16)*P2-s.Rational(15,32)*P4)==0
assert f.subs(x,1)==s.Rational(9,8)
print("PASS: exact S3 Gegenbauer expansion")

ti,tj,ss=s.symbols("ti tj ss",positive=True)
weighted=s.expand(ti**2*tj**2*f.subs(x,ss/s.sqrt(ti*tj)))
assert s.simplify(weighted-s.Rational(3,8)*(4*ss**4-ti*tj*ss**2))==0
print("PASS: polynomialized quartic kernel")

A,E,D=s.symbols("A E D",nonnegative=True)
q=(5+4*E)**2/s.Integer(64)
R=(20-A-E)**4/s.Integer(3200)-s.Rational(3,2)*(20-A-E)
L=(19*A+57*E+2*E**2)/4+(1+E/2)*(s.Rational(9,4)*A*E+s.Rational(17,4)*E**2+E**3)+(q-s.Rational(1,4))*(3*A+9*E+2*E**2)+q*(s.Rational(9,2)+4*E)*D
for var in (A,E,D):
    coeffs=s.Poly(s.expand(s.diff(L,var)),A,E,D).coeffs()
    assert all(c>=0 for c in coeffs),(var,coeffs)
assert F(20)-F(383,504)-F(29,100)>18
assert F(18)**3/F(800)-F(3,2)>0
print("PASS: monotonicity of polynomial bounds")

A0=F(383,504)
cases=[
 (F(3,4),F(1,4),F(78380992451281,206477210419200)),
 (F(1780062775,4032758016),F(7,25),F(19455206461371049681,80655160320000000000)),
 (F(366383,1016064),F(29,100),F(11317880882876435281,80655160320000000000)),
]
for D0,E0,expected in cases:
    gap=s.factor((R-L).subs({
        A:s.Rational(A0.numerator,A0.denominator),
        E:s.Rational(E0.numerator,E0.denominator),
        D:s.Rational(D0.numerator,D0.denominator)
    }))
    assert gap==s.Rational(expected.numerator,expected.denominator) and gap>0
    print("PASS: D <=",D0," => lambda_min(Z) >",E0,"; gap",gap)
print("PASS: all exact rational certificates")
