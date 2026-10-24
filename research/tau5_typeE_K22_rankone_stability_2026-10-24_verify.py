#!/usr/bin/env python3
"""Exact symbolic/rational checks, not a Type-E feasibility solver."""
import sympy as s
v1,v2,w1,w2,h1,h2,k1,k2=s.symbols('v1 v2 w1 w2 h1 h2 k1 k2')
v=s.Matrix([v1,v2]);w=s.Matrix([w1,w2])
h=s.Matrix([h1,h2]);k=s.Matrix([k1,k2])
dot=lambda a,b:(a.T*b)[0]
m=[v+w+h,v+w-h,-v+w+k,-v+w-k]
sig=s.Matrix([1,1,-1,-1]);M=s.Matrix.hstack(*m)
C=sum(dot(x,x) for x in m)
D=-sum(dot(m[i],m[j]) for i in (0,1) for j in (2,3))
e=s.expand(C-D)
T=sum(dot(m[i]-sig[i]*v,m[i]-sig[i]*v) for i in range(4))
P=dot(m[0],m[1])+dot(m[2],m[3])
assert all(s.expand(z)==0 for z in [
 C-(4*dot(v,v)+4*dot(w,w)+2*dot(h,h)+2*dot(k,k)),
 D-4*(dot(v,v)-dot(w,w)),
 e-(8*dot(w,w)+2*dot(h,h)+2*dot(k,k)),
 T-(e-4*dot(w,w)),
 P-(D-C/2+8*dot(w,w))])
X=M.T*M;X0=dot(v,v)*sig*sig.T
P0=sig*sig.T/4;E=M*(s.eye(4)-P0);M0=M*P0
fro=lambda Y:s.trace(Y.T*Y)
assert s.expand(fro(X-X0)-2*fro(M0.T*E)-fro(E.T*E))==0
assert s.expand(fro(E)-T)==0
r=s.Rational;V=r(1,5);H=r(1,25)
a=[s.Matrix([V+H]),s.Matrix([V-H]),s.Matrix([-V]),s.Matrix([-V])]
A=s.Matrix.hstack(*a)
c=sum(dot(x,x) for x in a)
d=-sum(dot(a[i],a[j]) for i in (0,1) for j in (2,3))
assert fro(A.T*A-V**2*sig*sig.T)==2*c*(c-d)-(c-d)**2
b=[s.Matrix([V+H]),s.Matrix([V-H]),s.Matrix([-V+H]),s.Matrix([-V-H])]
c=sum(dot(x,x) for x in b)
z=[-dot(b[i],b[j]) for i in (0,1) for j in (2,3)]
d=sum(z)
assert all(x>0 for x in z)
assert sum((x-d/4)**2 for x in z)==(c*c-d*d)/4
print('PASS: exact SOS and orthogonal Gram decomposition')
print('PASS: sharp rational equality witnesses for both Gram inequalities')
print('NOTE: aligned-normal bound follows by Cauchy-Schwarz and T<=epsilon')
