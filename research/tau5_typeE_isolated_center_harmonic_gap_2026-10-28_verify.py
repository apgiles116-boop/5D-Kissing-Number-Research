#!/usr/bin/env python3
"""Exact SymPy regression for the 2026-10-28 isolated-center harmonic gap.

Analytic proofs of PSD and capped-simplex steps are in the companion .md.
"""
import sympy as S

t=S.symbols("t",real=True)
q=S.symbols("q",real=True)
F=lambda v:28*v**4-7*v**2
H2=lambda v:v**2-S.Rational(1,5)
H4=lambda v:v**4-S.Rational(2,3)*v**2+S.Rational(1,21)
D=lambda v:196*v-644*v**2+896*v**3-448*v**4

assert S.expand(F(t)-1-S.Rational(35,3)*H2(t)-28*H4(t))==0
assert H4(1)==S.Rational(8,21)

B=S.Rational(2595,256)
E=S.Rational(175,24)*q*q+S.Rational(147,4)*(S.Rational(5,7)+S.Rational(5,12)*q)**2
assert S.expand(E-10-S.Rational(35,64)*(5*q+4)**2)==0
assert S.Rational(175,24)*S.Rational(12,7)**2>B
v=S.symbols("v",nonnegative=True)
f=S.Rational(875,64)*v*v+S.Rational(7,2)*(S.Rational(1,10)-v)
assert S.diff(f,v).subs(v,S.Rational(1,10))<0
assert f.subs(v,S.Rational(1,10))==S.Rational(35,256)
assert 10+S.Rational(35,256)==B

# Test exact 41-vector harmonic identity with rational unit vectors.
vec=[]
for i in range(5):
    a=[S.Integer(0)]*5;a[i]=S.Integer(1);vec.append(S.Matrix(a))
for i in range(5):
    for j in range(i+1,5):
        for sign in (1,-1):
            a=[S.Integer(0)]*5
            a[i]=S.Rational(3,5);a[j]=sign*S.Rational(4,5)
            vec.append(S.Matrix(a))
vec += [-w for w in vec[:16]]
assert len(vec)==41 and all(w.dot(w)==1 for w in vec)
n=len(vec)
mat=sum((w*w.T for w in vec),S.zeros(5))
T=mat-S.Rational(n,5)*S.eye(5)
normT=S.trace(T*T)
K4=sum((H4(w.dot(z)) for w in vec for z in vec),S.Integer(0))
Fsum=sum((F(w.dot(z)) for w in vec for z in vec),S.Integer(0))
assert S.simplify(Fsum-n*n-S.Rational(35,3)*normT-28*K4)==0
assert K4>=0

def invD(c):
    return (1-S.sqrt((7+S.sqrt(2401-112*c))/56))/2
c=S.Rational(1245,256)
r=invD(c)
s1=invD(S.Rational(41,6))
s0=invD(S.Rational(43,3)-B/2)
for z,target in [(r,c),(s1,S.Rational(41,6)),(s0,S.Rational(43,3)-B/2)]:
    assert abs(float(S.N(D(z)-target,25)))<1e-20
assert D(S.Rational(27,1000))<c<D(S.Rational(28,1000))
assert D(S.Rational(39,1000))<S.Rational(41,6)<D(S.Rational(40,1000))
assert D(S.Rational(57,1000))<S.Rational(43,3)-B/2<D(S.Rational(58,1000))
assert S.Rational(27,1000)+S.Rational(39,1000)>S.Rational(58,1000)
assert S.Rational(28,1000)**2+S.Rational(40,1000)**2<S.Rational(57,1000)**2

Dp=lambda z:S.diff(D(t),t).subs(t,z)
assert Dp(S.Rational(58,1000))>129
assert (-3+S.Rational(57,500))*S.Rational(31,129)+S.Rational(58,1000)*S.Rational(98,129)<0

A=S.Rational(1,2)+r+s1
Useparate=S.Rational(1,8)+s0*s0
Ujoint=S.Rational(1,8)+r*r+s1*s1
L=30-3*A+A*A/10-Ujoint/2
assert float(S.N(A,20))<.567
assert float(S.N(Useparate,20))<.129
assert float(S.N(L,20))>28.2677

print("PASS: harmonic expansion, rational gap, 41-vector moment regression,")
print("      inverse roots, endpoint comparisons and Q-floor derivative.")
for label,z in [("B",B),("r",r),("Amax",A),("Umax",Useparate),
                ("Q_floor",L),("safe_P1_P3",L-S.Rational(473,256)),
                ("safe_P2",L-S.Rational(57,32))]:
    print(label,S.N(z,18))
