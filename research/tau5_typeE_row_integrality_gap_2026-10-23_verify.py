"""Exact rational audit for the 21-line row-integrality gap, 2026-10-23."""
from fractions import Fraction as F
from sympy import symbols, simplify, diff

pmax = F(9,20)
Vmax = F(27,350)
assert F(6,35)*pmax == Vmax
assert F(3,7)*pmax == F(27,140)
assert F(4,5)*Vmax == F(54,875) < F(1,16)

# Only E=134 or E=135 can be compatible with the rounding error.
lo, hi, L1 = F(168,5), F(168,5)+Vmax/2, F(27,140)
assert lo-F(133,4)>L1 and F(136,4)-hi>L1
assert lo-F(134,4)<=L1 and F(135,4)-hi<=L1

# Exact degree bound, with q=2E_+ in [0,27/70].
q = symbols('q', real=True)
for p in range(1,21):
    b = max(F(p,5), F(25-p,20))
    expr = (b-q)**2*(F(1,p)+F(1,21-p)) - F(21,80)*(1-q)**2
    points = [F(0), F(27,70)]
    a = simplify(diff(expr,q,2)/2)
    linear = simplify(diff(expr,q).subs(q,0))
    if a>0:
        vertex = -linear/(2*a)
        if 0<=vertex<=F(27,70):
            points.append(vertex)
    assert all(simplify(expr.subs(q,z))>=0 for z in points),p

V = symbols('V', real=True)
h = F(21,80)*(F(43,70)+F(10,3)*V)**2-F(89,20)*V
assert simplify(h.subs(V,F(3,100))) == F(3,7000)
assert simplify(diff(h,V).subs(V,0))<0
assert simplify(diff(h,V).subs(V,F(3,100)))<0

d = F(1,10)+F(3,200)-pmax/7
assert d==F(71,1400)
assert F(2,7)*(pmax-F(35,6)*F(3,100))==F(11,140)<F(1,8)
g = lambda x: 7*x-28*x*x
assert g(d)==F(19809,70000)
assert g(d)+F(35,6)*F(3,100)==F(32059,70000)>pmax

a=F(521,50000)
fstar=lambda x: 7*x*(17+(1+x)**2*(7+x))/(4*(1-x)**2)
assert pmax-fstar(a)==F(4072230841334633,24481714410000000000)>0

t=symbols('t')
P2=(5*t*t-1)/4
P4=(21*t**4-14*t*t+1)/8
assert simplify(7*t*t*(4*t*t-1)-(1+F(28,3)*P2+F(32,3)*P4))==0

print('PASS: exact rational and polynomial checks')
print('Universal P>9/20; conditional Type-E A>521/50000')
