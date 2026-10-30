"""Exact rational regression for the center-to-Q variance theorem, 2026-10-30.

The proof is in the companion markdown note. All certification comparisons
here use Fraction; no floating-point threshold is trusted.
"""
from fractions import Fraction as F
from itertools import product

q0 = F(-983, 5000)
q1 = F(-39, 200)
f = lambda q: F(10) + F(35, 64) * (5*q+4)**2
N0min = 7 * F(17, 5000) * (1-4*F(1, 200))
assert N0min == F(5831, 250000)
assert f(q1)-15 == F(87, 20480)
assert f(q0)+N0min-15 == F(72851, 64000000)
assert 5*q0+4 > 0

# Test the trace-free 5D directional Cauchy bound on 625 exact diagonals.
for entries in product(range(-2,3), repeat=4):
    b = [F(k,7) for k in entries]
    b.append(-sum(b))
    assert sum(x*x for x in b) >= F(5,4)*b[0]*b[0]

Vedge = F(5,4)*(F(2,5)-q0/2)**2
Aold, Anew = F(383,504), F(567,1000)
Vzold = F(5,4)*(F(2,5)-q0/2-Aold/5)**2
Vznew = F(5,4)*(F(2,5)-q0/2-Anew/5)**2
assert Vedge == F(24830289,80000000)
assert Vzold == F(47602076041,317520000000)
assert Vznew == F(14814801,80000000)
assert Vznew > Vzold > 0
assert Vedge/2 == F(24830289,160000000)

# Rational projected correlation floor using retained A and U caps.
Ucap = F(129,1000)
corr = 30-3*Anew+Anew*Anew/10-Ucap/2+Vznew/2
assert corr == F(36299829,1280000)

# Algebraic frame-decomposition check (not a feasible Type-E code).
a = F(9,25)
M, Z = [F(0)]*5, [F(0)]*5
for _ in range(20):
    M[0] += a
    Z[1] += 1-a
S = [M[j]+Z[j] for j in range(5)]
assert sum(S) == 20
q = 2*S[0]-F(36,5)
assert S[0]-4 == q/2-F(2,5)
assert Z[0]-(20-20*a)/5 == q/2-F(2,5)+(20*a)/5-M[0]

print("PASS: exact q cap, full-edge and projected-Q variance floors")
print("q <",q0)
print("Vedge >",Vedge)
print("Vz historical >",Vzold)
print("Vz stronger >",Vznew)
print("correlation >",corr)
