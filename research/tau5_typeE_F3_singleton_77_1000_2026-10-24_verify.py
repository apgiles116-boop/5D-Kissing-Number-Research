"""Exact rational 13-interval Type-E F3 certificate Q<77/1000."""
from fractions import Fraction as F
from itertools import combinations

edges=[(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]
ms=[m for m in combinations(edges,4) if len({v for e in m for v in e})==8]
assert len(ms)==3
patterns=[]
for m in ms:
    ids={v:i for i,e in enumerate(m) for v in e}
    cnt={p:0 for p in combinations(range(4),2)}
    for a,b in edges:
        if ids[a]!=ids[b]:cnt[tuple(sorted((ids[a],ids[b])))]+=1
    patterns.append(sorted(cnt.values()))
    if sorted(cnt.values())==[0,1,1,1,1,2]:
        zero=next(k for k,v in cnt.items() if v==0)
        double=next(k for k,v in cnt.items() if v==2)
        assert set(zero).isdisjoint(double)
assert sorted(patterns)==[[0,1,1,1,1,2],[0,1,1,1,1,2],[1,1,1,1,1,1]]

D=F(1780062775,4032758016);b=F(383,1008);qmax=F(77,1000)
alo=F(2071067,10**7);ahi=F(207107,10**6)
assert (1+2*alo)**2<2<(1+2*ahi)**2
assert D>b and alo>b/2 and ahi<2*b-D
assert D*D/3<qmax
assert b*b/2+(D-b)**2<qmax
assert ahi*ahi+(b-alo)**2+(D-b)**2<qmax

def P(x,y):return x+y+4*(x*x+y*y-x*y)-F(1,2)
def capped_sq(c,r):
    k=min(4,r//c)
    return k*c*c+(r-k*c)**2 if k<4 else 4*c*c

start=F(207,1000)
caps=[154180,149194,143883,138204,132102,125506,118321,
      110417,101606,91599,79902,65535,45863]
worst=F(0)
for i,num in enumerate(caps):
    left=start+F(i,300)
    right=min(left+F(1,300),F(1,4))
    c=F(num,10**6)
    assert right>left and P(left,c)>0
    assert 1+8*left-4*c>0
    bound=right*right+capped_sq(c,D-left)
    assert bound<qmax,(i,left,right,c,bound)
    worst=max(worst,bound)
assert start+F(12,300)<F(1,4)<=start+F(13,300)
assert worst==F(305420404476709867702417033,3970492484280336000000000000)

L=F(8790283,317520)
safe=L-F(3,2)-D-qmax
assert safe==F(12937988020021,504094752000)
assert safe-(L-F(3,2)-D-F(40949,500000))==F(4898,10**6)
print("PASS: 3 F3 matchings, all-singleton case, 13 exact rational double-contact intervals")
print("Q<77/1000; S_safe>",safe,"=",float(safe))
