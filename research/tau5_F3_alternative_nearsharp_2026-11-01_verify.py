#!/usr/bin/env python3
"""Exact rational/SymPy verifier for the near-sharp F3 alternative-matching theorem."""
from itertools import combinations
from sympy import Rational as R, symbols, expand, simplify, Matrix

E = {tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),
     (2,3),(2,7),(3,6),(5,6),(5,7)]}
P1={(0,2),(1,4),(3,6),(5,7)}
P2={(0,5),(1,4),(2,7),(3,6)}
swap=(0,1,5,6,4,2,3,7)
assert {tuple(sorted((swap[i],swap[j]))) for i,j in E}==E
assert {tuple(sorted((swap[i],swap[j]))) for i,j in P1}==P2

x=symbols('x0:10')
def forms(r,s):
    return (1+r*x[3]+s*x[4]+r*s*x[5],
            1+r*x[0]+s*x[2]+r*s*x[7],
            x[8]+r*x[1]+s*x[9]+r*s*x[6])
def qform(r,s,lam,sgn):
    A,B,T=forms(r,s)
    return A+lam**2*B+2*sgn*lam*T
A_pp,B_pp,_=forms(1,1)
k=R(2035298537,219942800000)
terms=[
 (R(475,199948),qform(-1,-1,R(74,5),1)),
 (R(1805,29722),qform(-1,1,R(11,19),-1)),
 (R(99019,199948),qform(1,-1,R(7,100),-1)),
 (R(715,99974),qform(1,-1,R(69,1000),-1)),
 (R(15621,29722),A_pp),
 (R(1334800019,2856400000),B_pp),
 (R(95,2702),qform(1,1,1,1)),
 (R(357799867,9997400000),x[0]+R(1,2)),
 (R(95,814),-R(1,2)-x[4]),
 (R(380,1351),-R(1,2)-x[6]),
]
assert all(c>0 for c,f in terms)
assert simplify(expand(2+x[3]+x[7]-k-sum(c*f for c,f in terms)))==0
assert k>R(505,63488) and k>R(1,109)

p=R(698608951,10000000000)
t=R(17281125305,10000000000)
q=R(9999999999999,10000000000000)
eta=R(1,10000000000000)
eps=(1-q*q)/2
a=p*p/2
b=(3-t*t)/2
v=[None]*10
v[0]=-R(1,2)
v[2]=R(1,2)-b
v[3]=-1+a
v[4]=-R(1,2)-eps
v[5]=R(1,2)-a+eps
v[7]=-1+b
Rpp=R(0);Rpm=p;Rmp=q*t;Rmm=-2-4*eta+q*t+p
v[8]=(Rpp+Rpm+Rmp+Rmm)/4
v[1]=(Rpp+Rpm-Rmp-Rmm)/4
v[9]=(Rpp-Rpm+Rmp-Rmm)/4
v[6]=(Rpp-Rpm-Rmp+Rmm)/4
assert all(-1<=v[j]<-R(1,2) for j in [3,4,6,7])
assert all(-R(1,2)<=v[j]<=R(1,2) for j in [0,1,2,5,8,9])

expected={(-1,-1):2,(-1,1):1,(1,-1):1,(1,1):0}
for (r,s),rk in expected.items():
    A,B,T=(expand(f.subs(dict(zip(x,v)))) for f in forms(r,s))
    M=Matrix([[A,T],[T,B]])
    assert A>=0 and B>=0 and A*B-T*T>=0
    assert M.rank()==rk
assert sum(expected.values())==4

orbits={
 0:[(1,6),(3,4)],
 1:[(0,6),(1,2),(3,7),(4,5)],
 2:[(1,3),(4,6)],
 3:[(0,2),(5,7)],
 4:[(0,5),(2,7)],
 5:[(0,7),(2,5)],
 6:[(0,4),(1,7),(2,3),(5,6)],
 7:[(1,4),(3,6)],
 8:[(0,1),(2,6),(3,5),(4,7)],
 9:[(0,3),(1,5),(2,4),(6,7)],
}
assert {tuple(sorted(pair)) for pairs in orbits.values() for pair in pairs}==set(combinations(range(8),2))
G=Matrix.eye(8)
for j,pairs in orbits.items():
    for u,w in pairs:G[u,w]=G[w,u]=v[j]
assert G.rank()==4
assert all(G[i,j]<-R(1,2) for i,j in E)
assert all(-R(1,2)<=G[i,j]<=R(1,2) for i,j in combinations(range(8),2) if (i,j) not in E)
upper=a+b
assert 2+sum(G[i,j] for i,j in P1)/2==upper
assert k<upper<R(1,108) and upper-k<R(1,10000000)
print("PASS: exact Fourier-SOS identity and strict positive coefficients")
print("PASS: F3 matching-exchange automorphism")
print("PASS: exact rank-four Gram with ten strict deep contacts and 18 safe pairs")
print("LOWER:",k,"=",float(k))
print("UPPER:",upper,"=",float(upper))
print("GAP:",upper-k,"=",float(upper-k))
print("STATUS: standalone F3 theorem; Type E transfer conditional")
