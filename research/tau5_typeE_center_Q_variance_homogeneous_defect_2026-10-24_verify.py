"""Exact symbolic/rational checks: center/Q-frame variance and defect tradeoff.

This script checks algebraic identities and rational consequences, not
the universal inequalities by finite sampling.
"""
from fractions import Fraction as F
import itertools
import sympy as sp

x=sp.symbols("x", real=True)
h=x/(16*(1-x)**2)
assert sp.simplify(sp.diff(h,x)-(1+x)/(16*(1-x)**3))==0
assert sp.simplify(sp.diff(h,x,2)-(4+2*x)/(16*(1-x)**4))==0

B=F(383,504)
def hf(a):
    return a/(16*(1-a)**2)
def H(a):
    k=(4*a).numerator//(4*a).denominator
    return F(k,36)+hf(a-F(k,4))

assert H(B)==F(250891,2988012)
A0=F(297,500)
assert H(A0)==F(17159,273612)
d0=F(25,28)-F(5,4)*H(A0)
assert d0>0
assert d0*d0-F(65,98)==F(107327905,1197816424704)

# Exact spectral variance / homogeneous-defect identity.
S2,S4,E,L,T=sp.symbols("S2 S4 E L T")
V=sp.Rational(68,7)+2*S4-sp.Rational(4,5)*S2
rhs=sp.Rational(5,7)-sp.Rational(3,10)*T+2*E-2*L
assert sp.expand(V.subs(S4,S2/4+E-L).subs(S2,30+T)-rhs)==0

eta=F(25,28)-F(5,4)*H(B)
assert eta==F(65919115,83664336)
Vmin=F(14,13)*eta**2
Lmax=F(5,14)-Vmin/2
assert Vmin==F(4345329722383225,6499741038440832)
assert Lmax==F(42477492561665,1857068868125952)
assert Lmax<F(3,128)
assert F(7,13)*F(25,28)**2-F(5,14)==F(15,208)

# Exact D5 minimax algebra.
a,b=sp.symbols("a b", nonnegative=True)
assert sp.expand((a+b)**2-sp.Rational(4,5)*(a*a+4*b*b)
                 -(a-b)*(a+11*b)/5)==0

# D5 Gram sanity check, independent of the center cap.
v=[]
for i,j in itertools.combinations(range(5),2):
    for sign in (1,-1):
        w=sp.zeros(5,1)
        w[i]=sp.sqrt(2)/2
        w[j]=sign*sp.sqrt(2)/2
        v.append(w)
assert len(v)==20
K=sp.Matrix(20,20,lambda i,j:
            sp.expand((v[i].dot(v[j]))**2-sp.Rational(1,5)))
assert K.rank()==14 and K.trace()==16
assert sp.simplify((K*K).trace()-19)==0
s2=sum((v[i].dot(v[j]))**2
       for i in range(20) for j in range(i+1,20))
s4=sum((v[i].dot(v[j]))**4
       for i in range(20) for j in range(i+1,20))
assert sp.simplify(s2-30)==0
assert sp.simplify(s4-sp.Rational(15,2))==0
assert sp.simplify((K*K).trace()-sp.Rational(128,7)-sp.Rational(5,7))==0

print("PASS: symbolic identities, exact rational certificates, D5 check")
print("H(B) =",H(B))
print("A > 297/500 in the tight/no-normalized-excess subcase")
print("Lminus <=",Lmax,"< 3/128")
