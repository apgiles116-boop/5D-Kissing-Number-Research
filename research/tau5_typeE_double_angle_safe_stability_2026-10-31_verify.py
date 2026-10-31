"""Exact SymPy checks for Type-E double-angle and safe leakage theorems.
Tests supplement analytic proofs; synthetic matrices are not Type-E codes.
"""
import sympy as S
from itertools import combinations

R=S.Rational
Astar=R(383,504)
assert S.simplify(9*(1-Astar)**2-R(1,2))==R(529,28224)

L=R(3,20)
F=lambda a,l: l*l/2+(16-a-l)**2/3-(76-a+a*a)
assert S.simplify(F(Astar,L))==R(92579,952560)
assert F(Astar,L)>0
Lroot=(7681-S.sqrt(55944906))/1260
assert S.simplify(F(Astar,Lroot))==0
assert S.simplify(Lroot-L)>0

# Exact four-core planar endpoint-feasible local witness.
t=R(5,6)
units=[S.Matrix([1,0]), S.Matrix([R(3,5),R(4,5)]),
       S.Matrix([0,1]), S.Matrix([-R(3,5),R(4,5)])]
z=[S.sqrt(t)*v for v in units]
m=[sg*S.sqrt(R(1,6)) for sg in [1,-1,1,-1]]
for i,j in combinations(range(4),2):
    c=m[i]*m[j]
    d=S.simplify(z[i].dot(z[j]))
    assert S.simplify(R(1,2)-c-abs(d))>=0
assert sum(v*v for v in m)==R(2,3)

def wedge_for_axes(p,q):
    r=[S.expand(v.dot(p)**2) for v in z]
    s=[S.expand(v.dot(q)**2) for v in z]
    return S.simplify(sum((r[i]*s[j]-r[j]*s[i])**2 for i,j in combinations(range(4),2)))

for p,q in [(S.Matrix([1,0]),S.Matrix([0,1])),
            (S.Matrix([R(3,5),R(4,5)]),S.Matrix([-R(4,5),R(3,5)])),
            (S.Matrix([R(5,13),R(12,13)]),S.Matrix([-R(12,13),R(5,13)]))]:
    assert wedge_for_axes(p,q)>=R(81,2048)
assert wedge_for_axes(S.Matrix([1,0]),S.Matrix([0,1]))==R(433,432)

for p,q in [(S.Matrix([1,0]),S.Matrix([0,1])),
            (S.Matrix([R(3,5),R(4,5)]),S.Matrix([-R(4,5),R(3,5)]))]:
    x=[S.simplify((v.dot(p)**2-v.dot(q)**2)/t) for v in z]
    variance=S.simplify(sum((x[i]-x[j])**2 for i,j in combinations(range(4),2)))
    assert variance>=R(1,2)

# 16 safe D5 lines check the exact 120-pair frame identity.
roots=[]
for i,j in combinations(range(5),2):
    for sign in [1,-1]:
        v=S.zeros(5,1)
        v[i]=1/S.sqrt(2)
        v[j]=sign/S.sqrt(2)
        roots.append(v)
I=roots[4:]
assert len(I)==16
Qsum=S.zeros(5,5)
Rsum=S.Integer(0)
for v in I:
    Qsum+=v*v.T
for i,j in combinations(range(16),2):
    d=S.simplify(I[i].dot(I[j]))
    assert abs(d)<=R(1,2)
    Rsum+=R(1,4)-d*d
assert S.simplify(S.trace(Qsum*Qsum)-(76-2*Rsum))==0
for axes in [(0,1),(0,4),(2,3)]:
    l=sum(S.simplify(v[axes[0]]**2+v[axes[1]]**2) for v in I)
    assert S.simplify(F(0,l))<=0
    assert l>R(3,20)

# Exact two-ray Cauchy-Binet test; no endpoint-feasibility claim.
pvals=[R(i,11) for i in range(1,9)]
qvals=[R(i,13) for i in range(1,9)]
r=[R(1,5),R(2,5),R(3,5),R(4,5)]
s=[R(4,7),R(3,7),R(2,7),R(1,7)]
D=S.Matrix([[x*x*v for v in r] for x in pvals]+[[y*y*v for v in s] for y in qvals])
rho=sum(x**4 for x in pvals)
sigma=sum(y**4 for y in qvals)
wedge=sum((r[c]*s[d]-r[d]*s[c])**2 for c,d in combinations(range(4),2))
minors=sum((D[i,c]*D[j,d]-D[i,d]*D[j,c])**2
           for i,j in combinations(range(16),2) for c,d in combinations(range(4),2))
assert S.simplify(minors-rho*sigma*wedge)==0
assert D.rank()==2

print("PASS: exact rational wedge, safe leakage, D5 frame and Cauchy-Binet checks")
print("Leakage lower root:",Lroot,"approx",S.N(Lroot,15))
print("Core wedge witness:",wedge_for_axes(S.Matrix([1,0]),S.Matrix([0,1])))
print("Minimum core wedge:",R(81,2048))
print("Synthetic two-ray minor sum:",minors)
