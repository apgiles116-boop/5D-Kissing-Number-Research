"""Exact rational checks for capped-mass quartic Type-E noncollapse.

Companion note proves the S^3 harmonic positivity, Karamata majorization,
and the pairwise analytic estimates. This script checks polynomial algebra,
monotonicities, exact spectral gaps, and a finite rational sanity grid.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

A,E,D=s.symbols("A E D",nonnegative=True)
q=(5+4*E)**2/s.Integer(64)
Lsix=(19*A+57*E+2*E**2)/4+(1+E/2)*(s.Rational(9,4)*A*E+s.Rational(17,4)*E**2+E**3)+(q-s.Rational(1,4))*(3*A+9*E+2*E**2)+q*(s.Rational(9,2)+4*E)*D
Lpath=(19*A+57*E+s.Rational(19,10)*E**2)/4+(1+E/2)*(s.Rational(109,50)*A*E+s.Rational(102,25)*E**2+E**3/2)+(q-s.Rational(1,4))*(2*A+s.Rational(21,4)*E+E**2)+q*(s.Rational(9,2)+4*E)*D

for name,L in [("six",Lsix),("path",Lpath)]:
    for var in [A,E,D]:
        p=s.Poly(s.expand(s.diff(L,var)),A,E,D)
        assert all(c>=0 for c in p.coeffs()),(name,var,p)
print("PASS: upper polynomial monotonicity")

assert s.Rational(109,50)**2>s.Rational(19,4)
assert s.Rational(13,8)**2-s.Rational(13,8)-1>0
assert s.Rational(18)**3/s.Integer(800)>6
print("PASS: sqrt(19)/2, golden-ratio, and Rcap rational checks")

A0=s.Rational(383,504)
assert A0-s.Rational(3,4)==s.Rational(5,504)
U=16+2*s.Rational(3,4)**4+s.Rational(499,504)**4+(s.Rational(3,4)-E)**4
R=(20-A0-E)**4/s.Integer(3200)-s.Rational(3,2)*U
cases=[
 ("six",s.Rational(3,10),s.Rational(3,4),Lsix,s.Rational(50930070610356481,129048256512000000)),
 ("global",s.Rational(673,2000),s.Rational(1780062775,4032758016),Lsix,s.Rational(670796742034030475489,89616844800000000000000)),
 ("canonical",s.Rational(461,1250),s.Rational(366383,1016064),Lpath,s.Rational(113450575137045459617281,31505922000000000000000000)),
]
for name,e,d,L,expected in cases:
    gap=s.factor(R.subs(E,e)-L.subs({A:A0,E:e,D:d}))
    assert gap==expected and gap>0,(name,gap)
    print("PASS:",name,"lambda_min >",e,"gap =",gap)

vals=[F(0),F(1,8),F(1,4)]
for aa in product(vals,repeat=3):
    At=sum(aa)
    if At>=1:continue
    k=int(4*At)
    r=At-F(k,4)
    for ee in product(vals,repeat=3):
        Et=sum(ee)
        if max(x+y for x,y in zip(aa,ee))>1:continue
        actual=sum((1-x-y)**4 for x,y in zip(aa,ee))
        if k==0:
            bstar=[At+Et,F(0),F(0)]
        else:
            bstar=([Et+F(1,4)]+[F(1,4)]*(k-1)+[r]+[F(0)]*3)[:3]
        assert actual<=sum((1-v)**4 for v in bstar)
print("PASS: finite exact Karamata sanity grid")
print("PASS: all exact arithmetic certificates")
