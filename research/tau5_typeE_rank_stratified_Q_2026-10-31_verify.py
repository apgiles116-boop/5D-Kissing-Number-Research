#!/usr/bin/env python3
"""Exact SymPy verification: Type-E isolated Q rank stratification (2026-10-31)."""
import sympy as s
from itertools import combinations, product

I5=s.eye(5)
roots=[]
for i,j in combinations(range(5),2):
    for sign in (+1,-1):
        v=s.zeros(5,1); v[i]=1; v[j]=sign
        roots.append(((i,j,sign), v/s.sqrt(2)))
Q={label:s.simplify(v*v.T-I5/5) for label,v in roots}
core=[(0,j,+1) for j in range(1,5)]
iso=[lab for lab,_ in roots if lab not in core]
assert len(iso)==16
K=s.Matrix(16,16,lambda i,j:s.trace(Q[iso[i]]*Q[iso[j]]))
lam=s.symbols('lam')
char=s.factor(K.charpoly(lam).as_expr())
expected=lam**2*(lam-1)**6*(4*lam**2-7*lam+2)**3*(20*lam**2-31*lam+6)/1280
assert s.factor(char-expected)==0
assert K.rank()==14
assert s.expand(char).coeff(lam,2)==s.Rational(3,80)

l1=(31-s.sqrt(481))/40
l2=(7-s.sqrt(17))/8
l3=(31+s.sqrt(481))/40
l4=(7+s.sqrt(17))/8
assert 0<l1<l2<1<l3<l4
thresholds={13:l1,12:l1+l2,11:l1+2*l2,10:l1+3*l2,9:l1+3*l2+1}
for r, bound in thresholds.items():
    print('rank<=',r,' E2 >= ',bound,' ~= ',s.N(bound,14))

# Synthetic rational 14-dimensional example: isolated rank 13.
FI=s.zeros(14,16)
for j in range(13): FI[j,j]=1
for j in range(3):
    for k in range(13): FI[k,13+j]=s.Rational((j+2)*(k+1)%7-3,7)
assert FI.rank()==13
FC=s.zeros(14,4)
for j in range(4):
    for k in range(13): FC[k,j]=s.Rational((j+1)*(k+3)%11-5,11)
residual=s.Matrix([s.Rational(2,3),-s.Rational(3,5),s.Rational(5,7),-s.Rational(7,9)])
for j in range(4): FC[13,j]=residual[j]
B=FI[:,:13]
G=B.T*B
Y=B.T*FC
KCC=FC.T*FC
pred=Y.T*G.inv()*Y
R=s.simplify(KCC-pred)
assert R==residual*residual.T
assert R.rank()==1 and R.is_positive_semidefinite
rho=[R[i,i] for i in range(4)]
assert all(s.factor(R[i,j]**2-rho[i]*rho[j])==0 for i,j in combinations(range(4),2))
for i,j,k in combinations(range(4),3):
    assert s.factor(R[i,j]*R[j,k]*R[k,i]-rho[i]*rho[j]*rho[k])==0
completions=set()
for signs in product((-1,1), repeat=3):
    t=s.Matrix([s.sqrt(rho[0])]+[signs[j]*s.sqrt(rho[j+1]) for j in range(3)])
    completions.add(tuple((t*t.T)[i,j] for i,j in combinations(range(4),2)))
assert len(completions)==8

# Rank-12 residual dimension <=2; all 3x3 principal minors vanish.
F12=FI.copy(); F12[12,:]=s.zeros(1,16)
assert F12.rank()==12
C12=FC.copy()
R12=C12.T*(s.eye(14)-s.diag(*([1]*12+[0]*2)))*C12
assert R12.rank()<=2
assert all(R12.extract(list(idx),list(idx)).det()==0 for idx in combinations(range(4),3))
print('D5 characteristic polynomial: PASS')
print('rank-13 eight-sign completion: PASS')
print('rank-12 residual 3x3 minors: PASS')
print('ALL EXACT TESTS PASSED')
