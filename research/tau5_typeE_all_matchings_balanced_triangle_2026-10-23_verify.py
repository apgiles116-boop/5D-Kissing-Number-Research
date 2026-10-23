"""Exact combinatorial and rational checks for the balanced-quotient-triangle theorem.
Analytic Cauchy-Schwarz proof is in the companion Markdown note.
"""
from itertools import combinations, product
from fractions import Fraction as F

E = {(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
matchings = [tuple(s) for s in combinations(sorted(E),4)
             if {v for e in s for v in e} == set(range(8))]
assert len(matchings) == 3
assert set(matchings) == {
    ((0,2),(1,4),(3,6),(5,7)),
    ((0,4),(1,7),(2,3),(5,6)),
    ((0,5),(1,4),(2,7),(3,6))
}
for M in matchings:
    idx = {v:i for i,e in enumerate(M) for v in e}
    sgn = {v:(1 if v==e[0] else -1) for e in M for v in e}
    pairs = {}
    for e in E-set(M):
        ij = tuple(sorted((idx[e[0]],idx[e[1]])))
        pairs.setdefault(ij,[]).append((e,sgn[e[0]]*sgn[e[1]]))
    witness = None
    for tri in combinations(range(4),3):
        keys = list(combinations(tri,2))
        if not all(k in pairs for k in keys): continue
        for choices in product(*(pairs[k] for k in keys)):
            if choices[0][1]*choices[1][1]*choices[2][1] == 1:
                witness = (tri,choices)
                break
        if witness: break
    assert witness, M
    print('PASS matching:',M,'balanced quotient triangle:',witness)
assert F(10,7)**2>2
assert F(49,20)**2>6
assert 4608==48**2*2
margin=F(129,1024)-F(10,7)/64-F(49,20)/24
assert margin==F(169,107520)>0
print('PASS exact positive rational margin:',margin)
