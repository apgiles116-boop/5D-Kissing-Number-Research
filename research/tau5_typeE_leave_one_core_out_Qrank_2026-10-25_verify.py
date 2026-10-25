"""Exact rational checks: signed 19-line Q-rank and four core-deletion counts."""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational, symbols, expand
S,T=symbols('S T')
assert expand(F(1,4)*S*S-F(1,5)*(F(3,4)*S+T)**2
  -(F(11,80)*(S-F(12,11)*T)**2-F(4,11)*T*T))==0
assert F(1)-F(4,11)*F(19,7)==F(1,77)
c=F(5,16)
assert (5*c*c+F(25,14)*c*c)/2==F(2375,7168)
O=list(range(16));C=list(range(16,20))
sets=[set(O)|set(T) for T in combinations(C,3)]
assert all(sum(i in X and j in X for X in sets)==4 for i,j in combinations(O,2))
assert all(sum(i in X and j in X for X in sets)==3 for i in O for j in C)
assert all(sum(i in X and j in X for X in sets)==2 for i,j in combinations(C,2))
V=[]
for i,j in combinations(range(5),2):
 for s in (-1,1):
  v=[0]*5;v[i]=1;v[j]=s;V.append(v)
for omit in C:
 W=[V[i] for i in range(20) if i!=omit]
 dots=Matrix(19,19,lambda i,j:Rational(sum(W[i][k]*W[j][k] for k in range(5)),2))
 K=Matrix(19,19,lambda i,j:dots[i,j]**2-Rational(1,5))
 E=Matrix(19,19,lambda i,j:Rational(1,4)-dots[i,j]**2 if i!=j else 0)
 assert K.rank()<=14 and E.trace()==0
 assert sum(E[i,j]**2 for i in range(19) for j in range(i+1,19))>=Rational(2375,7168)
q=F(819,10000);u=q-F(1,16)
assert u==F(97,5000) and F(7,50)**2>u
t=F(25,256)+u+u*u+2*u*F(7,50)
assert t==F(12286461,100000000)
assert F(2375,7168)-t/2==F(755723921,2800000000)
print('PASS: exact SOS, 19-line Q-rank constant, four-subset counting, D5 examples, rational core bound')
