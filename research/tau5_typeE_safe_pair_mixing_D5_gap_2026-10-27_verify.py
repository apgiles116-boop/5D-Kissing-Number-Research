#!/usr/bin/env python3
"""Exact SymPy verifier for the 2026-10-27 safe-pair/D5 template note."""
from collections import Counter
from itertools import combinations
import sympy as s

x=s.symbols("x")
B,X,Y,Z=s.symbols("B X Y Z",real=True)
q=[B+sig*X+tau*Y+sig*tau*Z for sig in (1,-1) for tau in (1,-1)]
assert s.expand(sum(v*v for v in q)/4-(B*B+X*X+Y*Y+Z*Z))==0

# Twenty D5 projective lines, each having twelve |inner product|=1/2 contacts.
lines=[]
for p in range(5):
    for r in range(p+1,5):
        for sign in (1,-1):
            v=s.zeros(5,1); v[p]=1; v[r]=sign
            lines.append(v)
assert len(lines)==20
assert all(sum(j!=i and abs(v.dot(w))==1 for j,w in enumerate(lines))==12
           for i,v in enumerate(lines))

# Fix the distinguished line (e0+e1)/sqrt(2). Its twelve neighbours
# are w/sqrt(2), w=e_a +/- e_k, a in {0,1}, k in {2,3,4}.
ws=[]
for a in (0,1):
    for k in (2,3,4):
        for sign in (1,-1):
            w=s.zeros(5,1);w[a]=1;w[k]=sign;ws.append(w)
D=s.diag(6,6,4,4,4) # Eight times the full contact-frame operator
U=s.Matrix([[1,0,0,0],[-1,0,0,0],[0,1,0,0],
            [0,0,1,0],[0,0,0,1]]) # u_i-perpendicular basis
metric=U.T*U
assert metric==s.diag(2,1,1,1)

patterns=Counter()
c=(11-s.sqrt(57))/32
for triple in combinations(range(12),3):
    T=D-s.Add(*(ws[j]*ws[j].T for j in triple))
    poly=s.factor((U.T*T*U-x*metric).det()/2)
    patterns[poly]+=1
    # Exact PSD at the sharp lower generalized eigenvalue.
    R=U.T*(T-8*c*s.eye(5))*U
    for k in range(1,5):
        v=s.simplify(R[:k,:k].det())
        assert v==0 or v.is_positive is True

expected={
    s.factor((x-4)*(x-2)*(2*x*x-15*x+26)/2):96,
    s.factor((x-3)**2*(2*x*x-15*x+24)/2):64,
    s.factor((x-4)*(2*x**3-19*x*x+52*x-40)/2):48,
    s.factor((x-4)**2*(2*x*x-11*x+8)/2):12,
}
assert patterns==Counter(expected)
assert sum(patterns.values())==220
assert c>s.Rational(1,10)
gap=s.factor(s.Rational(49,32)*c)
assert gap==(539-49*s.sqrt(57))/1024
print("PASS: Hadamard/Parseval identity, D5 12-contact structure")
print("PASS: all 220 triple-deletion generalized characteristic polynomials")
print("PASS: exact sharp restricted operator c =",c)
print("CONDITIONAL D5 midpoint gap A >=",gap,"~",gap.evalf(15))
