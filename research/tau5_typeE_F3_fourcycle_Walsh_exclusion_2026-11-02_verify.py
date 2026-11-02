"""Exact symbolic audit of F3 four-cycle Walsh exclusion (2026-11-02).
Independent 28-variable Gram identity; no SDP, numerical tolerance, or rank assumption.
"""
from itertools import combinations
from sympy import Rational, symbols, simplify

DEEP = {frozenset(e) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),
                                (2,3),(2,7),(3,6),(5,6),(5,7)]}
MATCHINGS = [
    [(0,4),(1,7),(2,3),(5,6)],
    [(0,2),(1,4),(3,6),(5,7)],
    [(0,5),(1,4),(2,7),(3,6)],
]
SWITCH = [(1,-1,1,1),(1,-1,-1,1),(1,-1,1,1)]
QUOTIENT_MATCHINGS = [[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
K4 = list(combinations(range(4),2))
G = {frozenset((i,j)): symbols(f'g{i}{j}') for i,j in combinations(range(8),2)}
def dot(i,j):
    return Rational(1) if i == j else G[frozenset((i,j))]

for case,(matching,signs) in enumerate(zip(MATCHINGS,SWITCH)):
    A = [pair[0] if sign == 1 else pair[1] for pair,sign in zip(matching,signs)]
    B = [pair[1] if sign == 1 else pair[0] for pair,sign in zip(matching,signs)]
    assert len(set(A+B))==8
    k = {}
    for i,j in K4:
        same = [(A[i],A[j]),(B[i],B[j])]
        opposite = [(A[i],B[j]),(B[i],A[j])]
        assert all(frozenset(e) not in DEEP for e in opposite)
        k[(i,j)] = sum(frozenset(e) in DEEP for e in same)
    assert sorted(k.values()) == ([[1]*6,[0,1,1,1,1,2],[0,1,1,1,1,2]][case])
    for F in QUOTIENT_MATCHINGS:
        E = [p for p in K4 if p not in F]
        assert len(E)==4 and sum(k[p] for p in F)==2
        f_contacts = [(A[i],A[j]) for i,j in F] + [(B[i],B[j]) for i,j in F]
        assert sum(frozenset(e) in DEEP for e in f_contacts)==2
        lamF = sum((Rational(-1,2) if frozenset((u,v)) in DEEP else Rational(1,2))-dot(u,v)
                   for u,v in f_contacts)
        e_contacts = [(A[i],B[j]) for i,j in E] + [(B[i],A[j]) for i,j in E]
        assert all(frozenset(e) not in DEEP for e in e_contacts)
        lamE = sum(Rational(1,2)-dot(u,v) for u,v in e_contacts)
        N = 8+2*sum(dot(A[i],A[j])+dot(B[i],B[j]) for i,j in K4)
        sum_w = sum((dot(A[i],A[j])+dot(B[i],B[j])
                     -dot(A[i],B[j])-dot(B[i],A[j]))/4 for i,j in E)
        assert simplify(sum_w+2-N/8-(lamF+lamE)/4)==0
        print(f'PASS P{case}, omitted {F}, exact Gram identity')
print('PASS: all 9 four-cycle patterns, strict slack exclusion')
print('Type E OPEN; 40<=tau_5<=44')
