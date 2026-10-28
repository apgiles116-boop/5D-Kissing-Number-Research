#!/usr/bin/env python3
"""Exact algebra regression for Type E mass/Q/safe-pair bridge.
Analytic PSD and convexity arguments are in the companion proof note.
"""
import sympy as s
from itertools import combinations

a,t=s.symbols('a t',real=True)
D=s.expand(21-7*(1-2*a)**2*(4*(1-2*a)**2-1))
assert D==196*a-644*a**2+896*a**3-448*a**4
assert s.expand(7*t*t*(4*t*t-1)-(1+s.Rational(35,3)*(t*t-s.Rational(1,5))+28*(t**4-s.Rational(2,3)*t*t+s.Rational(1,21))))==0
assert s.expand(s.diff(D,a,2)+56*(96*a*a-96*a+23))==0
assert s.diff(D,a).subs(a,s.Rational(1,4))==14
r=(1-s.sqrt((7+s.sqrt(721))/56))/2
s0=(1-s.sqrt((7+s.sqrt(s.Rational(2387,3)))/56))/2
s1=(1-s.sqrt((7+s.sqrt(s.Rational(4907,3)))/56))/2
for v,target in [(r,15),(s0,s.Rational(43,3)),(s1,s.Rational(41,6))]:
    assert s.simplify(D.subs(a,v)-target)==0
    assert 0<float(v)<.25
assert float(r)>float(s0)>float(s1)>0
Astar=s.Rational(1,2)+r+s1
Ustar=s.Rational(1,8)+r*r+s1*s1
Lstar=30-3*Astar+Astar*Astar/10-Ustar/2
ar=s.Rational(651038,10**6)
rr=s.Rational(111256,10**6)
sr=s.Rational(39782,10**6)
assert D.subs(a,rr)>15 and D.subs(a,sr)>s.Rational(41,6)
assert float(Astar)<float(ar)
Ur=s.Rational(1,8)+rr*rr+sr*sr
Lr=30-3*ar+ar*ar/10-Ur/2
assert Lr==s.Rational(17512369247009,625000000000)
assert float(Lstar)>float(Lr)>28.01979

g=lambda x:x+x*x
v=s.symbols('v',real=True)
h=s.Rational(1,6)-v/3-v*v/3
assert 2*g(s.Rational(1,8))==s.Rational(9,32)
assert h.subs(v,s.Rational(1,4))==s.Rational(1,16)
assert g(h.subs(v,s.Rational(1,4)))+s.Rational(9,8)*s.Rational(1,4)==s.Rational(89,256)
assert s.Rational(57,256)+s.Rational(17,32)*s.Rational(1,8)==s.Rational(74,256)
assert s.diff(h,v)==-(1+2*v)/3
assert s.Rational(9,8)-s.Rational(2,3)>0
assert s.Rational(3,2)+s.Rational(89,256)==s.Rational(473,256)
assert s.Rational(3,2)+s.Rational(9,32)==s.Rational(57,32)

F3={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[[(0,2),(1,4),(3,6),(5,7)],[(0,4),(1,7),(2,3),(5,6)],[(0,5),(1,4),(2,7),(3,6)]]
for kP,P in enumerate(matchings):
    cross={};forced={}
    for i,j in combinations(range(4),2):
        contacts=[(-1)**(ai+aj) for ai,u in enumerate(P[i]) for aj,w in enumerate(P[j]) if tuple(sorted((u,w))) in F3]
        assert len(set(contacts))<=1
        cross[(i,j)]=len(contacts)
        if contacts:forced[(i,j)]=-contacts[0]
    assert sorted(cross.values())==([1]*6 if kP==1 else [0,1,1,1,1,2])
    for triple in combinations(range(4),3):
        pairs=list(combinations(triple,2))
        if all(e in forced for e in pairs):
            assert forced[pairs[0]]*forced[pairs[1]]*forced[pairs[2]]==-1

Z=s.Matrix([[s.Rational(((i+2)*(j+3))%7-3,13) for j in range(5)] for i in range(20)])
rvec=[(Z.row(i)*Z.row(i).T)[0] for i in range(20)]
aval=[1-x for x in rvec]
A=sum(aval);U=sum(x*x for x in aval)
Fz=Z.T*Z
Vz=s.trace((Fz-(20-A)/5*s.eye(5))**2)
wtotal=sum(((Z.row(i)*Z.row(j).T)[0])**2 for i in range(20) for j in range(i+1,20))
assert s.simplify(wtotal-(30-3*A+A*A/10-U/2+Vz/2))==0

print("PASS: exact mass/Q/F3 bridge regression")
for label,value in [("Astar",Astar),("Ustar",Ustar),("Lstar",Lstar),("P1/P3 safe floor",Lstar-s.Rational(473,256)),("P2 safe floor",Lstar-s.Rational(57,32))]:
    print(label,s.N(value,20))

cstar=s.Rational(1,4)-Astar/10-Ustar/100
cr=s.Rational(1,4)-ar/10-Ur/100
assert cr==s.Rational(917532974747,5000000000000)
assert float(cstar)>float(cr)>float(s.Rational(34697,201600))
print("new frame/mixing coefficient",s.N(cstar,20))
