#!/usr/bin/env python3
"""Exact checks for the sharp 21-line quartic-to-raw defect conversion.
The upstream P>1/58 analytic theorem is an explicitly retained input.
"""
from fractions import Fraction
import sympy as S

t=S.symbols('t',nonnegative=True)
x,y=S.symbols('x y',nonnegative=True)
g=t*(1+t)*(t+S.Rational(1,2))**2
assert S.expand(g)==t**4+2*t**3+S.Rational(5,4)*t**2+t/4
assert S.simplify((t+S.Rational(1,2))**2*((t+S.Rational(1,2))**2-S.Rational(1,4))-g)==0
gap=S.factor(g.subs(t,x+y)-g.subs(t,x)-g.subs(t,y))
assert all(c>=0 for c in S.Poly(gap,x,y).coeffs())
rho=S.sqrt((1+S.sqrt(S.Rational(61,29)))/8)-S.Rational(1,2)
assert S.simplify(g.subs(t,rho)-S.Rational(1,58))==0
assert S.ask(S.Q.positive(rho-S.Rational(1,19))) is True
d=Fraction(1,19)
assert d*(1+d)*(d+Fraction(1,2))**2==Fraction(2205,130321)
assert Fraction(1,58)-Fraction(2205,130321)==Fraction(2431,7558618)
assert Fraction(1,58)-Fraction(3,196)==Fraction(11,5684)

# Check the six signed-Huber endpoint and two trace margins of
# tau5_21line_quartic_gap_1over58_2026-10-29.md exactly.
p=S.Rational(1,58); vstar=S.Rational(9,1160)
def G(E):
    return (S.Rational(1,8)-S.sqrt(S.Rational(1,64)-E)
            if E<=S.Rational(1,64) else
            S.Rational(1,4)-S.sqrt(S.Rational(1,32)-E))
def L(V):return 4*p+G(p-S.Rational(5,24)*V)
def B(V):return (S.Rational(21,5)+S.sqrt(S.Rational(4,5)*V))*V
def h(c,lam,eta):
    alpha,beta=lam+eta,lam-eta
    if c< -alpha/2:return -alpha*c-alpha**2/4
    if c>beta/2:return beta*c-beta**2/4
    return c*c
def H(k,lam,eta):
    return ((5 if k==134 else 3)*h(-S.Rational(1,5),lam,eta)
            +(16 if k==134 else 18)*h(S.Rational(1,20),lam,eta))
for k,lam,eta,v in ((134,S.Rational(1,3),-S.Rational(1,40),S.Rational(179,5000)),
                    (135,S.Rational(1,3),S.Rational(1,4),S.Rational(23,1000))):
    for V in (S.S.Zero,vstar,v):
        D=V+S.Rational(336,5)-S.Rational(k,2)
        margin=S.simplify(H(k,lam,eta)-B(V)-2*lam*L(V)-eta*D)
        assert S.ask(S.Q.positive(margin)) is True,(k,V,margin)
    D=v+S.Rational(336,5)-S.Rational(k,2)
    margin=S.simplify((D if k==134 else -D)-2*L(v))
    assert S.ask(S.Q.positive(margin)) is True,(k,margin)
    print("Exact Huber comparisons:",k,"PASS")
assert S.ask(S.Q.positive(S.Rational(3,4)*rho-S.Rational(3,76))) is True
print("P>1/58 -> D>rho =",S.N(rho,18))
print("Type E Walsh right-hand constant (3/4)rho =",S.N(3*rho/4,18))
print("PASS: polynomial, rational, algebraic and eight Huber comparisons")
