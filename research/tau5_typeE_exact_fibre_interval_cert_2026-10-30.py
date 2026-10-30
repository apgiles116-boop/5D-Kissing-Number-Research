#!/usr/bin/env python3
"""Exact integer-arithmetic branch certificate for a conditional Type-E D5 fibre theorem.
No floats, numerical optimizers, external packages, or rounding assumptions are used
in certification. The domain is the sorted five-coordinate probability simplex.
"""
from fractions import Fraction
from math import isqrt
from itertools import combinations

PAIRS = list(combinations(range(5), 2))
TARGET = Fraction(5, 2)


def sqrt_ceil(n):
    s = isqrt(n)
    return s if s*s == n else s+1


def lower_bound(V, D):
    """Exact lower bound for F(p) on simplex with vertices V/D.

    F(p) = sum_{i<j} max(0, (sqrt(p_i)+sqrt(p_j))**2 - 2/3)
                             / (p_i-p_j+sqrt(p_i*p_j)), p sorted.
    """
    lo = [min(row[k] for row in V) for k in range(5)]
    hi = [max(row[k] for row in V) for k in range(5)]
    if 3*(lo[0]+lo[1]) > 2*D:
        return None
    total = Fraction(0)
    for i, j in PAIRS:
        sqrtlo = isqrt(lo[i]*lo[j])
        numer = 3*(lo[i]+lo[j]+2*sqrtlo) - 2*D
        if numer <= 0:
            continue
        sqrtup = sqrt_ceil(hi[i]*hi[j])
        denom = 3*(hi[i]-lo[j]+sqrtup)
        assert denom > 0
        total += Fraction(numer, denom)
    return total


def split(V, D):
    """Bisect the longest edge; preserve an exact cover of the parent simplex."""
    best = (-1, None, None)
    for i, j in PAIRS:
        sq = sum((V[i][k]-V[j][k])**2 for k in range(5))
        if sq > best[0]:
            best = (sq, i, j)
    _, i, j = best
    doubled = [tuple(2*x for x in row) for row in V]
    midpoint = tuple(V[i][k]+V[j][k] for k in range(5))
    left = list(doubled)
    right = list(doubled)
    left[i] = midpoint
    right[j] = midpoint
    return (tuple(left), 2*D), (tuple(right), 2*D)


def run():
    D = 60
    V = tuple(tuple(D//k if i<k else 0 for i in range(5)) for k in range(1,6))
    assert all(sum(row)==D for row in V)
    assert all(all(row[i]>=row[i+1] for i in range(4)) for row in V)
    pending = [(V, D)]
    count = 0
    pruned_bound = 0
    pruned_domain = 0
    max_depth = 0
    while pending:
        V, D = pending.pop()
        count += 1
        max_depth = max(max_depth, D.bit_length())
        for child, Dc in split(V, D):
            bound = lower_bound(child, Dc)
            if bound is None:
                pruned_domain += 1
            elif bound >= TARGET:
                pruned_bound += 1
            else:
                pending.append((child, Dc))
        if count > 500000:
            raise RuntimeError('Certificate did not close within 500000 subdivisions')
    assert Fraction(47,162) < Fraction(7,24)
    assert 2*(Fraction(7,25)+Fraction(7,25)**3/3) > Fraction(77,135)
    assert Fraction(11,14)-Fraction(383,504) == Fraction(13,504)
    print('EXACT CERTIFICATE PASSED: F(p) >= 5/2')
    print('Subdivided simplices:', count)
    print('Bound-pruned children:', pruned_bound)
    print('Domain-pruned children:', pruned_domain)
    print('Maximum denominator bit length:', max_depth)
    print('Energy implication: A >= 11/14')
    print('Gap above retained cap:', Fraction(11,14)-Fraction(383,504))

if __name__ == '__main__':
    run()
