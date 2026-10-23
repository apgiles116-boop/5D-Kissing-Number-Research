"""Exact rational checks for the 21-line P>459/1000 proof."""
import sympy as s
p=s.Rational(459,1000)
v0=s.Rational(1541,50000)
v=s.symbols('v', real=True)
b=1-s.Rational(6,7)*p+s.Rational(10,3)*v
h=s.expand(s.Rational(21,80)*b**2+b*v/10+v**2/20-s.Rational(1743,400)*v)
assert s.factor(h.subs(v,v0))==s.Rational(463361,175000000000)
assert s.diff(h,v).subs(v,0)<0 and s.diff(h,v).subs(v,v0)<0
assert s.Rational(63,400)**2-s.Rational(4,5)*s.Rational(31,1000)==s.Rational(1,160000)
assert s.Rational(2,7)*(p-s.Rational(35,6)*v0)<s.Rational(1,8)
g=lambda t:7*t-28*t*t
d=s.Rational(1,10)+v0/2-p/7
assert s.factor(g(d)+s.Rational(35,6)*v0-p)==s.Rational(5491693,52500000000)
F=g(s.Rational(1,10)+v/2-p/7)+s.Rational(35,6)*v
assert s.diff(F,v).subs(v,v0)>0 and s.diff(F,v).subs(v,s.Rational(6,35)*p)>0
a=s.Rational(5313,500000)
f=lambda a:7*a*(17+(1+a)**2*(7+a))/(4*(1-a)**2)
assert s.factor(p-f(a))==s.Rational(5575655015507445273,244715227969000000000000)
print("PASS: exact rational checks")
