"""Exact SymPy checks for the 2026-10-27 saturated 17-line Type-E note.
The universal covering inequality is proved algebraically in the companion note.
"""
import sympy as s
from itertools import combinations
R=s.Rational
rt2=s.sqrt(2)
E=[s.eye(5)[:,i] for i in range(5)]
D=[]
for j,k in combinations(range(1,5),2):
    D.extend([(E[j]+E[k])/rt2,(E[j]-E[k])/rt2])
for j in range(1,5):
    D.append((E[0]+E[j])/rt2)
x=s.Matrix([8,-3,-3,-3,-3])/10
assert len(D)==16 and x.dot(x)==1
assert all(s.simplify(v.dot(v)-1)==0 for v in D)
assert all(s.simplify(v.dot(w)**2-R(1,4))<=0 for v,w in combinations(D,2))
assert {s.simplify(x.dot(v)**2) for v in D}=={0,R(1,8),R(9,50)}
c=R(3,5)+rt2/4
rho2=s.simplify(1/(2*(1+c*c)))
kappa=s.simplify(1/(4*rho2))
a=s.simplify(1-kappa)
assert s.simplify(c*c-1)<0
assert s.simplify(rho2-R(1,4))>0
assert s.simplify(rho2-100/(297+60*rt2))==0
assert s.simplify(kappa-(R(297,400)+3*rt2/20))==0
assert s.simplify(a-(R(103,400)-3*rt2/20))==0
assert s.simplify(4*a-(R(103,100)-3*rt2/5))==0
h=s.symbols('h',real=True)
f=h*h+3*(1-h)**2
assert f.subs(h,R(1,2))==1 and f.subs(h,1)==1
assert s.diff(f,h,2)>0
print('PASS exact: 17-line coherence, covering constants, conditional four-core gap')
print('rho0^2:',rho2,'~',rho2.evalf(16))
print('C at b=0 >=',4*a,'~',(4*a).evalf(16))
