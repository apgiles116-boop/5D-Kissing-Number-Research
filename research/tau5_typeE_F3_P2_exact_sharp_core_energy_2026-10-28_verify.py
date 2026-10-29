"""Exact SymPy verification: sharp F3 all-singleton (P2) midpoint energy."""
from sympy import Matrix, zeros, eye, sqrt, Rational as R, simplify, sqrtdenest, symbols, linear_eq_to_matrix
from itertools import combinations

F3={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
P={(0,4),(1,7),(2,3),(5,6)}
H=(0,2,7,5)
L=(4,3,1,6)
O4={(0,2),(0,5),(2,7),(5,7)}
O2={(1,4),(3,6)}
assert P|O4|O2==F3

h=sqrt(6)/4
v=1/sqrt(2)
u=1/sqrt(6)
a=(sqrt(6)-sqrt(2))/4
b=v-u
ell=(u+v)/2
c0=2-sqrt(2+sqrt(3))
assert simplify(2-2*(h+ell)+a+b/2-c0)==0

S=zeros(8)
for i in range(8):
    S[i,i]=h if i in H else ell
for edges,weight in [(P,R(1,2)),(O4,a/2),(O2,b/2)]:
    for i,j in edges: S[i,j]=S[j,i]=weight

blocks=[]
for lam,mu in [(2,1),(0,-1),(0,-1),(-2,1)]:
    T=Matrix([[h+a*lam/2,R(1,2)],[R(1,2),ell+b*mu/2]])
    blocks.append(T)
    assert T[0,0].is_positive and T[1,1].is_positive
    if (lam,mu)==(2,1): assert simplify(T.det()).is_positive
    else: assert simplify(T.det())==0
assert S.rank()==5
B=blocks[0]-eye(2)/4
assert B[0,0].is_positive and B[1,1].is_positive
assert simplify(B.det()).is_positive
assert all(simplify(T.trace()-R(1,4)).is_positive for T in blocks[1:])

U=zeros(8,3)
for k in range(4):
    cs=(1,0,-1,0)[k]; sn=(0,1,0,-1)[k]; sg=(-1)**k
    i,j=H[k],L[k]
    for d,val in enumerate([cs/sqrt(2),sn/sqrt(2),sg/sqrt(2)]):U[i,d]=val
    for d,val in enumerate([-sqrt(3)*cs/2,-sqrt(3)*sn/2,-R(sg,2)]):U[j,d]=val
G=U*U.T
assert G.rank()==3
assert all(simplify(G[i,i]-1)==0 for i in range(8))
assert all(simplify(sqrtdenest(G[i,j]+sqrt(2+sqrt(3))/2))==0 for i,j in P)
assert all(simplify(G[i,j]+R(1,2))==0 for i,j in O4|O2)
assert all(simplify(G[i,j]-R(1,2)).is_negative for i,j in combinations(range(8),2) if (i,j) not in F3)
assert (S*G).applyfunc(lambda x:simplify(sqrtdenest(x)))==zeros(8)
assert simplify(sqrtdenest(2+sum(G[i,j] for i,j in P)/2-c0))==0

# Equality-case uniqueness: G'=U*T*U^T, with T symmetric.
q=symbols("q0:6")
T=Matrix([[q[0],q[1],q[2]],[q[1],q[3],q[4]],[q[2],q[4],q[5]]])
Gq=U*T*U.T
eq=[Gq[i,i]-1 for i in range(8)]+[Gq[i,j]+R(1,2) for i,j in sorted(O4|O2)]
coef,rhs=linear_eq_to_matrix(eq,q)
assert coef.rank()==6
assert (coef*Matrix([1,0,0,1,0,1])-rhs).applyfunc(simplify)==zeros(len(eq),1)

# A rank-three realization with all ten deep contacts strict.
t=R(1,1000)
alpha=sqrt(R(1,2)-t); beta=sqrt(R(1,2)+t)
gamma=sqrt(R(3,4)+t); delta=sqrt(R(1,4)-t)
Ut=zeros(8,3)
for k in range(4):
    cs=(1,0,-1,0)[k];sn=(0,1,0,-1)[k];sg=(-1)**k
    i,j=H[k],L[k]
    for d,val in enumerate([alpha*cs,alpha*sn,beta*sg]):Ut[i,d]=val
    for d,val in enumerate([-gamma*cs,-gamma*sn,-delta*sg]):Ut[j,d]=val
Gt=Ut*Ut.T
assert all(simplify(Gt[i,i]-1)==0 for i in range(8))
assert all(simplify(Gt[i,j]+R(1,2)).is_negative for i,j in F3)
assert all(simplify(Gt[i,j]-R(1,2)).is_negative for i,j in combinations(range(8),2) if (i,j) not in F3)
assert simplify(2+sum(Gt[i,j] for i,j in P)/2-c0).is_positive
assert simplify(c0-R(17,250)).is_positive
print("PASS: PSD rank 5; positive gap >1/4; exact sharp 3D Gram; unique equality; strict witness.")
print("c* =",c0,"=",c0.evalf(17))
