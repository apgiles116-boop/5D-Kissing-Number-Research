"""Exact algebra/rational verifier for the 2026-11-01 coplanar Type-E Q-minor theorem.
Checks proof arithmetic and sample determinant identities; does not enumerate Type-E codes.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

D=F(1780062775,4032758016)
eps=F(5,18)
close_two=F(1,2)-F(3,4)*eps**2
assert close_two==F(191,432)
assert close_two-D==F(2939033,4032758016)
s0=eps-eps**3/6
assert s0==F(9595,34992)
d0=F(6,5)*F(3,4)**6*s0**6
assert d0==F(156062970888364764003125,1719070799748422591028658176)
assert d0>F(9,100000)
gap=F(25,32)*d0
assert gap==F(3901574272209119100078125,55010265591949522912917061632)
assert gap>F(7,100000)

def triple(vectors):
    ts=[sum(x*x for x in v) for v in vectors]
    def dot(i,j): return sum(vectors[i][k]*vectors[j][k] for k in range(2))
    K=sp.Matrix(3,3,lambda i,j:dot(i,j)**2-ts[i]*ts[j]/5)
    wedge=sp.prod(ts[i]*ts[j]-dot(i,j)**2 for i,j in combinations(range(3),2))
    assert sp.factor(K.det()-sp.Rational(6,5)*wedge)==0

examples=[
    [(1,0),(0,1),(1,1)],
    [(sp.Rational(3,4),sp.Rational(1,5)),(sp.Rational(1,2),sp.Rational(-3,4)),(sp.Rational(-2,3),sp.Rational(4,5))],
    [(1,2),(2,3),(3,5)],
    [(1,0),(2,0),(0,1)],
]
for example in examples:
    triple([(sp.Rational(x),sp.Rational(y)) for x,y in example])

vecs=[sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([sp.Rational(3,5),sp.Rational(4,5)]),sp.Matrix([sp.Rational(5,13),sp.Rational(12,13)])]
ts=[v.dot(v) for v in vecs]
K=sp.Matrix(4,4,lambda i,j:vecs[i].dot(vecs[j])**2-ts[i]*ts[j]/5)
assert K.det()==0 and K.rank()==3
for T in combinations(range(4),3):
    triple([tuple(vecs[i]) for i in T])

assert F(19,11)**2<3
assert F(11,12)*(F(1,2)-D)-F(1,19)==F(996996505,919468827648)
print("PASS: exact close-pair margin, Q-triple determinant, rank 3, spectral bound, A_C>1/19")
