#!/usr/bin/env python3
"""Exact F3 balanced-triangle enumeration and rational coefficient audit."""
from itertools import combinations
from fractions import Fraction as F
edges={(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
matchings=[p for p in combinations(sorted(edges),4) if len({v for e in p for v in e})==8]
assert len(matchings)==3
for P in matchings:
    idx={v:i for i,e in enumerate(P) for v in e}
    sign={v:(1 if v==e[0] else -1) for e in P for v in e}
    triangles=[]
    for I in combinations(range(4),3):
        cross=[(idx[u],idx[v],sign[u]*sign[v],(u,v)) for u,v in sorted(edges-set(P)) if idx[u] in I and idx[v] in I]
        for chosen in combinations(cross,3):
            if {frozenset((i,j)) for i,j,_,_ in chosen}!={frozenset(x) for x in combinations(I,2)}: continue
            if chosen[0][2]*chosen[1][2]*chosen[2][2]==1:
                triangles.append((I,tuple(e[-1] for e in chosen)))
    assert len(triangles)>=2
    assert len({t[0] for t in triangles})>=2
    print('Matching:',P,'balanced triangles:',triangles)
assert F(1,4)+F(1,16)==F(5,16)
assert 12+F(5,16)==F(197,16)
assert 64*48==3072 and 64*F(5,4)==80
assert 3072+80==3152 and F(3152,4)==788
assert F(4608,3152)==F(288,197)
for C in (F(0),F(1,8),F(3,4)):
    for dots in ((F(0),)*6,(F(1,8),F(-1,9),F(0),F(1,7),F(-1,11),F(-1,13))):
        lhs=4*(C-sum(max(-g,0) for g in dots))
        rhs=(C+2*sum(dots))+(3*C-2*sum(abs(g) for g in dots))
        assert lhs==rhs
print('PASS: F3 enumeration and exact rational identities')
