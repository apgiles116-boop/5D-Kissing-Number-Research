"""Exact SymPy verifier for sharp one-edge Type-E center hinge (2026-10-24)."""
import sympy as s

b,a,t=s.symbols("b a t", real=True)
F=a*a-(s.Rational(5,4)-b)*a+(b-s.Rational(1,2))**2
D=s.Rational(9,16)+s.Rational(3,2)*b-3*b*b
f=(s.Rational(5,4)-b-s.sqrt(D))/2
assert s.simplify(F.subs(a,f))==0

# Implicit stationarity of R=f(b)/(b^2-1/4)^2, reduced modulo F.
den=-3*b*b+5*b-s.Rational(1,4)
astat=(6*b-1)*(b-s.Rational(1,2))**2/den
elim=s.factor(F.subs(a,astat))
expected=3*b*(2*b-1)**3*(36*b*b-12*b-5)/(2*(12*b*b-20*b+1)**2)
assert s.simplify(elim-expected)==0

bstar=(1+s.sqrt(6))/6
astar=s.Rational(5,12)-s.sqrt(6)/6
Csharp=(297-108*s.sqrt(6))/25
assert s.simplify(F.subs({a:astar,b:bstar}))==0
assert s.simplify(f.subs(b,bstar)-astar)==0
assert s.simplify(astar/(bstar**2-s.Rational(1,4))**2-Csharp)==0
assert s.limit(f/(b*b-s.Rational(1,4))**2,b,s.Rational(1,2),dir="+")==s.Rational(4,3)
assert s.simplify(f.subs(b,s.Rational(3,4))-s.Rational(1,4))==0
assert s.simplify((f/(b*b-s.Rational(1,4))**2).subs(b,s.Rational(3,4))-s.Rational(64,25))==0

# Rational squared comparisons certify 1.298<Csharp<1.299
# and C_old<1.292, hence Csharp>C_old.
assert 5291**2>6*2160**2
assert 10581**2<6*4320**2
assert 61139**2<33*10659**2

# Exact two-dimensional equality witness.
c2=s.simplify(1-astar-bstar**2)
delta=bstar-s.Rational(1,2)
assert c2.is_positive
assert s.simplify(delta**2*(1+bstar**2/c2)-astar)==0
assert s.simplify(2*astar-1+s.Rational(1,2))<0

# Exact polynomial minorant for the Q-frame corollary.
p=s.Rational(39,64)*t*t-s.Rational(3,16)*t
assert s.factor((t-s.Rational(1,4))**2-p)==(5*t-2)**2/64

print("PASS: sharp coefficient",Csharp)
print("PASS: unique interior stationary point",bstar)
print("PASS: equality witness and polynomial minorant")
