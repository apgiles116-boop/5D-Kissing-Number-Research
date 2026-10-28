#!/usr/bin/env python3
"""Exact integer Bernstein certificate: all 17-line D5 subsets are flexible."""
from itertools import combinations, permutations, product
from math import comb

ROOTS = []
for i,j in combinations(range(5),2):
    for s in (-1,1):
        x=[0]*5; x[i]=1; x[j]=s; ROOTS.append(tuple(x))
LOOKUP={x:i for i,x in enumerate(ROOTS)}
WITNESSES={
    (0,1,2):{5:(1,0,0,0,0)},
    (0,1,14):{0:(0,-1,0,0,0),1:(0,-1,0,0,0),
              6:(1,0,0,0,0),7:(1,0,0,0,0)},
    (0,2,4):{6:(-1,0,0,0,0)},
    (0,2,8):{0:(0,0,-1,0,0)},
    (0,2,9):{0:(0,0,1,0,0),1:(0,-1,0,0,0),6:(1,0,0,0,0)},
    (0,2,10):{7:(-1,0,0,0,0)},
    (0,2,18):{7:(-1,0,0,0,0)}
}
def dot(x,y):return sum(a*b for a,b in zip(x,y))
actions=[]
for perm in permutations(range(5)):
    for signs in product((-1,1),repeat=5):
        if sum(s==-1 for s in signs)%2:continue
        action=[]
        for x in ROOTS:
            y=[0]*5
            for k in range(5):y[perm[k]]=x[k]*signs[k]
            if next(v for v in y if v)<0:y=[-v for v in y]
            action.append(LOOKUP[tuple(y)])
        actions.append(tuple(action))
assert len(actions)==1920
remaining=set(combinations(range(20),3))
orbits={}
while remaining:
    rep=min(remaining)
    orbit={tuple(sorted(a[i] for i in rep)) for a in actions}
    assert orbit<=remaining
    remaining-=orbit
    orbits[rep]=len(orbit)
assert orbits=={
    (0,1,2):120,(0,1,14):60,(0,2,4):160,
    (0,2,8):40,(0,2,9):40,(0,2,10):480,(0,2,18):240}
assert sum(orbits.values())==1140
def bernstein_scaled(p):
    # 12*10^4 times Bernstein coefficients of P(s/10), degree four
    return [sum(p[k]*comb(j,k)*(12//comb(4,k))*10**(4-k)
                for k in range(j+1)) for j in range(5)]
for missing,sparse in WITNESSES.items():
    roots=[ROOTS[i] for i in range(20) if i not in missing]
    vels=[sparse.get(i,(0,0,0,0,0)) for i in range(17)]
    assert all(dot(x,v)==0 for x,v in zip(roots,vels))
    varying=0;strict=0;checked=0
    for i,j in combinations(range(17),2):
        x,y,v,w=roots[i],roots[j],vels[i],vels[j]
        d0=dot(x,y);d1=dot(x,w)+dot(v,y);d2=dot(v,w)
        ai,aj=dot(v,v),dot(w,w)
        assert d0 in (-1,0,1)
        p=[4-4*d0*d0,-8*d0*d1,
           2*(ai+aj)-4*(d1*d1+2*d0*d2),
           -8*d1*d2,ai*aj-4*d2*d2]
        assert min(bernstein_scaled(p))>=0,(missing,i,j,p)
        varying+=(d1!=0)
        strict+=(abs(d0)==1 and d0*d1<0)
        checked+=1
    assert checked==136 and varying>0
    print(f'{missing}: orbit={orbits[missing]}, pairs=136, '
          f'varying={varying}, relaxing={strict}, PASS')
print('PROVED: all 1140 D5 17-line subsets admit noncongruent finite flexes')
print('TYPE-E APPLICATION CONDITIONAL; 40<=tau_5<=44 UNCHANGED')
