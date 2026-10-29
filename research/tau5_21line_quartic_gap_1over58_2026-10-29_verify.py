"""Exact rational certificate for the universal 21-line quartic gap P>1/58.

All decisive inequalities use Fraction and integer-square-root intervals.
The companion mathematical note supplies the analytic PSD/convexity proofs.
"""
from fractions import Fraction as F
from math import isqrt

p=F(1,58)
vmax=F(24,5)*p
vstar=F(9,1160)
assert vmax==F(12,145)
assert p-F(5,24)*vstar==F(1,64)
assert 0<vstar<vmax
assert 2*(4*p+F(1,4))==F(37,58)<F(7,10)
assert F(4,5)-vmax>F(7,10)

# Exact Gegenbauer identity: t^4-t^2/4 = 1/28 + P2/3 + 8P4/21.
p2={0:F(-1,4),2:F(5,4)}
p4={0:F(1,8),2:F(-14,8),4:F(21,8)}
poly={j:F(1,28)*(j==0)+F(1,3)*p2.get(j,0)+F(8,21)*p4.get(j,0)
      for j in (0,2,4)}
assert poly=={0:F(0),2:F(-1,4),4:F(1)}

def sqrt_bounds(q,places=14):
    q=F(q)
    assert q>=0
    scale=10**places
    floor=isqrt((q.numerator*scale*scale)//q.denominator)
    lo,hi=F(floor,scale),F(floor+1,scale)
    assert lo*lo<=q<hi*hi
    return lo,hi

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo)
        self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=toI(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-toI(o))
    def __rsub__(self,o):return toI(o)+(-self)
    def __mul__(self,o):
        o=toI(o)
        values=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(values),max(values))
    __rmul__=__mul__
    def positive(self):assert self.lo>0,(self.lo,self.hi)

def toI(x):return x if isinstance(x,I) else I(x)
def root(q):return I(*sqrt_bounds(q))
def G(E):
    assert 0<=E<F(1,32)
    if E<=F(1,64):return F(1,8)-root(F(1,64)-E)
    return F(1,4)-root(F(1,32)-E)
def L(V):return 4*p+G(p-F(5,24)*V)
def B(V):return (F(21,5)+root(F(4,5)*V))*V
def huber(c,lam,eta):
    alpha,beta=lam+eta,lam-eta
    if c < -alpha/2:return -alpha*c-alpha*alpha/4
    if c > beta/2:return beta*c-beta*beta/4
    return c*c

params=((134,F(1,3),-F(1,40),F(179,5000),F(13219,57600)),
        (135,F(1,3), F(1,4), F(23,1000),F(131,800)))
for K,lam,eta,v,H in params:
    n12=5 if K==134 else 3
    n13=21-n12
    assert 12*n12+13*n13==2*K
    assert n12*huber(-F(1,5),lam,eta)+n13*huber(F(1,20),lam,eta)==H
    assert 0<vstar<v<vmax
    D=lambda V:V+F(336,5)-F(K,2)
    ((D(v) if K==134 else -D(v))-2*L(v)).positive()
    for V in (F(0),vstar,v):
        (H-(B(V)+2*lam*L(V)+eta*D(V))).positive()
        print("PASS exact Huber comparison",K,V)
    print("PASS exact signed-trace comparison",K)

assert F(81,256)*p==F(81,14848)
assert F(81,256)*F(320,81)==F(5,4)
assert F(81,256)*F(16,9)==F(9,16)
print("PASS: all eight exact surd inequalities and constants; P>1/58")
