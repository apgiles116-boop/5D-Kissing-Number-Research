#!/usr/bin/env python3
"""Exact symbolic/rational checks for D5 isolated-neighbour coercivity.
The analytic endpoint and perturbation lemmas are proved in the companion note.
"""
from itertools import combinations
import sympy as S

t = S.symbols("t")
I = S.eye(5)
roots = {}
for p, q in combinations(range(5), 2):
    for sign in (1, -1):
        roots[p, q, sign] = I[:, p] + sign*I[:, q]
core = {(0, j, 1) for j in range(1, 5)}
iso = [r for r in roots if r not in core]
assert len(iso) == 16

def meets(r, s):
    return len(set(r[:2]) & set(s[:2])) == 1

degree_counts = {9: 0, 10: 0}
class_counts = {}
for r in iso:
    N = [s for s in iso if meets(r, s)]
    degree_counts[len(N)] += 1
    Z = sum((roots[s]*roots[s].T/S.Integer(2) for s in N), S.zeros(5))
    V = S.Matrix.hstack(*roots[r].T.nullspace())
    restricted = S.factor((V.T*(t*S.eye(5)-Z)*V).det()/(V.T*V).det())
    if r[0] == 0:
        expected = (t-S.Rational(3,2))**2*(t*t-S.Rational(15,4)*t+3)
        full = (t-3)*(t-S.Rational(3,2))**2*(t*t-3*t+S.Rational(3,2))
    elif r[2] == 1:
        expected = (t-1)*(t-2)**2*(t-S.Rational(5,2))
        full = (t-2)**2*(t-S.Rational(5,2))*(t*t-S.Rational(7,2)*t+2)
    else:
        expected = (t-2)**2*(t*t-S.Rational(7,2)*t+2)
        full = (t-2)**2*(t-S.Rational(5,2))*(t*t-S.Rational(7,2)*t+2)
    assert S.expand(restricted-expected) == 0
    assert S.expand(Z.charpoly(t).as_expr()-full) == 0
    class_counts[str(expected)] = class_counts.get(str(expected), 0)+1

assert degree_counts == {9:4, 10:12}
assert sum(k*v for k,v in degree_counts.items()) == 156
assert sorted(class_counts.values()) == [4,6,6]
lam = (7-S.sqrt(17))/4
k = 2-S.sqrt(3)
assert lam>S.Rational(7,10)
assert (7+S.sqrt(17))/4 < 3
assert (15-S.sqrt(33))/8 > 1
assert k<S.Rational(27,100)
gap = S.simplify(3*lam/(80*k*k))
assert gap>S.Rational(175,486)

# Robust estimates at x<=1/250 and x<1/35.
assert 40*S.Rational(27,100)**2 < 3
assert S.Rational(3,4)*(S.Rational(7,10)-S.Rational(16,200)) == S.Rational(93,200)
assert (S.Rational(93,200)-S.Rational(3,250))/80 == S.Rational(453,80000)>S.Rational(1,180)
assert S.Rational(250,200**2)>S.Rational(1,180)
assert (S.Rational(3,4)*(S.Rational(7,10)-S.Rational(16,95))-S.Rational(3,35))/80 == S.Rational(333,85120)>S.Rational(1,260)
assert S.Rational(35,95**2)==S.Rational(7,1805)>S.Rational(1,260)

# Conditional Type-E resource reduction, D(x)+E(s)<=15, E(s)>=10.
x,y=S.symbols("x y")
D=196*x-644*x**2+896*x**3-448*x**4
assert S.expand(D-28*x*(1-x)*(7-16*x*(1-x)))==0
Dy=28*y*(7-16*y)
assert Dy.subs(y,S.Rational(34,1225))==S.Rational(1092216,214375)>5
assert Dy.subs(y,S.Rational(1,4))==21
assert S.Rational(383,504)<S.Rational(34,35)
print("PASS: D5 neighbour spectra, degree partition 9^4 10^12, 78 meeting pairs")
print("PASS: exact-D5 x=0 or x>0.3756559642; robust E2>=x/180 (small strip)")
print("PASS: conditional resource x<1/35; robust E2>x/260 (full resource strip)")
