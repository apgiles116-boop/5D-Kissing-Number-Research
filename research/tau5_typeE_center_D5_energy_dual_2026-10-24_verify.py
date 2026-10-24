"""Exact symbolic certificate for isolated-center / D5 energy dual theorem."""
import sympy as s
from itertools import combinations
q=s.symbols('q', positive=True)
r2=s.sqrt(2)
alpha=s.Rational(25,16)*(r2-1)
beta=s.Rational(7,4)-s.Rational(11,8)*r2
p=alpha*q*q+beta*q
g=(1+2*q-2*s.sqrt(3*q*(1-q)))/4
q0=s.Rational(2,5)
assert s.simplify((g-p).subs(q,q0))==0
assert s.simplify(s.diff(g-p,q).subs(q,q0))==0
assert s.simplify(s.diff(g,q,2)-s.sqrt(3)/(8*(q*(1-q))**s.Rational(3,2)))==0
assert s.simplify(beta+alpha/4)==(87-63*r2)/64
assert float(beta+alpha/4)<0
assert float(s.sqrt(3)-2*alpha)>0
assert s.simplify(alpha*s.Rational(8,5)+4*beta)==s.Rational(9,2)-3*r2
assert s.simplify(g.subs(q,q0))==s.Rational(9,20)-3*r2/10
assert s.simplify(10*g.subs(q,q0))==s.Rational(9,2)-3*r2
assert s.simplify(2*alpha+beta)==(14*r2-11)/8
u=s.symbols('u0:5',real=True)
Q=[]
for i,j in combinations(range(5),2):
    Q.extend([(u[i]+u[j])**2/2,(u[i]-u[j])**2/2])
norm2=sum(x*x for x in u)
assert s.expand(sum(Q)-4*norm2)==0
assert s.expand(sum(t*t for t in Q)-(s.Rational(3,2)*norm2**2+s.Rational(1,2)*sum(x**4 for x in u)))==0
ubal={x:1/s.sqrt(5) for x in u}
qs=[s.simplify(t.subs(ubal)) for t in Q]
assert qs.count(s.Rational(2,5))==10 and qs.count(0)==10
a=s.simplify(g.subs(q,q0))
assert s.simplify(s.sqrt(1-a)*s.sqrt(q0)-s.sqrt(a)*s.sqrt(1-q0)-s.Rational(1,2))==0
assert s.simplify((s.sqrt(1-a)/2+s.sqrt(3*a)/2)**2-q0)==0
for r in [s.Rational(0),s.Rational(1,10),s.Rational(1,4),s.Rational(3,10),q0,s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)]:
    gr=0 if r<=s.Rational(1,4) else g.subs(q,r)
    assert float(s.N(gr-p.subs(q,r),30))>-1e-13
print('PASS: exact dual tangency, curvature and D5 moment identities')
print('PASS: exact balanced-center equality')
print('Sharp center-only energy:',s.Rational(9,2)-3*r2)
print('Decimal:',s.N(s.Rational(9,2)-3*r2,18))
print('STATUS: conditional on normalized D5 template; no Type-E elimination')
