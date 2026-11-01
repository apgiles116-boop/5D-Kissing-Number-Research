"""Exact arithmetic checks for tau5_typeE_mixed_Walsh_incidence_2026-11-01.md.
Analytic inequalities and universal quantifiers are proved in the note.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

B=F(2595,256); c=F(1245,256)
def D(t): return 196*t-644*t*t+896*t**3-448*t**4
assert D(F(39781,10**6)) < F(41,6) < D(F(39782,10**6))
assert D(F(27150,10**6)) > c
assert 64*10**12 < 175*604745**2
assert 64*200**2 < 175*121**2
assert F(7,250)/c < F(7,1200)
assert F(3,140)-F(17,4)*F(7,1200)+F(3,200)==F(391,33600)>0
Ahi=F(539782,10**6); Alo=F(539781,10**6)
rhi=F(27150,10**6); hhi=F(604745,10**6)
glo=F(4,5)-Ahi/5-hhi/2
assert glo>0
fupper=F(3,10)+4*Ahi-Alo**2/10-(Alo-rhi)**2/8+hhi/4+F(9,28)-F(5,8)*glo**2
assert fupper==F(3107838072643181,1120000000000000)<F(111,40)

a,b,cc,d=sp.symbols('a b c d')
vals=[a+b+cc+d,a+b-cc-d,a-b+cc-d,a-b-cc+d]
assert sp.expand(sum(v*v for v in vals)/4-(a*a+b*b+cc*cc+d*d))==0
assert sp.expand((vals[0]+vals[3])/2-(a+d))==0
assert sp.expand((vals[1]+vals[2])/2-(a-d))==0

# Rational 5D unit-vector sanity check of global mixed-Walsh identity.
eye=[sp.eye(5)[:,i] for i in range(5)]
ms=[]; zs=[]
for i in range(20):
    v=eye[i%5]; w=-sp.Rational(3,5)*v+sp.Rational(4,5)*eye[(i+1)%5]
    ms.append((v+w)/2); zs.append((v-w)/2)
A=sum((v.dot(v) for v in ms),sp.Integer(0))
U=sum((v.dot(v)**2 for v in ms),sp.Integer(0))
Sm=sum((v*v.T for v in ms),sp.zeros(5))
Sz=sum((v*v.T for v in zs),sp.zeros(5))
u=eye[0]
T=u*u.T+2*(Sm+Sz)-sp.Rational(41,5)*sp.eye(5)
q=(u.T*T*u)[0]
Vz=sp.trace((Sz-(20-A)*sp.eye(5)/5)**2)
R=sum((ms[i].dot(ms[j])**2+ms[i].dot(zs[j])**2+zs[i].dot(ms[j])**2
       for i in range(20) for j in range(i+1,20)),sp.Integer(0))
Rrhs=sp.Rational(1,10)+4*A-A*A/10-U/2-q/4+sp.trace(T*T)/8-Vz/2
assert sp.simplify(R-Rrhs)==0

E={tuple(sorted(p)) for p in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
def matchings(vertices):
    if not vertices:
        yield ()
        return
    v=vertices[0]
    for w in vertices[1:]:
        if (v,w) in E:
            for rest in matchings(tuple(x for x in vertices if x!=v and x!=w)):
                yield ((v,w),)+rest
allm=list(matchings(tuple(range(8))))
assert len(allm)==3
patterns=[]
for P in allm:
    counts=[]
    for i,j in combinations(range(4),2):
        deep=[(x,y) for x in P[i] for y in P[j] if tuple(sorted((x,y))) in E]
        counts.append(len(deep))
        if len(deep)==2:
            assert len({x for x,y in deep})==len({y for x,y in deep})==2
    patterns.append(tuple(sorted(counts)))
assert patterns.count((1,1,1,1,1,1))==1
assert patterns.count((0,1,1,1,1,2))==2

Dmax=F(441401,10**6)
safe=F(282677,10000)+F(949,5000)/2-F(5,4)-Dmax-Dmax**2
assert safe==F(26476364157199,10**12)
assert F(42,4)+F(143,9)==F(475,18)<safe
print("PASS: exact rational brackets, global identity, F3 incidence and 43-count")
