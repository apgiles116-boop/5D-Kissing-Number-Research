"""Exact SymPy verification of Type-E harmonic-4 localization identities."""
import sympy as s
V,P,E,t,T,e,a,si,x=s.symbols("V P E t T e a si x")
H=lambda x: x**4-s.Rational(2,3)*x**2+s.Rational(1,21)
assert H(s.Integer(1))==s.Rational(8,21)
assert s.simplify(s.gegenbauer(4,s.Rational(3,2),x)/s.gegenbauer(4,s.Rational(3,2),1)-H(x)/H(s.Integer(1)))==0
S21=s.Rational(168,5)+V/2
W21=P-E+S21/4
K21=s.expand(21+2*W21-s.Rational(2,3)*(21+2*S21)+s.Rational(441,21))
assert s.simplify(K21-(2*(P-E)-s.Rational(5,12)*V))==0
row21=H(s.Integer(1))+T-s.Rational(2,3)*t+s.Rational(20,21)
assert s.simplify(row21-(T-s.Rational(2,3)*t+s.Rational(4,3)))==0
assert s.simplify(row21.subs(t,e+s.Rational(16,5))-(T-s.Rational(2,3)*e-s.Rational(4,5)))==0
S20=s.Integer(30)+V/2
W20=P-E+S20/4
K20=s.expand(20+2*W20-s.Rational(2,3)*(20+2*S20)+s.Rational(400,21))
assert s.simplify(K20-(s.Rational(5,7)+2*(P-E)-s.Rational(5,12)*V))==0
row20=T-s.Rational(2,3)*t+s.Rational(20,21)
assert s.simplify(row20-(T-s.Rational(12,7)-s.Rational(2,3)*(t-4)))==0
delta=s.Rational(12,7)-s.Rational(1043632,747003)
assert delta==s.Rational(1658612,5229021)
cap=1/(4*(1-a))
assert s.simplify(cap*si-si/4-a*si/(4*(1-a)))==0
assert s.simplify(cap*a/(4*(1-a))-a/(16*(1-a)**2))==0
assert s.simplify(a/s.Integer(9)-a/(16*(1-a)**2)).subs(a,s.Rational(1,4))==0
print("PASS: degree-four Gegenbauer normalization")
print("PASS: 21-line and 20-line harmonic kernel identities")
print("PASS: isolated-center row and exact quartic deficit")
print("PASS: individual midpoint energy envelope")
