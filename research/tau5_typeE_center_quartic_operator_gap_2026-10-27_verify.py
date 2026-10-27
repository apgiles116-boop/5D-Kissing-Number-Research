"""Exact SymPy checks for the 2026-10-27 center quartic Type-E note."""
import sympy as s
from itertools import combinations

A = s.Rational(383,504)
r = A-3*s.Rational(1,4)
assert r == s.Rational(5,504)
Tcap = (16+3*(s.Rational(4,3))**2+(1-r)**(-2))/16
assert Tcap == s.Rational(1043632,747003)
gap = s.Rational(8,5)-Tcap
assert gap == s.Rational(757864,3735015)>0

x = s.symbols('x0:5',real=True)
D = [(x[i]+eps*x[j])/s.sqrt(2)
     for i,j in combinations(range(5),2) for eps in (-1,1)]
T = s.expand(sum(t**4 for t in D))
assert s.expand(T-s.Rational(3,2)*sum(t*t for t in x)**2
                -s.Rational(1,2)*sum(t**4 for t in x)) == 0

t = s.symbols('t',real=True)
assert s.expand(s.Rational(1,16)-(s.Rational(1,2)-t)**4
  -t*sum(s.Rational(1,2)**(3-k)*(s.Rational(1,2)-t)**k
         for k in range(4))) == 0

c,y = s.symbols('c y',real=True)
a = 1-s.Rational(25,4)*c*c
b = c*(5*c-2)
assert s.factor((y-c)**2-a*y*y-b*y)==c*c*(5*y-2)**2/4
assert s.factor(a*c+b)==-c*(5*c-2)**2/4
assert s.factor(a*s.Rational(8,5)+4*b-10*(s.Rational(2,5)-c)**2)==0

Vcap = 3*s.Rational(1,12)**2+(r/(4*(1-r)))**2
assert Vcap == s.Rational(62269,2988012)
Qdist = 2*(3/s.sqrt(40)-s.sqrt(Vcap))**2
assert s.N(Qdist,20) > s.Rational(1,5)

print("PASS: exact quartic cap",Tcap)
print("PASS: D5 fourth moment, quartic-excess minorant, center correction")
print("PASS: exact quartic operator gap",gap)
print("PASS: aggregate Q displacement lower bound",s.N(Qdist,15))
