"""Exact symbolic verification of canonical isolated-16 radical transfer."""
import sympy as s
b,e=s.symbols("b e",real=True)
c0=2-(s.sqrt(6)+s.sqrt(2))/2
b0=s.Rational(383,504)-c0
F=s.Rational(1393,80)-s.Rational(17,10)*b-s.Rational(2,5)*b*b
frame=s.Rational(88,5)-s.Rational(11,5)*b+b*b/10-s.Rational(1,2)*(s.Rational(1,8)+(b-s.Rational(1,2))**2)
assert s.simplify(frame-F)==0
rad=s.Rational(11497727,635040)-s.Rational(223,630)*(s.sqrt(6)+s.sqrt(2))-s.Rational(2,5)*s.sqrt(3)
assert s.simplify(F.subs(b,b0)-rad)==0
assert s.diff(F,b)==-s.Rational(17,10)-s.Rational(4,5)*b
assert s.N(b0)>s.Rational(1,2) and s.N(b0)<s.Rational(3,4)
old=s.Rational(254678471,15876000)
assert s.N(F.subs(b,b0)-old)>0
k=s.sqrt(6)/3
gain=k*(s.Rational(17,10)+s.Rational(4,5)*b0)*e-s.Rational(2,5)*k*k*e*e
assert s.simplify(F.subs(b,b0-k*e)-F.subs(b,b0)-gain)==0
low=s.Rational(88,5)-s.Rational(93,40)*b+b*b/10
assert s.N(low.subs(b,s.Rational(1,2))-F.subs(b,b0))>0
print("PASS: exact radical expression, monotonicity, improvement, and margin polynomial")
print("b0 =",s.N(b0,18))
print("new =",s.N(F.subs(b,b0),18),"old =",s.N(old,18))
