"""Exact rational regression for the 2026-10-29 Walsh parity/gap/frame note."""
from fractions import Fraction as F
from itertools import product

q = F(1, 2)
vals = [-q, -F(2, 5), -F(3, 10), -F(1, 4), -F(1, 5),
        -F(1, 10), F(0), F(1, 10), F(1, 5), F(1, 4),
        F(3, 10), F(2, 5), q]

# Regression over rational fully safe four-contact Walsh boxes.
count = 0
for a, b, c, d in product(vals, repeat=4):
    pp = (a+b+c+d, a-b+c-d, a+b-c-d, a-b-c+d)
    if any(abs(p) > q for p in pp):
        continue
    count += 1
    up, um = q-abs(a+d), q-abs(a-d)
    assert up >= 0 and um >= 0
    h = q-abs(d)
    e = h*h+a*a-b*b-c*c
    correction = max(abs(a)-abs(d), F(0))
    residual = (up*up-(b+c)**2 + um*um-(b-c)**2)/2
    assert residual >= 0 and e == correction+residual
    assert abs(b*b-c*c) <= up*um
    assert b*b+c*c <= h*h+a*a-correction

# Sharpness of the abstract Walsh-box inequality for all feasible a,d
# on the chosen grid. The proof in the note is algebraic, not grid-based.
sharp = 0
for a, d in product(vals, repeat=2):
    if abs(a)+abs(d) > q:
        continue
    up, um = q-abs(a+d), q-abs(a-d)
    b, c = (up+um)/2, (up-um)/2
    pp = (a+b+c+d, a-b+c-d, a+b-c-d, a-b-c+d)
    assert all(abs(p) <= q for p in pp)
    h = q-abs(d)
    assert h*h+a*a-b*b-c*c == max(abs(a)-abs(d), F(0))
    sharp += 1

a, b, c, d = F(3, 10), F(1, 5), -F(1, 10), F(1, 10)
assert (q-abs(d))**2+a*a-b*b-c*c == F(1, 5)

# Exhaustively audit all three F3 perfect matchings.
edges = {frozenset(e) for e in
         [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings = [
    [(0,2),(1,4),(3,6),(5,7)],
    [(0,4),(1,7),(2,3),(5,6)],
    [(0,5),(1,4),(2,7),(3,6)],
]
safe_counts = []
for matching in matchings:
    mult, bad = [], 0
    for i in range(4):
        for j in range(i+1, 4):
            ei, ej = matching[i], matching[j]
            deep = [(si, sj) for si in (0, 1) for sj in (0, 1)
                    if frozenset((ei[si], ej[sj])) in edges]
            mult.append(len(deep))
            parities = {si ^ sj for si, sj in deep}
            assert len(parities) <= 1
            bad += len(parities)
    assert sum(mult) == 6
    assert sorted(mult) in ([0,1,1,1,1,2], [1,1,1,1,1,1])
    safe_counts.append(380-bad)
assert safe_counts == [375, 374, 375]

# Exact global frame/Parseval check using genuine rational unit endpoint
# pairs in R^5, with A<=383/504. No graph safety is claimed.
n = 20
m, z = [], []
for i in range(n):
    mi, zi = [F(0)]*5, [F(0)]*5
    mi[i % 5] = F(11, 61)
    zi[(i+1) % 5] = F(60, 61)
    m.append(mi)
    z.append(zi)
def dot(x, y):
    return sum((p*q for p, q in zip(x, y)), F(0))
A = sum((dot(mi, mi) for mi in m), F(0))
U = sum((dot(mi, mi)**2 for mi in m), F(0))
assert A <= F(383, 504)
S4 = sum((dot(m[i],m[j])**2+dot(m[i],z[j])**2
          +dot(z[i],m[j])**2+dot(z[i],z[j])**2
          for i in range(n) for j in range(i+1, n)), F(0))
T = [[sum((m[i][p]*m[i][r]+z[i][p]*z[i][r]
           for i in range(n)), F(0)) for r in range(5)]
     for p in range(5)]
W = sum(((T[p][r]-(F(4) if p == r else F(0)))**2
         for p in range(5) for r in range(5)), F(0))
assert S4 == F(30)+A-U+W/2
assert U <= A/4
assert F(1)-F(383,504)/5 == F(2137,2520)
assert F(3)-F(383,504) == F(1129,504)

print("PASS: 1449 safe rational Walsh boxes, 85 sharpness instances,")
print("      F3 parity counts", safe_counts, "and exact frame identity.")
print("      Frame witness: A=", A, "S4=", S4, "W=", W)
