#!/usr/bin/env python3
"""Exact symbolic/rational verifier for Type-E outside-16 spectral gap > 1/18.
The proof note supplies Gegenbauer positivity and the weak-majorization argument.
"""
from fractions import Fraction as Q
import sympy as sp

a,s=sp.symbols('a s',real=True)
c=sp.Rational(7,2)
eff=1-(1-a-s)/(1+s)**2
upper=a+(3-2*a)*s-c*s*s
assert sp.simplify((upper-eff)*(1+s)**2
    -s*s*(sp.Rational(3,2)-3*a-(4+2*a)*s-c*s*s))==0
assert Q(3,4)-Q(9,2)*Q(1,18)-Q(7,2)*Q(1,18)**2==Q(317,648)

L=Q(1,18)
B=Q(383,504)
p1=Q(1,4)+Q(5,2)*L-c*L*L
p2=Q(1,2)+Q(5,2)*L-c*L*L/2
p3=Q(3,4)+Q(5,2)*L-c*L*L/3
p4=B+3*L-c*L*L/16
v=[Q(p1),Q(p2-p1),Q(p3-p2),Q(p4-p3)]+[Q(0)]*12
assert v[:4]==[Q(245,648),Q(331,1296),Q(979,3888),Q(8845,217728)]
assert len(v)==16 and all(0<=v[i+1]<=v[i]<1 for i in range(15))
assert p4==Q(67199,72576)

x=[1/(1-u) for u in v]
F=sum((xi*xi*xj*xj-xi*xj) for i,xi in enumerate(x) for xj in x[i+1:])/8
assert F==Q(222154536100028717800410627996,
            55841664360277980735448954225)
assert 4-F==Q(1212121341083205141385188904,
              55841664360277980735448954225)>0

t=sp.symbols('t')
P2=(4*t*t-1)/3
P4=(16*t**4-12*t*t+1)/5
assert sp.expand((1+6*P2+5*P4)/16-(t**4-t*t/4))==0

x,y=sp.symbols('x y',positive=True)
difference=2*x**3*y**2-x*x*y-2*x*x*y**3+x*y*y
assert sp.factor(difference)==x*y*(x-y)*(2*x*y-1)

u=sp.symbols('u')
a4=[sp.Rational(1,4)]*4+[u]+[sp.Integer(0)]*11
x4=[1/(1-t) for t in a4]
F4=sp.factor(sum((xi*xi*xj*xj-xi*xj)
    for i,xi in enumerate(x4) for xj in x4[i+1:])/8)
assert sp.simplify(F4-(752*u*u-1063*u+800)/(216*(1-u)**2))==0
root=(665-sp.sqrt(413553))/224
assert sp.simplify(112*root**2-665*root+64)==0
assert 0<root<sp.Rational(1,4)

print("PASS: exact polynomial identities, majorization vector and rational gap")
print("lambda_min(Z_O)>1/18")
print("F(v)=",F,"; gap=",4-F)
print("H_184 > A_C/18+A_O/36 >= A/36")
