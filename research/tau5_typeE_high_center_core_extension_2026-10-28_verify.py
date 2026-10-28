#!/usr/bin/env python3
"""Exact D5 orbit, triangle-kernel, and integer-extension checks.
Upstream Type-E harmonic/mass/rounding hypotheses are not checked here.
No floating-point numerics or third-party packages.
"""
from itertools import combinations, permutations, product
from fractions import Fraction as Q
from collections import Counter

roots=[]
for i,j in combinations(range(5),2):
    for s in (-1,1):
        v=[0]*5;v[i]=1;v[j]=s
        roots.append(tuple(v))
idx={r:i for i,r in enumerate(roots)}
def canonical(v):
    for a in v:
        if a:return tuple(v if a>0 else (-x for x in v))
    raise AssertionError('zero')
def transform(r,p,s):
    v=[0]*5
    for i,a in enumerate(r):v[p[i]]=s[i]*a
    return canonical(v)
maps=[]
for p in permutations(range(5)):
    for s in product((-1,1),repeat=5):
        if s.count(-1)%2==0:
            maps.append(tuple(idx[transform(r,p,s)] for r in roots))
assert len(maps)==1920
unseen=set(combinations(range(20),3));orbits=[]
while unseen:
    rep=min(unseen)
    orbit={tuple(sorted(m[i] for i in rep)) for m in maps}
    assert orbit<=unseen
    unseen-=orbit;orbits.append((rep,len(orbit)))
assert sorted(sz for _,sz in orbits)==[40,40,60,120,160,240,480]
assert sum(sz for _,sz in orbits)==1140

def rank_mod(rows,prime=101):
    if not rows:return 0
    a=[[v%prime for v in row] for row in rows]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        k=pow(a[rank][j],-1,prime)
        a[rank]=[(v*k)%prime for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                k=a[i][j]
                a[i]=[(v-k*w)%prime for v,w in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank

def inverse(M):
    n=len(M)
    a=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)]
       for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j]
        d=a[j][j];a[j]=[x/d for x in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j]
                a[i]=[x-d*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]
def dot(x,y):return sum(a*b for a,b in zip(x,y))

results=[]
for missing,sz in orbits:
    kept=[i for i in range(20) if i not in missing]
    rel=[]
    for a,b,c in combinations(range(17),3):
        for s,t in product((-1,1),repeat=2):
            if all(roots[kept[a]][j]+s*roots[kept[b]][j]+t*roots[kept[c]][j]==0 for j in range(5)):
                q=[0]*17;q[a]=1;q[b]=s;q[c]=t;rel.append(q)
    assert rank_mod(rel)==12,(missing,'triangle rank')
    basis=[]
    for i in kept:
        if rank_mod([roots[j] for j in basis+[i]])>len(basis):basis.append(i)
        if len(basis)==5:break
    assert len(basis)==5
    inv=inverse([roots[i] for i in basis])
    feasible={}
    for c in product((-1,0,1),repeat=5):
        t=tuple(dot(row,c) for row in inv)
        if all(dot(t,roots[j]) in (-1,0,1) for j in kept):
            feasible[t]=dot(t,t)
    hist=Counter(feasible.values())
    assert hist[Q(0)]==1 and hist[Q(1)]==10
    assert hist[Q(5,4)]==32 and hist[Q(2)]==6
    assert set(hist)<={Q(0),Q(1),Q(5,4),Q(2),Q(3)}
    omitted={tuple(s*x for x in roots[j]) for j in missing for s in (-1,1)}
    assert {t for t,v in feasible.items() if v==2}==omitted
    assert hist[Q(3)] in (0,2)
    assert len(feasible) in (49,51)
    results.append((missing,sz,len(rel),hist[Q(3)],len(feasible)))

assert sum(sz for _,sz,_,extra,_ in results if extra==2)==40
# Exact rational safety margins used by the geometric proof:
assert Q(5,336)<Q(1,64) and Q(2,17)<Q(1,8)
assert Q(17,18)>Q(8,9)**2 and Q(17,18)>Q(17,18)**2
assert Q(3,4)<1   # sqrt(3)/2 < 1
assert Q(121)>Q(80) and Q(225)>Q(128) # radial norm gaps >1/4
assert Q(15,16)>Q(1,2) # duplicate signed root violates kissing bound
print('PASS: 1920 Weyl maps, 1140 triples, seven orbits')
for row in results:print('orbit',row)
print('PASS: triangle relation rank 12 in all orbits')
print('PASS: 49/51 feasible columns; norm-2 columns = six signed missing roots')
print('PASS: all rational threshold checks')
print('UPSTREAM mass/rounding/D5 geometric certificates are assumed, not checked.')
