#!/usr/bin/env python3
"""Exact rational checks for the rank-13 phase-retrieval refinement.
Synthetic data only: no claim of Type-E endpoint feasibility.
"""
from itertools import product, combinations
import sympy as S

I5 = S.eye(5)

def Q(z):
    z=S.Matrix(z)
    w=(z.T*z)[0]
    return z*z.T-w*I5/5

def dot(A,B):
    return S.trace(A*B)

def coords(A):
    return S.Matrix([A[i,i] for i in range(4)]+
                    [A[i,j] for i in range(5) for j in range(i+1,5)])

def rankQ(vs):
    return S.Matrix.hstack(*(coords(Q(v)) for v in vs)).rank()

def rankone(A,w):
    return A*A-S.Rational(3,5)*w*A-S.Rational(4,25)*w*w*I5

def zero(A):
    return all(S.simplify(x)==0 for x in A)

iso2=[
(1,1,-2,-2,-2),(1,1,-2,-2,-1),(1,1,-2,-2,0),
(1,1,-2,-1,-2),(1,1,-2,-1,-1),(1,1,-2,0,-2),
(1,1,-1,-2,-2),(1,1,-1,-2,-1),(1,1,-1,-1,-2),
(1,1,0,-2,-2),(1,-1,-2,-2,-2),(1,-1,-2,-2,-1),
(1,-1,-2,-1,-2),(1,-1,-2,-1,-1),(1,-1,-2,-1,0),
(1,-1,-2,-1,1)]
N2=S.diag(1,-1,0,0,0)
assert rankQ(iso2)==13 and N2.rank()==2
assert all(dot(Q(v),N2)==0 for v in iso2)
cores=[S.Matrix([S.Rational(a,c),S.Rational(b,c),0,0,0])
       for a,b,c in [(3,4,5),(5,12,13),(8,15,17),(20,21,29)]]
for z in cores:
    w=z.dot(z); P=Q(z)
    t=dot(P,N2)/dot(N2,N2); L=P-t*N2
    zp=S.Matrix([z[1],z[0],0,0,0])
    assert w==1 and t!=0 and Q(zp)==L-t*N2
    assert zero(rankone(L+t*N2,w))
    assert zero(rankone(L-t*N2,w))
    assert all(S.Matrix(v).dot(z)**2==S.Matrix(v).dot(zp)**2
               for v in iso2)
out=set()
for signs in product((0,1),repeat=3):
    zs=[cores[0]]
    for z,flip in zip(cores[1:],signs):
        zs.append(S.Matrix([z[1],z[0],0,0,0]) if flip else z)
    out.add(tuple(zs[i].dot(zs[j])**2
                  for i,j in combinations(range(4),2)))
assert len(out)==8
print("Rank-two missing Q direction: eight rank-one completions PASS")

iso4=[
(1,1,1,1,0),(2,2,2,2,-1),(1,1,1,1,-1),
(2,1,2,1,0),(2,1,2,1,-1),(1,0,1,0,0),
(1,1,-1,1,0),(4,4,-4,4,-1),(2,1,-1,2,0),
(4,2,-2,4,-1),(1,0,0,1,0),(5,5,-1,7,0),
(10,5,2,11,0),(10,5,2,11,-1),(10,5,2,11,-2),
(5,0,3,4,0)]
N4=S.diag(1,1,-1,-1,0)
assert rankQ(iso4)==13 and N4.rank()==4
assert all(dot(Q(v),N4)==0 for v in iso4)
z=S.Matrix([1,0,0,0,0]); w=z.dot(z)
P=Q(z); t=dot(P,N4)/dot(N4,N4); L=P-t*N4
assert t!=0 and zero(rankone(L+t*N4,w))
assert not zero(rankone(L-t*N4,w))
B0=L*L+t*t*N4*N4-S.Rational(3,5)*w*L-S.Rational(4,25)*w*w*I5
B1=L*N4+N4*L-S.Rational(3,5)*w*N4
assert not zero(B1)
assert S.simplify(t+dot(B0,B1)/dot(B1,B1))==0
assert zero(B0+t*B1)
print("Rank-four missing Q direction: unique sign selector PASS")

x=S.Matrix([1,2,0,0,0]); y=S.Matrix([2,1,0,0,0])
assert x.dot(x)==y.dot(y)
for v in iso2:
    v=S.Matrix(v)
    assert S.expand(v.dot(x)**2-v.dot(y)**2)==S.expand(v.dot(x-y)*v.dot(x+y))
assert S.simplify((x-y).dot(x-y)*(x+y).dot(x+y)-
                  2*dot(Q(x)-Q(y),Q(x)-Q(y)))==0
print("Norm-aware phase-retrieval identities PASS")

# Exact algebra behind the universal 8-subset trace-square no-go.
W=S.Rational(16); U=S.Rational(16)
Rmin=W*W/10-U/2
avg_upper=S.Rational(7,120)*W*W-S.Rational(13,30)*U-S.Rational(7,15)*Rmin
assert avg_upper==S.Rational(7,600)*W*W-U/5==-U/75
print("Uniform 8-subset trace-square no-go arithmetic PASS")
print("ALL EXACT TESTS PASSED")
