"""Exact rational synthetic check of rank-13 two-ray Type-E bridge.
Not a kissing-code feasibility certificate.
"""
from itertools import combinations,product
from sympy import Matrix,Rational,eye,trace,simplify

v0=[[2,0,2,1,0],[3,0,0,-1,2],[1,0,0,-2,-2],
[3,0,1,1,0],[3,0,0,1,-1],[1,0,-2,-1,-1],
[2,0,2,2,-1],[2,0,2,-2,-2],
[0,2,1,-2,2],[0,3,2,-1,1],[0,2,0,-2,1],
[0,1,2,-2,0],[0,1,1,0,2],[0,3,1,-1,-2],
[0,2,-1,-1,2],[0,2,-2,0,-2]]
I=[Matrix(v)/5 for v in v0]
C=[Matrix(v) for v in [
[Rational(2,5),Rational(4,5),0,0,0],
[Rational(-2,5),Rational(4,5),0,0,0],
[Rational(4,5),Rational(2,5),0,0,0],
[Rational(22,25),Rational(-11,25),0,0,0]]]
Z=I+C
def Q(v):return v*v.T-v.dot(v)*eye(5)/5
def features(v):
 q=Q(v)
 return [q[a,b] for a in range(5) for b in range(a,5)]
assert Matrix([features(v) for v in I]).rank()==13
D=Matrix([[(i.dot(c))**2 for c in C] for i in I])
t=Matrix([c.dot(c) for c in C])
assert D.rank()==2 and D.col_join(t.T).rank()==2
counts=[]
for i,j in combinations(range(16),2):
 n=sum(D[i,c]*D[j,d]!=D[i,d]*D[j,c] for c,d in combinations(range(4),2))
 assert (n>0)==(i<8 and j>=8)
 counts.append(n)
assert sum(counts)==256 and set(counts)=={0,4}
i,j=0,8
c,d=next((c,d) for c,d in combinations(range(4),2)
 if D[i,c]*D[j,d]!=D[i,d]*D[j,c])
det=D[i,c]*D[j,d]-D[i,d]*D[j,c]
alpha=(t[c]*D[j,d]-t[d]*D[j,c])/det
beta=(D[i,c]*t[d]-D[i,d]*t[c])/det
assert alpha>0 and beta>0
assert all(alpha*D[i,k]==C[k][0]**2 and beta*D[j,k]==C[k][1]**2 for k in range(4))
patterns=set()
for e in product([-1,1],repeat=3):
 signs=(1,)+e
 core=[Matrix([signs[k]*abs(C[k][0]),abs(C[k][1]),0,0,0]) for k in range(4)]
 patterns.add(tuple((core[c].dot(core[d]))**2 for c,d in combinations(range(4),2)))
assert len(patterns)==8
assert tuple((C[c].dot(C[d]))**2 for c,d in combinations(range(4),2)) in patterns
a=[1-v.dot(v) for v in Z];A=sum(a);U=sum(x*x for x in a)
T=sum((v*v.T for v in Z),Matrix.zeros(5))
V=trace((T-(20-A)*eye(5)/5)**2)
h=sum(v[0]*v[1] for v in C)
assert h!=0
Vrest=V-2*h*h
assert Vrest>=0
Qall=sum((Z[i].dot(Z[j]))**2 for i,j in combinations(range(20),2))
Qsafe=sum((Z[i].dot(Z[j]))**2 for i,j in combinations(range(20),2)
 if not (i>=16 and j>=16))
Q6=sum((C[i].dot(C[j]))**2 for i,j in combinations(range(4),2))
Rp=sum(v[0]**2 for v in C);Rq=sum(v[1]**2 for v in C)
B=(Rp**2+Rq**2-sum(v.dot(v)**2 for v in C))/2
L=30-3*A+A*A/10-U/2
assert simplify(Qall-L-V/2)==0
assert simplify(Q6-B-h*h)==0
assert simplify(Qsafe-L+B-Vrest/2)==0
print("PASS: rank13; safe rank2; 256 nonzero minors; eight signs; exact frame cancellation")
