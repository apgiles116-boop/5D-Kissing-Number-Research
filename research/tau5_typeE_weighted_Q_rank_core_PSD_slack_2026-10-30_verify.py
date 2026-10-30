#!/usr/bin/env python3
"""Exact Fraction regression for the Type-E weighted-Q / negative-core Gram theorem.
The universal inequalities are proved analytically in the companion Markdown note.
"""
from fractions import Fraction as F
from itertools import combinations, product

B=F(383,504)
D=B/2+B*B
assert D==F(243205,254016)
assert F(9,10)**2<D<F(49,50)**2
assert F(27,448)==F(21,2*7*14)*F(3,4)**2
assert F(19,16)==F(18,16)+F(1,16)
assert F(106,1024)==F(11,32)**2+F(49,1024)-F(1,16)
assert F(11,32)==F(1,4)+F(3,4)*F(1,8)
assert F(27,224)*7-F(19,16)<0

# Sharp core positive scalar at a_i=a_j=1/4, c_ij=-1/4.
a=F(1,4);s=2*a;p=a*a;c=-a;w=(1-a)**2;d=F(1,2)-c
assert d*d-w/4==F(27,32)*s
assert d*d-w/4==(-c)+s/4+3*p/4

# Sign-balanced rank-one equality in the universal negative-Gram-square lemma.
q=[F(1,2),F(1,2),-F(1,2),-F(1,2)]
T=sum(t*t for t in q)
N=sum(max(-q[i]*q[j],F(0))**2 for i,j in combinations(range(4),2))
assert T==1 and N==T*T/4
for q in product(range(-2,3),repeat=4):
    if not any(q): continue
    T=sum(t*t for t in q)
    N=sum(max(-q[i]*q[j],0)**2 for i,j in combinations(range(4),2))
    assert 4*N<=T*T

# Four-core and twenty-edge combinatorial identities.
a=[F(1,4),F(1,5),F(1,6),F(1,7)]
AC=sum(a);UC=sum(t*t for t in a)
assert sum((a[i]+a[j])**2 for i,j in combinations(range(4),2))==2*UC+AC*AC
a=[F(i%5,40) for i in range(20)]
A=sum(a);U=sum(t*t for t in a)
assert sum((a[i]+a[j])**2 for i,j in combinations(range(20),2))==18*U+A*A

# Strict concavity endpoint and terminal rational comparisons.
g_upper=D/16-(B/2+F(11,32)*F(9,10))**2+F(21,64)*B-F(49,1024)*D
assert g_upper<0
base=F(27,448)*(7-F(7,4)*B)**2-(F(19,4)*B+B*B)/16-F(3,8)
T=base+D/16-(B/2+F(11,32)*F(49,50))**2+F(21,64)*B-F(49,1024)*D
assert T==F(21346842527,20321280000)
assert T-1==F(1025562527,20321280000)>0

# Exact weighted D5+center rank regression (not a Type-E feasibility example).
roots=[]
for i,j in combinations(range(5),2):
    for sg in (1,-1): roots.append((i,j,sg))
def dot_sq(r,t):
    x=[0]*5;y=[0]*5
    x[r[0]]=1;x[r[1]]=r[2]
    y[t[0]]=1;y[t[1]]=t[2]
    return F(sum(a*b for a,b in zip(x,y))**2,4)
ws=[F(3,4) if i<3 else F(1) for i in range(20)]+[F(1)]
Esq=F(0)
for i,j in combinations(range(21),2):
    d2=dot_sq(roots[i],roots[j]) if j<20 else (
        F(1,2) if 0 in roots[i][:2] else F(0))
    E=ws[i]*ws[j]*(d2-F(1,4))
    Esq+=E*E
assert Esq==F(20401,4096)
assert Esq>=F(27,448)*(7-2*F(3,4)+F(3,16))**2
print("Exact rational lower:",T)
print("Margin above 1:",T-1)
print("CONDITIONAL TYPE E: H204 > 1")
print("PASS")
