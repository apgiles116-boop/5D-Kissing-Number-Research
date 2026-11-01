#!/usr/bin/env python3
"""Exact rational verifier of the F3 alternative-matching Fourier SOS certificate."""
from itertools import combinations
from sympy import Rational, symbols, expand, simplify

E = {tuple(sorted(e)) for e in [
    (0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
M = [(0,2),(1,4),(3,6),(5,7)]
M2 = [(0,5),(1,4),(2,7),(3,6)]
M0 = [(0,4),(1,7),(2,3),(5,6)]

def all_matchings(vertices):
    if not vertices:
        yield ()
        return
    a, *rest = vertices
    for b in rest:
        for tail in all_matchings([v for v in rest if v != b]):
            yield ((a,b),) + tail

found = {frozenset(frozenset(e) for e in mat)
         for mat in all_matchings(list(range(8)))
         if all(tuple(sorted(e)) in E for e in mat)}
expected = {frozenset(frozenset(e) for e in mat) for mat in (M,M2,M0)}
assert found == expected, (found,expected)

# Klein-four automorphisms preserving M, as 8-vertex permutations.
perms = [tuple(range(8)),
         (2,6,0,4,3,7,1,5),
         (5,3,7,1,6,0,4,2),
         (7,4,5,6,1,2,3,0)]
for p in perms:
    assert {tuple(sorted((p[a],p[b]))) for a,b in E} == E
    assert {tuple(sorted((p[a],p[b]))) for a,b in M} == {tuple(sorted(e)) for e in M}

orbits = {
 0: [(1,6),(3,4)],
 1: [(0,6),(1,2),(3,7),(4,5)],
 2: [(1,3),(4,6)],
 3: [(0,2),(5,7)],
 4: [(0,5),(2,7)],
 5: [(0,7),(2,5)],
 6: [(0,4),(1,7),(2,3),(5,6)],
 7: [(1,4),(3,6)],
 8: [(0,1),(2,6),(3,5),(4,7)],
 9: [(0,3),(1,5),(2,4),(6,7)]}
assert {tuple(sorted(e)) for orbit in orbits.values() for e in orbit} == set(combinations(range(8),2))
for k,orbit in orbits.items():
    assert {tuple(sorted((p[a],p[b]))) for p in perms for a,b in orbit} == {tuple(sorted(e)) for e in orbit}
assert all(tuple(sorted(e)) not in E for e in orbits[0])
assert all(tuple(sorted(e)) in E for k in (3,4,6,7) for e in orbits[k])

x = symbols('x0:10')
def forms(r,s):
    A = 1 + r*x[3] + s*x[4] + r*s*x[5]
    B = 1 + r*x[0] + s*x[2] + r*s*x[7]
    R = x[8] + r*x[1] + s*x[9] + r*s*x[6]
    return A,B,R

def q(r,s,lam,sign):
    A,B,R=forms(r,s)
    return A+lam**2*B+2*sign*lam*R

Aplus,Bplus,_ = forms(1,1)
certificate = (
    Rational(1,496)*q(-1,-1,16,1)
    +Rational(2,31)*q(-1,1,Rational(1,2),-1)
    +Rational(121,248)*q(1,-1,Rational(1,16),-1)
    +Rational(7,496)*q(1,-1,Rational(1,8),-1)
    +Rational(1,31)*q(1,1,1,1)
    +Rational(33,62)*Aplus
    +Rational(29831,63488)*Bplus
    +Rational(889,31744)*(x[0]+Rational(1,2))
    +Rational(1,8)*(-Rational(1,2)-x[4])
    +Rational(8,31)*(-Rational(1,2)-x[6])
)
C = 2+x[3]+x[7]
assert simplify(expand(certificate-(C-Rational(505,63488)))) == 0
assert Rational(505,63488)-Rational(1,128) == Rational(9,63488)

# Automorphism exchanging the two alternative perfect matchings.
swap = (0,1,5,6,4,2,3,7)
assert {tuple(sorted((swap[a],swap[b]))) for a,b in E} == E
assert {tuple(sorted((swap[a],swap[b]))) for a,b in M} == {tuple(sorted(e)) for e in M2}

print('PASS: all 3 F3 perfect matchings and both alternative orbits')
print('PASS: Klein-four averaging and 10 pair-orbit definitions')
print('PASS: exact rational Fourier SOS identity C - 505/63488 > 1/128')
print('PASS: strict positivity from four deep-edge orbit x4 and x6')
print('PROOF STATUS: exact 8-endpoint lemma; Type E application conditional on retained graph')
