#!/usr/bin/env python3
"""Exact low-center near-seven algebra and 16-line D5 extension atlas.
Upstream Type-E mass/harmonic and small-rank integer atlas are assumed.
No floating-point decisions.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import Counter
import sympy as sp

d=sp.symbols('d')
n=7*d*(1-4*d)
q=-sp.Rational(1,5)-d
E=sp.Rational(175,24)*q*q+sp.Rational(147,4)*(sp.Rational(5,7)+sp.Rational(5,12)*q+n/28)**2
g=sp.factor(E+n-sp.Rational(955,64))
assert g==7*d*(84*d**3+28*d**2-151*d+5)/16
assert (84*d**3+28*d**2-151*d+5).subs(d,sp.Rational(1,30))==sp.Rational(1,1125)
assert sp.simplify(sp.diff(E,d)-7*(336*d**3+84*d**2-174*d-11)/16)==0
assert 15-E.subs(d,sp.Rational(1,30))<sp.Rational(281,1000)
D=lambda a:196*a-644*a*a+896*a**3-448*a**4
assert D(sp.Rational(1,2500))>sp.Rational(5,64)
assert 7*sp.Rational(1,9)**2*(1-4*sp.Rational(1,9)**2)>sp.Rational(5,64)
assert 7*sp.Rational(12,25)**2*(1-4*sp.Rational(12,25)**2)>sp.Rational(5,64)
E16=sp.Rational(81,1078)*sp.Rational(5,64)+sp.Rational(1,2500)**2
assert E16==sp.Rational(158207437,26950000000)
assert E16<sp.Rational(1,169) and 4*E16<sp.Rational(16,625)
J=sp.Rational(281,5250)
ev2=J/4+sp.Rational(2,3)*J*J
assert ev2==sp.Rational(2528719,165375000)
assert ev2<sp.Rational(1,64)
assert (sp.Rational(100,147)+sp.Rational(175,288))/13<sp.Rational(1,10)

def ratio(k,q,h=13):
    return (Q(2)**(2*k)*(Q(k)+Q(k-q,h))**(2*q)/q**(2*q)
            *Q(1,h*h*(k-q))**(k-q))
assert max(ratio(7,q) for q in range(1,6))<9
for k in range(8,17):
    assert max(ratio(k,q) for q in range(1,6))<1

roots=[]
for i,j in combinations(range(5),2):
    for sign in (-1,1):
        v=[0]*5;v[i]=1;v[j]=sign;roots.append(tuple(v))
idx={r:i for i,r in enumerate(roots)}
def canon(v):
    for a in v:
        if a:return tuple(v if a>0 else [-x for x in v])
def trans(r,p,s):
    v=[0]*5
    for i,a in enumerate(r):v[p[i]]=s[i]*a
    return canon(v)
maps=[]
for p in permutations(range(5)):
    for s in product((-1,1),repeat=5):
        if s.count(-1)%2==0:
            maps.append(tuple(idx[trans(r,p,s)] for r in roots))
assert len(maps)==1920
unseen=set(combinations(range(20),4));orbits=[]
while unseen:
    rep=min(unseen)
    orbit={tuple(sorted(m[i] for i in rep)) for m in maps}
    assert orbit<=unseen
    unseen-=orbit;orbits.append((rep,len(orbit)))
assert len(orbits)==17 and sum(sz for _,sz in orbits)==4845

def rank_mod(rows,prime=101):
    if not rows:return 0
    a=[[v%prime for v in row] for row in rows];rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,prime)
        a[rank]=[(v*inv)%prime for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                k=a[i][j]
                a[i]=[(v-k*w)%prime for v,w in zip(a[i],a[rank])]
        rank+=1
    return rank
hist=Counter()
for missing,sz in orbits:
    kept=[i for i in range(20) if i not in missing]
    rel=[]
    for a,b,c in combinations(range(16),3):
        for s,t in product((-1,1),repeat=2):
            if all(roots[kept[a]][j]+s*roots[kept[b]][j]+t*roots[kept[c]][j]==0 for j in range(5)):
                q=[0]*16;q[a]=1;q[b]=s;q[c]=t;rel.append(q)
    assert rank_mod(rel)==11
    basis=[]
    for i in kept:
        if rank_mod([roots[j] for j in basis+[i]])>len(basis):basis.append(i)
        if len(basis)==5:break
    inv=sp.Matrix([roots[i] for i in basis]).inv()
    feasible={}
    for c in product((-1,0,1),repeat=5):
        t=tuple(inv*sp.Matrix(c))
        if all(sum(t[j]*roots[k][j] for j in range(5)) in (-1,0,1) for k in kept):
            feasible[t]=sum(x*x for x in t)
    omitted={tuple(s*x for x in roots[j]) for j in missing for s in (-1,1)}
    assert {t for t,v in feasible.items() if v==2}==omitted
    assert set(feasible.values())<={sp.Rational(0),sp.Rational(1),sp.Rational(5,4),sp.Rational(2),sp.Rational(3),sp.Rational(13,4)}
    assert len(feasible) in (51,53)
    hist[(len(feasible),sz)]+=1
print('PASS: exact low-center polynomial and rational bounds')
print('PASS: 4845 omitted quadruples in 17 Weyl orbits')
print('PASS: triangle kernel rank 11 and norm-two roots = eight omitted signed roots')
print('PASS: sixteen-vector Gram determinant and center rounding bounds')
print('Orbit histogram:',sorted(hist.items()))
print('CONDITIONAL: upstream Type-E mass and signed-Gram atlases assumed')
