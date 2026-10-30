#!/usr/bin/env python3
"""Exact integer/rational certificate for the robust Type-E support-fibre theorem."""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt

EPS=F(1,650)
ETA=3*EPS
TARGET=F(13,5)
PAIRS=tuple(combinations(range(5),2))

def ceilroot(n):
    s=isqrt(n)
    return s+(s*s<n)

def lower(V,D):
    lo=[min(row[k] for row in V) for k in range(5)]
    hi=[max(row[k] for row in V) for k in range(5)]
    if 3*(lo[0]+lo[1])>(2+3*ETA)*D:
        return None
    out=F(0)
    for i,j in PAIRS:
        numer=3*(lo[i]+lo[j]+2*isqrt(lo[i]*lo[j]))-(2+3*ETA)*D
        if numer<=0:
            continue
        denom=3*(hi[i]-lo[j]+ceilroot(hi[i]*hi[j]))
        assert denom>0
        out+=F(numer,denom)
    return out

def bisect(V,D):
    _,i,j=max(
        (sum((V[i][k]-V[j][k])**2 for k in range(5)),i,j)
        for i,j in PAIRS
    )
    twice=[tuple(2*x for x in row) for row in V]
    middle=tuple(V[i][k]+V[j][k] for k in range(5))
    left=twice.copy()
    right=twice.copy()
    left[i]=middle
    right[j]=middle
    return (tuple(left),2*D),(tuple(right),2*D)

def verify():
    supports=list(PAIRS)
    star={e for e in supports if 0 in e}
    meeting=[(e,f) for e,f in combinations(supports,2) if set(e)&set(f)]
    safe=[(e,f) for e,f in meeting if not (e in star and f in star)]
    assert len(star)==4 and len(meeting)==30 and len(safe)==24
    assert all(sum(e in pair for pair in safe)==(3 if e in star else 6)
               for e in supports)

    tmax=F(16,9)*(1+4*EPS)**2-1
    assert tmax==F(84471,105625) and tmax<F(4,5)
    x=F(2,7)
    assert 2*(x+x**3/3)==F(604,1029)>F(44,75)
    assert F(1,4)/(2*(1-F(1,4)))==F(1,6)
    assert F(6,5)**2>F(4,3)
    assert 2*(F(6,5)*EPS+EPS**2)<=3*EPS

    upper=F(35,11)*F(383,504)+F(960,11)*EPS
    assert upper==F(131387,51480)
    assert TARGET-upper==F(2461,51480)>0
    assert F(11,35)*TARGET==F(143,175)
    assert F(143,175)-F(383,504)==F(103,1800)

    D=60
    V=tuple(tuple(D//k if i<k else 0 for i in range(5))
            for k in range(1,6))
    assert all(sum(row)==D for row in V)
    assert all(all(row[i]>=row[i+1] for i in range(4)) for row in V)
    todo=[(V,D)]
    splits=bound_pruned=domain_pruned=bits=0
    while todo:
        V,D=todo.pop()
        splits+=1
        bits=max(bits,D.bit_length())
        for child,dc in bisect(V,D):
            lb=lower(child,dc)
            if lb is None:
                domain_pruned+=1
            elif lb>=TARGET:
                bound_pruned+=1
            else:
                todo.append((child,dc))
        if splits>250000:
            raise RuntimeError("certificate did not close")
    assert bound_pruned+domain_pruned==splits+1
    assert (splits,bound_pruned,domain_pruned,bits)==(92685,77956,14730,33)
    print("EXACT CERTIFICATE PASSED")
    print("F_(3/650)(p) >= 13/5 on the feasible sorted simplex")
    print("Splits:",splits,"bound prunings:",bound_pruned,
          "domain prunings:",domain_pruned,"max denominator bits:",bits)
    print("Forbidden max-projector-distance radius: 1/650")
    print("Exact-fibre A >= 143/175, gap over cap 103/1800")
    print("Robust contradiction margin:",TARGET-upper)

if __name__=="__main__":
    verify()
