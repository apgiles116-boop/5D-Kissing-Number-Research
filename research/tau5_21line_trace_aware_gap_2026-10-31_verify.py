"""Exact rational arithmetic verifier for trace-aware 21-line defect gap.
This checks arithmetic, not universal quantification."""
from fractions import Fraction as Q
import sympy as s

p=Q(3,196)
L=Q(33,98)
kappa=Q(35,12)
assert L==22*p and kappa==Q(14)*Q(5,24)
assert Q(3,28)*(Q(1,4)-Q(3,28))==p
assert Q(1,7)*(Q(1,4)-Q(1,7))==p
assert Q(1,64)>p
x=s.symbols("x")
P2=(5*x*x-1)/4
P4=(21*x**4-14*x*x+1)/8
assert s.expand(s.Rational(1,28)+P2/3+s.Rational(8,21)*P4-(x**4-x*x/4))==0

v134=(L-Q(1,5))/(1+kappa)
v135=(L-Q(3,10))/(kappa-1)
assert v134==Q(402,11515) and v135==Q(108,5635)
assert 0<v135<v134<Q(1,20)
B=lambda v:L-kappa*v
assert B(v134)==Q(1,5)+v134
assert B(v135)==Q(3,10)-v135

margin134=(Q(4,5)-v134)**2/5+Q(1,25)-Q(22,5)*v134
margin135=Q(1083,9604)-Q(22,5)*v135
assert margin134==Q(459297,132595225) and margin134>0
assert margin135==Q(157029,5522300) and margin135>0
assert Q(3,5)-(L-Q(3,10))/2==Q(57,98)
assert 2*kappa/Q(5)<Q(22,5)

z=s.symbols("z")
assert s.expand((z-s.Rational(1,2))*(s.Rational(3,2)-z*z*(z+s.Rational(1,2)))-
  (s.Rational(3,2)*(z-s.Rational(1,2))-z*z*(z*z-s.Rational(1,4))))==0
assert Q(2,3)*p==Q(1,98)
assert Q(3,4)*Q(1,98)==Q(3,392)
print("PASS: polynomial identity, exact roots, both trace branches and rational margins")
print("P >",p,"D >",Q(1,98))
print("K=134:",v134,margin134)
print("K=135:",v135,margin135)
