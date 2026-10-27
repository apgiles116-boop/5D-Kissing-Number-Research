"""Exact SymPy regression: four-core rank-five lift and near-antipodal bounds.
Analytic universality of the stability inequalities is proved in the companion note.
This constructs nine code points, NOT a complete Type-E 41-code.
"""
import sympy as sp
from itertools import combinations

b = sp.Rational(131,1008)
E = sp.eye(5)
e = [E[:,j] for j in range(5)]
dot = lambda u,v: sp.simplify((u.T*v)[0])
m = [e[0]/2,-e[0]/2,sp.sqrt(b)*e[1],-sp.sqrt(b)*e[1]]
z = [sp.sqrt(3)*e[2]/2,sp.sqrt(3)*e[2]/2,
     e[2]/sp.sqrt(3)+sp.sqrt(sp.Rational(5,12))*e[3]+sp.sqrt(sp.Rational(1,4)-b)*e[4],
     e[2]/sp.sqrt(3)+sp.sqrt(sp.Rational(5,12))*e[3]-sp.sqrt(sp.Rational(1,4)-b)*e[4]]
Gm=sp.Matrix([[dot(u,v) for v in m] for u in m])
Gz=sp.Matrix([[dot(u,v) for v in z] for u in z])
assert Gm == sp.Matrix([[sp.Rational(1,4),-sp.Rational(1,4),0,0],
                         [-sp.Rational(1,4),sp.Rational(1,4),0,0],
                         [0,0,b,-b],[0,0,-b,b]])
assert Gz == sp.Matrix([[sp.Rational(3,4),sp.Rational(3,4),sp.Rational(1,2),sp.Rational(1,2)],
                         [sp.Rational(3,4),sp.Rational(3,4),sp.Rational(1,2),sp.Rational(1,2)],
                         [sp.Rational(1,2),sp.Rational(1,2),1-b,sp.Rational(1,2)+b],
                         [sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,2)+b,1-b]])
assert all(dot(mi,zj)==0 for mi in m for zj in z)
assert all(dot(m[i],m[i])+dot(z[i],z[i])==1 for i in range(4))
V=[m[i]+sgn*z[i] for i in range(4) for sgn in (1,-1)]
assert all(dot(V[i],V[j])<=sp.Rational(1,2) for i,j in combinations(range(8),2))
deep={(i,j) for i,j in combinations(range(8),2) if dot(V[i],V[j])<=-sp.Rational(1,2)}
assert deep=={(i,j) for i in range(0,8,2) for j in range(1,8,2)}
x=(e[0]+e[1])/sp.sqrt(2)
assert dot(x,x)==1
assert all(abs(dot(x,v))<sp.Rational(1,2) for v in V)
assert sp.Matrix.hstack(*m,*z,x).rank()==5
A=sum(dot(mi,mi) for mi in m)
assert A==sp.Rational(383,504)
d={(i,j):max(sp.Integer(0),abs(dot(z[i],z[j]))-sp.Rational(1,2))
   for i,j in combinations(range(4),2)}
assert list(d.values())==[sp.Rational(1,4),0,0,0,0,b]
assert sum(d.values())==A/2
f=lambda t:(sp.Rational(1,2)+t)**2*t*(1+t)
assert sum(f(t) for t in d.values())==sp.Rational(241638909745,1032386052096)
for i,j in [(0,1),(2,3)]:
    eps=sp.Rational(1,4)-d[i,j]
    sgn=sp.sign(dot(z[i],z[j]))
    assert dot(m[i]+m[j],m[i]+m[j])<=2*eps
    assert dot(z[i]-sgn*z[j],z[i]-sgn*z[j])<=4*eps
    assert abs(dot(m[i],z[j])+sgn*dot(z[i],m[j]))<=eps
print("PASS: exact rank five, all 36 nine-point kissing inequalities,")
print("      midpoint cap, quartic saturation, near-antipodal regression.")
print("A_C=",A,"sum_d=",sum(d.values()),"quartic=",sum(f(t) for t in d.values()))
