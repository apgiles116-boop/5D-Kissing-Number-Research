"""Exact rational regression for D5 Q-kernel fibre classification.
The theorem itself is proved algebraically in the accompanying research note.
"""
import sympy as s
from itertools import combinations
Q=s.Rational
I=s.eye(5)
E=list(combinations(range(5),2))
L=s.Matrix(5,10,lambda p,k:int(p in E[k]))-s.ones(5,10)/3
assert L*L.T==3*I-Q(5,9)*s.ones(5,5)
assert (L*L.T).eigenvals()=={s.S(3):4,Q(2,9):1}

pairs=[]
for i,j in E:
    u=s.zeros(5,1);v=s.zeros(5,1)
    u[i]=v[i]=1/s.sqrt(2)
    u[j]=1/s.sqrt(2);v[j]=-1/s.sqrt(2)
    pairs.append((u,v))

def check(pairs):
    S=[u*u.T+v*v.T for u,v in pairs]
    F=sum(S,s.zeros(5))
    B=[sum((S[k] for k,e in enumerate(E) if p in e),s.zeros(5))/3-Q(2,15)*F+I/5 for p in range(5)]
    err=[S[k]-B[i]-B[j] for k,(i,j) in enumerate(E)]
    assert sum(B,s.zeros(5))==I
    assert all(s.trace(x)==1 for x in B)
    Bls=[sum((S[k] for k,e in enumerate(E) if p in e),s.zeros(5))/3-F/12 for p in range(5)]
    cls=[S[k]-Bls[i]-Bls[j] for k,(i,j) in enumerate(E)]
    C=sum((s.trace(x*x) for x in cls),s.S.Zero)/2
    V=s.trace((F-4*I)**2)
    assert sum((s.trace(x*x) for x in err),s.S.Zero)==2*C+V/10
    D=[(B[i]+B[j])**2-(B[i]+B[j]) for i,j in E]
    for p in range(5):
        star=sum((D[k] for k,e in enumerate(E) if p in e),s.zeros(5))
        assert B[p]**2-B[p]==star-sum(D,s.zeros(5))/3
    for k,e in enumerate(E):
        meet=[h for h,f in enumerate(E) if h!=k and set(e)&set(f)]
        assert len(meet)==6
        assert sum((S[h] for h in meet),s.zeros(5))==S[k]+2*I+sum((err[h] for h in meet),s.zeros(5))-err[k]
    return C,V,B

C,V,B=check(pairs)
assert C==V==0 and all(b*b==b for b in B)
rot=list(pairs)
u,v=rot[0]
rot[0]=(Q(3,5)*u+Q(4,5)*v,-Q(4,5)*u+Q(3,5)*v)
C,V,_=check(rot)
assert C==V==0
pert=list(rot)
u,v=pert[0]
h=s.Matrix([1,2,0,0,0]);H=I-2*h*h.T/h.dot(h)
pert[0]=(H*u,v)
C,V,_=check(pert)
assert C>0 and V>0
for k,e in enumerate(E):
    if 0 in e:continue
    for h,f in enumerate(E):
        if h==k or not(set(e)&set(f)):continue
        assert all(s.simplify((u.dot(v))**2-Q(1,4))==0 for u in pairs[k] for v in pairs[h])
print('PASS: exact Q-fibre reconstruction, cycle/global residuals, projector identity, meeting incidence and D5 saturation')
