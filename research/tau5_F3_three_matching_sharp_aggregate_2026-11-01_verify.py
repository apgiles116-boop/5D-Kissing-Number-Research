#!/usr/bin/env python3
"""Exact SymPy verification: sharp F3 aggregate matching midpoint energy."""
import sympy as S

y = S.symbols("y", positive=True)
g = y**4 + 8*y**3 + 15*y**2 - 2*y - 4
lo, hi = S.Rational(509,1000), S.Rational(51,100)
assert g.subs(y,lo) < 0 < g.subs(y,hi)
assert S.expand(S.diff(g,y,2)-(12*y*y+48*y+30)) == 0

P0 = [(0,4),(1,7),(2,3),(5,6)]
P1 = [(0,2),(1,4),(3,6),(5,7)]
P2 = [(0,5),(1,4),(2,7),(3,6)]
edges = {tuple(sorted(e)) for P in (P0,P1,P2) for e in P}
assert edges == {(0,2),(0,4),(0,5),(1,4),(1,7),
                 (2,3),(2,7),(3,6),(5,6),(5,7)}
A, B = [0,2,5,7], [4,3,6,1]
order = A+B
W = S.zeros(8)
for P in (P0,P1,P2):
    for i,j in P:
        ii,jj = order.index(i),order.index(j)
        W[ii,jj] += 1
        W[jj,ii] += 1
J = S.zeros(4)
for i,j in [(0,3),(1,2)]:
    J[i,j]=J[j,i]=1
C4 = S.ones(4)-S.eye(4)-J
assert W[:4,:4] == C4
assert W[4:8,4:8] == 2*J
assert W[:4,4:8] == S.eye(4)
E = S.diag(J,S.zeros(4))
H = S.Matrix([[1,1,1,1],[1,1,-1,-1],
              [1,-1,1,-1],[1,-1,-1,1]])/2
assert H.T*H == S.eye(4)
assert H.T*C4*H == S.diag(2,0,0,-2)
assert H.T*J*H == S.diag(1,-1,-1,1)

mu = 1-2/(y*(y+4))
a = -mu-1/y
b = -2-y
K = W+mu*E-S.diag(*([a]*4+[b]*4))
expected = [
    S.Matrix([[4+1/(y+4),1],[1,y+4]]),
    S.Matrix([[1/y,1],[1,y]]),
    S.Matrix([[1/y,1],[1,y]]),
    S.Matrix([[1/(y+4),1],[1,y+4]])]
T = S.diag(H,H)
KT = S.simplify(T.T*K*T)
for i in range(4):
    blk = S.Matrix([[KT[i,i],KT[i,i+4]],
                    [KT[i+4,i],KT[i+4,i+4]]])
    assert all(S.cancel(blk[r,c]-expected[i][r,c]) == 0
               for r in range(2) for c in range(2))
    assert S.simplify(blk.det()-(4*(y+4) if i==0 else 0)) == 0
for i in range(8):
    for j in range(8):
        if i%4 != j%4:
            assert S.cancel(KT[i,j]) == 0

f = S.factor(6+a+b-mu/2)
assert S.factor(S.diff(f,y)+g/(y*y*(y+4)**2)) == 0
r = hi
assert S.factor(f.subs(y,r)-S.Rational(3067199,2300100)) == 0
assert S.Rational(3067199,2300100)-S.Rational(4,3) == S.Rational(133,766700)
assert S.factor(mu.subs(y,lo))>0

VA = S.Matrix.hstack(H[:,1]/S.sqrt(2),H[:,2]/S.sqrt(2),S.sqrt(3)*H[:,3])
VB = S.Matrix.hstack(-H[:,1]/(S.sqrt(2)*y),-H[:,2]/(S.sqrt(2)*y),
                     -S.sqrt(3)*H[:,3]/(y+4))
V = VA.col_join(VB)
G = S.simplify(V*V.T)
for i in range(4):
    assert G[i,i] == 1
    assert S.simplify(G[i+4,i+4]-1+g/(y*y*(y+4)**2)) == 0
assert G[0,3] == G[1,2] == S.Rational(1,2)
assert S.factor(S.trace(K*G)) == 0
Csum = S.factor(6+S.trace(W*G)/4)
assert S.simplify(Csum-f-(y+2)*g/(y*y*(y+4)**2)) == 0

# All distinct off-diagonal Gram entries are one of seven exact formulas.
deep = [-S.Rational(3,4),
        3/(4*(y+4)**2)-1/(4*y*y),
        -(y+1)/(y*(y+4))]
safe = [S.Rational(1,2),-3/(4*(y+4)**2),
        3/(4*(y+4)),(2-y)/(2*y*(y+4))]
# Rational interval arithmetic, using positive denominators and monotonicity.
assert hi < 1
assert (hi*hi+2*hi) < 2
assert 3/(4*(lo+4)**2)-1/(4*hi**2) < -S.Rational(1,2)
assert -(hi+1)/(hi*(hi+4)) < -S.Rational(1,2)
assert 3/(4*(lo+4)) < S.Rational(1,2)
assert (2-lo)/(2*lo*(lo+4)) < S.Rational(1,2)
assert 3/(4*(lo+4)**2) < S.Rational(1,2)

for i in range(8):
    for j in range(i+1,8):
        expression = S.factor(G[order.index(i),order.index(j)])
        pool = deep if (i,j) in edges else safe
        assert any(S.cancel(expression-q)==0 for q in pool), (i,j,expression)
print("PASS: exact sharp F3 three-matching aggregate theorem and witness")
print("root bracket:",lo,hi)
print("rational lower:",S.Rational(3067199,2300100))
