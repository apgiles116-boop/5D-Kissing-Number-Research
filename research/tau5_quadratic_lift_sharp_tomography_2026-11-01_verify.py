"""Exact regression for the sharp quadratic-lift Type-E tomography note.
The universal proof is analytic; this checks the equality family and constants.
"""
from fractions import Fraction as F
import sympy as s

n=3
c=F(3,2)
q=s.sqrt(3)/2
W=s.Matrix([[1,0],[s.Rational(1,2),q],[-s.Rational(1,2),q]])
assert W.T*W==s.Rational(3,2)*s.eye(2)
B=s.Matrix([[x*x,s.sqrt(2)*x*y,y*y] for x,y in W.tolist()])
eig=sorted((s.simplify(e) for e,m in (B.T*B).eigenvals().items() for _ in range(m)),key=float)
assert eig==[s.Rational(3,4),s.Rational(3,4),s.Rational(3,2)]
assert eig[-2]==s.Rational(c*c,n)

Dmass=lambda t:196*t-644*t*t+896*t**3-448*t**4
assert Dmass(F(7,250))>F(1245,256)
assert Dmass(F(41,1000))>F(41,6)
assert F(1,2)+F(7,250)+F(41,1000)<F(57,100)

c0=F(73,200)
eps=F(7,100000)
core=F(343,100)
sigma2sq=eps*c0*c0/16
sigma1lb=core*c0/8
minor=eps*c0**4*core**2/1024
old=F(1789089183,655360000000000000)
assert sigma2sq==F(37303,64000000000)
assert sigma2sq>F(3,4000)**2
assert sigma1lb==F(25039,160000)
assert minor==F(23387172587863,1638400000000000000000)
assert minor>F(1,100000000)
assert minor/old==F(117649,22500)

for aa,bb in [([1,2,3],[3,2,1]),([0,3,1,5],[2,0,4,1]),([1,1,1],[1,1,1])]:
    N=len(aa); aa=list(map(F,aa)); bb=list(map(F,bb))
    A=sum(aa);B0=sum(bb);a=sum(x*x for x in aa);b=sum(x*x for x in bb)
    d=sum(x*y for x,y in zip(aa,bb))
    assert (d-A*B0/N)**2<=(a-A*A/N)*(b-B0*B0/N)
print("PASS: sharp lift example, exact root brackets, singular values, minor floor")
print("sigma2(D)^2 >",sigma2sq,"≈",float(sigma2sq))
print("sum minor^2 >",minor,"≈",float(minor))
