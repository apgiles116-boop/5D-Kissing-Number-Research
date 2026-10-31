"""Exact rational verification for the 2026-10-31 mass-sensitive Type-E theorem.

The analytic proof is in the companion .md file. This script verifies all
finite rational comparisons and the sign-free rank-two triple identity.
"""
from fractions import Fraction as F
from itertools import combinations

def sqrt_less(a, b):
    assert a >= 0 and b > 0 and a < b*b

def sqrt_greater(a, b):
    assert a >= 0 and b >= 0 and a > b*b

E=F(1,2_000_000)
eta=F(1,125)
assert 128*E == eta*eta
sqrt_less(2*E/3,F(29,50_000))

cases=[
 dict(name="A_I<=1/200", ai=F(1,200), root=F(41,1000), inv=F(709,1000),
      B=F(747,1000), u0lo=F(664775,10**6), u0hi=F(664777,10**6),
      u1lo=F(438094,10**6), target=F(79,100)),
 dict(name="1/200<=A_I<=1/100", ai=F(1,100), root=F(58,1000),
      inv=F(711,1000), B=F(761,1000),
      u0lo=F(648702,10**6), u0hi=F(648704,10**6),
      u1lo=F(413297,10**6), target=F(189,250))
]

for q in cases:
    ai,B=q["ai"],q["B"]
    sqrt_less(ai/3,q["root"])
    assert 1<q["inv"]**2*2*(1-ai)
    budget=(1+q["root"])*q["inv"]+F(29,50_000)+eta
    assert budget<B
    assert B*B>=F(1,2) and B*B<F(3,4)-eta*eta
    u0sq=1-eta*eta-B*B
    u1sq=F(3,4)-eta*eta-B*B
    sqrt_greater(u0sq,q["u0lo"])
    sqrt_less(u0sq,q["u0hi"])
    sqrt_greater(u1sq,q["u1lo"])
    D_hi=q["u0hi"]-q["u1lo"]
    for name,n,c,etacoef,k in [
        ("2+2",8,2,4,8),
        ("3+1",12,3,6,16),
        ("4+0",24,6,12,24)
    ]:
        lb=(n*B*q["u0lo"]-c-etacoef*eta*eta)/(1+k*B*D_hi)
        assert lb>q["target"],(q["name"],name,lb)
        print("PASS",q["name"],name,"A_C >",lb)
assert F(79,100)>F(383,504)
assert F(189,250)+F(1,200)>F(383,504)
print("PASS Type-E midpoint contradiction in both rational cases")

# Double-angle rank-two identity on four rational planar vectors.
v=[(F(1),F(2)),(F(-2),F(3)),(F(3),F(1)),(F(5),F(-4))]
t=[x*x+y*y for x,y in v]
def C(i,j):
    d=v[i][0]*v[j][0]+v[i][1]*v[j][1]
    return 2*d*d-t[i]*t[j]
H=[[F(1) if i==j else C(i,j)/(t[i]*t[j])
    for j in range(4)] for i in range(4)]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
for i,j,k in combinations(range(4),3):
    f=(t[i]**2*t[j]**2*t[k]**2+2*C(i,j)*C(i,k)*C(j,k)
       -t[k]**2*C(i,j)**2-t[j]**2*C(i,k)**2-t[i]**2*C(j,k)**2)
    assert f==0
for rows in combinations(range(4),3):
    for cols in combinations(range(4),3):
        assert det3([[H[i][j] for j in cols] for i in rows])==0
print("PASS sign-free core polynomial and all 3x3 double-angle minors")
print("PASS; spectral gap >1/8 is a separately retained exact input")
