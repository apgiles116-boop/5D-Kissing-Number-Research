"""Exact rational checks for sharp kernel suppression and the Type-E gap.
The universal theorem is proved analytically in the companion Markdown note.
"""
import sympy as s
from itertools import combinations

gamma,d=s.symbols("gamma d", positive=True)
x=d/gamma
G0=s.diag(gamma,0)
G=gamma*s.Matrix([[1-x*x,x*s.sqrt(1-x*x)],
                  [x*s.sqrt(1-x*x),x*x]])
E=G-G0
assert s.simplify(E.trace())==0
assert s.simplify(E.det()+d*d)==0
assert s.simplify(G[1,1]-d*d/gamma)==0
print("PASS: exact sharpness witness")

I=s.eye(5)
ws=[]
for i,j in combinations(range(5),2):
    for sign in [1,-1]:
        w=(I[:,i]+sign*I[:,j])/s.sqrt(2)
        ws.append(w)
Qs=[w*w.T-I/5 for w in ws]
D5=s.Matrix(20,20,lambda i,j:s.trace(Qs[i]*Qs[j]))
assert D5*s.ones(20,1)==s.zeros(20,1)
assert D5.eigenvals()=={s.Rational(3,2):4,s.Integer(1):10,s.Integer(0):6}
print("PASS: exact D5 Q-Gram spectrum and all-ones kernel")

a,q=s.symbols("a q",real=True)
b=q-(1-a)/5
slack=q*(s.Rational(1,4)-q)+s.Rational(2,5)*a*(s.Rational(1,4)-q)+s.Rational(1,25)*a*(s.Rational(1,4)-a)
assert s.expand(b*b-(s.Rational(1,100)+s.Rational(3,50)*a-s.Rational(3,20)*b-slack))==0
print("PASS: exact slack identity")

B=s.Rational(383,504)
r=B-s.Rational(3,4)
C=30-3*B+2*r*(s.Rational(1,4)-r)
assert r==s.Rational(5,504)
assert C==s.Rational(3521297,127008)
gap=C/70
assert gap==s.Rational(3521297,8890560)
assert gap>s.Rational(99,250)
assert gap>s.Rational(5,14)
print("PASS: exact concentration correction and stronger Q-Gram gap")
print("gap =",gap,"≈",s.N(gap,18))
print("gap - 99/250 =",gap-s.Rational(99,250))
