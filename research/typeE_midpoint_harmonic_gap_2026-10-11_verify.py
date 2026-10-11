# Exact constant checks for the Type-E midpoint/harmonic gap
import sympy as s
k=4-2*s.sqrt(3)
alpha=4*(2/s.sqrt(3)-1)
assert s.simplify(alpha+alpha**2/8-s.Rational(2,3))==0
K=s.Rational(3607,162)-9*s.sqrt(3)
d=s.Rational(2857,4536)
E0=s.Rational(21,16)*d*d-s.Rational(5,14)
assert E0==s.Rational(366247,2239488)
E25=s.Rational(21,16)*(d-s.Rational(1,12))**2-s.Rational(5,14)+s.Rational(1,96)
assert E25==s.Rational(101431,2239488)
b=(4-s.sqrt(10))/(40*(49-14*s.sqrt(3)))
assert b>s.Rational(1,1200)
print('All exact symbolic checks passed')
print('eta=0 A>=',s.N(E0/K,15))
print('eta<=1/40 A>=',s.N(E25/K,15))
print('unconditional A>=',s.N(b,15))
