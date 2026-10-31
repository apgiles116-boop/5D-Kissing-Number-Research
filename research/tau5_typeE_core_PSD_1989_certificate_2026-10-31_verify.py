"""Exact rational verification of the Type-E four-core Q6 < 1989/1000 certificate.

Proof is the analytic four-case argument in the companion .md file.
No floating-point inequality is used as a proof step.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

T = F(383, 504)
D = F(1780062775, 4032758016)
target = F(1989, 1000)
h = F(1, 100)
p0, q0, q1 = F(11, 50), F(41, 250), F(1, 5)
c0 = F(273, 5000)
def Fmax(t):
    return F(1, 16) + (t-F(1, 4))**2

B = F(3, 2)+D/4+Fmax(D)+3*T/8
C = F(3, 2)+D+Fmax(D)
d0 = D-h
assert F(1, 4)<d0<D<F(1, 2)
assert T/2<F(19, 50)

# I: delta <= D-1/100
case1 = F(3, 2)+d0/4+Fmax(d0)+3*T/8
assert case1 < target

# II: q <= 41/250
def gap_small_q(t):
    return Fmax(t)-(F(1, 4)**2+q0**2+(t-F(1, 4)-q0)**2)
assert gap_small_q(d0) > B-target
assert gap_small_q(d0+F(1, 1000)) > gap_small_q(d0)
case2 = B-gap_small_q(d0)
assert case2 < target

# III: 41/250 < q <= 1/5, p <= 11/50
def gap_middle(t):
    return Fmax(t)-(p0**2+q1**2+(t-p0-q1)**2)
assert gap_middle(d0) > B-target
assert gap_middle(d0+F(1, 1000)) > gap_middle(d0)
case3 = B-gap_middle(d0)
assert case3 < target

# IVa: q>1/5, so p+q>2/5>T/2, forcing adjacent pairs
assert 2*q1>T/2
case4a = C-F(7, 100)*(1-F(7, 100))
assert case4a < target

# IVb: p>11/50, q>41/250, forcing adjacent pairs
assert p0+q0==F(48, 125)>T/2
rad = (F(1, 16)-p0**2)*(F(1, 16)-q0**2)
assert rad==F(1255041, 2500000000)
assert rad<F(2243, 100000)**2
assert p0*q0-F(2243, 100000)==c0/4
case4b = C-c0*(1-c0)
assert case4b < target

# Strict safe-correlation floors
Qglobal = F(17456771, 635040)
Qcenter = F(5876056025347, 211680000000)
assert Qglobal-target == F(404841911, 15876000)
assert Qcenter-target == F(5455024505347, 211680000000)

# Supplementary exact-rational Gram checks; not an exhaustive proof
rng = Random(20261031)
for _ in range(1500):
    ms = [[F(rng.randint(-5, 5), 100) for k in range(5)] for i in range(4)]
    a = [sum(t*t for t in m) for m in ms]
    if max(a)>F(1, 4) or sum(a)>T:
        continue
    def dot(u, v):
        return sum(x*y for x,y in zip(u,v))
    for i,j,k in combinations(range(4),3):
        cij,cik,cjk = dot(ms[i],ms[j]),dot(ms[i],ms[k]),dot(ms[j],ms[k])
        assert (a[i]*cjk-cij*cik)**2 <= (a[i]*a[j]-cij*cij)*(a[i]*a[k]-cik*cik)
        assert (cjk+cik)**2 <= a[k]*(a[i]+a[j]+2*cij)

print("PASS: exact four-case rational certificate")
for label,val in [
    ("scalar baseline B",B),("case I",case1),("case II",case2),
    ("case III",case3),("case IVa",case4a),("case IVb",case4b),
    ("new Q6 cap",target),("safe floor",Qglobal-target),
    ("center safe floor",Qcenter-target)]:
    print(f"{label}: {val} ~ {float(val):.12f}")
