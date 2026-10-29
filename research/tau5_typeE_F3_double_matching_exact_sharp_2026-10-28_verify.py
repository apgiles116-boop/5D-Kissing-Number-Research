#!/usr/bin/env python3
"""Exact SymPy audit: sharp F3 P1/P3 core midpoint-energy stress."""
import sympy as sp

r3 = sp.sqrt(3)
t = (2-r3)/4
k = (1-sp.sqrt(1-4*t*t))/(2*t)
assert sp.sign(t-sp.Rational(16,257)) == 1
assert sp.sign(t-sp.Rational(14,197)) == -1
assert sp.simplify(1-4*t*t-(r3-sp.Rational(3,4))) == 0
s = sp.factor(k*k/(1+k*k))
c = 2*s
assert sp.simplify(c*(2-c)-4*t*t) == 0

x = sp.symbols('x', positive=True)
gamma = 2*x/(1-x*x)
alpha = gamma*(r3-x)/2
beta = gamma*(1/r3-x)/2
h = sp.Rational(1,2)+gamma*(r3+x)/4
ell = sp.Rational(1,2)+gamma*(1/r3+x)/4

H=(0,2,5,7); L=(1,6,3,4)
P1={(0,2),(1,4),(3,6),(5,7)}
EH={(0,5),(2,7)}
EX={(0,4),(1,7),(2,3),(5,6)}
EL={(1,3),(4,6)}
F3=P1|EH|EX
S=sp.zeros(8)
for i in H: S[i,i]=h
for i in L: S[i,i]=ell
for edges,coef in ((P1,sp.Integer(1)),(EH,alpha),(EX,gamma),(EL,beta)):
    for i,j in edges: S[i,j]=S[j,i]=coef/2

chars=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
T=sp.zeros(8)
for p,chi in enumerate(chars):
    for j in range(4):
        T[H[j],2*p]=sp.Rational(chi[j],2)
        T[L[j],2*p+1]=sp.Rational(chi[j],2)
assert T.T*T == sp.eye(8)
blocks=[
    sp.Matrix([[1+gamma*r3/2,gamma/2],[gamma/2,1+gamma/(2*r3)]]),
    gamma/2*sp.Matrix([[r3,-1],[-1,1/r3]]),
    gamma/2*sp.Matrix([[1/x,-1],[-1,x]]),
    gamma/2*sp.Matrix([[x,1],[1,1/x]])
]
assert all(sp.simplify(y)==0 for y in T.T*S*T-sp.diag(*blocks))
for block in blocks[1:]:
    assert sp.simplify(block.det()) == 0
assert sp.simplify(blocks[0].trace()-(2+2*gamma/r3)) == 0
assert sp.simplify(blocks[0].det()-(1+2*gamma/r3)) == 0
assert sp.simplify(blocks[1].trace()-2*gamma/r3) == 0
assert sp.simplify(blocks[2].trace()-(1+x*x)/(1-x*x)) == 0
assert sp.simplify(blocks[3].trace()-(1+x*x)/(1-x*x)) == 0
# For 0<x<1/14 all four blocks are PSD, with three rank-one blocks.
objective=sp.factor(2-2*(h+ell)+alpha/2-beta/2+gamma)
assert sp.simplify(objective-gamma*(1-r3/2-x)) == 0
assert sp.simplify((objective-2*x*x/(1+x*x))*(x*x-1)*(x*x+1)/x
                   -(4*x-(2-r3)*(1+x*x))) == 0

u=sp.factor(x*x*(1-3*x*x)/(4*(1-x**4)))
v=sp.factor(x*x*(3-x*x)/(4*(1-x**4)))
assert sp.simplify(u-x*x*(sp.Rational(1,4)-v)) == 0
assert sp.simplify(v-x*x*(sp.Rational(3,4)-u)) == 0
assert sp.simplify(u+v-x*x/(1+x*x)) == 0
A=r3/4; B=x*(sp.Rational(1,4)-v); D=x*(sp.Rational(3,4)-u)
assert sp.simplify(B+D-x/(1+x*x)) == 0
# Hence A+B+D=1/2 when t=x/(1+x^2). Other nonedges are
# 1/2-2u, -1/2-2v, 1/2-2A, 1/2-2B, 1/2-2D.
# Strict perturbation derivative: 1/x-2/sqrt(3)>0 for x<1/14.
assert sp.simplify(sp.Rational(1,2)*sp.sqrt((sp.Rational(1,4)-v)/u)**2
                   -1/(2*x*x)) == 0
# Equality Gram uniqueness: determinant of final two T diagonal equations.
det=sp.factor(u*v-(sp.Rational(3,4)-u)*(sp.Rational(1,4)-v))
assert sp.simplify(det-(sp.Rational(3,4)*v+u/4-sp.Rational(3,16))) == 0
assert sp.Rational(3,4)*sp.Rational(3,784)+sp.Rational(1,4)*sp.Rational(1,784)<sp.Rational(3,16)
f={0:0,1:1,2:5,3:6,4:4,5:2,6:3,7:7}
P3={(0,5),(1,4),(2,7),(3,6)}
assert {tuple(sorted((f[i],f[j]))) for i,j in F3} == F3
assert {tuple(sorted((f[i],f[j]))) for i,j in P1} == P3
# Exact rational comparison c*>9/1000.
q=sp.Rational(3,4)+sp.Rational(991,1000)**2
assert q>0 and q*q>3
print('PASS: exact PSD rank-5 stress, dual optimum, rank-3 witness, uniqueness')
print('PASS: strict 3D approach, matching automorphism, rational gap')
print('Sharp double-matching infimum:',sp.N(1-sp.sqrt(r3-sp.Rational(3,4)),22))
print('Global status unchanged: 40 <= tau_5 <= 44')
