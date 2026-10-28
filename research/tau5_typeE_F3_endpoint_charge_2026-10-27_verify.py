"""Exact finite audit: Type-E F3 endpoint-charge and P2 quartic budget."""
from fractions import Fraction as Q
from itertools import combinations, product

E = {frozenset(e) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),
                              (2,3),(2,7),(3,6),(5,6),(5,7)]}
P = {
    'P1': [(0,2),(1,4),(3,6),(5,7)],
    'P2': [(0,4),(1,7),(2,3),(5,6)],
    'P3': [(0,5),(1,4),(2,7),(3,6)],
}
D0=Q(1780062775,4032758016)
f=lambda d:(Q(1,2)+d)**2*(d+d*d)
g=lambda d:d+d*d
assert f(Q(1,8))==Q(225,4096)
assert 2*f(Q(1,8))==Q(225,2048)
assert 2*g(Q(1,8))==Q(9,32)
assert 2*f(Q(1,8))+Q(7,64)*2*g(Q(1,8))==Q(9,64)
assert 0<D0-Q(3,8)<Q(1,8)

for name,match in P.items():
    pairs=list(combinations(range(4),2))
    count={}; forced={}
    for i,j in pairs:
        cross=[]
        for u in match[i]:
            for v in match[j]:
                if frozenset((u,v)) in E:
                    a=1 if u==match[i][0] else -1
                    b=1 if v==match[j][0] else -1
                    cross.append(-a*b)
        assert len(cross)<=2 and len(set(cross))<=1
        count[i,j]=len(cross)
        if cross: forced[i,j]=cross[0]
    switch=[eps for eps in product((-1,1),repeat=4)
            if eps[0]==1 and all(eps[i]*eps[j]*s==-1
                                 for (i,j),s in forced.items())]
    assert len(switch)==1, (name,switch)
    assert sum(Q(k-1,2) for k in count.values())==0
    if name=='P2': assert sorted(count.values())==[1]*6
    else: assert sorted(count.values())==[0,1,1,1,1,2]

    possible=[]
    for mask in range(64):
        active={pairs[i] for i in range(6) if mask & (1<<i)}
        if any(count[e]==0 for e in active): continue
        # Signed-triangle exclusion, independently established from PSD.
        if any(all(tuple(sorted(e)) in active for e in combinations(vs,2))
               for vs in combinations(range(4),3)): continue
        k1=sum(count[e]==1 for e in active)
        # The endpoint-charge budget implies sum d <= 1-k1/4.
        total_cap=Q(1)-Q(k1,4)
        if active and total_cap<=0: continue
        caps=sorted((Q(count[e],8) for e in active),reverse=True)
        remaining=min(D0,total_cap)
        allocation=[]
        for cap in caps:
            v=min(cap,remaining)
            allocation.append(v)
            remaining-=v
        possible.append((sum(map(f,allocation),Q(0)),active,allocation,k1))
    best=max(possible,key=lambda x:x[0])
    if name=='P2':
        assert all(len(x[1])<=3 for x in possible)
        assert best[0]==Q(225,2048),best
        assert all(sum(x[2])<=Q(1,4) for x in possible)
        assert all(sum(map(g,x[2]))<=Q(9,32) for x in possible)
    else:
        assert all(len(x[1])<=3 for x in possible)
        assert best[0]==f(Q(1,4))+f(Q(1,8))+f(D0-Q(3,8))
    print(name,'switch=',switch[0], 'maximum_active=',max(len(x[1]) for x in possible),
          'max_quartic=',best[0], 'decimal=',float(best[0]))
print('PASS: all matchings, antibalanced switching, endpoint-charge supports, exact P2 bound.')
