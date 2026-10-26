"""Exact rational verifier for the shifted-Huber P>1/71 and Type-E A>1/89."""
from fractions import Fraction as F

def g(k, lam, eta):
    c=F(k,4)-F(16,5)
    z=eta/2
    if abs(c-z)<=lam/2: e=c
    else: e=z+(lam/2 if c>z else -lam/2)
    return e*e-eta*e+lam*abs(e-c)

p=F(1,71)
assert F(24,5)*p==F(24,355)
assert 24*p==F(24,71)

l=F(3,10); eta=F(0)
assert g(12,l,eta)==F(3,80) and g(13,l,eta)==F(1,400)
assert all(g(k-1,l,eta)-2*g(k,l,eta)+g(k+1,l,eta)>=0 for k in range(1,20))
C=5*g(12,l,eta)+16*g(13,l,eta)
assert C==F(91,400)
low=(C-24*l*p)/(F(24,5)+4*p-F(10,3)*l-eta)
up=(24*p-F(1,5))*F(3,13)
assert low==F(3581,109520) and up==F(147,4615)
assert low-up==F(17075,20217392)>0

l=F(1,5); eta=-F(1,10)
assert g(12,l,eta)==F(7,400) and g(13,l,eta)==F(3,400)
assert all(g(k-1,l,eta)-2*g(k,l,eta)+g(k+1,l,eta)>=0 for k in range(1,20))
C=3*g(12,l,eta)+18*g(13,l,eta)
assert C==F(3,16)
low=(C-24*l*p)/(F(24,5)+4*p-F(10,3)*l-eta)
up=(24*p-F(3,10))*F(3,7)
assert low==F(2043,73096) and up==F(81,4970)
assert low-up==F(2116467,181643560)>0

A=F(1,89)
P0=(24*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)
P15=(19*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)
assert P0==F(17007011,959512576)
assert P15==F(6741083,479756288)
assert F(4,5)-24*P0>0
assert (F(4,5)-24*P0)**2-F(96,25)*P0==F(1039618626526225,14385380992221184)>0
assert p-P15==F(1139395,34062696448)>0

print("PASS: universal exact 21-line quartic gap P>1/71")
print("PASS: conditional Type-E total midpoint energy A>1/89")
print("exact contradiction margin:",p-P15)
