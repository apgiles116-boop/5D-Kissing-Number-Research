"""Exact checks for coplanar Type-E label-free tomography.
Universal lift lemma is proved analytically in the companion research note.
"""
from fractions import Fraction as F
from math import sqrt
import sympy as sp

c=F(73,200)
eps=F(7,100000)
n=16
sigma2_sq=eps*c*c/F(4*n)
minor_sq=F(9,4096)*eps*c**4
assert sigma2_sq == F(37303,256000000000)
assert sigma2_sq > F(3,8000)**2
assert minor_sq == F(1789089183,655360000000000000)
assert minor_sq > F(1,40000**2)

# Exact example: two perpendicular rays have positive-definite 2D frame
# but their quadratic lifts span only a 2D subspace of Sym^2(R^2).
w=[(F(1,2),F(0)),(F(0),F(1,2))]*2
V=[sp.Matrix([(x*x+y*y)/sp.sqrt(2),(x*x-y*y)/sp.sqrt(2),
              sp.sqrt(2)*x*y]) for x,y in w]
R=sum((v*v.T for v in V),sp.zeros(3))
assert R.rank()==2
assert R.eigenvals()=={sp.Rational(1,8):2,sp.Integer(0):1}
S=sum((sp.Matrix([[x*x,x*y],[x*y,y*y]]) for x,y in w),sp.zeros(2))
assert S==sp.eye(2)/2

t=sp.symbols('t',real=True)
assert sp.simplify(1-(1+t*t)/2-(1-t)/4-(1-t)*(2*t+1)/4)==0

M=sp.diag(sp.Rational(3,5),1,1)
assert M.is_positive_definite and (sp.eye(3)-M).is_positive_semidefinite
print('PASS: exact thresholds, minor constant, rank-two witness, scalar identity, Q metric')
print('sigma2(D) >',sqrt(float(sigma2_sq)))
print('minor sum >',float(minor_sq))
