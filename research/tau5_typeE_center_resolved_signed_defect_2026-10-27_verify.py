#!/usr/bin/env python3
"""Exact rational checks for center-resolved Type-E signed-defect bounds.
Inherited Type-E graph/endpoint lemmas are assumptions, not verified here.
"""
import sympy as S
Q=S.Rational
t,R,L,V=S.symbols('t R L V', real=True)
Amax=Q(383,504)
rem=Amax-3*Q(1,4)
Rmax=S.factor(3*Q(1,36)+rem/(16*(1-rem)**2))
assert rem==Q(5,504) and Rmax==Q(250891,2988012)
assert Rmax<Q(1,10)
q=Q(5,12)*t-Q(20,21)-R
g=-Q(5,14)+Q(25,96)*(t-4)**2+Q(21,16)*q**2
tstar=4*(7*R+20)/25
f=R*(7*R-10)/10
assert S.simplify(g-Q(125,256)*(t-tstar)**2-f)==0
assert S.factor(f.subs(R,Rmax))==-Q(7056029129753,89282157121440)
assert Q(12,5)*(Q(20,21)+Rmax)<Q(5,2)
assert Q(25,96)*Q(9,4)>Q(5,14)
assert tstar.subs(R,Rmax)<Q(37,10)
assert q.subs({t:Q(37,10),R:Rmax})>0
assert S.factor(g.subs({t:Q(37,10),R:Rmax}))==Q(274102462207,190468601859072)
assert S.factor(g.subs({t:4,R:Rmax}))==Q(7824330390487,47617150464768)
F=(16-Q(5,4)*L)**2/13+Q(25,16)*L**2
assert S.simplify(F-(Q(128,7)+(35*L-32)**2/Q(728)))==0
assert S.simplify((F-19+Q(3,20)*V)/2-
 (-Q(5,14)+Q(3,40)*V+(35*L-32)**2/Q(1456)))==0
roots=[]
for i in range(5):
 for j in range(i+1,5):
  for sign in (1,-1):
   v=S.zeros(5,1)
   v[i]=1/S.sqrt(2);v[j]=sign/S.sqrt(2)
   roots.append(v)
assert len(roots)==20
frame=S.zeros(5)
for v in roots: frame+=v*v.T
assert frame==4*S.eye(5)
B=S.Matrix(20,20,lambda i,j:S.simplify((roots[i].dot(roots[j]))**2-Q(1,5)))
assert B.rank()==14
assert S.simplify(sum(B[i,j]**2 for i in range(20) for j in range(20)))==19
print("PASS: exact algebra, sharp energy allocation, defect floors, rank-13 Schur and D5 Q rank")
