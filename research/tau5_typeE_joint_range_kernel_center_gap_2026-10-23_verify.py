"""Exact SymPy checks for the joint range/kernel Type-E Q-Gram gap.
The analytic frame inequality and piecewise optimization are proved in the note.
"""
import sympy as s
from itertools import combinations

I=s.eye(5)
ws=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        ws.append((I[:,i]+sign*I[:,j])/s.sqrt(2))
Qs=[w*w.T-I/5 for w in ws]
G0=s.Matrix(20,20,lambda i,j:s.trace(Qs[i]*Qs[j]))
assert G0.eigenvals()=={s.Rational(3,2):4,s.Integer(1):10,s.Integer(0):6}
assert G0*s.ones(20,1)==s.zeros(20,1)
print('PASS D5 spectrum and all-ones kernel')

a,q=s.symbols('a q',real=True)
b=q-(1-a)/5
S=q*(s.Rational(1,4)-q)+s.Rational(2,5)*a*(s.Rational(1,4)-q)+s.Rational(1,25)*a*(s.Rational(1,4)-a)
assert s.expand(b*b-(s.Rational(1,100)+s.Rational(3,50)*a-s.Rational(3,20)*b-S))==0
print('PASS exact scalar slack identity')

h,A,k=s.symbols('h A k',real=True)
r=h-k/4
f=s.Rational(5,2)*(h-s.Rational(5,2)+A/5)**2+50*r*(s.Rational(1,4)-r)
assert s.diff(f,h,2)==-95
print('PASS quarter-interval concavity')

B=s.Rational(383,504)
ra=B-s.Rational(3,4)
assert ra==s.Rational(5,504)
p=s.Rational(5,2)*(A/5)**2
q=s.Rational(5,2)*(s.Rational(1,4)-A/5)**2
assert s.simplify((p-q).subs(A,s.Rational(5,8)))==0
assert s.diff(p,A)==A/5
assert s.diff(q,A)==A/5-s.Rational(1,4)
print('PASS grid switch and derivative')

bound=(s.Rational(195,8)-3*B+2*ra*(s.Rational(1,4)-ra)
       +s.Rational(5,2)*(s.Rational(1,4)-B/5)**2)/40
assert bound==s.Rational(56198549,101606400)
assert bound>s.Rational(3521297,8890560)
assert bound>s.Rational(11,20)
print('PASS exact new gap:',bound,'=',s.N(bound,18))
