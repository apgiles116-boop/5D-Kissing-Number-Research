"""Exact arithmetic checks for Type-E Walsh-Cauchy spectral note, 2026-11-02."""
from itertools import combinations
import sympy as S

a,b,h,p,q,d=S.symbols("a b h p q d",real=True)
G=S.Matrix([[a,0,h,p],[0,1-a,q,d],[h,q,b,0],[p,d,0,1-b]])
assert S.expand(G.extract([0,2,3],[0,2,3]).det()-((1-b)*(a*b-h*h)-b*p*p))==0
assert S.expand(G.extract([0,1,2],[0,1,2]).det()-((1-a)*(a*b-h*h)-a*q*q))==0
print("PASS two principal 3x3 Gram determinant identities")

edges=list(combinations(range(4),2))
n=0
for mask in range(64):
    E={edges[i] for i in range(6) if mask>>i&1}
    tri=any(all(tuple(sorted(e)) in E for e in combinations(T,2))
            for T in combinations(range(4),3))
    deg=[sum(v in e for e in E) for v in range(4)]
    c4=len(E)==4 and deg==[2,2,2,2]
    if tri or c4: continue
    n+=1
    B=S.zeros(4)
    for i,j in E:B[i,j]=B[j,i]=1
    H=S.sqrt(3)*S.eye(4)-B
    for k in range(1,5):
        for idx in combinations(range(4),k):
            det=S.simplify(H.extract(idx,idx).det())
            assert det.is_nonnegative, (E,det)
assert n==38
print("PASS all 38 labeled triangle-free/C4-free supports: rho<=sqrt(3)")

D,T=S.symbols("D T")
assert S.simplify(S.Rational(18,17)*(D+T/2)-(D+T))==(D-8*T)/17
assert S.simplify(S.Rational(18,17)*S.sqrt(3)/2-9*S.sqrt(3)/17)==0
Q=S.Rational(141813,5000)
max44=S.Rational(44,4)+S.Rational(140,9)
max45=S.Rational(45,4)+S.Rational(139,9)
assert max44==S.Rational(239,9) and max45==S.Rational(961,36)
C45=S.simplify((Q-S.Rational(3,2)-max44)*17/(9*S.sqrt(3)))
C46=S.simplify((Q-S.Rational(3,2)-max45)*17/(9*S.sqrt(3)))
assert S.simplify(C45-234889*S.sqrt(3)/1215000)==0
assert S.simplify(C46-128639*S.sqrt(3)/1215000)==0
assert 0<C46<C45<S.Rational(383,504)
print("PASS conditional 45 threshold",C45, C45.evalf(15))
print("PASS conditional 46 threshold",C46, C46.evalf(15))

V=[]
for i,j in combinations(range(5),2):
    for t in (1,-1):
        v=S.zeros(5,1);v[i]=1;v[j]=t
        V.append(v/S.sqrt(2))
QQ=[v*v.T-S.eye(5)/5 for v in V]
K=S.Matrix(20,20,lambda i,j:S.trace(QQ[i]*QQ[j]))
assert K.eigenvals()=={S.Rational(3,2):4,S.Integer(1):10,S.Integer(0):6}
assert K.rank()==14
print("PASS exact D5 Q Gram spectrum; nullity 6")
print("STATUS: Type E open; global 40<=tau_5<=44")
