"""Exact rational verifier: Type-E two-eigenspace inverse gap, 2026-10-24.
Run: python tau5_typeE_two_eigenspace_inverse_gap_2026-10-24_verify.py
No third-party packages; no floating-point comparisons.
"""
from fractions import Fraction as F
from itertools import combinations, product

edges = list(combinations(range(5), 2))
assert len(edges) == 10
d0 = F(139, 250)
B, r = F(383, 504), F(5, 504)
C = F(3, 16) + r*r
wl = 1/(1-d0)
wh = 1/(F(3, 2)-d0)

# Verify exact spectral projectors of the twenty-line D5 Q-Gram.
G0 = [[F(4,5) if i==j else F(-1,5) if i//2==j//2
       else F(1,20) if set(edges[i//2]) & set(edges[j//2])
       else F(-1,5) for j in range(20)] for i in range(20)]
L = [[F(1,2) if i==j else F(-1,2) if i//2==j//2
      else F(0) for j in range(20)] for i in range(20)]
H = [[F(len(set(edges[i//2]) & set(edges[j//2])),6)-F(2,15)
      for j in range(20)] for i in range(20)]
assert all(G0[i][j] == L[i][j]+F(3,2)*H[i][j]
           for i in range(20) for j in range(20))
for P in (L,H):
    assert all(sum(P[i][k]*P[k][j] for k in range(20)) == P[i][j]
               for i in range(20) for j in range(20))
assert all(sum(L[i][k]*H[k][j] for k in range(20)) == 0
           for i in range(20) for j in range(20))
assert sum(L[i][i] for i in range(20)) == 10
assert sum(H[i][i] for i in range(20)) == 4
print("PASS: exact orthogonal D5 projectors, ranks 10 and 4")

# For q=x/4 and s_e=x_(e,+)+x_(e,-), the canonical
# orientation is (0,0), (1,0), (1,1).
# q^TWq = Q/419136; (Wq)_i = n_i/104784.
# The q+linear objective is N/132027840.
maxN, count, best = -1, 0, None
checked = 0
for s in product((0,1,2), repeat=10):
    checked += 1
    deg = [0]*5
    for (v,w),occ in zip(edges,s):
        deg[v] += occ
        deg[w] += occ
    T = sum(s)
    k = s.count(1)
    dv = [5*t-2*T for t in deg]
    Q = 29500*k + 185*sum(t*t for t in dv)
    nums = []
    for (v,w),occ in zip(edges,s):
        h = 925*(dv[v]+dv[w])
        delta = int(occ==1)
        nums.extend((h+29500*delta, h-29500*delta))
    top = sorted((max(0,n) for n in nums),reverse=True)[:4]
    N = 315*Q + 126*sum(top[:3]) + 5*top[3]
    if N>maxN:
        maxN,count,best = N,1,s
    elif N==maxN:
        count += 1
assert checked == 59049
assert maxN == 104223500 and count == 1 and best == (1,)*10
print("PASS: 59,049 exact integer cases; unique all-one occupancy maximizer")

D = wl/2+wh/5
c = wh/30
assert D>c>0
quad = ((D-c)*C+c*B*B)/25
upper = F(maxN,132027840)+quad
alpha = F(5,16)+B/20+C/50
beta = (5*C+B*B)/750
assert upper == alpha/(1-d0)+beta/(F(3,2)-d0)
assert upper == F(2661669119,3327101568)
margin = F(4,5)-upper
assert margin == F(60677,16635507840)>0
print("PASS: exact upper bound",upper,"and positive margin",margin)

# Explicit scalar-relaxation equality witness, not a physical code.
q = [F(1,4) if i%2==0 else F(0) for i in range(20)]
a = [F(0)]*20
for i in (0,2,4):
    a[i]=F(1,4)
a[6]=r
assert sum(a)==B
assert all(len(set(edges[i//2]) & set(edges[j//2]))==1
           for i,j in combinations((0,2,4,6),2))
y = [q[i]+a[i]/5 for i in range(20)]
actual = sum(y[i]*(wl*L[i][j]+wh*H[i][j])*y[j]
             for i in range(20) for j in range(20))
assert actual == upper
print("PASS: exact scalar equality witness")
print("THEOREM (conditional): ||G_Q-G_D5||_op > 139/250 = 0.556")
