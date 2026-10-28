#!/usr/bin/env python3
"""Exact 16-line D5 Q-rank persistence verifier (Python 3, SymPy)."""
from itertools import combinations, permutations, product
from collections import Counter
from sympy import Matrix, Poly, Rational as R, Symbol, count_roots, sqrt, expand

a,d2=Symbol('a'),Symbol('d2')
c=1-(a+d2)/2
lhs=(1-a)**2+1-2*c**2-a**2/5
rhs=(2-a)*d2-d2**2/2+R(3,10)*a**2
assert expand(lhs-rhs)==0

roots=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5;v[i]=1;v[j]=sign
        roots.append(((i,j,sign),tuple(v)))
assert len(roots)==20
idx={desc:k for k,(desc,_) in enumerate(roots)}
actions=set()
for perm in permutations(range(5)):
    for signs in product((-1,1),repeat=5):
        if signs[0]*signs[1]*signs[2]*signs[3]*signs[4]!=1:
            continue
        image=[]
        for (i,j,sg),_ in roots:
            u,v=perm[i],perm[j]
            cu,cv=signs[i],sg*signs[j]
            if u>v:
                u,v=v,u;cu,cv=cv,cu
            image.append(idx[(u,v,cu*cv)])
        actions.add(tuple(image))
assert len(actions)==1920

V=Matrix([list(v) for _,v in roots])
H=V*V.T
K=H.multiply_elementwise(H)*5-Matrix.ones(20,20)*4
assert all(K[i,i]==16 for i in range(20))
remaining=set(combinations(range(20),4));orbits=[]
while remaining:
    rep=min(remaining)
    orbit={tuple(sorted(action[i] for i in rep)) for action in actions}
    assert orbit<=remaining
    remaining-=orbit
    orbits.append((rep,len(orbit)))
assert len(orbits)==17 and sum(n for _,n in orbits)==4845
T=Symbol('T');h=Poly(T**2-26*T+20,T)
assert count_roots(h,R(3,4),R(4,5))==1
ranks=Counter();sharp_count=0
for rep,n in orbits:
    keep=[i for i in range(20) if i not in rep]
    cp=Poly(K.extract(keep,keep).charpoly(T).as_expr(),T)
    factors=cp.factor_list()[1]
    nullity=next(m for p,m in factors if p.as_expr()==T)
    ranks[16-nullity]+=n
    if any(p==h for p,m in factors):sharp_count+=n
    for p,m in factors:
        if p.as_expr()==T or p==h:continue
        assert count_roots(p,0,1)==0,(rep,p)
assert ranks==Counter({14:3360,13:1440,12:45})
assert sharp_count==160

lam=(13-sqrt(149))/20
assert R(489,40)**2>149
assert R(31,800)==2*R(1,10)**2+R(3,10)*R(1,4)**2
assert lam>R(31,800)
upper_sqrt149=13-20*R(199,1000)**2
assert upper_sqrt149>0 and upper_sqrt149**2>149
assert lam>R(199,1000)**2
err2=2*R(1,10)**2+R(3,10)*R(1,2500)**2
assert err2==R(1,50)+R(3,62500000)
assert err2<R(71,500)**2
assert R(199,1000)-R(71,500)==R(57,1000)

print("PASS: exact Q perturbation identity")
print("PASS: 4845 sixteen-line D5 subsets in 17 exact Weyl orbits")
print("PASS: ranks 3360/1440/45 and sharp spectral gap")
print("PASS: epsilon<=1/10, radial deficit<=1/4 forces rank persistence")
print("PASS: near-seven sigma_r(T_Y)>57/1000 under retained hypotheses")
