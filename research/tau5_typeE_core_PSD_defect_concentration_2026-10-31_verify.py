"""Exact rational checker for Type-E four-core PSD concentration theorem.

The analytic proof is in the companion .md file. This checker verifies all
constants and supplies deterministic rational Gram stress tests.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

D=F(1780062775,4032758016)
A=F(383,504)
eta=F(27,80000)
Fmax=lambda t: F(1,16)+(t-F(1,4))**2
B=F(3,2)+D/4+Fmax(D)+3*A/8
new=B-eta
assert D>F(441,1000) and D<F(9,20)
assert D-F(1,1000)>F(11,25)
assert A<F(19,25)
assert B==F(32436090936603055633,16263137215612256256)
assert new==F(20269126329870491560321,10164460759757660160000)
assert (2*D-F(251,1000))/1000 > eta
assert F(49,5000)-D/50 > F(1,1250) >= F(1,2000)
assert F(1,16)+F(9,50)**2+F(1,50)**2 == F(953,10000)
assert Fmax(F(11,25))-F(1,2000) == F(981,10000)
assert F(953,10000) < F(981,10000)
assert F(6,25)+F(9,50) > A/2
u,v=F(6,25),F(9,50)
rad=(F(1,16)-u*u)*(F(1,16)-v*v)
assert rad < F(13,1000)**2
assert 4*(u*v-F(13,1000)) > F(3,25)
assert F(12,25)-D-F(1,1000)>F(3,80)
assert F(1,4)-2*F(3,80)**2==F(791,3200)
assert F(3,25)*(F(1,4)-F(791,3200))==eta
qfloor=F(17456771,635040)
qsafe=qfloor-new
assert qsafe==F(259144239476339336023679,10164460759757660160000)
qcenter=F(5876056025347,211680000000)

rng=Random(5310)
pairs=list(combinations(range(4),2))
passed=0
for _ in range(3000):
    raw=[[F(rng.randint(-5,5),10) for _ in range(4)] for _ in range(4)]
    sq=sum(v*v for row in raw for v in row)
    if sq==0: continue
    scale=F(1,16)
    while scale*scale*sq>A or any(scale*scale*sum(v*v for v in row)>F(1,4) for row in raw):
        scale/=2
    m=[[scale*v for v in row] for row in raw]
    ai=[sum(v*v for v in row) for row in m]
    C={(i,j):sum(m[i][k]*m[j][k] for k in range(4)) for i,j in pairs}
    eps={}
    remaining=D
    for ij in pairs:
        cap=max(F(0),-C[ij])
        e=min(cap,remaining)*F(rng.randint(0,4),4)
        eps[ij]=e
        remaining-=e
    delta=sum(eps.values())
    E2=sum(e*e for e in eps.values())
    N=sum(max(F(0),-c) for c in C.values())
    s=sum(sum(m[i][k] for i in range(4))**2 for k in range(4))
    d={ij:min(F(1,2)-C[ij],F(1,2)+eps[ij]) for ij in pairs}
    Q6=sum(t*t for t in d.values())
    pos_gap=sum(c*(F(1,4)-c) for c in C.values() if c>0)
    rhs=F(3,2)+delta/4+E2+F(3,8)*(sum(ai)-s)-F(3,4)*(N-delta)-pos_gap
    assert Q6<=rhs, (Q6,rhs)
    assert Q6<=new, (Q6,new)
    passed+=1
print('EXACT PASS: new six-exception cap',new,float(new))
print('EXACT PASS: safe floor',qsafe,float(qsafe))
print('EXACT PASS: center-derived safe floor >',float(qcenter-new))
print('SUPPLEMENTARY PASS: rational Gram cases',passed)
