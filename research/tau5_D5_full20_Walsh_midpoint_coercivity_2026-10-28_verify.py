#!/usr/bin/env python3
"""Exact D5 20-line Walsh-midpoint coercivity certificate."""
from itertools import combinations
from sympy import Matrix, Rational, symbols, factor, eye

pairs=list(combinations(range(5),2))
roots=[]
for i,j in pairs:
    for s in (1,-1):
        v=[0]*5; v[i]=1; v[j]=s
        roots.append(tuple(v))
assert len(roots)==20
V=Matrix(roots)
D=V*V.T
contacts=[(i,j,int(D[i,j])) for i,j in combinations(range(20),2)
          if abs(D[i,j])==1]
assert len(contacts)==120
assert sum(D[i,j]==0 for i,j in combinations(range(20),2))==70
adj=Matrix(20,20,lambda i,j: 1 if i!=j and abs(D[i,j])==1 else 0)
assert adj.eigenvals()=={Rational(12):1,Rational(2):4,Rational(-4):5,Rational(0):10}
assert V.T*V==8*eye(5)

rows=[]
for i in range(20):
    row=[0]*100
    for d in range(5): row[5*i+d]=roots[i][d]
    rows.append(row)
for i,j,sig in contacts:
    row=[0]*100
    for d in range(5):
        row[5*j+d]=roots[i][d]
        row[5*i+d]=sig*roots[j][d]
    rows.append(row)
L=Matrix(rows)
assert L.shape==(140,100)
x=symbols('x')
char=factor((L.T*L).charpoly(x).as_expr())
expected=(x-8)**10*(x-4)**10*(x-2)**20*\
    (x**3-24*x**2+146*x-48)**5*\
    (x**3-16*x**2+74*x-96)**15
assert factor(char-expected)==0
p=x**3-24*x**2+146*x-48
q=x**3-16*x**2+74*x-96
assert p.subs(x,Rational(1,3))<0<p.subs(x,Rational(7,20))
for lo,hi in [(10,11),(13,14)]:
    assert p.subs(x,lo)*p.subs(x,hi)<0
for lo,hi in [(2,3),(4,5),(8,9)]:
    assert q.subs(x,lo)*q.subs(x,hi)<0

assert Rational(57,100)**2 < Rational(1,3)
assert Rational(51,10)**2 > 26
assert Rational(3,2)**2 > 2
coef=5+Rational(1,5000)+Rational(1,2)*Rational(201,50)**2
assert coef==Rational(32701,2500)
assert Rational(117,250)>Rational(3,2)*coef/Rational(50)
print('PASS: D5 contacts=120, orthogonal pairs=70, frame operator=4I')
print('PASS: contact adjacency spectrum {12:1, 2:4, -4:5, 0:10}')
print('PASS: exact Walsh-midpoint 100x100 characteristic polynomial:',char)
print('PASS: minimum squared singular value >1/3')
print('PASS: under epsilon^2<=A, either A=0 or A>1/2500')
