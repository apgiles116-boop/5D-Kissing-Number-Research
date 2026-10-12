"""Exact rational Q-Gram counterexample: nullity 6 with no orthogonal pairs."""
from fractions import Fraction as F
from itertools import product
import random
import sympy as s

def sphere(t):
    sq=sum(k*k for k in t)
    den=1+sq
    return tuple([F(1-sq,den)]+[F(2*k,den) for k in t])
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))
def qvec(v):
    # 14 coordinates for a traceless 5x5 symmetric matrix
    return [v[i]*v[i]-F(1,5) for i in range(4)]+[
        v[i]*v[j] for i in range(5) for j in range(i+1,5)
    ]
vec=[]; params=[]
candidates=list(product(range(-2,3),repeat=4))
random.Random(1729).shuffle(candidates)
for t in candidates:
    v=sphere(t)
    if all(dot(v,u)!=0 and abs(dot(v,u))!=1 for u in vec):
        vec.append(v);params.append(t)
    if len(vec)==20:break
assert len(vec)==20
assert all(dot(v,v)==1 for v in vec)
assert all(dot(vec[i],vec[j])!=0 for i in range(20) for j in range(i+1,20))
mat=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in qvec(v)] for v in vec])
assert mat.rank()==14
print("PASS: 20 rational unit directions; all 190 pairs nonorthogonal")
print("PASS: Q-rank=14, Q-nullity=6")
print("integer quadruples:",params)
