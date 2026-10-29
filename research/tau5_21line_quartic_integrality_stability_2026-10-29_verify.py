"""Exact Fraction/SymPy audit for 21-line quartic-integrality theorem.
Proof is in tau5_21line_quartic_integrality_stability_2026-10-29.md.
"""
from fractions import Fraction as F
from random import Random
import sympy as sp

t=sp.symbols("t")
P2=(5*t*t-1)/4
P4=(21*t**4-14*t*t+1)/8
assert sp.expand(t**4-t*t/4-(sp.Rational(1,28)+P2/3+sp.Rational(8,21)*P4))==0
assert F(441,28)==F(63,4)
assert F(5,24)*F(1,20)==F(1,96)>F(1,120)
assert F(13,3)/24==F(13,72)
assert F(81,256)/120==F(27,10240)
assert F(81,256)*F(320,81)==F(5,4)
assert F(81,256)*F(16,9)==F(9,16)
assert F(27,10240)*F(16,29)==F(27,18560)

for k in range(4001):
    x=F(k,4000)
    r=min((F(0),F(1,4)),key=lambda v:abs(x-v))
    f=x*(x-F(1,4))
    assert abs(x-r)<=8*max(-f,0)+4*max(f,0)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def rational_unit(q):
    sq=sum(v*v for v in q)
    d=1+sq
    y=[2*v/d for v in q]+[(1-sq)/d]
    assert dot(y,y)==1
    return y

def check(ys):
    xs=[dot(ys[i],ys[j])**2 for i in range(21) for j in range(i+1,21)]
    P=sum(max(x*(x-F(1,4)),0) for x in xs)
    N=sum(max(-x*(x-F(1,4)),0) for x in xs)
    T=[[sum(y[i]*y[j] for y in ys) for j in range(5)] for i in range(5)]
    V=sum((T[i][j]-(F(21,5) if i==j else 0))**2 for i in range(5) for j in range(5))
    assert P-N>=F(5,24)*V
    assert P>F(1,120)
    assert 2*sum(xs)==F(336,5)+V
    rs=[min((F(0),F(1,4)),key=lambda v:abs(x-v)) for x in xs]
    assert abs(2*sum(xs)-2*sum(rs))<=16*N+8*P
    if V<F(1,20):
        assert P>=F(1,120)+F(13,72)*V

rng=Random(20261029)
for _ in range(25):
    ys=[rational_unit([F(rng.randint(-3,3),rng.randint(1,5)) for i in range(4)]) for j in range(21)]
    check(ys)
print("PASS: exact 21-line harmonic, rounding, and six-exception bridge audits")
