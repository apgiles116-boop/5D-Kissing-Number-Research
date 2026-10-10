"""Exact-rational checks for the F3 all-singleton signed-Gram gap.

The main mixed-term estimate and strict gap have analytic proofs in the
companion research note; this program is a consistency checker, not a
computer-assisted exhaustive proof of geometric feasibility.
"""
from fractions import Fraction as F
from itertools import product

EDGES = {(0, 2), (0, 4), (0, 5), (1, 4), (1, 7),
         (2, 3), (2, 7), (3, 6), (5, 6), (5, 7)}
MATCHING = {(0, 4), (1, 7), (2, 3), (5, 6)}
assert MATCHING <= EDGES
CROSS = EDGES - MATCHING
assert len(CROSS) == 6
ORIENTED = [(0, 4), (7, 1), (2, 3), (5, 6)]
SIGNS = {vertex: (i, sign)
         for i, (plus, minus) in enumerate(ORIENTED)
         for vertex, sign in ((plus, 1), (minus, -1))}
for p, q in CROSS:
    i, si = SIGNS[p]
    j, sj = SIGNS[q]
    assert i != j and si == sj
assert {frozenset((SIGNS[p][0], SIGNS[q][0])) for p, q in CROSS} == {
    frozenset((i, j)) for i in range(4) for j in range(i + 1, 4)
}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def check_signed_gram(vectors):
    a = [dot(m, m) for m in vectors]
    C = sum(a)
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    s = [dot(vectors[i], vectors[j]) for i, j in pairs]
    N = sum(max(F(0), -v) for v in s)
    total = tuple(sum(m[k] for m in vectors) for k in range(len(vectors[0])))
    e = sum(a[i] + a[j] - 2 * abs(dot(vectors[i], vectors[j]))
            for i, j in pairs)
    assert 4 * (C - N) == dot(total, total) + e
    assert e >= 0


for entries in product((-1, 0, 1), repeat=8):
    M = [tuple(F(v, 4) for v in entries[2*i:2*i+2])
         for i in range(4)]
    check_signed_gram(M)

assert F(1, 24*(4-F(33, 500))) == F(125, 11802)
assert F(125, 11802) > F(1, 96)

print("PASS: graph and cross-edge signs (six pairs)")
print("PASS: exact signed-Gram identity (6561 rational samples)")
print("PASS: conditional C > 33/500 arithmetic")
