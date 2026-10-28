#!/usr/bin/env python3
"""Exact SymPy regression for the Type-E core orthogonality penalty.
Analytic endpoint/PSD implications are proved in the companion Markdown note.
"""
import sympy as S

x=S.symbols("x",real=True)
D=lambda t:t+t*t
f=lambda t:(S.Rational(1,2)+t)**2*D(t)
h=lambda t:f(t)+S.Rational(7,64)*D(t)
pen=lambda t:(S.Rational(1,2)+t)**2*t*t/(2*(1-t))
F=lambda t:S.cancel(h(t)-pen(t))

assert S.factor(F(x)-x*(64*x**4+96*x**3-9*x**2-56*x-23)/(64*(x-1)))==0
assert F(S.Rational(1,4))==S.Rational(191,1024)
assert 2*F(S.Rational(1,8))==S.Rational(479,3584)
assert F(S.Rational(3,16))+F(S.Rational(1,8))==S.Rational(1110407,5963776)
assert F(S.Rational(3,16))+F(S.Rational(1,8))<F(S.Rational(1,4))
N=384*x**5-672*x**4-137*x**3+603*x**2-27*x-79
assert S.factor(S.diff(F(x),x,2)-N/(32*(x-1)**3))==0
assert S.Rational(384,1024)+S.Rational(603,16)<79
assert S.diff(F(x),x).subs(x,0)==S.Rational(23,64)
alpha=S.cancel(6*F(S.Rational(1,6)))
beta=S.cancel(8*F(S.Rational(1,8)))
assert alpha==S.Rational(10397,17280)
assert beta==S.Rational(479,896)
assert beta-alpha/2==S.Rational(56551,241920)>0
assert alpha*S.Rational(1,16)+beta*S.Rational(1,4)==S.Rational(331439,1935360)<F(S.Rational(1,4))

# Rational 20-edge test of the retained frame/mixing identity and new J3 floor.
I=S.eye(5); z=[]; m=[]
for i in range(20):
    p=i%5; q=(2*i+1)%5
    if p==q:q=(q+1)%5
    if i%4==0:
        m.append(S.zeros(5,1));z.append(I[:,q])
    else:
        m.append(S.Rational(5,13)*I[:,p]);z.append(S.Rational(12,13)*I[:,q])
a=[(v.T*v)[0] for v in m]
r=[(v.T*v)[0] for v in z]
assert all(a[i]+r[i]==1 and (m[i].T*z[i])[0]==0 for i in range(20))
assert all(t<=S.Rational(1,4) for t in a)
U=sum(t*t for t in a); Uc=sum(a[i]**2 for i in range(4))
R2=sum(t*t for t in r)
Fz=sum((v*v.T for v in z),S.zeros(5))
Fw=sum((r[i]*z[i]*z[i].T for i in range(20)),S.zeros(5))
B=sum((a[i]*m[i]*m[i].T for i in range(20)),S.zeros(5))
E=Fw-R2*S.eye(5)/5;B0=B-U*S.eye(5)/5
K={(i,j) for i in range(4) for j in range(i+1,4)}
R=[(i,j) for i in range(20) for j in range(i+1,20) if (i,j) not in K]
def X(i,j):return (m[i].T*z[j])[0]
def Y(i,j):return (z[i].T*m[j])[0]
def hij(i,j):return 1-r[i]*r[j]
TR=sum(hij(i,j)*(X(i,j)**2+Y(i,j)**2) for i,j in R)
J1=sum((hij(i,j)-a[i])*X(i,j)**2+(hij(i,j)-a[j])*Y(i,j)**2 for i,j in R)
J2=S.trace(B*(Fz-Fw))
J3=3*Uc-sum(a[i]*X(i,j)**2+a[j]*Y(i,j)**2 for i,j in K)
left=S.Rational(5,24)*S.trace(E*E)+TR/4
right=(U*R2/20-S.Rational(3,4)*Uc-S.Rational(3,40)*S.trace(B0*B0)
       +S.Rational(5,24)*S.trace((E+S.Rational(3,5)*B0)**2)+(J1+J2+J3)/4)
assert S.simplify(left-right)==0
J3floor=sum(a[i]**2*sum(a[j]+(z[i].dot(z[j]))**2/r[i]
            for j in range(4) if j!=i) for i in range(4))
assert J3>=J3floor>=0
print("PASS: exact frame identity, J3 orthogonality floor, convexity and branch caps")
print("P1/P3:",F(S.Rational(1,4)),"P2:",2*F(S.Rational(1,8)))
