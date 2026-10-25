"""Exact rational certificate: Type-E singleton cap 1/8, six-core Q < 19/250.
Geometric lemmas are proved in the companion .md note.
All comparisons below use Fraction and integer isqrt, never floating point.
"""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations

D=F(1780062775,4032758016)
L=F(8790283,317520)
Q=F(19,250)
assert F(3,8)<D<F(1,2)

edges=[(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]
matchings=[m for m in combinations(edges,4) if len({v for e in m for v in e})==8]
assert len(matchings)==3
patterns=[]
for m in matchings:
    ids={v:i for i,e in enumerate(m) for v in e}
    counts={p:0 for p in combinations(range(4),2)}
    for u,v in edges:
        if ids[u]!=ids[v]:
            counts[tuple(sorted((ids[u],ids[v])))]+=1
    pattern=sorted(counts.values())
    assert pattern in ([1]*6,[0,1,1,1,1,2])
    if pattern==[0,1,1,1,1,2]:
        zero=next(k for k,v in counts.items() if v==0)
        double=next(k for k,v in counts.items() if v==2)
        assert set(zero).isdisjoint(double)
    patterns.append(pattern)
assert sorted(patterns)==[[0,1,1,1,1,2]]*2+[[1]*6]

# All six capped at 1/8: three saturated entries and one remainder.
all_single=3*F(1,8)**2+(D-F(3,8))**2
assert all_single<Q

def P(x,y): return x+y+4*(x*x+y*y-x*y)-F(1,2)

def sqrt_upper(fr,scale=10**12):
    assert fr>=0
    n2=fr.numerator*fr.denominator*scale*scale
    n=isqrt(n2)
    if n*n<n2: n+=1
    ans=F(n,fr.denominator*scale)
    assert ans*ans>=fr
    return ans

def cap_at_left(x):
    # Largest permissible adjacent y is min(1/8, positive root of P(x,y)=0).
    disc=F(9)-24*x-48*x*x
    assert disc>=0
    root_upper=(4*x-1+sqrt_upper(disc))/8
    cap=min(F(1,8),max(F(0),root_upper))
    if cap<F(1,8): assert P(x,cap)>=0
    return cap

def capped_square(cap,R,n=4):
    if cap==0:return F(0)
    if R>=n*cap:return n*cap*cap
    k=R//cap
    assert 0<=k<n
    return k*cap*cap+(R-k*cap)**2

# P is increasing in x for x>=1/8, y<=1/8; its positive root
# is nonincreasing. On [l,h], x²<=h², each y<=cap(l), sum y<=D-l.
accepted=[]
def certify(l,h,depth=0):
    assert F(1,8)<=l<h<=F(1,4)
    C=cap_at_left(l)
    upper=h*h+capped_square(C,D-l)
    if upper<Q:
        accepted.append((l,h,upper))
        return
    assert depth<35,(l,h,upper)
    m=(l+h)/2
    certify(l,m,depth+1)
    certify(m,h,depth+1)

certify(F(1,8),F(1,4))
assert len(accepted)==20
assert accepted[0][0]==F(1,8) and accepted[-1][1]==F(1,4)
assert all(accepted[i][1]==accepted[i+1][0] for i in range(len(accepted)-1))
worst=max(item[2] for item in accepted)
assert worst<Q

safe=L-F(3,2)-D-Q
assert safe==F(12938492114773,504094752000)
print('PASS: 3 F3 matchings and all-singleton case')
print('PASS: 20 exact rational double-contact intervals')
print('Worst interval bound:',worst,'=',float(worst))
print('Q <',Q,'; safe squared mass >',safe,'=',float(safe))
