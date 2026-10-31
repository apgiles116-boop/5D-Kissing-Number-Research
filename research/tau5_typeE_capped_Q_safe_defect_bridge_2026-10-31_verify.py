#!/usr/bin/env python3
"""Exact arithmetic verifier for capped Q/six-defect bridge, 2026-10-31.
The proofs are analytic; this checks all stated rational constants and identities.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import symbols, simplify

A=F(383,504)
D=F(1780062775,4032758016)
assert F(3,4)<A<1 and F(1,4)<D<F(1,2)
U=3*F(1,16)+(A-F(3,4))**2
assert U==F(47653,254016)
L=30-3*A+A*A/F(10)-U/F(2)
assert L==F(8790283,317520)
assert L-F(17456771,635040)==F(131,672)
Phi=F(1,16)+(D-F(1,4))**2
Core=F(3,2)+D+Phi
Safe=L-Core
assert Safe==F(2085231131661776940907,81315686078061281280)
assert L-F(3,2)-F(1,3)-(F(1,16)+(F(1,3)-F(1,4))**2)==F(8186113,317520)

# Algebraic cancellation of core U_C in the variance-sensitive bound.
AA,UI,UC,AC,VM,V,DD,BC=symbols("AA UI UC AC VM V DD BC")
Q=30-3*AA+AA**2/10-(UI+UC)/2+V/2
E=DD+(AC**2-VM-UC)/2
S=Q-F(3,2)-E+BC
Target=F(57,2)-3*AA+AA**2/10-(UI+AC**2)/2+(V+VM)/2-DD+BC
assert simplify(S-Target)==0

# Capped-square extremizer checked exhaustively on a rational grid.
for n in range(33):
    total=F(n,64)
    if total>F(1,2): continue
    cap=total**2 if total<=F(1,4) else F(1,16)+(total-F(1,4))**2
    for i in range(17):
      for j in range(17):
        x,y=F(i,64),F(j,64)
        if x+y>total: continue
        rem=total-x-y
        val=x*x+y*y
        for _ in range(4):
          t=min(rem,F(1,4))
          val+=t*t
          rem-=t
        assert rem==0 and val<=cap

# Exact 20-line D5 template: 120 correlations squared 1/4, others zero.
roots=[]
for i,j in combinations(range(5),2):
    for sign in (1,-1):
        v=[0]*5
        v[i]=1
        v[j]=sign
        roots.append(v)
assert len(roots)==20
Qsum=F(0)
for i,j in combinations(range(20),2):
    dot=sum(x*y for x,y in zip(roots[i],roots[j]))
    Qsum+=F(dot*dot,4)
assert Qsum==30

print("Umax",U,"=",float(U))
print("Global Q floor",L,"=",float(L))
print("Improvement",F(131,672))
print("Six-core square upper",Core,"=",float(Core))
print("184-safe square lower",Safe,"=",float(Safe))
print("Symbolic variance identity: PASS")
print("Rational capped-simplex checks: PASS")
print("Exact D5 reference: PASS")
print("ALL CHECKS PASSED")
