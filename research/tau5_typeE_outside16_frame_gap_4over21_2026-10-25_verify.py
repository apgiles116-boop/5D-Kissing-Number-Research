"""Exact rational checks for Type-E 4/21 frame gap (2026-10-25).
Analytic inequalities and proof-status qualifications are in the companion note.
"""
from fractions import Fraction as F
from sympy import symbols, Rational, expand, diff, cancel, Matrix, diag, eye

B=F(4,21)
Dmin=F(1665618603949,2064772104192)
rhs=F(14297,3600)*B+F(79,64)*B**2+F(3,4)*B**3+F(1,8)*B**4
assert Dmin-rhs==F(4997736421,51619302604800)>0
assert F(15,4)<F(961,256)   # sqrt(15)/2 < 31/16
assert F(79,64)==F(3,4)+F(31,64)
assert F(3,4)-B==F(47,84)>0

a=symbols("a:16")
c=[1-t for t in a]
A=sum(a); S2=sum(t*t for t in a); S3=sum(t**3 for t in a); S4=sum(t**4 for t in a)
R=(sum(t*t for t in c)**2)/32-Rational(3,8)*sum(t**4 for t in c)
U=sum(1-c[i]*c[j] for i in range(16) for j in range(i+1,16))/16
D=expand(R-U)
poly=(64-46*A+5*A**2-4*A*S2-41*S2+S2**2+48*S3-12*S4)/32
assert expand(D-poly)==0
vertex=[F(1,4)]*3+[F(5,504)]+[F(0)]*12
assert D.subs({a[i]:Rational(v.numerator,v.denominator) for i,v in enumerate(vertex)})==Rational(Dmin.numerator,Dmin.denominator)
quot=cancel((diff(D,a[0])-diff(D,a[1]))/(a[0]-a[1]))
claimed=(-8*A+4*S2-82+144*(a[0]+a[1])-48*(a[0]**2+a[0]*a[1]+a[1]**2))/32
assert cancel(quot-claimed)==0

K=Matrix([[Rational(1,2),Rational(131,1008),Rational(3,2)],
          [Rational(131,336),0,Rational(5,84)],
          [Rational(3,8),Rational(5,1008),0]])
T=diag(3,1,12)*(Rational(27,25)*eye(3)-K)
assert T==T.T
assert [T[:k,:k].det() for k in (1,2,3)]==[
    Rational(87,50),Rational(121870727,70560000),Rational(22005127,73500000)]

ai,aj,qi,qj,p=symbols("ai aj qi qj p")
ci,cj=1-ai,1-aj
Delta=ci*qj+cj*qi-qi*qj
h=(Rational(1,2)+p)**4-((ci*cj-Delta)/4)*(Rational(1,2)+p)**2
upper=(1-ci*cj)/16+(qi+qj)/16+p/4+(ai+aj)*p/4+(qi+qj)*p/4+Rational(3,2)*p**2+(qi+qj)*p**2/4+2*p**3+p**4
assert expand(upper-h-(qi+qj-Delta)*(Rational(1,16)+p/4+p**2/4)-ai*aj*p/4-ci*cj*p**2/4)==0
print("PASS: exact deficit polynomial, spectral minors, pairwise quartic expansion")
print("PASS: strict 4/21 margin",Dmin-rhs)
print("STATUS: standalone theorem proved; Type E remains open")
