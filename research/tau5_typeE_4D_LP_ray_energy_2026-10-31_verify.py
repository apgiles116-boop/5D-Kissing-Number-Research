#!/usr/bin/env python3
"""Exact rational verification for Type-E 4D harmonic LP ray-energy theorem.
Analytic positivity of dimension-four Gegenbauer kernels is used in the proof.
"""
from fractions import Fraction as F
from itertools import combinations

# f(t)=t^4-t^2/4=1/16+U2(t)/8+U4(t)/16
# U2=4t^2-1, U4=16t^4-12t^2+1.
assert F(1,16)-F(1,8)+F(1,16)==0
assert F(4,8)-F(12,16)==-F(1,4)
assert F(16,16)==1

tiers=[
    (F(1,8), F(1,12), F(10399806,5603803)),
    (F(3,20), F(1,16), F(1406739590,750891141)),
    (F(1,5), F(1,50), F(119537125,63352692)),
    (F(9,40), F(1,400), F(4287685855250,2154561514983)),
]
for a0,x0,expected in tiers:
    beta=1-a0-x0
    B=(F(1,2)+(a0+x0)/2)/beta
    assert F(1,2)<B<1
    slope=B*B*(B+F(1,2))
    q=F(15,2)/(1+beta)
    upper=slope/beta*((4+q)*a0+(F(15,2)+q)*x0)
    assert upper==expected and upper<2
    print("PASS",a0,x0,"LP upper",upper)

# D4 roots, 12 projective lines, saturate 4D LP bound.
d4=[]
for i,j in combinations(range(4),2):
    for sign in (1,-1):
        v=[0]*4; v[i]=1; v[j]=sign; d4.append(tuple(v))
assert len(d4)==12
f=lambda t2:t2*t2-t2/F(4)
assert sum((f(F(sum(a*b for a,b in zip(v,w))**2,4))
            for v,w in combinations(d4,2)),F(0))==0

# Sixteen D5 roots: safe in 5D and exact 4D projection LP test.
roots=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5; v[i]=1; v[j]=sign; roots.append(tuple(v))
roots=roots[:16]
for v,w in combinations(roots,2):
    assert abs(sum(a*b for a,b in zip(v,w)))<=1
y=[v[1:] for v in roots]
norms=[sum(a*a for a in v) for v in y]
assert min(norms)>0
lp=F(0)
for i,j in combinations(range(16),2):
    dot=sum(y[i][k]*y[j][k] for k in range(4))
    lp+=f(F(dot*dot,norms[i]*norms[j]))
assert lp==7 and lp>=2
assert sum(F(v[0]*v[0],2) for v in roots)==4

# Rank-13 small-A_I two-ray gap (from prior exact wedge/minor theorem).
x0=F(1,12)
assert F(81,131072)*x0**4==F(1,33554432)
assert x0**2/F(128)==F(1,18432)
print("PASS: D4 equality, D5 projection, and absolute minor gap")
