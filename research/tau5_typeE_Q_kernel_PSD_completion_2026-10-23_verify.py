#!/usr/bin/env python3
"""Exact rational checker for D5 Q-kernel PSD completion; requires sympy."""
import itertools
from collections import Counter
import sympy as S
Q=S.Rational
roots=[]; labels=[]
for a,b in itertools.combinations(range(5),2):
    for sign in (1,-1):
        v=S.zeros(5,1);v[a]=1;v[b]=sign
        roots.append(v);labels.append((a,b,sign))
G=S.Matrix(20,20,lambda i,j:roots[i].dot(roots[j])**2/4-Q(1,5))
assert G.eigenvals()=={Q(3,2):4,S.Integer(1):10,S.Integer(0):6}
P=S.eye(20)-Q(5,3)*G+Q(2,3)*G**2
assert P**2==P and P*G==S.zeros(20) and P.trace()==6
for i,j in itertools.product(range(20),repeat=2):
    n=len(set(labels[i][:2]) & set(labels[j][:2]))
    assert P[i,j]=={2:Q(3,10),1:-Q(1,30),0:Q(2,15)}[n]
dets=Counter(); norms=Counter(); worst=0
for supports in itertools.combinations(range(10),4):
    core=[2*t for t in supports]
    H=P.extract(core,core); d=H.det()
    assert d>0
    dets[d]+=1
    V=H.inv()
    diag=[V[t,t] for t in range(4)]
    norms[max(diag)]+=1
    for r,s in itertools.combinations(range(4),2):
        worst=max(worst,diag[r]*diag[s])
    dual=[sum((V[s,r]*P[:,core[s]] for s in range(4)),S.zeros(20,1))
          for r in range(4)]
    for r in range(4):
        assert G*dual[r]==S.zeros(20,1)
        assert [dual[r][core[s]] for s in range(4)]==[int(r==s) for s in range(4)]
        for s in range(4):
            assert dual[r].dot(dual[s])==V[r,s]
assert dets==Counter({Q(1,135):5,Q(1,162):60,Q(7,1620):60,
                      Q(19,6480):60,Q(11,2160):15,Q(1,540):10})
assert norms==Counter({Q(7,2):5,Q(21,5):60,S.Integer(6):60,
                       Q(138,19):60,Q(46,11):15,S.Integer(14):10})
assert worst==112
assert 210*16+10*36*4+45==4845
for n in (2,3,4):
    for supports in itertools.combinations(range(10),n):
        inds=[2*t for t in supports]
        assert P.extract(inds,inds).det()>0
# The signless K5 cycle space has dimension five and is spanned by 4-cycles.
edges=list(itertools.combinations(range(5),2))
eid={e:i for i,e in enumerate(edges)}
B=S.Matrix(5,10,lambda v,e:int(v in edges[e]))
cycles=[]
for a,b,c,d in itertools.combinations(range(5),4):
    for u,v,w,x in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
        cvec=S.zeros(10,1)
        for e in [(u,v),(w,x)]:cvec[eid[tuple(sorted(e))]]+=1
        for e in [(u,w),(v,x)]:cvec[eid[tuple(sorted(e))]]-=1
        assert B*cvec==S.zeros(5,1)
        cycles.append(cvec)
assert B.rank()==5 and S.Matrix.hstack(*cycles).rank()==5
A=Q(383,504)
cap=Q(3,16)+(A-Q(3,4))**2
floor=30-3*A+A**2/10-cap/2
assert floor==Q(8790283,317520)>Q(17456771,635040)
assert -3+A/5<0
# Rational 20-distinct-line tight frame with the same scalar mass as D5.
vs=[S.Matrix(t) for t in [(1,2,3,4,5),(2,3,5,7,11),(1,3,4,7,10)]]
bases=[S.eye(5)]+[S.eye(5)-2*v*v.T/v.dot(v) for v in vs]
W=[b[:,i] for b in bases for i in range(5)]
assert all(w.dot(w)==1 for w in W)
assert all(abs(W[i].dot(W[j]))!=1 for i,j in itertools.combinations(range(20),2))
assert sum((w*w.T for w in W),S.zeros(5))==4*S.eye(5)
assert sum((W[i].dot(W[j]))**2 for i,j in itertools.combinations(range(20),2))==30
assert sum(1 for i,j in itertools.combinations(range(20),2)
           if abs(W[i].dot(W[j]))>Q(1,2))==35
print("PASS: D5 spectrum/projector, 210 exact certificates, max pair norm product 112")
print("PASS: K5 cycles, 3360/1440/45 support patterns, frame floor",floor)
print("PASS: distinct-line rational tight frame with 35 threshold violations")
