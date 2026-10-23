#!/usr/bin/env python3
"""Exact F3 quotient graph, cancellation, and rational constant checks."""
from itertools import combinations, product
from collections import defaultdict
from fractions import Fraction as F
E={(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
Pall=[P for P in combinations(sorted(E),4) if len({v for e in P for v in e})==8]
assert len(Pall)==3
nparallel=0
for P in Pall:
    idx={v:i for i,(u,w) in enumerate(P) for v in (u,w)}
    sign={v:(1 if v==u else -1) for u,w in P for v in (u,w)}
    cross=defaultdict(list)
    for u,v in sorted(E-set(P)):
        key=tuple(sorted((idx[u],idx[v])))
        cross[key].append(((u,v),sign[u]*sign[v],sign[u],sign[v]))
    assert sum(map(len,cross.values()))==6
    parallel=[key for key,val in cross.items() if len(val)==2]
    if not parallel:
        assert len(cross)==6
        for tri in combinations(range(4),3):
            beta=1
            for key in combinations(tri,2): beta*=cross[key][0][1]
            assert beta==1
        continue
    nparallel+=1
    assert len(parallel)==1
    pq=parallel[0]
    assert {v[2:4] for v in cross[pq]}=={(1,1),(-1,-1)}
    other=[v for v in range(4) if v not in pq]
    four=set()
    for h,pe in zip(other,cross[pq]):
        tri=tuple(sorted((*pq,h)))
        keys=list(combinations(tri,2))
        assert all(key in cross for key in keys)
        beta=1
        for key in keys:
            beta*=pe[1] if key==pq else cross[key][0][1]
        assert beta==1
        four.update(set(keys)-{pq})
    assert len(four)==4
assert nparallel==2
B=F(383,504)
t=F(1242)-1024-132*B
assert t>0
assert t*t-256*(64*B+8*B*B)==F(3458281,15876)>0
assert 4*F(1,1242)==F(2,621)
print("PASS: three matchings, two opposite-sign parallel pairs, balanced triangles")
print("PASS: D(383/504)<1242 and 4epsilon>2C^2/621")
