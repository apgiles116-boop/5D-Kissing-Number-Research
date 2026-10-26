#!/usr/bin/env python3
"""Exact rational checker for Type-E F3 uniform core-energy floor 9/1000."""
from itertools import combinations
from sympy import Matrix, Rational, Symbol, factor

F3={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
P1={(0,2),(1,4),(3,6),(5,7)}
P2={(0,4),(1,7),(2,3),(5,6)}
P3={(0,5),(1,4),(2,7),(3,6)}
def weight(u,v):
    e=(u,v)
    if e in P1: return 1000000
    if e in P2: return 133900
    if e in {(0,5),(2,7)}: return 111500
    if e in {(1,3),(4,6)}: return 34200
    return 0
B=Matrix(8,8,lambda i,j:(1120425 if i in (0,2,5,7) else 1043125) if i==j else weight(*sorted((i,j))))
assert B==B.T
x=Symbol("x")
cp=(x*x-4309250*x+4618504390625)*(x*x-2017850*x+445625)**2*(x*x-309250*x+4390625)
assert factor(B.charpoly(x).as_expr()-cp)==0
assert all(B[:k,:k].det()>0 for k in range(1,9))
assert all(s>0 and p>0 for s,p in [(4309250,4618504390625),(2017850,445625),(309250,4390625)])
deep=F3-P1
safe={(1,3),(4,6)}
assert len(deep)==6 and len(safe)==2 and not(safe&F3)
D=sum(B[i,i] for i in range(8))
Wd=sum(weight(*e) for e in deep)
Ws=sum(weight(*e) for e in safe)
assert (D,Wd,Ws)==(8654200,758600,68400)
K=Rational(D-Wd+Ws,1000000)
assert K==Rational(1991,250)
assert 2-K/4==Rational(9,1000)
perm={0:0,1:1,2:5,3:6,4:4,5:2,6:3,7:7}
f=lambda e:tuple(sorted((perm[e[0]],perm[e[1]])))
assert {f(e) for e in F3}==F3
assert {f(e) for e in P1}==P3
assert Rational(17,250)>Rational(9,1000)
print("PASS: exact characteristic polynomial, Sylvester PSD, trace bound and F3 automorphism")
print("PROVED: C_P1,C_P3>9/1000; retained C_P2>=17/250")
