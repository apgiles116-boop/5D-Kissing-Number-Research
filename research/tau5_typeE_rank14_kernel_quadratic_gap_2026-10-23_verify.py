#!/usr/bin/env python3
"""Exact SymPy verification for the rank-14 Type-E Q-Gram gap."""
import sympy as s
from itertools import combinations
I=s.eye(5)
W=[]
for i,j in combinations(range(5),2):
    for sg in (1,-1):
        w=s.zeros(5,1)
        w[i]=s.sqrt(2)/2
        w[j]=sg*s.sqrt(2)/2
        W.append(w)
Q=[w*w.T-I/5 for w in W]
G0=s.Matrix(20,20,lambda i,j:s.trace(Q[i]*Q[j]))
assert G0.eigenvals()=={s.Rational(3,2):4,s.Integer(1):10,s.Integer(0):6}
assert G0*s.ones(20,1)==s.zeros(20,1)
q,a=s.symbols('q a',real=True)
slack=q*(s.Rational(1,4)-q)+s.Rational(2,5)*a*(s.Rational(1,4)-q)+s.Rational(1,25)*a*(s.Rational(1,4)-a)
assert s.expand((q-(1-a)/5)**2-(s.Rational(1,25)-s.Rational(3,20)*q+s.Rational(3,100)*a-slack))==0
B=s.Rational(383,504)
d=s.Rational(5,14)
rem=30-3*B-40*d
assert rem==s.Rational(2257,168)>0
assert s.factor(rem**2-(30*d)**2/(1-d))==s.Rational(54049,28224)>0
print('PASS: D5 Q-Gram spectrum; exact slack identity; strict d>5/14 certificate')
