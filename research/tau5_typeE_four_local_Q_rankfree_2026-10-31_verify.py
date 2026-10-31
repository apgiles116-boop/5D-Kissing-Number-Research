#!/usr/bin/env python3
"""Exact rational checks for four-local Type-E Q identities. Requires sympy."""
from itertools import combinations
from sympy import Matrix, Rational as F, eye, zeros, sqrt

e=[Matrix([int(i==j) for i in range(5)]) for j in range(5)]
I=eye(5)
labels=[(i,j,s) for i in range(5) for j in range(i+1,5) for s in (1,-1)]
core=[(0,j,1) for j in range(1,5)]
iso=[p for p in labels if p not in core]
tr=lambda A,B:(A*B).trace()
norm=lambda A:tr(A,A)
ref={p:(e[p[0]]+p[2]*e[p[1]])*(e[p[0]]+p[2]*e[p[1]]).T/2 for p in labels}

def run(kind):
    P={}; a={}; Q={}
    for k,p in enumerate(labels):
        if kind=="D5":
            P[p]=ref[p]; a[p]=F(0)
        else:
            if kind=="rank1":
                u=e[0]
            else:
                t=[F((k+2*j)%7-3,7+j) for j in range(4)]
                s=sum(x*x for x in t)
                u=Matrix([(1-s)/(1+s)]+[2*x/(1+s) for x in t])
                assert (u.T*u)[0]==1
            P[p]=u*u.T; a[p]=F(k%5,80)
        Q[p]=(1-a[p])*(P[p]-I/5)
    W={}; L={}; R={}; b={}
    for j in range(1,5):
        W[j]={(0,j,1):F(1),(0,j,-1):F(1)}
        for k,l in combinations(range(1,5),2):
            if j not in (k,l):
                for s in (1,-1): W[j][(k,l,s)]=F(1,2)
        assert len(W[j])==8
        L[j]=sum((v*Q[p] for p,v in W[j].items() if p!=(0,j,1)),zeros(5))
        R[j]=Q[(0,j,1)]+L[j]
        b[j]=sum(v*a[p] for p,v in W[j].items())
    Z=sum((Q[p] for p in labels),zeros(5))
    assert sum(R.values(),zeros(5))==Z
    V=norm(Z); rho2=sum(norm(t) for t in R.values())
    diff=sum(norm(R[j]-R[k]) for j,k in combinations(R,2))
    assert rho2==V/4+diff/4
    H=sum(c*d*(1-a[p])*(1-a[q])*tr(P[p],P[q])
          for j in W for (p,c),(q,d) in combinations(W[j].items(),2))
    eta={p:sum(W[j].get(p,F(0))**2 for j in W) for p in labels}
    A=sum(a.values())
    Ak=sum(a[p] for p in iso if p[0]!=0)
    Ueta=sum(eta[p]*a[p]**2 for p in labels)
    assert sum(b.values())==A
    assert H==3-Ak/2-Ueta/2+sum(t*t for t in b.values())/10+rho2/2
    for c,d in combinations(core,2):
        j,k=c[1],d[1]
        actual=(1-a[c])*(1-a[d])*tr(P[c],P[d])
        pred=(1-a[c])*(1-a[d])/5+tr(L[j],L[k])
        assert actual-pred==-tr(R[j],L[k])-tr(L[j],R[k])+tr(R[j],R[k])
    for p in iso:
        e2=norm(P[p]-ref[p])
        q0=ref[p]-I/5
        assert norm(Q[p]-q0)==(1-a[p])*e2+F(4,5)*a[p]**2
    if kind=="D5": assert V==0 and H==3 and rho2==0
    print(kind,"PASS")
for mode in ("D5","generic","rank1"): run(mode)
V0=F(47602076041,317520000000)
V1=F(14814801,80000000)
assert 3-F(383,4032)-F(3,2000)-F(1,125000)+V0/8==F(7422961514761,2540160000000)
assert 3-F(567,8000)-F(3,2000)-F(1,125000)+V1/8==F(1888489681,640000000)
assert (31-sqrt(481))/40>F(9,40)
assert F(9,40)-F(4,5*250**2)==F(140617,625000)
print("ALL EXACT CHECKS PASS")
