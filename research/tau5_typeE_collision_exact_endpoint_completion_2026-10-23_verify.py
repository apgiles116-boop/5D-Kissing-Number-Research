#!/usr/bin/env python3
"""Exact D5 Q-Gram four-core complement-rank certificate."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
supports=list(combinations(range(5),2))
labels=[(a,b,s) for a,b in supports for s in (1,-1)]
def dot2(i,j):
    a,b,s=labels[i]; c,d,t=labels[j]
    return int(a==c)+t*int(a==d)+s*int(b==c)+s*t*int(b==d)
# G_ij = (dot2(i,j)/2)^2 - 1/5; scale by 20.
G20=[[5*dot2(i,j)**2-4 for j in range(20)] for i in range(20)]
assert set(v for row in G20 for v in row)=={-4,1,16}
def rank_mod(M,p=101):
    A=[[v%p for v in row] for row in M]
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        k=next((i for i in range(r,m) if A[i][c]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][c],-1,p)
        for j in range(c,n): A[r][j]=A[r][j]*inv%p
        for i in range(r+1,m):
            if A[i][c]:
                t=A[i][c]
                for j in range(c,n): A[i][j]=(A[i][j]-t*A[r][j])%p
        r+=1
        if r==m: break
    return r
assert rank_mod(G20)==14
# Six complete supports always span the traceless diagonal space.
for removed in combinations(range(10),4):
    kept=[s for s in range(10) if s not in removed]
    diag=[[int(k in supports[s])-int(4 in supports[s])
           for s in kept] for k in range(4)]
    assert rank_mod(diag)==4
counts=Counter()
for J in combinations(range(20),4):
    Jset=set(J); O=[i for i in range(20) if i not in Jset]
    h=sum(2*s in Jset and 2*s+1 in Jset for s in range(10))
    rank=rank_mod([[G20[i][j] for j in O] for i in O])
    assert rank==14-h,(J,h,rank)
    counts[(h,rank)]+=1
assert counts=={(0,14):3360,(1,13):1440,(2,12):45},counts
for s in range(10):
    i,j=2*s,2*s+1
    assert G20[i][i]==G20[j][j]==16 and G20[i][j]==-4
for s,t in combinations(range(10),2):
    intersect=bool(set(supports[s])&set(supports[t]))
    for i in (2*s,2*s+1):
        for j in (2*t,2*t+1):
            assert G20[i][j]==(1 if intersect else -4)
# Coarse coherence alone is not sharp enough: 2+2 residual axes
# with rational cosine 5/13 yield cross q^2=1/4 +/- 5/26.
qlo=Fraction(1,4)-Fraction(5,26)
qhi=Fraction(1,4)+Fraction(5,26)
assert 0<qlo<Fraction(1,4)<qhi<Fraction(9,16)
print("PASS 4845/4845 D5 core complement ranks",dict(counts))
print("PASS 210 diagonal span checks, D5 Gram entries")
print("PASS rational coarse-threshold witness",qlo,qhi)
print("Analytic planar opposite-cone lemma is proved in the note")
