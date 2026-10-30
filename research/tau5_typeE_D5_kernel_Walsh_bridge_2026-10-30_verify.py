"""Exact SymPy regression for D5 Q-kernel / Walsh-class bridge."""
import sympy as s
from itertools import combinations
E=list(combinations(range(5),2))
tags=[(e,t) for e in E for t in (1,-1)]
r=[]
for (i,j),t in tags:
    v=s.zeros(5,1);v[i]=1;v[j]=t;r.append(v)
K0=s.Matrix(20,20,lambda i,j:(r[i].dot(r[j]))**2/4-s.Rational(1,5))
P=s.eye(20)-s.Rational(5,3)*K0+s.Rational(2,3)*K0**2
Pg=s.ones(20,20)/20;Pc=P-Pg
assert K0.eigenvals()=={0:6,1:10,s.Rational(3,2):4}
assert P*P==P and P*Pc==Pc and Pc*Pc==Pc
assert P*s.ones(20,1)==s.ones(20,1)
O=[];D=[];J=[]
for i,j in combinations(range(20),2):
    ei,ej=set(tags[i][0]),set(tags[j][0])
    (O if ei==ej else J if ei&ej else D).append((i,j))
    assert P[i,j]==(s.Rational(3,10) if ei==ej else -s.Rational(1,30) if ei&ej else s.Rational(2,15))
assert (len(O),len(D),len(J))==(10,60,120)
core=[tags.index(((0,j),1)) for j in range(1,5)]
assert all(tuple(sorted((i,j))) in J for i,j in combinations(core,2))
# Rational nonuniform scaling and linewise rational Householder rotation.
t=[s.S.One]*20
for i,x in [(0,s.Rational(7,8)),(3,s.Rational(9,10)),(7,s.Rational(13,14))]:t[i]=x
v=list(r);u=s.Matrix([1,2,0,0,0])
for i in (1,8):v[i]=v[i]-2*u*(u.dot(v[i]))/u.dot(u)
w=s.Matrix([x*x for x in t]);a=s.ones(20,1)-w
A=sum(a);U=a.dot(a)
assert A<=s.Rational(383,504)
G=s.Matrix(20,20,lambda i,j:w[i]*w[j]*(v[i].dot(v[j]))**2/4)
K=G-w*w.T/5
Osum=sum(G[i,j] for i,j in O)
Dsum=sum(G[i,j] for i,j in D)
Jsum=sum(G[i,j]-s.Rational(1,4) for i,j in J)
X=9*Osum+4*Dsum-Jsum
V=sum(K);C=s.trace(Pc*K);S=sum(G[i,j] for i,j in combinations(range(20),2))
assert s.expand(X-(3*A-s.Rational(9,2)*U+3*(a.T*P*a)[0]+15*s.trace(P*K)))==0
assert s.expand(X-(3*A-s.Rational(9,2)*U+3*A*A/20+s.Rational(3,4)*V+3*(a.T*Pc*a)[0]+15*C))==0
assert s.expand(X-(s.Rational(3,2)*S-45+s.Rational(15,2)*A-s.Rational(15,4)*U+3*(a.T*Pc*a)[0]+15*C))==0
assert X>=s.Rational(15,8)*A+3*A*A/20+s.Rational(3,4)*V
# Rotate one orthonormal support pair: Q-kernel remains, safety breaks.
rot=list(r);c=s.Rational(3,5);h=s.Rational(4,5)
rot[0]=c*r[0]+h*r[1];rot[1]=-h*r[0]+c*r[1]
Kr=s.Matrix(20,20,lambda i,j:(rot[i].dot(rot[j]))**2/4-s.Rational(1,5))
assert Kr*P==s.zeros(20) and Kr!=K0
assert (rot[0].dot(rot[4]))**2/4==s.Rational(49,100)
print('PASS: exact spectral classes, three weighted identities, star incidence and Q-kernel soft mode')
