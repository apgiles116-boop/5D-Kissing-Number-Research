"""Exact rational verification of the Type-E safe-pair bridge.
Prior graph and raw-defect certificates are inputs, not re-proved here.
"""
from fractions import Fraction as F
import sympy as s
A=F(383,504); P=F(1780062775,4032758016)
U=3*F(1,16)+(A-F(3,4))**2
S=30-3*A+A*A/10-U/2
assert S==F(8790283,317520)
assert S-F(17456771,635040)==F(131,672)
L=S-F(3,2)-P
assert L==F(519072132637,20163790080)
assert L**2/184==F(269435878880323320573769,74810431191816378777600)
assert (L-23)**2/184==F(3058638688757706875209,74810431191816378777600)
a,u,v=s.symbols("a u v")
lhs=30-3*a+a*a/10-u/2+v/2-s.Rational(3,2)
rhs=s.Rational(57,2)-s.Rational(25,8)*a+a*a/10+(a/4-u)/2+v/2
assert s.simplify(lhs-rhs)==0
for k in range(4):
    q=s.Rational(k,16)+(a-s.Rational(k,4))**2
    f=30-3*a+a*a/10-q/2
    assert s.simplify(s.diff(f,a)+3+s.Rational(4,5)*a-s.Rational(k,4))==0
    assert s.diff(f,a).subs(a,s.Rational(k+1,4))<0
print("PASS: exact identity, cap, rational safe-mass and fourth-moment cuts")
