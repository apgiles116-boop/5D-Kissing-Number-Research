"""Exact rational regression for the conditional high-center Type-E rank-seven upgrade.

Checks quantization constants and all 50 determinant inequalities.
The spectral/geometric arguments are in the companion proof note.
"""
from fractions import Fraction as Q

Nmax = Q(5, 64)
xmax = Q(1, 2500)
c = Q(539, 81)

assert 7 * (1 - 4 * Q(1, 9)**2) == c
high_ratio_floor = 28 * Q(12, 25)**2 * Q(49, 50) / Q(1, 50)
assert high_ratio_floor > c

E = Nmax / c + xmax*xmax
assert E == Q(158205281, 13475000000)
assert E < Q(1, 81)

worst = (Q(0), None)
for k in range(8, 18):
    for q in range(1, 6):
        ratio_squared = (
            ((Q(k) + Q(k-q, 9)) / q)**(2*q)
            * Q(1, 81*(k-q))**(k-q)
            * 2**(2*k)
        )
        assert ratio_squared < 1, (k, q, ratio_squared)
        if ratio_squared > worst[0]:
            worst = (ratio_squared, (k, q))

assert worst == (Q(640000000000, 847288609443), (8, 5))
print("PASS: high-center rank<=7 rational certificates")
print("Squared Frobenius error upper bound:", E)
print("Worst squared determinant ratio:", worst)
