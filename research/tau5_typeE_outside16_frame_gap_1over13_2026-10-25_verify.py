#!/usr/bin/env python3
"""Exact rational verification for the outside-16 frame gap > 1/13."""
from fractions import Fraction as Q

A=Q(383,504)
delta=Q(1,13)
a=[Q(1,4)]*3+[A-Q(3,4)]+[Q(0)]*12
assert len(a)==16 and sum(a)==A and a[3]==Q(5,504)

def g(d,e):
    u,v=1-d,1-e
    return (1-u*v)/(16*u*u*v*v)

def G(d):
    return sum(g(d[i],d[j]) for i in range(16) for j in range(i+1,16))

G0=G(a)
assert G0==Q(9105610,6723027)

def secant(i):
    d=a.copy()
    d[i]+=delta
    return (G(d)-G0)/delta

secants=[secant(i) for i in (0,3,4)]
assert secants==[Q(13569181756,3529589175),
                 Q(12624681311424,8913311757289),
                 Q(2347319377,1721094912)]
c_up=[Q(385,100),Q(142,100),Q(137,100)]
assert all(x<y for x,y in zip(secants,c_up))

def K(ai,aj):
    ci,cj=1-ai,1-aj
    D=ci*cj-delta*max(ci,cj)
    assert D>0
    h=(1+delta)/2
    return 4*h**3/D**2-h/(2*D)

pairs={(0,0):K(a[0],a[0]),(0,1):K(a[0],a[3]),
       (0,2):K(a[0],a[4]),(1,2):K(a[3],a[4]),
       (2,2):K(a[4],a[4])}
assert pairs=={(0,0):Q(5608,2925),
               (0,1):Q(81104688,80925325),
               (0,2):Q(318,325),
               (1,2):Q(211307796,465351757),
               (2,2):Q(413,936)}
K_up={(0,0):Q(192,100),(0,1):Q(101,100),
      (0,2):Q(98,100),(1,2):Q(46,100),
      (2,2):Q(45,100)}
assert all(pairs[k]<K_up[k] for k in pairs)

n=(3,1,12)
L=Q(83,10)
B=[[c_up[i]+(n[i]-1)*K_up.get((i,i),Q(0))/2 if i==j
    else n[j]*K_up[tuple(sorted((i,j)))]/2
    for j in range(3)] for i in range(3)]
M=[[n[i]*((L if i==j else Q(0))-B[i][j])
    for j in range(3)] for i in range(3)]
assert M==[[Q(759,100),-Q(303,200),-Q(441,25)],
           [-Q(303,200),Q(172,25),-Q(69,25)],
           [-Q(441,25),-Q(69,25),Q(2673,50)]]

def det2(X):
    return X[0][0]*X[1][1]-X[0][1]*X[1][0]

def det3(X):
    return (X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])
            -X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])
            +X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0]))

minors=(M[0][0],det2(M),det3(M))
assert minors==(Q(759,100),Q(1996959,40000),
                Q(645502959,2000000))
assert all(x>0 for x in minors)
assert c_up[0]-K_up[(0,0)]/2==Q(289,100)<L
assert c_up[2]-K_up[(2,2)]/2==Q(229,200)<L

for s in [Q(-1),Q(-1,2),Q(0),Q(1,3),Q(1,2),Q(1)]:
    assert s**4-s*s/4 == (Q(1,16)+Q(1,8)*(4*s*s-1)
                         +Q(1,16)*(16*s**4-12*s*s+1))
assert (16**2*Q(1,16)-16*Q(3,4))/2==2
margin=2-G0-L*delta
assert margin==Q(6246479,873993510)>0
print("PASS: exact 4D polynomial, secants, pair coefficients, 3-class PSD minors")
print("PASS: contradiction margin",margin,"=",float(margin))
print("THEOREM: F_O > I/13; Type-E conditional corollary H_184 >= A/26")
