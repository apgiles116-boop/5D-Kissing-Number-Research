"""Exact rational derivative certificate and high-precision evaluation.

All geometric implications are proved in the companion note. Numerical
sampling here is regression only and not a substitute for those proofs.
"""
import sympy as S

q = S.Rational
X = S.symbols('x', real=True)
D = 196*X-644*X**2+896*X**3-448*X**4
Dp = S.diff(D, X)
Dpp = S.diff(Dp, X)
B = q(2595,256)

def inv(w):
    return (1-S.sqrt((7+S.sqrt(2401-112*w))/56))/2

r = inv(15-B)
c0 = inv(q(43,3)-B/2)
c1 = inv(q(41,6))

def certify(name, expr):
    v = S.simplify(expr)
    assert v.is_positive, (name, v)
    print(name, ':', v)

certify('r<7/250', S.factor(D.subs(X,q(7,250))-(15-B)))
certify('c0<3/50', S.factor(D.subs(X,q(3,50))-(q(43,3)-B/2)))
certify('c1>7/250', S.factor(q(41,6)-D.subs(X,q(7,250))))
certify('Dp(7/250)>160', Dp.subs(X,q(7,250))-160)
certify('Dp(3/50)>128', Dp.subs(X,q(3,50))-128)
# Dpp is increasing on [0,1/4] and negative at 1/4.
assert S.diff(Dpp,X).subs(X,q(1,4))>0
assert Dpp.subs(X,q(1,4))<0
# The directional derivative lower bound is strictly positive.
certify('Lprime lower bound 27/56', -q(153,100)+q(9,5)*q(313,14)/20)

# Algebraic expressions at x=0; no floating-point optimization is assumed.
a0=q(1,2)+c0
u0=q(1,8)+c0**2
b0=q(7,2)-c0-4/S.sqrt(7)
L0=30-3*a0+a0**2/10-u0/2+b0**2/40
for label,expr in [('r',r),('c0',c0),('c1',c1),('L0',L0),
                   ('safe_P1_P3',L0-q(473,256)),('safe_P2',L0-q(57,32))]:
    print(label, '=', S.N(expr,30))

# Exact Q-frame identity follows from
# tr(F^2)=sum_i ||z_i||^4+2sum_{i<j}(z_i.z_j)^2.
A,U,V=S.symbols('A U V',real=True)
R2=20-2*A+U
traceF=20-A
Q=(traceF**2/5+V-R2)/2
assert S.expand(Q-(30-3*A+A**2/10-U/2+V/2))==0
print('Exact frame identity: PASS')
print('Conditional Type-E directional-frame certificate: PASS')
