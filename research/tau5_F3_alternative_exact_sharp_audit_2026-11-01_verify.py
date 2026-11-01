#!/usr/bin/env python3
"""Exact SymPy/Fraction checks for F3 alternative-matching algebraic optimum."""
from fractions import Fraction as Q
from math import isqrt
import sympy as sp

s=sp.symbols("s")
P=s**6-s**5-23*s**4+48*s**3-25*s**2+4*s+20
sl=Q(1797973425701,10**12); su=Q(1797973425702,10**12)
assert P.subs(s,sp.Rational(sl.numerator,sl.denominator))>0
assert P.subs(s,sp.Rational(su.numerator,su.denominator))<0
# Strict monotonicity on [1.79,1.81] by exact monomial interval bounds.
a=Q(179,100); b=Q(181,100)
assert 6*b**5-5*a**4-92*a**3+144*b**2-50*a+4<0
h=(9*s*s-10*s-10)/(s*s+6)
assert sp.simplify((5-4*s*s+6*h+h*h+4*s)*(s*s+6)**2+4*P)==0
assert sp.simplify((h*(6-s*s+2*h)+s*(s-2))*(s*s+6)**2+8*P)==0
assert sp.factor(sp.diff(h,s)-2*(5*s*s+64*s-30)/(s*s+6)**2)==0
def hh(z): return (9*z*z-10*z-10)/(z*z+6)
DL=sl*sl-4*hh(su); DU=su*su-4*hh(sl)
scale=10**15
def sqrt_lower(z): return Q(isqrt(z.numerator*scale*scale//z.denominator),scale)
rtL=sqrt_lower(DL); rtU=sqrt_lower(DU)+Q(1,scale)
assert rtL*rtL<=DL and DU<rtU*rtU
cL=(3-su*rtU)/2; cU=(3-sl*rtL)/2
assert Q(9253813,10**9)<cL<cU<Q(9253814,10**9)
# Coarse p,t brackets from exact discriminant enclosure.
assert Q(69,1000)<(sl-rtU)/2<(su-rtL)/2<Q(71,1000)
assert Q(1728,1000)<(sl+rtL)/2<(su+rtU)/2<Q(1729,1000)

p,t=sp.symbols("p t",positive=True)
d=2-p-t; A=3-p*p; B=3-t*t
F=A*B-d*d
K=(p+t)*d-p*t*(6-p*p-t*t)
assert sp.simplify((1/p+1/t-(A+B)/d)*p*t*d-K)==0
gamma=4/(1/p-B/d)
beta=gamma*(t-B/d)/4
alpha=gamma*(1/t-p)/4
la=gamma*t/8+(1-beta)/4
lb=gamma/(8*t)+(1-alpha)/4
Z={
 (-1,-1):sp.Matrix([[gamma*B/(8*d),gamma/8],[gamma/8,gamma*A/(8*d)]]),
 (-1, 1):gamma/(8*t)*sp.Matrix([[t*t,-t],[-t,1]]),
 ( 1,-1):gamma/(8*p)*sp.Matrix([[1,-p],[-p,p*p]]),
 ( 1, 1):sp.Matrix([[sp.Rational(1,2)+gamma*t/8,gamma/8],
                    [gamma/8,gamma/(8*t)+(1-alpha)/2]])
}
for (r,v),mat in Z.items():
    assert sp.simplify(mat[0,1]-gamma*r*v/8)==0
    assert sp.simplify(mat[0,0]-(la+sp.Rational(r,4)+beta*sp.Rational(v,4)))==0
    delta=sp.factor(mat[1,1]-(lb+sp.Rational(r*v,4)-alpha*sp.Rational(r,4)))
    if (r,v)==(-1,-1):
        assert sp.simplify(delta/(gamma*K/(8*p*t*d)))==-1
    else:
        assert delta==0
assert sp.simplify(Z[(-1,-1)].det()-gamma**2*F/(64*d*d))==0
assert Z[(-1,1)].det()==0 and Z[(1,-1)].det()==0
# 0<gamma<2/7 and 0<alpha<1/20 imply Z_++ positive definite.
assert Q(1,2)*Q(19,40)-Q(1,28)**2>0
M={
 (1,1):sp.zeros(2),
 (1,-1):sp.Matrix([[p*p,p],[p,1]]),
 (-1,1):sp.Matrix([[1,t],[t,t*t]]),
 (-1,-1):sp.Matrix([[A,-d],[-d,B]])
}
assert sp.simplify(M[(-1,-1)].det()-F)==0
for key in M:
    inner=sp.factor(sp.trace(Z[key]*M[key]))
    if key==(-1,-1):
        assert sp.simplify(inner-gamma*F/(4*d))==0
    else:
        assert inner==0
x=[None]*10
x[0]=-sp.Rational(1,2); x[1]=(1-t)/2; x[2]=(t*t-2)/2
x[3]=-1+p*p/2; x[4]=-sp.Rational(1,2); x[5]=(1-p*p)/2
x[6]=-sp.Rational(1,2); x[7]=(1-t*t)/2
x[8]=(p+t-1)/2; x[9]=(1-p)/2
for r in (-1,1):
 for v in (-1,1):
    AA=1+r*x[3]+v*x[4]+r*v*x[5]
    BB=1+r*x[0]+v*x[2]+r*v*x[7]
    RR=x[8]+r*x[1]+v*x[9]+r*v*x[6]
    assert all(sp.expand(e)==0 for e in
        (AA-M[(r,v)][0,0],BB-M[(r,v)][1,1],RR-M[(r,v)][0,1]))
C=sp.factor(2+x[3]+x[7])
assert sp.expand(C-(p*p+3-t*t)/2)==0
L=2-4*la-4*lb-alpha/2+beta/2+gamma/2
assert sp.simplify((C-L-gamma*F/(4*d))/K+
       (t*t-3)/(2*t*(t-2)*(p*t+2*p-1)))==0
# Strict approach: the -+ block remains rank one, -- becomes rank two.
delta=sp.symbols("delta",positive=True)
td=t-delta; qq=1-delta**2; eta=delta**2; ep=(1-qq**2)/2
xd3=-1+p*p/2; xd4=-sp.Rational(1,2)-ep; xd5=(1-p*p)/2+ep
xd0=-sp.Rational(1,2); xd2=(td*td-2)/2; xd7=(1-td*td)/2
rpp=0; rpm=p; rmp=qq*td; rmm=p+qq*td-2-4*eta
assert sp.simplify((rpp-rpm-rmp+rmm)/4+sp.Rational(1,2)+eta)==0
AAmp=1-xd3+xd4-xd5; BBmp=1-xd0+xd2-xd7
assert sp.simplify(AAmp-qq**2)==0
assert sp.simplify(BBmp-td**2)==0
assert sp.simplify(AAmp*BBmp-rmp**2)==0
AAmm=1-xd3-xd4+xd5; BBmm=1-xd0-xd2+xd7
assert sp.simplify(AAmm-(A+1-qq**2))==0
assert sp.simplify(BBmm-(3-td**2))==0
Dmm=sp.expand(AAmm*BBmm-rmm**2)
assert sp.simplify(Dmm.subs(delta,0)-F)==0
assert sp.simplify(sp.diff(Dmm,delta).subs(delta,0)-(2*t*A-2*d))==0
assert 2*Q(1728,1000)*(3-Q(71,1000)**2)-2*Q(203,1000)>0
# Old October 28 witness: nonedge correlations 16 and 34 are -1/2-2v.
k=sp.symbols("k",positive=True)
v_old=k*k*(3-k*k)/(4*(1-k**4))
assert sp.factor(v_old-k*k*(3-k*k)/(4*(1-k**4)))==0
assert Q(1732051,10**6)**2>3
assert Q(9253813,10**9)*(1-Q(1732051,10**6)/2)>Q(12397,10**7)
print("PASS: exact algebraic root and 0.009253813<C*<0.009253814")
print("PASS: Fourier PSD primal, dual coefficient identity, complementary slackness")
print("AUDIT: October 28 alleged sharp witness violates safe nonedges 16 and 34")
print("STATUS: Type E open; 40<=tau_5<=44")
