#!/usr/bin/env python3
"""Exact F3 quotient, rational mixed-term identities, and rational root certificate."""
from itertools import combinations, product
from collections import defaultdict
from fractions import Fraction as F
from random import Random
import sympy as sp

E={(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
P1=((0,2),(1,4),(3,6),(5,7))
P3=((0,5),(1,4),(2,7),(3,6))
Pall=[p for p in combinations(sorted(E),4) if len({v for e in p for v in e})==8]
assert len(Pall)==3 and P1 in Pall and P3 in Pall
rng=Random(20261023)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def add(x,y): return [a+b for a,b in zip(x,y)]
def sub(x,y): return [a-b for a,b in zip(x,y)]

for P,p,q,r,h in [(P1,0,3,1,2),(P3,0,2,1,3)]:
    idx={v:i for i,(u,w) in enumerate(P) for v in (u,w)}
    sg={v:(1 if v==u else -1) for u,w in P for v in (u,w)}
    cross=sorted(E-set(P))
    eta=next(t for t in product((-1,1),repeat=4)
             if all(t[idx[u]]*t[idx[v]]==sg[u]*sg[v] for u,v in cross))
    K=sp.zeros(4); mult=defaultdict(int)
    for u,w in cross:
        i,j=idx[u],idx[w]
        lam=sg[u]*eta[i]
        assert lam==sg[w]*eta[j]
        K[i,j]+=lam; K[j,i]+=lam
        mult[tuple(sorted((i,j)))]+=1
    assert mult[tuple(sorted((p,q)))]==2
    assert tuple(sorted((r,h))) not in mult
    assert len(mult)==5 and K[p,q]==0 and K[r,h]==0
    assert K[p,h]==1 and K[p,r]==-1 and K[q,h]==-1 and K[q,r]==1
    assert K.eigenvals()=={sp.Integer(2):1,sp.Integer(-2):1,sp.Integer(0):2}
    for _ in range(200):
        m=[]; z=[]
        for i in range(4):
            a=[F(rng.randint(-4,4)) for k in range(5)]
            b=[F(rng.randint(-4,4)) for k in range(5)]
            if dot(a,a)==0:a[0]=1
            b=sub(b,[dot(a,b)*x/dot(a,a) for x in a])
            m.append(a); z.append(b)
        v=[[eta[i]*x for x in z[i]] for i in range(4)]
        T=F(0); contacts=F(0)
        for u,w in cross:
            i,j=idx[u],idx[w]
            xu=add(m[i],[sg[u]*x for x in z[i]])
            xw=add(m[j],[sg[w]*x for x in z[j]])
            contacts+=dot(xu,xw)
            T+=sg[u]*dot(z[i],m[j])+sg[w]*dot(m[i],z[j])
        fact=dot(sub(m[p],m[q]),sub(v[h],v[r]))+dot(sub(m[h],m[r]),sub(v[p],v[q]))
        assert T==fact
        U=add(v[p],v[q]); N=add(m[p],m[q])
        Z=dot(add(U,v[r]),add(U,v[r]))+dot(add(U,v[h]),add(U,v[h]))
        M=dot(add(N,m[r]),add(N,m[r]))+dot(add(N,m[h]),add(N,m[h]))
        diag=sum((2 if i in (p,q) else 1)*(dot(m[i],m[i])+dot(z[i],z[i])) for i in range(4))
        assert 2*contacts==Z+M-diag+2*T

root=(sp.sqrt(16-2*sp.sqrt(3))-2*sp.sqrt(3))**2
assert root>sp.Rational(1,171)
assert root>2-sp.sqrt(9+4*sp.sqrt(3))/2
assert F(1732051,1000000)**2>3
assert F(13246,100000)**2>F(3,171)
assert 4-2*F(1732051,1000000)-F(1,171)-4*F(13246,100000)==F(17959,85500000)>0
K=4-2*sp.sqrt(3)
newroot=(48-18*sp.sqrt(3)-4*sp.sqrt(175-91*sp.sqrt(3)))/17
assert sp.simplify(17*newroot**2-(18*K+24)*newroot+K**2)==0
assert newroot>sp.Rational(1,117)
assert newroot>root
assert F(1732050,1000000)**2<3<F(1732051,1000000)**2
Klo=F(267949,500000)
Khi=F(5359,10000)
c=F(1,117)
assert (Klo-c)**2-8*c*(2*(Khi-c)+3)==F(2923336101089,3422250000000000)>0
print("PASS: 3 matchings, doubled quotient signs and spectra")
print("PASS: 400 exact-rational two-triangle identities")
print("PASS: exact quadratic root and rational C>1/117 certificate")
print("C floor =",sp.N(newroot,16))
