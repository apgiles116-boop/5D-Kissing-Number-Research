#!/usr/bin/env python3
from fractions import Fraction as F
Dstar=F(1780062775,4032758016)
d=F(5,18)
s=d-d**3/6
assert s==F(9595,34992)
assert F(191,432)-Dstar==F(2939033,4032758016)>0
eigen=F(3,40)*s**4
assert eigen-F(1,2500)==F(59970773847862061,2498755783880540160000)>0
c=F(73,200)
sig2=c/F(200)
sig1=c*F(343,800)
minor=sig1**2*sig2**2
assert sig2==F(73,40000)
assert sig1==F(25039,160000)
assert minor==F(3341024655409,40960000000000000000)
old=F(23387172587863,1638400000000000000000)
assert minor/old==F(40,7)
print('PASS: exact core Q gap and coplanar tomography constants')
