"""Exact arithmetic checks for Type-E five-to-four Q-frame variance stability.

The full proof of the SOS and majorization lemmas is in the companion note.
No numerical SDP or floating-point solver is used.
"""
from fractions import Fraction as F
import sympy as sp

A0=F(383,504)
r=F(5,504)
M0=3*F(1,16)+r*r
P0=30-3*A0+A0*A0/10-M0/2
assert M0==F(47653,254016)
assert P0==F(8790283,317520)
assert P0-F(17456771,635040)==F(131,672)
print('PASS retained capped midpoint Q-floor:',P0)

# Universal 5D-to-4D identity: exact test on twenty rational vectors.
unit=[sp.Matrix([int(j==i) for j in range(5)]) for i in range(5)]
nonunit=[
 sp.Matrix([sp.Rational(4,5),sp.Rational(2,5),sp.Rational(1,5),0,0]),
 sp.Matrix([0,sp.Rational(4,5),sp.Rational(2,5),sp.Rational(1,5),0]),
 sp.Matrix([0,0,sp.Rational(4,5),sp.Rational(2,5),sp.Rational(1,5)]),
 sp.Matrix([sp.Rational(1,5),0,0,sp.Rational(4,5),sp.Rational(2,5)])]
z=unit*3+unit[:1]+nonunit
assert len(z)==20
t=[v.dot(v) for v in z]
a=[1-ti for ti in t]
assert all(0<=ai<sp.Rational(1,4) for ai in a)
A=sum(a); T=sum(t)
assert A==sp.Rational(16,25) and A<sp.Rational(383,504)
Z=sum((v*v.T for v in z),sp.zeros(5,5))
P=sum(z[i].dot(z[j])**2 for i in range(20) for j in range(i+1,20))
base=30-3*A+A**2/10-sp.Rational(1,2)*sum(ai**2 for ai in a)
B=Z-(T/5)*sp.eye(5)
V=sp.trace(B*B)
assert sp.simplify(P-base-V/2)==0

x=sp.Matrix([1,0,0,0,0])
c=[x.dot(v) for v in z]
y=[v-x*ci for v,ci in zip(z,c)]
E=sum(ci**2 for ci in c)
U=sum((ci*yi for ci,yi in zip(c,y)),sp.zeros(5,1))
Y=sum((yi*yi.T for yi in y),sp.zeros(5,5))
proj=sp.eye(5)-x*x.T
Ytr=Y-((T-E)/4)*proj
residual=(T-5*E)**2/20+2*U.dot(U)+sp.trace(Ytr*Ytr)
assert sp.simplify(V-residual)==0
assert sp.simplify(P-base-(T-5*E)**2/40-U.dot(U)-sp.trace(Ytr*Ytr)/2)==0
s2=sum(yi.dot(yi)**2 for yi in y)
cross2=sum(y[i].dot(y[j])**2 for i in range(20) for j in range(i+1,20))
assert sp.simplify(sp.trace(Ytr*Ytr)-(s2+2*cross2-(T-E)**2/4))==0
signed=sum(c[i]*c[j]*z[i].dot(z[j]) for i in range(20) for j in range(i+1,20))
assert sp.simplify(signed-(E**2-E+sum(a[i]*c[i]**2 for i in range(20))+U.dot(U))/2)==0
print('PASS exact 5-to-4 SOS splitting, signed identity and 4D residual')

Dg=F(1780062775,4032758016)
Dp=F(366383,1016064)
assert F(1,4)<Dg<F(1,2)
assert F(1,4)<Dp<F(3,8)

def defect_square_max(D,c):
    k=D//c
    return k*c*c+(D-k*c)**2

def safe_floor(E0,D,c):
    assert E0<=(20-A0)/5
    return P0+(20-A0-5*E0)**2/40-F(3,2)-D-defect_square_max(D,c)

def safe_cap(k):
    return F(184,9)+F(5*k,36)

cases=[
 ('general E<=1/2',F(1,2),Dg,F(1,4),87),
 ('canonical path E<=1/2',F(1,2),Dp,F(1,8),88),
 ('general E<=1',F(1),Dg,F(1,4),73),
 ('canonical path E<=1',F(1),Dp,F(1,8),74)]
for name,e0,D,c,k in cases:
    gap=safe_floor(e0,D,c)-safe_cap(k)
    assert gap>0,(name,gap)
    print('PASS',name,'K>=',k+1,'exact gap=',gap)

# High-defect path: four core masses > b=1/36.
b=F(1,36)
assert r<b<(A0-F(1,2))/2
v=[F(1,4),F(1,4),A0-F(1,2)-b,b]+[F(0)]*16
assert sum(v)==A0 and all(v[i]>=v[i+1] for i in range(19))
Mb=sum(w*w for w in v)
assert M0-Mb==F(1,126)
gain=(M0-Mb)/2
assert gain==F(1,252)
assert P0+gain==F(8791543,317520)

D=sp.symbols('D',real=True)
bD=4*(D-sp.Rational(1,4))**2
rr=sp.Rational(5,504)
A00=sp.Rational(383,504)
Mparam=sp.Rational(1,8)+(A00-sp.Rational(1,2)-bD)**2+bD**2
Munrestricted=sp.Rational(3,16)+rr**2
assert sp.factor((Munrestricted-Mparam)/2-(bD-rr)*(sp.Rational(1,4)-bD))==0
bmax=4*(sp.Rational(Dp.numerator,Dp.denominator)-sp.Rational(1,4))**2
assert bmax<(sp.Rational(1,4)+rr)/2
assert bmax<(A00-sp.Rational(1,2))/2
print('PASS canonical path D>=1/3: extra exact Q-floor =1/252')
print('GLOBAL STATUS UNCHANGED: 40<=tau_5<=44; Type E remains open')
