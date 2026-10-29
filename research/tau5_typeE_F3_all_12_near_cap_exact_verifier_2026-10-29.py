"""Exact rational verification of 12 strict F3 near-cap configurations in R^5.
Only Python's standard library is required. No floating-point arithmetic enters
any assertion. Run from any directory with this file and its JSON companion.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

DATA=Path(__file__).with_name("tau5_typeE_F3_all_12_near_cap_witnesses_2026-10-29.json")
W=json.loads(DATA.read_text())
E={tuple(sorted(p)) for p in [(0,2),(0,4),(0,5),(1,4),(1,7),
                                (2,3),(2,7),(3,6),(5,6),(5,7)]}
P={"P1":[(0,2),(1,4),(3,6),(5,7)],
   "P2":[(0,4),(1,7),(2,3),(5,6)],
   "P3":[(0,5),(1,4),(2,7),(3,6)]}
assert len(W)==12
for name,pairs in P.items():
    for small in range(4):
        key=f"{name}_{small}"
        D=W[key]["denom"]
        rows=W[key]["params"]
        assert len(rows)==8
        V=[]
        for row in rows:
            assert len(row)==4
            t=[F(n,D) for n in row]
            t2=sum(q*q for q in t)
            V.append([2*q/(1+t2) for q in t]+[(1-t2)/(1+t2)])
        assert all(sum(q*q for q in u)==1 for u in V)
        def dot(i,j):
            return sum(x*y for x,y in zip(V[i],V[j]))
        slacks=[]
        for i,j in combinations(range(8),2):
            d=dot(i,j)
            if (i,j) in E:
                slacks.append(-F(1,2)-d)
            else:
                slacks.extend([F(1,2)-d,d+F(1,2)])
        assert min(slacks)>0,(key,"endpoint constraint")
        a=[(1+dot(i,j))/2 for i,j in pairs]
        assert all(F(1249,5000)<a[i]<F(1,4) for i in range(4) if i!=small)
        assert F(99,10000)<a[small]<F(1,100)
        A=sum(a)
        U=sum(q*q for q in a)
        assert F(759,1000)<A<F(383,504)
        assert U>F(4686,25000)
        print(key,"PASS")
Ustar=F(3,16)+F(5,504)**2
assert F(4686,25000)/Ustar>F(999,1000)
print("PASS: 12 strict exact-deep-graph F3 witnesses; U > 99.9% of Ustar")
