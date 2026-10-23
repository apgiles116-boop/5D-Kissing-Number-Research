"""Numerical consistency and exact equality checks for the four-core identities."""
import numpy as np
from fractions import Fraction
rng=np.random.default_rng(20261023)
for k in range(1000):
    m=rng.normal(size=(4,5))
    if k%11==0: m[0]=0
    a=np.sum(m*m,axis=1); b=np.sqrt(a); C=float(a.sum())
    M=m.sum(axis=0); d=d2=K=psi_sum=0.
    for i in range(4):
        for j in range(i+1,4):
            dot=float(m[i]@m[j]); t=dot/(b[i]*b[j]) if b[i]*b[j]>0 else 0.
            delta=max(-dot,0.); d+=delta; d2+=delta*delta
            K+=b[i]*b[j]*(1-abs(t))
            psi=(1-t)/2-max(-t,0.)**2
            psi_sum+=a[i]*a[j]*psi
    W=np.sum(b[:,None]*m,axis=0)
    assert abs((C-d)-(np.sum((b-b.mean())**2)+np.sum(M*M)/4+K/2))<1e-9
    assert abs((C*C/4-d2)-(np.sum(W*W)/4+psi_sum))<1e-9
    T=m.T@m; eps=C-d; eps2=C*C/4-d2
    assert C*C-np.trace(T@T)<=4*C*eps+1e-8
    assert C*C-np.trace(T@T)<=8*eps2+1e-8
a=Fraction(7,13); C=4*a; d=4*a; d2=4*a*a
assert C==d and C*C/4==d2
print("PASS: 1000 numerical checks and exact equality case")
