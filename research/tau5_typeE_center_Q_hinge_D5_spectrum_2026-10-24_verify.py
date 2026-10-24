#!/usr/bin/env python3
"""Exact algebraic checks; see accompanying note for quantified proofs."""
import sympy as S
b,x=S.symbols("b x", real=True)
r=(S.sqrt(33)-1)/8
D=(b+S.Rational(1,2))**2*(1-b*b)
Dmax=(207+33*S.sqrt(33))/512
C=1/Dmax
assert S.simplify(D.subs(b,r)-Dmax)==0
assert S.simplify(S.diff(D,b)+(2*b+1)*(4*b*b+b-2)/2)==0
assert S.simplify(C-(S.Rational(46,3)-S.Rational(22,9)*S.sqrt(33)))==0
p=S.Rational(39,64)*x*x-S.Rational(3,16)*x
assert S.factor((x-S.Rational(1,4))**2-p)==(5*x-2)**2/64
assert S.simplify(p-x*(39*x-12)/64)==0
I=S.eye(5)
vs=[]
for i in range(5):
    for j in range(i+1,5):
        for sign in (1,-1):
            v=S.zeros(5,1)
            v[i]=1/S.sqrt(2)
            v[j]=sign/S.sqrt(2)
            vs.append(v)
Qs=[v*v.T-I/5 for v in vs]
K=S.Matrix(20,20,lambda i,j:S.trace(Qs[i]*Qs[j]))
assert K.rank()==14
assert K.eigenvals()=={S.Rational(3,2):4,S.Integer(1):10,S.Integer(0):6}
assert S.trace(K)==16 and S.trace(K*K)==19
assert sum(Qs,S.zeros(5,5))==S.zeros(5,5)
d=S.symbols("d0:4",real=True)
o=S.symbols("o0:10",real=True)
V=S.diag(*d,-sum(d))
pos=0
for i in range(5):
    for j in range(i+1,5):
        V[i,j]=V[j,i]=o[pos]
        pos+=1
lhs=S.expand(sum(S.trace(Q*V)**2 for Q in Qs))
Vdiag=S.diag(*[V[i,i] for i in range(5)])
Voff=V-Vdiag
rhs=S.Rational(3,2)*S.trace(Vdiag*Vdiag)+S.trace(Voff*Voff)
assert S.simplify(lhs-rhs)==0
print("PASS: center hinge denominator, polynomial minorant, Q spectrum and frame identity")
print("C* =",S.N(C,16))
print("Q spectrum =",K.eigenvals())
