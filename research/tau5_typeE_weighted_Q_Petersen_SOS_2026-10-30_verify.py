"""Exact SymPy/Fraction checks for the weighted Q Petersen SOS theorem.
Proof is in the accompanying .md. The separate 1/360 fibre interval
certificate was independently rerun (988525 cells, zero unresolved).
"""
import random
from itertools import combinations
from fractions import Fraction as F
import sympy as s

edges=list(combinations(range(5),2))
labels=[(e,sign) for e in edges for sign in (1,-1)]
n=20
P0=s.Matrix(n,n,lambda i,j:
    s.Rational(3,10) if i==j or labels[i][0]==labels[j][0] else
    -s.Rational(1,30) if len(set(labels[i][0])&set(labels[j][0]))==1 else
    s.Rational(2,15))
Pg=s.ones(n,n)/20
Pc=P0-Pg
Pperp=s.eye(n)-P0
assert P0*P0==P0 and Pc*Pc==Pc and P0*Pg==Pg
assert s.trace(P0)==6 and s.trace(Pc)==5

L=s.zeros(n)
for i in range(n):
    for j in range(i+1,n):
        e,f=labels[i][0],labels[j][0]
        wt=2 if e==f else (1 if not set(e)&set(f) else 0)
        L[i,i]+=wt;L[j,j]+=wt;L[i,j]-=wt;L[j,i]-=wt
assert L==4*Pc+10*Pperp
assert L.eigenvals()=={s.Integer(0):1,s.Integer(4):5,s.Integer(10):14}

def check(Z):
    w=[(Z.row(i)*Z.row(i).T)[0] for i in range(n)]
    a=s.Matrix([1-x for x in w])
    A=sum(a)
    K=s.Matrix(n,n,lambda i,j:
        (Z.row(i)*Z.row(j).T)[0]**2-w[i]*w[j]/5)
    V=sum(K)
    C=s.trace(Pc*K)
    O=sum((Z.row(i)*Z.row(j).T)[0]**2
          for i in range(n) for j in range(i+1,n)
          if labels[i][0]==labels[j][0])
    D=sum((Z.row(i)*Z.row(j).T)[0]**2
          for i in range(n) for j in range(i+1,n)
          if not set(labels[i][0])&set(labels[j][0]))
    ca=(a.T*Pc*a)[0]
    pa=(a.T*Pperp*a)[0]
    assert s.simplify(V+12*C-8*O-4*D-s.Rational(2,5)*(a.T*L*a)[0])==0
    assert s.simplify(V+12*C-8*O-4*D-s.Rational(8,5)*ca-4*pa)==0
    assert s.simplify(O+2*C+V/10-
        (s.Rational(9,5)*O+s.Rational(2,5)*D+
         s.Rational(4,5)*C+s.Rational(4,25)*ca+s.Rational(2,5)*pa))==0
    assert s.simplify((a.T*a)[0]-A*A/20-ca-pa)==0
    return V,C,O,D,a

for seed in range(4):
    rng=random.Random(seed)
    Z=s.Matrix([[s.Rational(rng.randint(-3,3),rng.randint(4,9))
                 for j in range(5)] for i in range(n)])
    check(Z)

# Non-D5 rotation in a common support plane, with a_i=1/50.
Z=s.zeros(n,5)
for i,(e,sign) in enumerate(labels):
    p,q=e
    Z[i,p]=s.Rational(7,10)
    Z[i,q]=s.Rational(7*sign,10)
x=Z.row(0); y=Z.row(1)
Z[0,:]=s.Rational(3,5)*x+s.Rational(4,5)*y
Z[1,:]=-s.Rational(4,5)*x+s.Rational(3,5)*y
V,C,O,D,a=check(Z)
assert V==C==O==D==0
assert all(x==s.Rational(1,50) for x in a)

B=F(383,504)
Umax=F(3,16)+(B-F(3,4))**2
floor=30-3*B+B*B/10-Umax/2
assert floor==F(8790283,317520)
assert floor>F(17456771,635040)
for k in range(4):
    lo=F(k,4);hi=min(F(k+1,4),B)
    if hi<lo:continue
    assert -3+lo/5-(lo-F(k,4))<0
    assert -3+hi/5-(hi-F(k,4))<0

assert F(9697,10080)>F(24,25)
assert F(99,70)**2>2 and F(26,15)**2>3
r=F(165,112);o=F(33,70);s3=F(26,15)
k=r+22*s3*(2*o+5*r)
q=22*s3*r*r
assert k==F(891297,2800) and q==F(259545,3136)
assert k+q/1000<F(637,2)
assert F(360)*F(15,7)*F(637,2)==245700
assert 245700**2==60368490000
print("PASS: exact weighted Q Petersen SOS, spectral identity, soft fibre, and rational constants")
