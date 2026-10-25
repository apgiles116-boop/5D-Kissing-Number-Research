"""Exact SymPy/Fraction verifier: 16-line Q-rank safe-slack gap, 2026-10-25."""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational, symbols, expand

S,T=symbols("S T")
lhs=F(1,4)*S*S-F(1,5)*(F(3,4)*S+T)**2
rhs=F(11,80)*(S-F(12,11)*T)**2-F(4,11)*T*T
assert expand(lhs-rhs)==0
assert F(1)-F(4,11)*F(8,3)==F(1,33)
assert F(8,7)*F(5,16)**2==F(25,224)

# Sharp K0 lower eigenvalue for b1=b2=3/4 and the remaining b_i=1.
b=[Rational(3,4)]*2+[Rational(1)]*14
K0=Matrix(16,16,lambda i,j:(b[i]**2 if i==j else Rational(1,4))-b[i]*b[j]/5)
x=Matrix([1,-1]+[0]*14)
assert K0*x==Rational(5,16)*x
assert sum(1-bi for bi in b)==Rational(1,2)<=Rational(383,504)

# Independent exact D5 test of Q-rank, E trace, and squared safe slack.
V=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[i],v[j]=1,sign
        V.append(v)
V=V[:16]
dots=Matrix(16,16,lambda i,j:Rational(sum(V[i][k]*V[j][k] for k in range(5)),2))
K=Matrix(16,16,lambda i,j:dots[i,j]**2-Rational(1,5))
E=Matrix(16,16,lambda i,j:Rational(1,4)-dots[i,j]**2 if i!=j else 0)
H=sum((Rational(1,2)-abs(dots[i,j]))**2 for i in range(16) for j in range(i+1,16))
assert K.rank()<=14
assert E.trace()==0
assert E==Matrix(16,16,lambda i,j:Rational(4,5) if i==j else Rational(1,20))-K
assert (E*E).trace()==2*sum(E[i,j]**2 for i in range(16) for j in range(i+1,16))
assert H>Rational(25,224)
print("PASS: exact SOS identity, constants, sharp K0 eigenvalue, and D5 test.")
print("D5 sample Q rank =",K.rank(),"squared outside slack =",H)


# Same-day exact n=15..19 extension.
for n in range(15,20):
    k=n-14
    assert F(1)-F(4*n,77)>0
    assert F(25*n*k,7168)==F(k*n,28)*F(5,16)**2
assert F(25*17*3,7168)==F(1275,7168)

# Exact 17-line D5 test, all pairings raw-safe.
W=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[i],v[j]=1,sign
        W.append(v)
W=W[:17]
K17=Matrix(17,17,lambda i,j:Rational(sum(W[i][k]*W[j][k] for k in range(5)),2)**2-Rational(1,5))
H17=sum((Rational(1,2)-abs(Rational(sum(W[i][k]*W[j][k] for k in range(5)),2)))**2 for i in range(17) for j in range(i+1,17))
assert K17.rank()<=14 and H17>Rational(1275,7168)
print("PASS: exact n=15..19 extension; Type-E n=17 bound 1275/7168.")
