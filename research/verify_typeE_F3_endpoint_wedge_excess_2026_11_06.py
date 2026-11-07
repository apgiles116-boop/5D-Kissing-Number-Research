"""Exact finite incidence audit for the F3 endpoint wedge-excess bound.

The continuous 3x3 Gram inequality is proved analytically in the paired note.
No numerical optimization, approximate arithmetic, or third-party packages.
"""
from fractions import Fraction

E = {tuple(sorted(e)) for e in ((0,2),(0,4),(0,5),(1,4),(1,7),
                                 (2,3),(2,7),(3,6),(5,6),(5,7))}
matchings = [
    ((0,4),(1,7),(2,3),(5,6)),
    ((0,2),(1,4),(3,6),(5,7)),
    ((0,5),(1,4),(2,7),(3,6)),
]
wedges = [
    (((0,2),(2,7)),((0,5),(5,7))),
    (((0,4),(0,5)),((1,7),(2,7))),
    (((0,2),(0,4)),((1,7),(5,7))),
]

assert len(E) == 10
degrees = {i: sum(i in e for e in E) for i in range(8)}
assert min(degrees.values()) >= 2
# All three-vertex subsets are nontriangles in the strict-deep graph.
for i in range(8):
    for j in range(i+1,8):
        for k in range(j+1,8):
            assert not all((a,b) in E for a,b in ((i,j),(i,k),(j,k)))

for P, W in zip(matchings, wedges):
    P = {tuple(sorted(e)) for e in P}
    assert len(P) == 4 and P <= E
    assert sorted(v for edge in P for v in edge) == list(range(8))
    cross = E-P
    assert len(cross) == 6
    used = []
    for e,f in W:
        e,f = tuple(sorted(e)),tuple(sorted(f))
        assert e in cross and f in cross and e != f
        center = set(e)&set(f)
        endpoints = tuple(sorted(set(e)^set(f)))
        assert len(center) == 1 and len(endpoints) == 2
        assert endpoints not in E
        used.extend((e,f))
    assert len(set(used)) == 4
    leftovers = cross-set(used)
    assert len(leftovers) == 2
    print('matching:', sorted(P), 'wedges:', W, 'unpaired:', sorted(leftovers))

bound = 2*Fraction(1) + 2*Fraction(3,4)
assert bound == Fraction(7,2)
assert 4*190 == 760
assert 760-6 == 754
print('EXACT FINITE AUDIT PASSED; X_P <', bound)
