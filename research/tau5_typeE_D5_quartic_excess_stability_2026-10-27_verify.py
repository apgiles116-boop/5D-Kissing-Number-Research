"""Exact SymPy checks for the D5 quartic-excess / isolated-center separation theorem."""
from itertools import combinations
from sympy import symbols, Rational as R, simplify, sqrt, pi, asin, N

c, t = symbols("c t", real=True)
h = R(2, 5)
q = (1 - c*c/(h*h))*t*t - 2*c*(1-c/h)*t
assert simplify((t-c)**2 - q - (c*c/(h*h))*(t-h)**2) == 0
assert simplify(q.subs(t, c) + (c*c/(h*h))*(c-h)**2) == 0
assert simplify((1-c*c/(h*h))*R(8,5)-8*c*(1-c/h)-10*(h-c)**2) == 0
assert simplify(q.subs(c,R(1,4))-(R(39,64)*t*t-R(3,16)*t)) == 0
assert 10*(h-R(1,4))**2 == R(9,40)
assert 10*(h-R(1,3))**2 == R(2,45)

x = symbols("x0:5", real=True)
T = []
for i,j in combinations(range(5), 2):
    T.extend([(x[i]+x[j])**2/2, (x[i]-x[j])**2/2])
norm2 = sum(v**2 for v in x)
assert simplify(sum(T)-4*norm2) == 0
assert simplify(sum(v**2 for v in T)
                - R(3,2)*norm2**2 - R(1,2)*sum(v**4 for v in x)) == 0
uniform = {v: 1/sqrt(5) for v in x}
vals = [simplify(v.subs(uniform)) for v in T]
assert vals.count(h) == 10 and vals.count(0) == 10
assert 10*(h-R(1,4))**2 == R(9,40)

Amax = R(383,504)
assert Amax < R(9,10)
L = (3/sqrt(40)-sqrt(Amax)/6)**2
assert N(L-R(1,10), 30) > 0
angle = asin(sqrt(L/20))*180/pi
print("PASS: sharp D5 quartic positive-part certificate")
print("PASS: D5 second and fourth moments and equality witness")
print("PASS: Type-E isolated-center Q-tensor distance > 1/5")
print("minimum aggregate sin^2 =", N(L,16))
print("minimum maximal angular mismatch (degrees) =", N(angle,14))
