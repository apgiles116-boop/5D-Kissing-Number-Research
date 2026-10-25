#!/usr/bin/env python3
"""Exact SymPy verifier: D5 midpoint mixing and all 4845 four-core deletions."""
from itertools import combinations
import sympy as S

roots=[]; labels=[]
for p,q in combinations(range(5),2):
    for sign in (1,-1):
        r=[0]*5; r[p]=1; r[q]=sign
        roots.append(S.Matrix(r)); labels.append((p,q,sign))
assert len(roots)==20

rows=[]
for i,r in enumerate(roots):
    row=[0]*100
    for k in range(5): row[5*i+k]=r[k]
    rows.append(row)
contacts=[]
for i,j in combinations(range(20),2):
    d=int(roots[i].dot(roots[j]))
    if abs(d)==1:
        row=[0]*100
        for k in range(5):
            row[5*i+k]=roots[j][k]
            row[5*j+k]=(1 if d>0 else -1)*roots[i][k]
        rows.append(row); contacts.append((i,j,d))
assert len(contacts)==120
B=S.Matrix(rows)
assert B.rank()==100
P=S.zeros(100)
for i,r in enumerate(roots):
    P[5*i:5*i+5,5*i:5*i+5]=S.eye(5)-r*r.T/2
assert P*P==P and P.rank()==80
T=P*(B[20:,:].T*B[20:,:]/2)*P
X=S.Symbol('X')
poly=(X**20*(X-1)**20*(X-2)**10*(X-4)**10
      *(X**2-S.Rational(13,2)*X+6)**5
      *(X**2-S.Rational(9,2)*X+4)**15)
assert S.expand(T.charpoly(X).as_expr()-poly)==0
assert (13-S.sqrt(73))/4>1 and (9-S.sqrt(17))/4>1
print("PASS: exact sharp spectral gap 1, equality multiplicity 20")

Ginv=(B.T*B).inv()
lev=B[20:,:]*Ginv*B[20:,:].T
index={(i,j):k for k,(i,j,_) in enumerate(contacts)}
def special(core):
    supports=[labels[i][:2] for i in core]
    ss=set(supports)
    return len(ss)==2 and all(supports.count(s)==2 for s in ss) and len(set.intersection(*(set(s) for s in ss)))==1

bad=[]
for core in combinations(range(20),4):
    ids=[index[(i,j)] for i,j in combinations(core,2) if (i,j) in index]
    k=len(ids)
    D=S.eye(k)-lev.extract(ids,ids)
    singular=(D.det(method='domain-ge')==0) if k else False
    assert singular==special(core)
    if singular:
        assert k==4 and D.rank()==3
        bad.append(core)
assert len(bad)==30
print("PASS: all 4845 cores checked exactly; 30 corank-one exceptions")

mode=S.zeros(100,1)
for i,k,val in [(0,2,1),(1,2,-1),(2,1,1),(3,1,-1),(8,0,-1),(9,0,1)]:
    mode[5*i+k]=val
assert B[:20,:]*mode==S.zeros(20,1)
active=[contacts[k][:2] for k in range(120) if (B[20+k,:]*mode)[0]!=0]
assert set(active)=={(0,2),(0,3),(1,2),(1,3)}
print("PASS: explicit A2 six-line mode")
print("ALL EXACT CHECKS PASSED")
