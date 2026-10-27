"""Exact SymPy verification of four-core midpoint SDP sharpness.
This checks only the RELAXED midpoint Gram problem, not full Type E.
"""
import sympy as sp

t = sp.symbols("t", real=True)
D = sp.Rational(383,1008)
Amax = sp.Rational(383,504)
a = sp.Rational(1,4)
b = D-a
d12 = a-2*t
d34 = b-2*t
G = sp.Matrix([[a,-d12,-t,-t],[-d12,a,-t,-t],
               [-t,-t,b,-d34],[-t,-t,-d34,b]])
assert G*sp.ones(4,1) == sp.zeros(4,1)
assert sp.trace(G) == Amax
assert G.eigenvals() == {sp.Integer(0):1,4*t:1,
                          sp.Rational(1,2)-2*t:1,2*b-2*t:1}
assert sp.simplify(d12+d34+4*t-D) == 0
f = lambda d: (sp.Rational(1,2)+d)**2*d*(1+d)
P = sp.factor(f(d12)+f(d34)+4*f(t))
P0 = sp.factor(P.subs(t,0))
assert P0 == sp.Rational(241638909745,1032386052096)
d = sp.Symbol("d")
assert sp.simplify(sp.diff(f(d),d,2)-(24*d**2+24*d+5)/2) == 0
for tv in [sp.Rational(1,10000),sp.Rational(1,100),sp.Rational(1,20)]:
    assert tv < b/2
    vals = [sp.factor(ev.subs(t,tv)) for ev in G.eigenvals()]
    assert all(v >= 0 for v in vals)
    assert all(v > 0 for v in [d12.subs(t,tv),d34.subs(t,tv),tv])
    assert sp.simplify(P.subs(t,tv)) < P0
print("PASS: exact PSD spectrum, midpoint caps, six positive defects, energy saturation")
print("D =",D,"Amax =",Amax,"P_sup =",P0,"~",sp.N(P0,18))
print("P(t)-P_sup =",sp.factor(P-P0))
