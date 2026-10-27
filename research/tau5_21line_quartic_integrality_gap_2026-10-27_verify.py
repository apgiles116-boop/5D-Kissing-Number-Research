#!/usr/bin/env python3
"""Exact checks for the 21-line quartic-defect gap.
The universal harmonic PSD is proved analytically in the companion note;
finite test configurations are NOT a substitute for that proof.
"""
import itertools
import sympy as S

N = 21
pstar = (S.sqrt(15)-3)/80
qstar = (2*S.sqrt(15)-5)/40
assert S.simplify(qstar**2 - (S.Rational(1,64)-pstar)) == 0
assert S.simplify(4*pstar + S.Rational(1,8) - qstar - S.Rational(1,10)) == 0
assert pstar > 0 and pstar < S.Rational(1,80)
assert S.simplify(S.Rational(168,5)-S.Rational(67,2)) == S.Rational(1,10)

roots=[]
for i,j in itertools.combinations(range(5),2):
    for sign in (+1,-1):
        v=S.zeros(5,1)
        v[i]=S.sqrt(S.Rational(1,2))
        v[j]=sign*S.sqrt(S.Rational(1,2))
        roots.append(v)

I=S.eye(5)
Q=[v*v.T-I/5 for v in roots]
B=S.Matrix(20,20,lambda i,j:S.trace(Q[i]*Q[j]))
assert B.eigenvals()=={S.Rational(3,2):4,S.Integer(1):10,S.Integer(0):6}
assert B.rank()==14
assert sum(Q,S.zeros(5,5))==S.zeros(5,5)

# Concrete 21-line exact test: D5 root lines plus e1.
lines=roots+[I[:,0]]
F=sum((v*v.T for v in lines),S.zeros(5,5))
V=S.trace((F-S.Rational(21,5)*I)**2)
P=E=S.Integer(0)
for i,j in itertools.combinations(range(N),2):
    x=S.expand((lines[i].dot(lines[j]))**2)
    defect=S.expand(x*(x-S.Rational(1,4)))
    if defect>0:
        P+=defect
    elif defect<0:
        E-=defect
K=sum((lines[i].dot(lines[j]))**4 - S.Rational(2,3)*(lines[i].dot(lines[j]))**2 + S.Rational(1,21)
      for i in range(N) for j in range(N))
assert V==S.Rational(4,5)
assert P==1 and E==0
assert S.simplify(K)==S.Rational(5,3)
assert S.simplify(P-E-S.Rational(5,24)*V-K/2)==0

# Independent 21-line exact polynomial identity test.
vecs=[]
for i in range(21):
    v=S.Matrix([S.Rational((i+2*j*j+3*j+1)%11-5,7) for j in range(5)])
    if v.dot(v)==0: v[0]=1
    vecs.append(v/S.sqrt(v.dot(v)))
F2=sum((v*v.T for v in vecs),S.zeros(5,5))
V2=S.trace((F2-S.Rational(21,5)*I)**2)
D2=sum((vecs[i].dot(vecs[j]))**4 - S.Rational(1,4)*(vecs[i].dot(vecs[j]))**2
       for i,j in itertools.combinations(range(21),2))
K2=sum((vecs[i].dot(vecs[j]))**4-S.Rational(2,3)*(vecs[i].dot(vecs[j]))**2+S.Rational(1,21)
       for i in range(21) for j in range(21))
assert S.simplify(D2-S.Rational(5,24)*V2-K2/2)==0
print('PASS: exact quartic identity, D5 Q spectrum, and gap constant')
print('pstar =',pstar,'~',pstar.evalf(16))
