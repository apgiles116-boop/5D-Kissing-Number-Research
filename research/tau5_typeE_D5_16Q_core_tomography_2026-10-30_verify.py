from itertools import combinations
import random
import sympy as s

E=s.eye(5)
R={}
for i,j in combinations(range(5),2):
    for h in (1,-1):
        v=s.zeros(5,1)
        v[i]=s.sqrt(s.Rational(1,2))
        v[j]=h*s.sqrt(s.Rational(1,2))
        R[i,j,h]=v

def q(v):
    return v*v.T-v.dot(v)*E/5

Q={k:q(v) for k,v in R.items()}
C=[(0,j,1) for j in range(1,5)]
I=[k for k in R if k not in C]
K=s.Matrix([[s.trace(Q[i]*Q[j]) for j in I] for i in I])
t=s.Symbol('lambda')
assert s.factor(K.charpoly(t).as_expr())==s.factor(t*t*(t-1)**6*(4*t*t-7*t+2)**3*(20*t*t-31*t+6)/1280)
assert K.rank()==14

for j in range(1,5):
    T=[(k,l) for k,l in combinations(range(1,5),2) if j not in (k,l)]
    assert Q[0,j,1]+Q[0,j,-1]+sum((Q[k,l,1]+Q[k,l,-1] for k,l in T),s.zeros(5))/2==s.zeros(5)
    for k,l in T:
        assert (k,l,1) in I and (k,l,-1) in I

for cycle in ({(1,3):1,(1,4):-1,(2,3):-1,(2,4):1},
              {(1,2):1,(1,4):-1,(2,3):-1,(3,4):1}):
    assert sum((c*(Q[i,j,1]+Q[i,j,-1]) for (i,j),c in cycle.items()),s.zeros(5))==s.zeros(5)

B=[k for k in I if k not in ((2,4,1),(3,4,1))]
G=s.Matrix([[s.trace(Q[i]*Q[j]) for j in B] for i in B])
assert G.det()==s.Rational(1,1280)
Y=s.Matrix([[s.trace(Q[i]*Q[c]) for c in C] for i in B])
H=s.Matrix([[s.trace(Q[c]*Q[d]) for d in C] for c in C])
assert H==Y.T*G.inv()*Y

# The Schur-complement reconstruction is universal, not D5-specific.
rng=random.Random(20261030)
Z={k:s.Matrix([s.Rational(rng.randrange(-9,10),13) for _ in range(5)]) for k in R}
Q2={k:q(v) for k,v in Z.items()}
G2=s.Matrix([[s.trace(Q2[i]*Q2[j]) for j in B] for i in B])
assert G2.det()!=0
Y2=s.Matrix([[s.trace(Q2[i]*Q2[c]) for c in C] for i in B])
H2=s.Matrix([[s.trace(Q2[c]*Q2[d]) for d in C] for c in C])
assert H2==Y2.T*G2.inv()*Y2

assert s.sqrt(s.Rational(1,5))<s.Rational(9,20)
assert s.Rational(47,100)**2<s.Rational(9,40)
assert s.Rational(9,20)+s.Rational(1,250)<s.Rational(47,100)
print('PASS: exact spectrum, four core relations, two cycles, determinant, D5 and non-D5 tomography, rank threshold')
