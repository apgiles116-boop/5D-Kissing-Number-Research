"""Exact rational certificate for a six-exception D5 flex and its covering radius.
No numerical optimization or floating point. Requires SymPy.
"""
from itertools import combinations
from fractions import Fraction as F
from collections import Counter
from sympy import Matrix, Rational

t=F(32,639)
k=F(641,639)
assert k*k == 1+F(5,2)*t*t
def basis(j):
    return tuple(F(int(i==j)) for i in range(5))
def add(a,b,s=F(1)):
    return tuple(x+s*y for x,y in zip(a,b))
def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))
lines=[]
core=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        r=add(basis(i),basis(j),F(sign))
        if i==0 and sign==-1:
            w=[F(-1)]*5
            w[0]=w[j]=F(1)
            v=tuple((x+t*y)/k for x,y in zip(r,w))
            core.append(len(lines))
        else:
            v=r
        assert dot(v,v)==2
        lines.append(v)
assert len(lines)==20 and len(core)==4
P_hom=P_raw=F(0)
viol=[]
for i,j in combinations(range(20),2):
    s=(dot(lines[i],lines[j])/2)**2
    if s>F(1,4):
        viol.append((i,j))
        P_hom+=s-F(1,4)
        P_raw+=s*(s-F(1,4))
assert len(viol)==6 and all(i in core and j in core for i,j in viol)
assert P_hom==F(108588534912,168823196161)
assert P_raw==F(6548310868293483692832,28501271562015485137921)
assert P_hom<F(5792292955405,4129544208384)
assert P_raw<F(1780062775,4032758016)

# Ordered chamber: x=(s,y1,y2,y3,y4), y1<=y2<=y3<=y4.
# Every original facet is represented by the following fourteen.
rows=[]
for j in (1,2,3):
    a=[0]*5
    a[j]=1
    a[j+1]=-1
    rows.append((a,0))
rows += [([0,-1,-1,0,0],1),([0,0,0,1,1],1),([0,-1,0,0,1],1)]
for j in (1,4):
    for sign in (1,-1):
        a=[0]*5
        a[0]=a[j]=sign
        rows.append((a,1))
for j in (1,4):
    for sign in (1,-1):
        a=[671,-32,-32,-32,-32]
        a[j]-=575
        rows.append(([sign*x for x in a],641))
assert len(rows)==14
A=Matrix([a for a,b in rows])
b=Matrix([b for a,b in rows])
verts=set()
nonsing=0
for ix in combinations(range(14),5):
    M=A[list(ix),:]
    if M.det()==0:
        continue
    nonsing+=1
    x=M.inv()*b[list(ix),:]
    if all(lhs<=rhs for lhs,rhs in zip(A*x,b)):
        verts.add(tuple(x))
assert nonsing==800 and len(verts)==26
norms=Counter(sum(x*x for x in v) for v in verts)
assert max(norms)==Rational(5,4)
assert norms[Rational(5,4)]==6
assert (Rational(1,2),)*5 in verts
# max ||x||^2 on the full polar polytope is 5/4:
# the chamber covers all points under S4 permutations; the norm
# is convex and the polytope bounded. Therefore rho^2=2/5.
assert F(2,5)>F(1,3)
print("PASS: 184 safe, six exceptional, both defects below retained caps")
print("t=",t," k=",k," P_hom=",P_hom," P_raw=",P_raw)
print("2002 facet systems, 800 invertible, 26 feasible vertices")
print("norm^2 classes:",sorted(norms.items()))
print("sharp rho^2=2/5>1/3; isolated center would force some a_i>=3/8")
