#!/usr/bin/env python3
"""Exact SymPy verifier for the Type-E Delsarte safe-contact slack bridge.

The paper's analytic convexity/integration arguments are the proof.
This checks the exact polynomial identities, root brackets, endpoint
comparison certificate, Walsh formulas, and combinatorial counts.
"""
import sympy as S
from itertools import product

Q=S.Rational
x,b,t,B,X,Y,Z=S.symbols("x b t B X Y Z", real=True)
F=lambda v: 28*v**4-7*v**2
D=lambda v: 196*v-644*v**2+896*v**3-448*v**4
Dp=S.diff(D(x),x)

r=(1-S.sqrt((7+S.sqrt(721))/56))/2
assert S.simplify(D(r)-15)==0
assert D(Q(9,80))>15
assert D(Q(1,25))>Q(41,6)
assert D(Q(1,4))==21 and S.simplify(Dp.subs(x,Q(1,4)))==14
assert S.factor(S.diff(D(x),x,2))==-56*(96*x*x-96*x+23)

# Rational root brackets for r0, s0=D^-1(43/3), s1=D^-1(41/6).
for target,lo,hi in [
    (S.Integer(15),Q(111255,10**6),Q(111256,10**6)),
    (Q(43,3),Q(103544,10**6),Q(103545,10**6)),
    (Q(41,6),Q(39781,10**6),Q(39782,10**6)),
]:
    assert D(lo)<target<D(hi)
assert Q(111255,10**6)**2+Q(39781,10**6)**2 > Q(103545,10**6)**2

# Positive derivative comparison on 0<=u<=9/80, s1<1/25.
u=S.symbols("u", nonnegative=True)
p=S.expand(2*Dp.subs(x,u+Q(1,25))-Dp.subs(x,u))
assert p==(-1792*u**3+Q(56448,25)*u**2-Q(546952,625)*u+Q(1583316,15625))
lower=Q(1583316,15625)-Q(546952,625)*Q(9,80)-1792*Q(9,80)**3
assert lower==Q(82341,250000)>0

# Isolated-center row: two safe endpoint contacts.
assert S.expand(-F(b+t)-F(b-t)
    -14*(b*b+t*t)+56*(b**4+6*b*b*t*t+t**4))==0

# Four safe endpoint contacts: Walsh/Parseval and quartic character product.
v=[B+sig*Y+tau*X+sig*tau*Z
   for sig,tau in product((-1,1),repeat=2)]
L2=B*B+X*X+Y*Y+Z*Z
L4=(B**4+X**4+Y**4+Z**4
    +6*(B*B*X*X+B*B*Y*Y+B*B*Z*Z
        +X*X*Y*Y+X*X*Z*Z+Y*Y*Z*Z)
    +24*B*X*Y*Z)
assert S.expand(sum(q*q for q in v)-4*L2)==0
assert S.expand(sum(q**4 for q in v)-4*L4)==0
assert S.expand(-sum(F(q) for q in v)-28*L2+112*L4)==0

# Sharp -F(s)>=(21/4)*rho(s)^2:
# s<=1/4 uses rho=s; s>=1/4 uses rho=1/2-s.
s=S.symbols("s", real=True)
assert S.factor(-F(s)-Q(21,4)*s*s)==-Q(7,4)*s*s*(4*s-1)*(4*s+1)
assert S.factor(-F(s)-Q(21,4)*(Q(1,2)-s)**2)==(
    -Q(7,16)*(2*s-1)*(4*s-1)*(8*s*s+6*s+3))

# Exact pair partition: 26 deep and 794 nondeep; 40+736+18=794.
assert 41*40//2==820
assert 16+10==26
assert 820-26==794
assert 40+184*4+18==794

rval=S.N(r,24)
s1val=S.nsolve(D(x)-Q(41,6),Q(4,100))
Astar=Q(1,2)+r+s1val
Ustar=Q(1,8)+r*r+s1val*s1val
cN=(r/15)*(3-Astar/5)+r*r/30
print("PASS: exact algebra, root brackets, endpoint comparison, Walsh and 794-contact partition")
print("r0 =",rval)
print("Astar =",S.N(Astar,18))
print("Ustar =",S.N(Ustar,18))
print("cN =",S.N(cN,18))
