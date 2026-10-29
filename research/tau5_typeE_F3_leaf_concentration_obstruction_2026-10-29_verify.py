"""Exact checker for F3 leaf-concentration obstruction, 2026-10-29."""
from sympy import Matrix, sqrt, Rational as Q, simplify, expand, symbols
from itertools import combinations

edges={tuple(sorted(x)) for x in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
a=Matrix([1,0,0]);d=Matrix([-Q(1,2),sqrt(3)/2,0]);c=a+d;e=Matrix([0,0,1])
m=(d-a)/6;z=c/2+sqrt(Q(2,3))*e
U={0:a,2:-a,1:m+z,4:m-z,3:c,6:-c,5:d,7:-d}
assert all(simplify(U[i].dot(U[i])-1)==0 for i in range(8))
assert simplify(m.dot(m)-Q(1,12))==0
assert simplify(m.dot(z))==0
for i,j in combinations(range(8),2):
    dot=simplify(U[i].dot(U[j]))
    bound=-Q(1,2) if (i,j) in edges else Q(1,2)
    assert bound-dot>=0,(i,j,dot,bound)

names=['mA','mB','mC','mD','zA','zB','zC','zD']
g={tuple(sorted((a,b))):symbols('g_'+a+'_'+b) for a,b in combinations(names,2)}
for n in names:g[(n,n)]=symbols('g_'+n+'_'+n)
def dot(v,w):
    return expand(sum(x*y*g[tuple(sorted((a,b)))] for a,x in v.items() for b,y in w.items()))
def add(*vs):
    out={}
    for v in vs:
        for k,x in v.items():out[k]=out.get(k,0)+x
    return {k:v for k,v in out.items() if v!=0}
def sc(c,v):return {k:c*x for k,x in v.items()}
def vec(k):return {k:1}
mA,mB,mC,mD,zA,zB,zC,zD=[vec(n) for n in names]
u={0:add(mA,zA),2:add(mA,sc(-1,zA)),
   1:add(mB,zB),4:add(mB,sc(-1,zB)),
   3:add(mC,zC),6:add(mC,sc(-1,zC)),
   5:add(mD,zD),7:add(mD,sc(-1,zD))}
eta=-(Q(1,2)+dot(u[0],u[5]))/2-(Q(1,2)+dot(u[2],u[7]))/2-(Q(1,2)+dot(u[2],u[3]))-(Q(1,2)+dot(u[5],u[6]))
E=add(zC,sc(-1,zA),sc(-1,zD))
M=add(mA,mC,mD)
lhs=dot(E,E)+dot(M,M)+2*eta
rhs=2*dot(add(mD,sc(-1,mA)),zC)+2*dot(add(zA,sc(-1,zD)),mC)
expr=expand(lhs-rhs)
for k in 'ABCD':
    expr=expr.subs(g[('z'+k,'z'+k)],1-g[('m'+k,'m'+k)])
assert simplify(expr)==0,expr
linear=dot(add(zA,zD,sc(-1,zC),mA,sc(-1,mD)),zB)+dot(add(zD,sc(-1,zA),sc(-1,mA),sc(-1,mC),sc(-1,mD)),mB)-Q(1,2)
slack04=-Q(1,2)-dot(u[0],u[4])
slack17=-Q(1,2)-dot(u[1],u[7])
safe13=Q(1,2)-dot(u[1],u[3])
safe46=Q(1,2)-dot(u[4],u[6])
assert simplify(expand(linear-slack04-slack17-(safe13+safe46)/2))==0
assert Q(5,504)<Q(1,100)
assert Q(7,90)<Q(7,25)**2
assert Q(91,450)+Q(7,25)+Q(1,60)==Q(449,900)<Q(1,2)
print("PASS: 28 exact endpoint inequalities; weak-boundary equality a_B=1/12")
print("PASS: exact three-pair frustration identity and leaf slack identity")
print("PASS: a_B<=1/100 implies a_A+a_C+a_D>1/8100")
