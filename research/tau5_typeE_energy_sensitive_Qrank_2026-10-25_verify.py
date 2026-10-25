#!/usr/bin/env python3
"""Exact rational audit: Type-E energy-sensitive Q-rank constants.
The analytic projector proof is in the companion research note.
Standard library only.
"""
from fractions import Fraction as F
from itertools import combinations

Amax = F(383, 504)

def quartic_floor(n):
    k = n - 14
    t = F(3*k, 4) - 2*Amax
    assert t > 0
    return F(n, 28*k)*t*t

assert quartic_floor(20) == F(2820005, 2667168)
assert quartic_floor(19) == F(1500259, 2222640)
assert quartic_floor(20) > F(375, 896)

# Exact radical comparison (3-2 sqrt(2))/2 > 819/10000.
r = F(3,2)-F(819,10000)
assert r > 0 and r*r-2 == F(1100761,100000000)

core_cap = 5*F(1,16)+F(25,256)
assert core_cap == F(105,256)
safe_floor = quartic_floor(20)-core_cap
assert safe_floor == F(13808395,21337344)
assert safe_floor > F(1275,7168)
assert safe_floor > 10*F(1,16)  # >=11 strictly subthreshold safe pairs

# Four 19-subsets count OO four times, OC three, CC twice.
O=list(range(16))
C=list(range(16,20))
counts={p:0 for p in combinations(range(20),2)}
for omitted in C:
    subset=O+[j for j in C if j != omitted]
    for p in combinations(subset,2):
        counts[p]+=1
for p,count in counts.items():
    assert count=={0:4,1:3,2:2}[sum(i in C for i in p)]

weighted_floor=quartic_floor(19)-core_cap/2
assert weighted_floor==F(33422213,71124480)

# D5 twenty projective lines: roots (e_i +/- e_j)/sqrt(2).
roots=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[i],v[j]=1,sign
        roots.append(v)
assert len(roots)==20

def dot(u,v):
    return sum(x*y for x,y in zip(u,v))

def rank(M):
    M=[[F(x) for x in row] for row in M]
    m,n=len(M),len(M[0])
    row=0
    for col in range(n):
        pivot=next((i for i in range(row,m) if M[i][col]),None)
        if pivot is None: continue
        M[row],M[pivot]=M[pivot],M[row]
        fac=M[row][col]
        M[row]=[x/fac for x in M[row]]
        for i in range(row+1,m):
            if M[i][col]:
                fac=M[i][col]
                M[i]=[x-fac*y for x,y in zip(M[i],M[row])]
        row+=1
        if row==m: break
    return row

K=[[F(dot(u,v)**2,4)-F(1,5) for v in roots] for u in roots]
assert rank(K)==14
d5_quartic=sum((F(1,4)-F(dot(u,v)**2,4))**2
               for u,v in combinations(roots,2))
assert d5_quartic==F(35,8)
assert d5_quartic>=F(5,42)*F(9,2)**2

print("PASS: rational floors, radical core cap, subset counts, exact D5 Q rank.")
print("20-vector floor:",quartic_floor(20))
print("Type-E 184-safe floor:",safe_floor)
print("Weighted 19-subset floor:",weighted_floor)
