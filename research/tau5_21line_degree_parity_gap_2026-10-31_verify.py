"""Exact rational check of the 21-line integer-degree certificate.
Verifies the arithmetic, not all spherical configurations.
"""
from fractions import Fraction as F
import sympy as s
p=F(71,5000)
x=s.symbols('x')
P2=(5*x**2-1)/4
P4=(21*x**4-14*x**2+1)/8
assert s.expand(x**4-x**2/4-(s.Rational(1,28)+P2/3+s.Rational(8,21)*P4))==0
assert F(24,5)*p<F(1,14)
for tag,large,count,rest,distance,denom in [
    ('134',F(1),5,F(1,25),F(1,5),13),
    ('135',F(3,5),3,F(9,200),F(3,10),7)]:
    vmax=F(3,denom)*(24*p-distance)
    budget=24*p-F(10,3)*vmax
    margin=(large-budget)**2/count+rest-F(22,5)*vmax
    assert 0<vmax<F(1,25) and 0<budget<F(9,20) and margin>0
    print(tag, 'vmax=',vmax,'budget=',budget,'margin=',margin)
assert F(3,4)*F(71,7500)==F(71,10000)
assert F(71,5000)>F(1,103)
assert F(71,7500)>F(2,309)
print('PASS')
