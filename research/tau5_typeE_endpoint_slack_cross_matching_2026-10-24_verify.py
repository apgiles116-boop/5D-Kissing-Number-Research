"""Exact symbolic audit of Type-E endpoint-slack cross-matching theorem.
The universal inequality is proved analytically in the companion note.
"""
from fractions import Fraction
from sympy import Matrix, Rational as R, sqrt, simplify, symbols
X,U,V,W,C,p,q,L=symbols("X U V W C p q L",real=True)
cross=[(X+U+V+W)/4,(X-U-V+W)/4,
       (X-U+V-W)/4,(X+U-V-W)/4]
expected=[X+U+V+W,X-U-V+W,X-U+V-W,X+U-V-W]
assert all(simplify(4*x-y)==0 for x,y in zip(cross,expected))
r=C-2*(p+q+L)
assert simplify(C*C-r*(2*C-r)-4*(p+q+L)**2)==0
print("PASS: exact Walsh and endpoint-slack algebra")
e=[Matrix([int(j==i) for j in range(5)]) for i in range(5)]
u=3/sqrt(10); v=11*sqrt(10)/60; t=sqrt(R(203,360))
m=[e[0]/sqrt(10),-e[0]/sqrt(10),e[1]/sqrt(10),-e[1]/sqrt(10)]
z=[u*e[2],v*e[2]+t*e[3],u*e[4],
   v*e[4]+t*(R(3,5)*e[2]-R(4,5)*e[3])]
dot=lambda a,b:simplify((a.T*b)[0])
for i in range(4):
    assert dot(m[i],z[i])==0
    assert dot(m[i],m[i])==R(1,10)
    assert dot(z[i],z[i])==R(9,10)
assert dot(z[0],z[1])==dot(z[2],z[3])==R(11,20)
assert dot(z[0],z[3])==3*sqrt(203)/100
assert dot(z[1],z[3])==11*sqrt(203)/600-R(203,450)
assert 14<sqrt(203)<15 and 9*203<2500
for i in range(4):
    for j in range(i+1,4):
        for s in (-1,1):
            for tsgn in (-1,1):
                assert dot(m[i]+s*z[i],m[j]+tsgn*z[j])<=R(1,2)
p=q=R(1,20)
ell12=-dot(m[0],m[1])-p
ell34=-dot(m[2],m[3])-q
C=sum((dot(a,a) for a in m),R(0))
assert ell12==ell34==R(1,20) and C==R(2,5)
assert (p+q+ell12+ell34)**2==C**2/4
print("PASS: exact 5D endpoint-feasible equality witness")
B=Fraction(383,504); h=Fraction(1,1000)
assert B*h-h*h==Fraction(11953,15750000)
assert h-Fraction(1,50)**2/B==Fraction(907,1915000)
print("PASS: exact Type-E near-saturation constants")
print("STATUS: local theorem; no Type-E exclusion")
