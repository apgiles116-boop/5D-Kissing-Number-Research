#!/usr/bin/env python3
"""Exact rational verifier for the 16-vector frame gap >1/14."""
from fractions import Fraction as Q

A, delta = Q(383,504), Q(1,14)
a = [Q(1,4)]*3 + [Q(5,504)] + [Q(0)]*12
assert sum(a)==A and len(a)==16

def g(d,e):
    u,v=1-d,1-e
    return (1-u*v)/(16*u*u*v*v)

def G(x):
    return sum(g(x[i],x[j]) for i in range(16) for j in range(i+1,16))

G0=G(a)
assert G0==Q(9105610,6723027)

def slope(i):
    x=a.copy();x[i]+=delta
    return (G(x)-G0)/delta

slopes=[slope(i) for i in (0,3,4)]
assert slopes==[Q(27586331276,7281038241),
                Q(74735317440,53378095369),
                Q(226951305,168324676)]
cup=[Q(379,100),Q(141,100),Q(135,100)]
assert all(x<y for x,y in zip(slopes,cup))

def K(ai,aj):
    D=(1-ai-delta)*(1-aj-delta)
    h=(1+delta)/2
    return 4*h**3/D**2-h/(2*D)

actual={(0,0):K(a[0],a[0]), (0,1):K(a[0],a[3]),
        (0,2):K(a[0],a[4]), (1,2):K(a[3],a[4]),
        (2,2):K(a[4],a[4])}
kup={(0,0):Q(232,100), (0,1):Q(116,100),
     (0,2):Q(113,100), (1,2):Q(54,100),
     (2,2):Q(52,100)}
assert all(actual[k]<kup[k] for k in actual)

# Rational congruence certificate for 9I-B' on the group-constant subspace.
n=(3,1,12)
B=[[Q(0) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        if i==j:
            B[i][j]=cup[i]+(n[i]-1)*kup.get((i,i),Q(0))/2
        else:
            B[i][j]=n[j]*kup[tuple(sorted((i,j)))]/2
M=[[n[i]*((Q(9) if i==j else Q(0))-B[i][j])
    for j in range(3)] for i in range(3)]
assert M==[[Q(867,100),-Q(87,50),-Q(1017,50)],
           [-Q(87,50),Q(759,100),-Q(81,25)],
           [-Q(1017,50),-Q(81,25),Q(1437,25)]]
d1=M[0][0]
d2=M[0][0]*M[1][1]-M[0][1]*M[1][0]
d3=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
    -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
    +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert (d1,d2,d3)==(Q(867,100),Q(627777,10000),Q(18501129,125000))
assert all(d>0 for d in (d1,d2,d3))
assert cup[0]-kup[(0,0)]/2<9 and cup[2]-kup[(2,2)]/2<9

# Gegenbauer identity f=(1/16)C0+(1/8)C2+(1/16)C4 on S^3.
for s in [Q(-1),Q(-1,2),Q(0),Q(1,3),Q(1,2),Q(1)]:
    assert s**4-s*s/4==Q(1,16)+Q(1,8)*(4*s*s-1)+Q(1,16)*(16*s**4-12*s*s+1)
assert (16**2*Q(1,16)-16*Q(3,4))/2==2
margin=2-G0-Q(9,14)
assert margin==Q(258973,94122378)>0
print("PASS: exact rational 1/14 frame-gap certificate; margin",margin)
print("Conditional Type-E consequence: H_184>=A/28")
