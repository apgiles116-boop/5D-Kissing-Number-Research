"""Exact D5 traceless-projector Gram spectrum and Type-E correlation corollary.
Uses SymPy exact rationals and fractions; no floating point certification decisions.
"""
from itertools import combinations
from fractions import Fraction as F
from sympy import Matrix, Rational, eye, zeros

pairs = list(combinations(range(5), 2))
Qs = []
for i, j in pairs:
    for sign in (1, -1):
        P = zeros(5)
        P[i, i] = P[j, j] = Rational(1, 2)
        P[i, j] = P[j, i] = Rational(sign, 2)
        Qs.append(P - eye(5) / 5)

G = Matrix([
    [sum(Qs[i][a, b] * Qs[j][a, b]
         for a in range(5) for b in range(5))
     for j in range(20)]
    for i in range(20)
])
assert G.eigenvals() == {
    Rational(3, 2): 4, Rational(1): 10, Rational(0): 6
}
assert G.rank() == 14

B = zeros(5, 10)
for k, (i, j) in enumerate(pairs):
    B[i, k] = B[j, k] = 1
P0 = eye(5) - Matrix.ones(5, 5) / 5
assert P0 * B * B.T * P0 == 3 * P0
assert (B.T * P0 * B / 3) ** 2 == B.T * P0 * B / 3

# Exact K5 even/odd synthesis sum of squares.
c = Matrix([Rational((i*i + 3*i + 7) % 17 - 8, 11)
            for i in range(20)])
s = Matrix([(c[2*k] + c[2*k+1])/2 for k in range(10)])
d = Matrix([(c[2*k] - c[2*k+1])/2 for k in range(10)])
assert (c.T * G * c)[0] == (
    2 * (d.T * d)[0] + (s.T * B.T * P0 * B * s)[0]
)

assert 5 * 6 // 2 - 1 == 14  # dimension Sym_0(5)

A = F(383, 504)
Umax = F(3, 16) + (A - F(3, 4))**2
Vmin = F(47602076041, 317520000000)
Qmin = F(30) - 3*A + A*A/10 - Umax/2 + Vmin/2
assert Umax == F(47653, 254016)
assert Qmin == F(5876056025347, 211680000000)
assert Qmin > F(8790283, 317520)

print("PASS: D5 Q-Gram spectrum 0^6, 1^10, (3/2)^4")
print("PASS: exact K5 incidence identity and rank 14")
print("PASS: universal dimension 14 implies >=6 kernel modes")
print("PASS: conditional Type-E correlation floor >", Qmin, float(Qmin))
