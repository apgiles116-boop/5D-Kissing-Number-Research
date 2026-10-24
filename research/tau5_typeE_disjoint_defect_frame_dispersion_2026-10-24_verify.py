#!/usr/bin/env python3
"""Exact rational certificate: Type-E disjoint-defect frame dispersion."""
from fractions import Fraction as F

B=F(383,504)
b=B/2
h=F(1,1000)
D0=F(1780062775,4032758016)
q0=F(40949,500000)
S_cap=F(3,16)+(B-F(3,4))**2
L=F(8790283,317520)
assert S_cap==F(47653,254016)
assert 30-3*B+B**2/F(10)-S_cap/2==L
assert b-h>F(1,4)
S_near=2*(F(1,16)+(b-F(1,4))**2)+2*h+4*h*h
L_near=30-3*B+B**2/F(10)-S_near/2
K_near=L_near-F(3,2)-D0-q0
assert S_near==F(1276298377,7938000000)
assert S_near<S_cap
assert L_near==F(146575669291,5292000000)
assert L_near-L==F(212857873,15876000000)
assert K_near==F(32355694067773,1260236880000)
assert K_near>L-F(3,2)-D0-q0

# Exact midpoint-only equality witness for (1), with E=0.
p,q=F(1,4),F(1,9)
a=[p,p,q,q]+[F(0)]*16
A=sum(a)
E=A-2*(p+q)
assert E==0
assert sum(x*x for x in a)==2*(p*p+q*q)+max(4*p*E+E*E,4*q*E+E*E,E/4)

# The general inequality (1) is proved analytically by the convex
# quadratic vertex reduction in the companion note, not by finite testing.
print("PASS exact rational frame constants")
print("PASS midpoint-only equality witness")
print("L_near =",L_near, "~",float(L_near))
print("K_near =",K_near, "~",float(K_near))
print("Conditional improvement =",L_near-L)
