"""Exact rational verification for the 20-vector Q comparison theorem.
Requires sympy; tests symbolic identities, rational constants, and exact D5 rank.
"""
from fractions import Fraction as F
import sympy as s

# The exact rank-one decomposition of K0 in a symbolic three-variable test.
a1, a2, a3 = s.symbols('a1 a2 a3')
a = s.Matrix([a1, a2, a3]); one = s.ones(3,1); b = one-a
K0 = s.diag(*[bi**2-s.Rational(1,4) for bi in b]) + one*one.T/4 - b*b.T/5
rhs = s.diag(*[bi**2-s.Rational(1,4) for bi in b]) + (one+4*a)*(one+4*a).T/20 - a*a.T
assert all(s.simplify(v)==0 for v in K0-rhs)

# Exact SOS identity, checked symbolically in three variables.
t = s.symbols('t0:3'); x=s.Matrix(s.symbols('x0:3'))
bt=s.Matrix([s.Rational(3,4)+ti for ti in t]); ones=s.ones(3,1)
Kt=s.diag(*[bi**2-s.Rational(1,4) for bi in bt]) + ones*ones.T/4 - bt*bt.T/5
S=sum(x); T=sum(ti*xi for ti,xi in zip(t,x))
D=sum(ti*(s.Rational(3,2)+ti)*xi**2 for ti,xi in zip(t,x))
assert s.expand((x.T*(Kt-s.Rational(5,16)*s.eye(3))*x)[0] - (D+s.Rational(11,80)*(S-s.Rational(12,11)*T)**2-s.Rational(4,11)*T**2))==0

# The two case certificates meet at A=7/32.
assert F(3,4)-2*F(7,32)==F(5,16)
assert F(20,7)-F(24,49)*F(7,32)==F(11,4)

# Exact rank and spectral arithmetic.
c=F(5,16)
assert F(30,7)*c*c==F(375,896)
assert F(375,896)-F(2535,6776)==F(4815,108416)
Tplus=F(12286461,100000000)
assert F(375,896)-Tplus==F(206963523,700000000)

# Verify the inherited convex-concentration rational cap.
u=F(97,5000)
assert u<F(7,50)**2
Tupper=F(25,256)+u+u*u+2*u*F(7,50)
assert Tupper==Tplus

# Exact D5 test: twenty normalized lines (ei +/- ej)/sqrt(2).
vecs=[]
for i in range(5):
 for j in range(i+1,5):
  for sign in (-1,1):
   v=s.zeros(5,1); v[i]=1; v[j]=sign; vecs.append(v)
assert len(vecs)==20
K=s.Matrix(20,20,lambda i,j: s.Rational((vecs[i].dot(vecs[j]))**2,4)-s.Rational(1,5))
assert K.rank()==14
assert K*s.ones(20,1)==s.zeros(20,1)
E=s.Matrix(20,20,lambda i,j: 0 if i==j else s.Rational(1,4)-s.Rational(vecs[i].dot(vecs[j])**2,4))
assert sum(E[i,j]**2 for i in range(20) for j in range(i+1,20))>=s.Rational(375,896)

# Sharpness: two short vectors and all other squared norms 1.
b=s.Matrix([s.Rational(3,4)]*2+[s.Integer(1)]*18); one=s.ones(20,1)
K0=s.diag(*[bi**2-s.Rational(1,4) for bi in b])+one*one.T/4-b*b.T/5
x=s.zeros(20,1);x[0]=1;x[1]=-1
assert K0*x==s.Rational(5,16)*x

print('PASS: exact decomposition, SOS identity, threshold, quartic rank arithmetic, D5 rank, sharpness.')
print('Improved universal quartic floor:',F(375,896))
print('Improved Type-E joint safe/core slack:',F(206963523,700000000))
