#!/usr/bin/env python3
"""Exact-rational checks for Type-E core affine-centroid theorem.
Analytic proof is in the companion Markdown; finite tests are supplementary.
"""
from fractions import Fraction as F
from math import ceil

HALF=F(1,2)
QUARTER=F(1,4)
D=F(1780062775,4032758016)
A_MAX=F(383,504)
Q_BASIC=F(17456771,635040)
V_CENTER=F(47602076041,317520000000)
Q_CENTER=F(5876056025347,211680000000)
Q6_OLD=F(1051426055,504094752)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
def endpoints(m,z):
    return [[mi+zi for mi,zi in zip(m,z)],
            [mi-zi for mi,zi in zip(m,z)]]

def check_pair(m,z,n,w):
    assert dot(m,z)==0 and dot(n,w)==0
    assert norm2(m)+norm2(z)==1 and norm2(n)+norm2(w)==1
    assert norm2(m)<=QUARTER and norm2(n)<=QUARTER
    for x in endpoints(m,z):
        for y in endpoints(n,w):
            assert dot(x,y)<=HALF
    c=dot(m,n)
    d=abs(dot(z,w))
    eps=max(F(0),d-HALF)
    assert d*d<=QUARTER+HALF*eps-F(3,4)*c
    return c,d,eps

tests=0
for ic in range(-20,21):
    c=F(ic,80)
    for idd in range(61):
        d=F(idd,80)
        if c+d>HALF: continue
        eps=max(F(0),d-HALF)
        assert d*d<=QUARTER+HALF*eps-F(3,4)*c
        tests+=1

Z=[F(0),F(1,2),F(1,2),F(1,2),F(0)]
Zflip=[F(0),F(1,2),F(1,2),F(-1,2),F(0)]
M=[F(1,2),F(0),F(0),F(0),F(0)]
minusM=[-v for v in M]
for n,w,expected in [(M,Zflip,(F(1,4),F(1,4),F(0))),
                     (minusM,Z,(F(-1,4),F(3,4),F(1,4)))]:
    c,d,eps=check_pair(M,Z,n,w)
    assert (c,d,eps)==expected
    assert d*d==QUARTER+HALF*eps-F(3,4)*c

cap_squares=F(3,16)+(A_MAX-F(3,4))**2
assert 30-3*A_MAX+A_MAX*A_MAX/10-cap_squares/2+V_CENTER/2==Q_CENTER

Q6_NEW=F(3,2)+D/2+F(3,8)*A_MAX
assert Q6_NEW==F(16176768847,8065516032)
assert Q6_NEW<Q6_OLD
QSAFE_BASIC=Q_BASIC-Q6_NEW
QSAFE_CENTER=Q_CENTER-Q6_NEW
assert QSAFE_BASIC==F(1027690941349,40327580160)
assert QSAFE_CENTER==F(64910958829119229,2520473760000000)

def threshold(q,r):
    k=(q-184*r*r)/(QUARTER-r*r)
    return max(0,ceil(k))

basic_expected={F(0):102,F(1,5):87,F(1,4):75,F(1,3):37}
center_expected={F(0):104,F(1,8):98,F(1,5):88,F(1,4):77,F(1,3):39}
for r,expect in basic_expected.items():
    assert threshold(QSAFE_BASIC,r)==expect
for r,expect in center_expected.items():
    assert threshold(QSAFE_CENTER,r)==expect

# Independent exact trace-identity check on rational 20-vector data.
vecs=[]
for j in range(20):
    v=[F(0)]*5
    v[j%5]=F(1)-F(j%3,10)
    vecs.append(v)
A=sum(F(1)-norm2(v) for v in vecs)
Q=sum(dot(vecs[i],vecs[j])**2 for i in range(20) for j in range(i+1,20))
Zmat=[[sum(v[i]*v[j] for v in vecs) for j in range(5)] for i in range(5)]
t=sum(norm2(v) for v in vecs)
V=sum((Zmat[i][j]-(t/5 if i==j else 0))**2 for i in range(5) for j in range(5))
assert Q==30-3*A+A*A/10-F(1,2)*sum((1-norm2(v))**2 for v in vecs)+V/2

print("PASS scalar contact grid",tests)
print("PASS rational R5 equality witnesses")
print("PASS global Q/frame identity and capped-simplex floor")
print("Q6 bound:",Q6_NEW,float(Q6_NEW))
print("Qsafe basic:",QSAFE_BASIC,float(QSAFE_BASIC))
print("Qsafe center-conditional:",QSAFE_CENTER,float(QSAFE_CENTER))
print("PASS exact safe-pair count thresholds")
