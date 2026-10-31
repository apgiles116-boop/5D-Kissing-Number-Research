#!/usr/bin/env python3
"""Exact D5 16-line Q-subframe rank and spectral audit.

Exhausts all 4845 four-root deletions via signed-coordinate-permutation
orbits. SymPy rational characteristic polynomials and exact Sturm root
counts; no floating-point decisions.
"""
from itertools import combinations
from collections import Counter
import sympy as S

labels = [(i, j, sg) for i, j in combinations(range(5), 2) for sg in (1, -1)]
lookup = {v: i for i, v in enumerate(labels)}

def act(lab, perm, signs):
    i, j, sg = lab
    a, b = perm[i], perm[j]
    sa, sb = signs[i], sg * signs[j]
    if a > b:
        a, b, sa, sb = b, a, sb, sa
    return lookup[(a, b, sa * sb)]

generators = []
for k in range(4):
    perm = list(range(5))
    perm[k], perm[k+1] = perm[k+1], perm[k]
    generators.append(tuple(act(v, perm, [1]*5) for v in labels))
generators.append(tuple(act(v, list(range(5)), [-1,1,1,1,1]) for v in labels))

remaining = set(combinations(range(20), 4))
orbits = []
while remaining:
    seed = min(remaining)
    orbit = {seed}
    queue = [seed]
    while queue:
        current = queue.pop()
        for perm in generators:
            nxt = tuple(sorted(perm[i] for i in current))
            if nxt not in orbit:
                orbit.add(nxt)
                queue.append(nxt)
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbits.append((seed, len(orbit)))
assert len(orbits) == 17
assert sum(size for _, size in orbits) == 4845

Q = []
for i, j, sg in labels:
    v = S.zeros(5, 1)
    v[i], v[j] = 1, sg
    Q.append(v*v.T/S.Integer(2) - S.eye(5)/5)
K20 = S.Matrix(20, 20, lambda i, j: S.trace(Q[i]*Q[j]))
x = S.symbols('x')
rank_counts = Counter()
min_orbits = []
max_orbits = []
min_poly = 20*x*x - 26*x + 1
star_poly = 20*x*x - 31*x + 6
star_count = 0
extremal_count = 0

for omitted, size in orbits:
    kept = [i for i in range(20) if i not in omitted]
    cp = S.Poly(K20.extract(kept, kept).charpoly(x).as_expr(), x)
    zero_mult = 0
    while cp.eval(0) == 0:
        cp = cp.exquo(S.Poly(x, x))
        zero_mult += 1
    rank = 16 - zero_mult
    rank_counts[rank] += size
    missing_supports = Counter((labels[i][0], labels[i][1]) for i in omitted)
    k = sum(count == 2 for count in missing_supports.values())
    assert rank == 14-k, (omitted, rank, k)
    if rank == 14:
        count_small = cp.count_roots(S.Integer(0), S.Rational(1,20))
        count_below_fifth = cp.count_roots(S.Integer(0), S.Rational(1,5))
        is_min = cp.rem(S.Poly(min_poly, x)).is_zero
        is_star = (cp.rem(S.Poly(star_poly, x)).is_zero
                   and count_below_fifth == 0)
        if is_min:
            assert count_small == 1 and size == 80
            extremal_count += size
            min_orbits.append(omitted)
        else:
            assert count_small == 0, (omitted, cp)
        if is_star:
            assert count_small == 0 and size == 80
            star_count += size
            max_orbits.append(omitted)
        else:
            assert count_below_fifth >= 1, (omitted, cp)
    elif rank == 13:
        assert k == 1
    else:
        assert rank == 12 and k == 2
    print('orbit', size, 'omitted', omitted, 'rank', rank)

assert rank_counts == Counter({14:3360, 13:1440, 12:45})
assert extremal_count == 160 and star_count == 80
assert len(min_orbits) == 2 and len(max_orbits) == 1

alpha = (13-S.sqrt(149))/20
beta = (31-S.sqrt(481))/40
assert S.simplify(min_poly.subs(x, alpha)) == 0
assert S.simplify(star_poly.subs(x, beta)) == 0
assert 0 < alpha < S.Rational(1,20) < S.Rational(1,5) < beta
print('EXACT RANK COUNTS:', dict(sorted(rank_counts.items())))
print('SHARP FULL-RANK MINIMUM:', alpha, '=', S.N(alpha, 15))
print('SHARP FULL-RANK MAXIMUM:', beta, '=', S.N(beta, 15))
print('MINIMIZING DELETIONS:', min_orbits, 'total', extremal_count)
print('MAXIMIZING DELETIONS:', max_orbits, 'total', star_count)
print('ALL EXACT TESTS PASSED')
