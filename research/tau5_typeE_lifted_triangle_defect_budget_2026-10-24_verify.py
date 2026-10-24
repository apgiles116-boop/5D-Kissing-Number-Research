#!/usr/bin/env python3
"""Exact rational checker for the lifted-triangle Type-E six-defect certificate."""
from fractions import Fraction as F
from itertools import combinations

B=F(383,504)
D=F(1780062775,4032758016)
L=F(8790283,317520)
b=B/2
r=D-b
T=F(122237,500000)
Q=F(819,10000)
K=L-F(3,2)-D-Q

def P(t,c):
    return t+c+4*(t*t+c*c-t*c)-F(1,2)

def Fcase(t):
    return t*t+(b-t)**2+r*r

# Exact algebra for the lifted triangle weighted Cauchy argument.
for p,q in [(F(1,2),F(1,2)),(F(3,4),F(2,3)),(F(1),F(1,2))]:
    lam,mu=2*p-q,2*q-p
    f=p*p+q*q-p*q
    assert lam>=0 and mu>=0
    assert lam*p+mu*q==2*f
    assert lam*lam+lam*mu+mu*mu==3*f

# All rational comparisons needed for the four-case global certificate.
assert 0<D/3<b/2<T<F(1,4)
assert 0<r<F(1,16)
assert D+F(1,4)<B
assert D*D/3<Q
assert b*b/2+r*r<Q
assert Fcase(T)<Q
assert 4*D>1+B
assert D-T<F(1,5)
assert P(T,r)>0
assert 8*T-12*F(1,16)>1
assert F(3,40)<Q
assert K==F(64677589778681,2520473760000)

# Exact scalar-relaxation witness, NOT a physical kissing configuration.
edges=list(combinations(range(4),2))
tw=F(244473,1000000)
witness={(0,1):tw,(2,3):b-tw,(0,2):r}
x=[witness.get(e,F(0)) for e in edges]
assert sum(x)==D and all(F(0)<=a<=F(1,4) for a in x)
for i,j in combinations(range(6),2):
    if set(edges[i])&set(edges[j]):
        assert P(x[i],x[j])<=0
    assert x[i]+x[j]<=b
Qw=sum(a*a for a in x)
assert Qw<Q and Q-Qw<F(2,1000000)

print("PASS: all exact rational inequalities")
print("D0:",D,float(D))
print("P(T,r):",P(T,r),float(P(T,r)))
print("F(T):",Fcase(T),float(Fcase(T)))
print("Witness sum(delta^2):",Qw,float(Qw))
print("Certified sum(delta^2) <",Q,float(Q))
print("Certified safe squared-correlation mass >",K,float(K))
