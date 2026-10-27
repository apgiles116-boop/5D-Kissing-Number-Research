"""Exact Fraction verifier: universal P>2/141 and conditional Type-E A>1/80."""
from fractions import Fraction as F

def g(k, lam, eta):
    c=F(k,4)-F(16,5)
    z=eta/2
    e=min(max(c,z-lam/2),z+lam/2)
    return e*e-eta*e+lam*abs(e-c)

def mincost(K, lam, eta, require14=False):
    # Relaxed exact DP over all 21 integer degrees 0..20, sum 2K.
    dp={(0,False):F(0)}
    for _ in range(21):
        nd={}
        for (s,seen),cost in dp.items():
            for k in range(min(20,2*K-s)+1):
                key=(s+k,seen or k>=14)
                val=cost+g(k,lam,eta)
                if key not in nd or val<nd[key]: nd[key]=val
        dp=nd
    return min(v for (s,seen),v in dp.items() if s==2*K and (not require14 or seen))

def margin(K,p,lam,eta,C):
    vup=(24*p-(F(1,5) if K==134 else F(3,10)))*F(3,13 if K==134 else 7)
    D=F(24,5)+4*p-F(10,3)*lam-eta
    assert vup>=0 and D>0
    return C-24*lam*p-D*vup

p=F(2,141)
assert F(24,5)*p<F(7,10)
assert F(4,5)-F(24,5)*p>24*p
for K,lam,eta,C,expected in [
    (134,F(3,10),F(0),F(91,400),F(899,2297360)),
    (135,F(1,5),-F(1,10),F(3,16),F(278881,6185200))]:
    vals=[g(k,lam,eta) for k in range(21)]
    assert all(vals[k-1]-2*vals[k]+vals[k+1]>=0 for k in range(1,20))
    assert mincost(K,lam,eta)==C
    assert margin(K,p,lam,eta,C)==expected>0

p=F(1,64)
assert F(24,5)*p<F(7,10)
assert F(4,5)-F(24,5)*p>24*p
for K,lam,eta,C,expected in [
    (134,F(3,10),F(0),F(131,400),F(491,8320)),
    (135,F(1,5),-F(1,10),F(99,400),F(771,22400))]:
    assert mincost(K,lam,eta,require14=True)==C
    assert margin(K,p,lam,eta,C)==expected>0

def Pk(A,k):
    return ((k+4)*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)

A=F(1,80)
p0,p14,p13=(Pk(A,k) for k in (20,14,13))
assert p0==F(12358961,623201296)
assert F(11,20)-24*p0-F(3,50)==F(54709819,3895008100)>0
assert F(1,64)-p14==F(1802237,2492805184)>0
assert F(2,141)-p13==F(9133091,87871382736)>0
print("PASS: exact P>2/141; P<=1/64 implies all k<=13; conditional Type-E A>1/80")
