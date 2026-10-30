#!/usr/bin/env python3
"""Exact SymPy regression for Type-E inverse Q-kernel rounding note.
Universal inequalities are proved in the companion markdown, not by finite tests.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, eye, zeros, sqrt, simplify

assert 80 < 81
assert 3*16 < 49
assert 77**2 + 232**2 == 59753 < 245**2
assert 245*3250 == 796250
assert F(1, 796250**2)>0

N=5
I=eye(N)
edges=list(combinations(range(N),2))

def roots():
    out=[]
    for p,q in edges:
        a=zeros(N,1); b=zeros(N,1)
        a[p]=1/sqrt(2); a[q]=1/sqrt(2)
        b[p]=1/sqrt(2); b[q]=-1/sqrt(2)
        out.extend((a,b))
    return out

def fro2(M):
    return simplify(sum(x*x for x in M))

def check(us):
    S=[]
    for j in range(10):
        u,v=us[2*j:2*j+2]
        S.append(u*u.T+v*v.T)
    FF=sum(S,zeros(N,N))
    Bs=[]
    for p in range(N):
        B=sum((S[j] for j,(a,b) in enumerate(edges) if p in (a,b)),zeros(N,N))/3-F(2,15)*FF+I/5
        Bs.append(B)
    assert sum(Bs,zeros(N,N))==I
    assert all(simplify(B.trace()-1)==0 for B in Bs)
    E=[S[j]-Bs[p]-Bs[q] for j,(p,q) in enumerate(edges)]
    residual=simplify(sum(fro2(e) for e in E))
    V=fro2(FF-4*I)
    Q=[u*u.T-I/5 for u in us]
    K=Matrix(20,20,lambda i,j:simplify((Q[i]*Q[j]).trace()))
    K0=check.K0
    P0=eye(20)-F(5,3)*K0+F(2,3)*(K0*K0)
    Pc=P0-Matrix.ones(20,20)/20
    C=simplify((Pc*K).trace())
    assert simplify(residual-2*C-V/10)==0
    O=simplify(sum((us[2*j].dot(us[2*j+1]))**2 for j in range(10)))
    defect=simplify(sum(fro2(B*B-B) for B in Bs))
    assert O>=0 and C>=0 and V>=0 and defect>=0
    return O,C,V,residual,defect

u0=roots()
check.K0=Matrix(20,20,lambda i,j:simplify(((u0[i]*u0[i].T-I/5)*(u0[j]*u0[j].T-I/5)).trace()))
assert check(u0)==(0,0,0,0,0)
u1=roots()
u,v=u1[:2]
u1[0]=F(3,5)*u+F(4,5)*v
u1[1]=-F(4,5)*u+F(3,5)*v
assert check(u1)==(0,0,0,0,0)
u2=roots()
u2[0]=F(3,5)*u2[0]+F(4,5)*Matrix([0,0,1,0,0])
O,C,V,rho2,defect=check(u2)
assert rho2>0 and defect>0
print("PASS: K5 reconstruction, normalized Q residual identity, rational constants")
print("PASS: exact D5, ten-angle soft mode, and non-fibre rational perturbation")
print("Non-fibre O,C,V:",O,C,V)
