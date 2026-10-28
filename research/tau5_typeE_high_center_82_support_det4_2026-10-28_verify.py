"""Exact arithmetic checks for conditional Type-E high-center 82-support
and determinant-four rank-seven pruning.

Does not reprove the upstream F3/harmonic high-center certificates.
"""
from fractions import Fraction as F
from itertools import combinations

Nmax = F(5, 64)
xmax = F(1, 2500)
c = F(539, 81)

L = F(102, 5) - F(12, 5)*xmax - F(2, 5)*xmax*xmax
low = Nmax/(2*c)
assert L == F(318734999, 15625000)
assert low == F(405, 68992)
assert L - F(81, 4) - low == F(19292115751, 134750000000) > 0

# All 7-by-7 principal determinants of 2*Ghat have abs value <5.
# The argument bounding each determinant uses the PSD rank-5 nearby Gram
# and the Frobenius bound <1/9, as detailed in the proof note.
ratios = {}
for q in range(1, 6):
    k = 7
    R = (2**(2*k)
         * ((F(k)+F(k-q, 9))/q)**(2*q)
         * F(1, 81*(k-q))**(k-q))
    ratios[q] = R
    assert R < 25, (q, R)
assert max(ratios, key=ratios.get) == 5
assert ratios[5] == F(564668382613504, 22876792454961)

# D5 20-line template sanity: 20 lines, degree 12, 120 edges.
roots = []
for i in range(5):
    for j in range(i+1, 5):
        for sign in (-1, 1):
            v = [0]*5
            v[i] = 1
            v[j] = sign
            roots.append(v)
assert len(roots) == 20
edges = []
for i, j in combinations(range(20), 2):
    dot = sum(a*b for a, b in zip(roots[i], roots[j]))
    assert abs(dot) in (0, 1)
    if dot:
        edges.append((i, j))
assert len(edges) == 120
assert all(sum(i in edge for edge in edges) == 12 for i in range(20))
min_17 = min(sum(i in chosen and j in chosen for i, j in edges)
             for chosen in map(set, combinations(range(20), 17)))
assert min_17 == 84

print("PASS: exact 17-vector Welch gap, h>=82")
print("PASS: all five 7x7 determinant ratios <25; worst:", ratios[5])
print("PASS: D5 17-subset sanity check; minimum:", min_17)
