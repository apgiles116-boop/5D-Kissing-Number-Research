"""Fraction-exact certificate for universal P>101/6000 and conditional Type-E A>1/68.
Requires only Python's standard-library fractions module. The Type-E defect
estimate is retained input, not proved by this script.
"""
from fractions import Fraction as F

p = F(101,6000)
a = F(1,68)

def g(k, lam, eta):
    c=F(k,4)-F(16,5)
    z=eta/2
    e=max(z-lam/2,min(c,z+lam/2))
    return e*e-eta*e+lam*abs(e-c)

def vcap(K,p):
    assert K in (134,135)
    return (24*p-(F(1,5) if K==134 else F(3,10)))*F(3,13 if K==134 else 7)

def cert(K,p,lam,eta,require14=False):
    assert p<F(7,240)
    gs=[g(k,lam,eta) for k in (12,13,14)]
    curvature=gs[0]+gs[2]-2*gs[1]
    assert curvature>=0
    C=(5*gs[0]+16*gs[1] if K==134 else 3*gs[0]+18*gs[1])
    if require14: C+=curvature
    # Independent exhaustive enumeration of all possible degree multisets.
    costs=[]
    for t in range(22):
        n12=(5 if K==134 else 3)+t
        n13=21-n12-t
        if n13<0 or (require14 and t==0): continue
        assert 12*n12+13*n13+14*t==2*K
        costs.append(n12*gs[0]+n13*gs[1]+t*gs[2])
    assert min(costs)==C
    D=3+12*p-F(10,3)*lam-eta
    assert D>0 and vcap(K,p)>0
    margin=C-24*lam*p-D*vcap(K,p)
    assert margin>0
    return margin

assert 12*p+F(3,25)==F(161,500)<F(9,20)
assert cert(134,p,F(3,10),F(0))==F(8569,3250000)
assert cert(135,p,F(1),-F(93,100))==F(1233,3500000)

def Pk(A,k):
    return ((k+4)*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)

p20,p14,p13=[Pk(a,k) for k in (20,14,13)]
assert p20==F(7597709,322417936)
assert p14==F(5711117,322417936)
assert p13==F(5396685,322417936)
assert F(9,20)-F(3,25)-12*p20==F(47579409,1007556050)>0
assert cert(134,p14,F(3,10),F(0),True)==F(179521022690742833,2111551923294533200)
assert cert(135,p14,F(1,5),-F(1,10),True)==F(3344950076830347,162427071022656400)
assert p-p13==F(5753173,60453363000)>0

print("PASS: universal P>101/6000")
print("PASS: conditional Type-E A>1/68")
print("PASS: all four exact rational contradiction margins")
