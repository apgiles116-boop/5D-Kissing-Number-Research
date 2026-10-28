#!/usr/bin/env python3
"""Exact combinatorial/rational verifier for D5 sparse-eight Q circuits."""
from itertools import combinations
from collections import Counter
from sympy import Matrix, eye, zeros, Rational
E=list(combinations(range(5),2))
roots=[(e,s) for e in E for s in (1,-1)]
Q={}
for (i,j),s in roots:
    v=zeros(5,1);v[i]=1;v[j]=s
    Q[((i,j),s)]=v*v.T/2-eye(5)/5
cycles=set()
for a,b,c,d in combinations(range(5),4):
    for p in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
        cycles.add(frozenset(tuple(sorted((p[i],p[(i+1)%4]))) for i in range(4)))
tri=set()
for t in combinations(range(5),3):
    rest=tuple(k for k in range(5) if k not in t)
    tri.add(frozenset(list(combinations(t,2))+[rest]))
assert (len(cycles),len(tri))==(15,10)
for C in cycles:
    a,b,c,d=sorted(set(x for e in C for x in e))
    matchings=[{tuple(sorted((a,b))),tuple(sorted((c,d)))},
               {tuple(sorted((a,c))),tuple(sorted((b,d)))},
               {tuple(sorted((a,d))),tuple(sorted((b,c)))}]
    M=[x for x in matchings if x<=C]
    assert len(M)==2
    R=sum(((1 if e in M[0] else -1)*(Q[e,1]+Q[e,-1]) for e in C),zeros(5,5))
    assert R==zeros(5,5)
for C in tri:
    deg=Counter(x for e in C for x in e)
    edge=next(e for e in C if deg[e[0]]==deg[e[1]]==1)
    R=sum(((2 if e==edge else 1)*(Q[e,1]+Q[e,-1]) for e in C),zeros(5,5))
    assert R==zeros(5,5)
    F=sum(((2 if e==edge else 1)*(Q[e,s]+eye(5)/5) for e in C for s in (1,-1)),zeros(5,5))
    assert F==2*eye(5)
for k,expected in ((16,{1:960,2:2160,3:360,4:960,5:360,8:30,9:15}),
                   (17,{3:80,4:640,5:240,8:120,9:60})):
    hist=Counter();without_cycle=0
    for ids in combinations(range(20),k):
        chosen={roots[i] for i in ids}
        doubled={e for e in E if (e,1) in chosen and (e,-1) in chosen}
        nc=sum(C<=doubled for C in cycles)
        nt=sum(C<=doubled for C in tri)
        hist[nc+nt]+=1
        without_cycle+=(nc==0)
    assert hist==expected
    assert without_cycle==(240 if k==16 else 0)
    print('PASS',k,'line subsets:',dict(sorted(hist.items())))
V=[]
for (i,j),s in roots:
    v=[0]*5;v[i]=1;v[j]=s;V.append(v)
V=Matrix(V);H=V*V.T
K=5*H.multiply_elementwise(H)-4*Matrix.ones(20,20)
assert K.eigenvals()=={30:4,20:10,0:6}
print('PASS: 25 sparse Q circuits, positive tight frames, full D5 Q spectrum')
