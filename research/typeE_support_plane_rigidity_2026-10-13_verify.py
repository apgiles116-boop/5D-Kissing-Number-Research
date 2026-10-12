"""Exact rational certificate for conditional support-plane rigidity.
Analytic geometric steps are proved in the accompanying Markdown note.
"""
from fractions import Fraction as F
from math import asin, degrees
Amax=F(383,504)
A=F(5,23)
d=A/(1-A)
sine=(F(3,5)-A/9)/(4+A/3)
assert A<=Amax
assert d==F(5,18)
assert sine==F(596,4215)
gap=d*d-4*sine*sine*(1-sine*sine)
assert gap==-F(1535336051479,1262555003002500)<0
assert sine<F(1,2) and d<F(1)
print("PASS: exact support-plane and fourth-moment contradiction")
print("rational gap:",gap)
print("CONDITIONAL on the unproved support-plane hypothesis: A>5/23")
print("Angular upper cap:",degrees(asin(float(d)))/2)
print("Angular lower floor:",degrees(asin(float(sine))))
