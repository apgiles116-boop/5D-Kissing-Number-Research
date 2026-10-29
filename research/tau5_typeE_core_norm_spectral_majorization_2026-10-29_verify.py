"""Exact Fraction checks for Type-E core norm dispersion SOS (2026-10-29).
The algebraic proof is in the companion .md; tests are supplementary.
"""
from fractions import Fraction as F
from random import Random

n=5
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def mat(v): return [[a*b for b in v] for a in v]
def plus(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def minus(A,B): return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,t): return [[t*a for a in x] for x in A]
def I(): return [[F(i==j) for j in range(n)] for i in range(n)]
def Z(): return [[F(0) for j in range(n)] for i in range(n)]
def frame(vecs):
    R=Z()
    for v in vecs: R=plus(R,mat(v))
    return R
def tr(A): return sum((A[i][i] for i in range(n)),F(0))
def f2(A): return sum((a*a for x in A for a in x),F(0))

def check(S,qs,p):
    assert dot(p,p)==1
    C=frame(qs); c=tr(C); mu=(tr(S)+c)/5
    P=mat(p); perp=minus(I(),P)
    S0=plus(scale(P,mu),scale(perp,mu-c/4))
    H=minus(S,S0); D=minus(C,scale(perp,c/4))
    E=minus(plus(S,C),scale(I(),mu))
    assert E==plus(H,D)
    w=[dot(q,q) for q in qs]
    var=sum(((a-c/4)**2 for a in w),F(0))
    core=2*sum((dot(qs[i],qs[j])**2 for i in range(4) for j in range(i+1,4)),F(0))
    pe=(c/2)*sum((dot(p,q)**2 for q in qs),F(0))
    assert f2(D)==var+core+pe

rng=Random(2901029)
p=[F(1),F(0),F(0),F(0),F(0)]
for trial in range(500):
    iso=[[F(rng.randint(-3,3),rng.randint(1,5)) for _ in range(n)] for _ in range(16)]
    core=[[F(rng.randint(-3,3),rng.randint(1,5)) for _ in range(n)] for _ in range(4)]
    check(frame(iso),core,p)

A=F(383,504); mu=4-A/5; c=4-A; r=mu-c/4
w=[F(499,504),F(3,4),F(3,4),F(3,4)]
S=Z(); C=Z()
for i in range(n): S[i][i]=mu if i==0 else r
for j in range(4): C[j+1][j+1]=w[j]
V=f2(minus(plus(S,C),scale(I(),mu)))
variance=sum(((a-c/4)**2 for a in w),F(0))
assert V==variance==F(14641,338688)
assert V/2==F(14641,677376)
assert mu==F(9697,2520) and r==F(30623,10080)
assert w[0]-c/4==F(121,672)>0
# Ky Fan k=1 necessary bound, exact in rational diagonal example.
assert V>=F(5,4)*(w[0]-mu+r)**2
print("PASS: 500 exact-rational SOS cases; boundary example and Ky Fan k=1")
print("V =",V,"Q-frame penalty =",V/2)
