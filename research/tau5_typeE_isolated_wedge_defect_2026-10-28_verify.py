#!/usr/bin/env python3
"""Exact SymPy regression for Type-E isolated/wedge SOS and core defect caps."""
import sympy as S
from itertools import product
Q=S.Rational
d=S.symbols("d", nonnegative=True)
f=(Q(1,2)+d)**2*(d+d*d)
g=d+d*d
w=(Q(1,2)+d)**2
Fsep=S.factor(f+g*g/(8*w)-d**3/2)
Fdiag=S.factor(f+Q(7,64)*g-w*d*d/(2*(1-d))-d**3/2)
assert S.simplify(Fsep-d*(16*d**5+40*d**4+50*d**3+34*d*d+11*d+1)/(4*(2*d+1)**2))==0
assert S.factor(S.diff(Fsep,d,2))==(384*d**6+1056*d**5+1240*d**4+800*d**3+300*d**2+62*d+7)/(2*(2*d+1)**4)
assert S.factor(S.diff(Fdiag,d,2))==(384*d**5-768*d**4+151*d**3+315*d*d+69*d-79)/(32*(d-1)**3)
assert 2*Fsep.subs(d,Q(1,8))==Q(6173,51200)
assert Fdiag.subs(d,Q(1,4))==Q(183,1024)

alpha1=Q(16,3)*Fdiag.subs(d,Q(3,16))
beta=8*Fsep.subs(d,Q(1,8))
p1=S.expand(alpha1*(Q(3,16)-d/2-d*d)+beta*d)
assert S.diff(p1,d).subs(d,Q(1,8))>0
assert p1.subs(d,Q(1,8))==Q(10904461,85196800)<Q(183,1024)
alpha2=6*Fdiag.subs(d,Q(1,6))
p2=S.expand(alpha2*(Q(1,6)-d/3-d*d/3)+beta*d)
assert S.diff(p2,d).subs(d,Q(1,4))>0
assert p2.subs(d,Q(1,4))==Q(13591,86400)<Q(183,1024)

for a,b,t in product([Q(1,16),Q(1,8),Q(1,4)],repeat=3):
    if a*b<t*t: continue
    ff=f.subs(d,t);gg=g.subs(d,t);ww=w.subs(d,t)
    local=ff+(a+b-a*b)*gg/4-(a*b*(a+b)+ww*(a*a/(1-a)+b*b/(1-b)))/4
    assert local<=Fsep.subs(d,t)
    assert local<=Fdiag.subs(d,t)

# Exact 20-edge algebra test with rational orthogonal midpoint/projection pairs.
N=20; DIM=5
e=[S.eye(DIM)[:,i] for i in range(DIM)]
triples=[(Q(0),Q(1)),(Q(5,13),Q(12,13)),(Q(8,17),Q(15,17)),(Q(7,25),Q(24,25))]
m=[];z=[]
for i in range(N):
    t,u=triples[(3*i+1)%4]
    m.append(t*e[(2*i+1)%DIM]);z.append(u*e[(2*i+2)%DIM])
    assert m[-1].dot(z[-1])==0
    assert m[-1].dot(m[-1])+z[-1].dot(z[-1])==1
a=[v.dot(v) for v in m];r=[v.dot(v) for v in z]
A=sum(a);U=sum(v*v for v in a);UC=sum(a[i]**2 for i in range(16,20));UI=U-UC
R2=sum(t*t for t in r)
Fz=S.zeros(DIM);Fw=S.zeros(DIM);B=S.zeros(DIM)
for i in range(N):
    Fz+=z[i]*z[i].T
    Fw+=r[i]*z[i]*z[i].T
    B+=a[i]*m[i]*m[i].T
E=Fw-R2*S.eye(DIM)/DIM
B0=B-U*S.eye(DIM)/DIM
W=S.trace(E*E)
TR=Q(0);J1=Q(0);J3=3*UC
for i in range(N):
 for j in range(i+1,N):
    X=m[i].dot(z[j]);Y=z[i].dot(m[j]);h=1-r[i]*r[j]
    if i>=16 and j>=16:
       J3-=a[i]*X*X+a[j]*Y*Y
    else:
       TR+=h*(X*X+Y*Y)
       J1+=(h-a[i])*X*X+(h-a[j])*Y*Y
J2=S.trace(B*(Fz-Fw))
Omega=U*U-S.trace(B*B)
square=S.trace((E+Q(3,5)*B0)*(E+Q(3,5)*B0))
lhs=Q(5,24)*W+TR/4
rhs=U*(Q(1,4)-A/10-U/100)+Q(3,4)*UI+Q(3,40)*Omega+Q(5,24)*square+(J1+J2+J3)/4
assert S.simplify(lhs-rhs)==0
assert all(v>=0 for v in [UI,Omega,square,J1,J2,J3])
J3core=Q(0)
for i in range(16,20):
 for j in range(i+1,20):
    wij=z[i].dot(z[j])**2
    J3core+=a[i]*a[j]*(a[i]+a[j])+wij*(a[i]**2/r[i]+a[j]**2/r[j])
assert J3>=J3core

# Rational isolation of scalar mass-deficit inverse roots.
x=S.symbols("x")
D=196*x-644*x*x+896*x**3-448*x**4
root=(1-S.sqrt((7+S.sqrt(721))/56))/2
assert S.simplify(D.subs(x,root)-15)==0
for target,lo,hi in [
 (S.Integer(15),Q(111255,10**6),Q(111256,10**6)),
 (Q(43,3),Q(103544,10**6),Q(103545,10**6)),
 (Q(41,6),Q(39781,10**6),Q(39782,10**6))]:
    assert D.subs(x,lo)<target<D.subs(x,hi)
print("PASS: exact rational caps, convexity, 20-edge SOS, wedge, J3core, and root brackets")
print("P1/P3:",Q(183,1024),"P2:",Q(6173,51200))
