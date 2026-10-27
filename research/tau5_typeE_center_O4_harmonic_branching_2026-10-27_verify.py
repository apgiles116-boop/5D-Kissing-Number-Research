#!/usr/bin/env python3
"""Exact SymPy verification of the Type-E center-adapted O(4) H4 decomposition."""
from itertools import combinations
import sympy as S

c,d,q,r,s=S.symbols("c d q r s")
R=c*c+q; U=d*d+r
H=(c*d+s)**4-S.Rational(2,3)*R*U*(c*d+s)**2+R**2*U**2/21
h=lambda a,b:(8*a**4-12*a*a*b+b*b)/21
K0=S.Rational(21,8)*h(c,q)*h(d,r)
K1=S.Rational(2,3)*c*d*(2*c*c-q)*(2*d*d-r)*s
K2=S.Rational(1,12)*(8*c*c-q)*(8*d*d-r)*(s*s-q*r/4)
K3=4*c*d*(s**3-q*r*s/2)
K4=s**4-S.Rational(3,4)*q*r*s*s+q*q*r*r/16
assert S.expand(H-K0-K1-K2-K3-K4)==0

# Second tangential trace-free Hessian norm, x=e1, A=diag(1,-1)/sqrt(2).
u1,u2,v1,v2=S.symbols("u1 u2 v1 v2")
xy=1+u1*v1+u2*v2
nx=1+u1*u1+u2*u2; ny=1+v1*v1+v2*v2
ker=xy**4-S.Rational(2,3)*nx*ny*xy**2+nx**2*ny**2/21
Du=lambda f:(S.diff(f,u1,2)-S.diff(f,u2,2))/S.sqrt(2)
Dv=lambda f:(S.diff(f,v1,2)-S.diff(f,v2,2))/S.sqrt(2)
assert S.simplify(Dv(Du(ker)).subs({u1:0,u2:0,v1:0,v2:0}))==S.Rational(64,3)

roots=[]
for i,j in combinations(range(5),2):
    for sg in (1,-1):
        v=S.zeros(5,1); v[i]=1/S.sqrt(2); v[j]=sg/S.sqrt(2)
        roots.append(v)
assert len(roots)==20
x=S.Matrix([1,0,0,0,0])
cs=[x.dot(v) for v in roots]
ws=[v-cs[i]*x for i,v in enumerate(roots)]
qs=[S.simplify(w.dot(w)) for w in ws]
hsum=S.simplify(sum(h(cs[i],qs[i]) for i in range(20)))
L=sum((cs[i]*(2*cs[i]**2-qs[i])*ws[i] for i in range(20)),S.zeros(5,1))
Bsq=T3sq=T4sq=S.S(0)
for i in range(20):
    for j in range(20):
        t=S.simplify(ws[i].dot(ws[j])); qi,qj=qs[i],qs[j]
        Bsq+=(8*cs[i]**2-qi)*(8*cs[j]**2-qj)*(t*t-qi*qj/4)
        T3sq+=cs[i]*cs[j]*(t**3-qi*qj*t/2)
        T4sq+=t**4-S.Rational(3,4)*qi*qj*t*t+qi*qi*qj*qj/16
Bsq,T3sq,T4sq=map(S.simplify,(Bsq,T3sq,T4sq))
assert (hsum,S.simplify(L.dot(L)),Bsq,T3sq,T4sq)==(S.Rational(2,7),0,0,0,S.Rational(1,2))
K=S.Rational(21,8)*hsum**2+S.Rational(2,3)*L.dot(L)+Bsq/12+4*T3sq+T4sq
assert S.simplify(K)==S.Rational(5,7)
assert S.simplify(-S.Rational(5,14)+K/2)==0

# Independently check raw weighted harmonic identity on 20 rational vectors.
vs=[S.Matrix([S.Rational(((i+1)*(k+2))%11-5,7+k) for k in range(5)]) for i in range(20)]
rs=[S.simplify(v.dot(v)) for v in vs]
R2=sum(ri**2 for ri in rs); S4=sum(ri**4 for ri in rs)
F=sum((rs[i]*vs[i]*vs[i].T for i in range(20)),S.zeros(5))
W=S.trace((F-R2*S.eye(5)/5)**2)
D=Kh=S.S(0)
for i in range(20):
    for j in range(i+1,20):
        wij=vs[i].dot(vs[j])**2
        D+=wij*(wij-rs[i]*rs[j]/4)
    for j in range(20):
        cij=vs[i].dot(vs[j])
        Kh+=cij**4-S.Rational(2,3)*rs[i]*rs[j]*cij**2+rs[i]**2*rs[j]**2/21
assert S.simplify(D-(R2**2/56-S.Rational(3,8)*S4+S.Rational(5,24)*W+Kh/2))==0
print("PASS: exact O(4) branching, Hessian norm, D5 sector test, raw identity")
