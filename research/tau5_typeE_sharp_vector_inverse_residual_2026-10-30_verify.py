"""Exact-rational checks for the improved Type-E inverse-Q vector rounding.

The inequalities are proved algebraically in the accompanying note. This script
checks rational constants and the terminal contradiction. It does not rerun
the upstream ~988k-cell interval certificate.
"""
from fractions import Fraction as F

assert F(2, 1) / (1-F(2,100)) == F(100,49)
assert F(1,2)/(1-F(1,200)) == F(100,199)
assert F(100,199) <= F(25,49)
assert F(10,7)+F(5,7)==F(15,7)

s=F(97,56)
assert s*s>3
K2=(44*s)**2+(1+22*s*F(501,100))**2
assert K2==F(334302852689,7840000)
assert 207**2-K2==F(1633307311,7840000)>0

r=F(49,1117800**2)
assert r==F(49,1249476840000)
assert r<F(1,10000)
assert 207*F(7,1117800)==F(7,5400)<F(1,10)
assert F(15,7)*F(7,5400)==F(1,360)
old=F(1,441000**2)
assert r/old==F(2941225,385641)>F(762,100)

e=F(1,360)
d2=2*e*e-e**4/2
assert d2==F(518399,33592320000)>F(1,255**2)
print('PASS: exact vector-rounding constants and improved Q-residual floor')
print('new lower bound:',r,'~',float(r))
print('improvement factor:',r/old,'~',float(r/old))
