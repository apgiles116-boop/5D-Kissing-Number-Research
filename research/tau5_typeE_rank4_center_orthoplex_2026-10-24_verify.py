"""Exact symbolic and rational checks for the rank-four center-cap note.
The quantified geometric proof is in the Markdown note, not this checker.
"""
import sympy as S

x,rho,s,v=S.symbols("x rho s v",real=True)
assert S.factor(rho*(1+rho)-x*(1+x)-(rho-x)*(1+rho+x))==0
f=(S.Rational(1,2)-s*v)/S.sqrt((1-s*s)*(1-v*v))
assert S.simplify(S.diff(f,s)*S.sqrt((1-s*s)*(1-v*v))*(1-s*s)-(s/2-v))==0

r9=(3*S.sqrt(2)-4)/8
r10=(S.sqrt(11)-3)/6
for k,r in [(9,r9),(10,r10)]:
    assert S.simplify(r*(1+r)-S.Rational(k-8,4*(k-1)))==0

t9sq=(13-2*S.sqrt(2))/21
t10sq=(43-3*S.sqrt(11))/70
assert S.simplify(t9sq-(S.Rational(1,2)-r9)/(1-r9))==0
assert S.simplify(t10sq-(S.Rational(1,2)-r10)/(1-r10))==0

t9=S.sqrt(t9sq)
t10=S.sqrt(t10sq)
c9=(S.Rational(1,2)+t9)/2
c10=(S.Rational(1,2)+t10)/2
a9=1-S.Rational(5,2)*c9**2
a10=1-S.Rational(5,2)*c10**2
g0=(9-6*S.sqrt(2))/20
B=8*g0+a9+a10

# Rational isolation and certified strict B>0.43.
assert S.Rational(141421,100000)**2<2<S.Rational(141422,100000)**2
assert S.Rational(331662,100000)**2<11<S.Rational(331663,100000)**2
assert S.Rational(33,10)**2<11
assert S.Rational(36,25)**2>2
assert S.Rational(34,25)**2<2
assert (13-2*S.Rational(34,25))/21<S.Rational(49,100)
assert (9-6*S.Rational(7,5))/20<=S.Rational(3,100)

u9=S.Rational(87,125)
u10=S.Rational(859,1250)
assert (13-2*S.Rational(141421,100000))/21<u9*u9
assert (43-3*S.Rational(331662,100000))/70<u10*u10
glo=(9-6*S.Rational(141422,100000))/20
a9lo=1-S.Rational(5,8)*(S.Rational(1,2)+u9)**2
a10lo=1-S.Rational(5,8)*(S.Rational(1,2)+u10)**2
Blo=8*glo+a9lo+a10lo
assert Blo==S.Rational(1077399,2500000)>S.Rational(43,100)

print("Exact polynomial, derivative and constants: PASS")
print("c9 =",S.N(c9,18),"c10 =",S.N(c10,18))
print("a9 =",S.N(a9,18),"a10 =",S.N(a10,18))
print("Balanced D5 A lower bound =",S.N(B,25))
print("Rational certificate lower bound =",Blo)
