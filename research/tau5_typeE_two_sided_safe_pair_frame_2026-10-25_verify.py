#!/usr/bin/env python3
"""Exact rational checks of the Type-E two-sided safe-pair and frame identities.
This verifies algebra on rational examples; the mathematical proof is in the .md note.
"""
from fractions import Fraction as Q
from itertools import product, combinations

half=Q(1,2)
count=0
for M,Z,X,Y in product((Q(k,8) for k in range(-4,5)),repeat=4):
    endpoints=(M+Z+X+Y,M+Z-X-Y,M-Z+X-Y,M-Z-X+Y)
    if all(abs(t)<=half for t in endpoints):
        assert abs(M+Z)+abs(X+Y)<=half
        assert abs(M-Z)+abs(X-Y)<=half
        assert max(abs(M),abs(Z))+max(abs(X),abs(Y))<=half
        assert half-abs(Z)>=max(abs(M),abs(X),abs(Y))
        count+=1
assert count==441

def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def v(k,c): return tuple(c if j==k else Q(0) for j in range(5))
def add(a,b,s=1): return tuple(x+s*y for x,y in zip(a,b))
def frame(vs):
    return [[sum((v[i]*v[j] for v in vs),Q(0)) for j in range(5)]
            for i in range(5)]
def traceprod(A,B):
    return sum((A[i][j]*B[j][i] for i in range(5) for j in range(5)),Q(0))
def norm2(A):
    return sum((x*x for row in A for x in row),Q(0))

z=[v(i%5,Q(12,13)) for i in range(20)]
m=[v((i+1)%5,Q(5,13)) for i in range(20)]
assert all(dot(z[i],m[i])==0 and dot(z[i],z[i])+dot(m[i],m[i])==1 for i in range(20))
safe=[]
for i,j in combinations(range(20),2):
    e=[dot(add(m[i],z[i],s),add(m[j],z[j],t))
       for s,t in product((1,-1),repeat=2)]
    if all(abs(q)<=half for q in e): safe.append((i,j))
assert len(safe)==160
H=sum(((half-abs(dot(z[i],z[j])))**2 for i,j in safe),Q(0))
M2=sum((dot(m[i],m[j])**2 for i,j in safe),Q(0))
XY=sum((dot(m[i],z[j])**2+dot(m[j],z[i])**2 for i,j in safe),Q(0))
assert M2<=H and XY<=2*H

F=frame(z); T=frame(m)
A=sum((dot(q,q) for q in m),Q(0))
V=norm2([[F[i][j]-(Q(20)-A)/5*(i==j) for j in range(5)] for i in range(5)])
W=norm2([[F[i][j]+T[i][j]-4*(i==j) for j in range(5)] for i in range(5)])
U=traceprod(T,T)
assert traceprod(T,F)==4*A-A*A/10+W/2-V/2-U/2
O=range(16); C=range(16,20)
F_O=frame([z[i] for i in O]); F_C=frame([z[i] for i in C])
T_O=frame([m[i] for i in O]); T_C=frame([m[i] for i in C])
S=sum((dot(m[i],z[j])**2+dot(m[j],z[i])**2
       for i,j in combinations(range(20),2) if i<16 or j<16),Q(0))
assert S==traceprod(T_O,F)+traceprod(T_C,F_O)
assert traceprod(T,F)==S+traceprod(T_C,F_C)

L=P=Q(0)
for i,j in combinations(range(20),2):
    r=abs(dot(z[i],z[j]))
    if r<=half: L+=Q(1,4)-r*r
    else: P+=r*r-Q(1,4)
a=[dot(q,q) for q in m]
assert L+V/2==Q(35,2)+3*A+sum((q*q for q in a),Q(0))/2-A*A/10+P
print("PASS: exact rational two-sided grid, 20-vector frame and defect identities")
