"""Exact Fraction checker for cap stability and outside-16 9/160 gap (2026-10-29).
Random rational diagnostics supplement, but do not replace, the proofs.
"""
from fractions import Fraction as F
from random import Random

B=F(383,504); L0=F(9,160); Q0=F(8790283,317520)
def cap(A,n=20):
    assert 0<=A<=n*F(1,4)
    k=A//F(1,4); r=A-k*F(1,4)
    return [F(1,4)]*k+([r] if k<n else [])+[F(0)]*(n-k-(k<n))
def g(A,n=20):
    return sum(t*t for t in cap(A,n))
def Fmajor(v):
    x=[1/(1-t) for t in v]
    return sum(x[i]**2*x[j]**2-x[i]*x[j]
               for i in range(len(x)) for j in range(i+1,len(x)))/8

assert g(B)==F(47653,254016)
assert 30-3*B+B*B/10-g(B)/2==Q0
assert Q0-F(17456771,635040)==F(131,672)
p=[F(k,4)+F(5,2)*L0-F(7,2)*L0*L0/k for k in (1,2,3)]
p.append(B+3*L0-F(7,32)*L0*L0)
v=[p[0],p[1]-p[0],p[2]-p[1],p[3]-p[2]]+[F(0)]*12
assert v[:4]==[F(19433,51200),F(26167,102400),
              F(25789,102400),F(2118311,51609600)]
assert v==sorted(v,reverse=True)
assert F(3,4)-F(9,2)*L0-F(7,2)*L0*L0==F(24873,51200)>0
assert 4-Fmajor(v)==F(
    3740587247549191288613004487326972299372,
    3122586346512138747653771770355267994729243)>0

rng=Random(20261029)
for _ in range(5000):
    a=[F(rng.randint(0,250),1000) for i in range(20)]
    A=sum(a)
    if A>B:
        a=[t*B/A for t in a]; A=B
    a.sort(reverse=True); b=cap(A)
    d=[bb-aa for aa,bb in zip(a,b)]
    U=sum(t*t for t in a); delta=sum(abs(t) for t in d)
    assert all(sum(d[:k])>=0 for k in range(1,21))
    assert g(A)-U>=sum(t*t for t in d)>=delta*delta/20
    assert 30-3*A+A*A/10-U/2 >= Q0+F(57,20)*(B-A)+delta*delta/40
    x=sum(a[:16]); y=sum(a[16:])
    assert U<=g(x,16)+g(y,4)
for j in range(1001):
    A=F(3,4)+F(5*j,504000)
    r=A-F(3,4); x=r*F(j,1000)
    assert g(x,16)+g(A-x,4)==g(A)-2*x*(r-x)
print("PASS: exact constants, 5000 capped-energy diagnostics, 1001 split identities")
print("9/160 certificate: 4-F(v) =",4-Fmajor(v))
