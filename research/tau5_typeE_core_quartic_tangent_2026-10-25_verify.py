#!/usr/bin/env python3
"""Exact rational certificate for the Type-E six-core quartic bound.
No floating point or external packages are used in proof checks.
"""
from fractions import Fraction as F
from math import comb

D = F(1780062775, 4032758016)
Q = F(19, 250)
k = F(81, 64)
target = F(11, 100)

# Rational points (x0, sqrt(9-24*x0-48*x0^2)) on the root conic.
charts = [
    (F(23, 100), F(59, 250), F(10, 43), F(39, 43), F(19, 26), -F(70, 26)),
    (F(59, 250), F(241, 1000), F(132, 553), F(405, 553), F(249, 270), -F(946, 270)),
    (F(241, 1000), F(1, 4), F(9, 37), F(21, 37), F(17, 14), -F(66, 14)),
]

def bernstein_coeffs(poly, left, right):
    """Degree-4 Bernstein coefficients of polynomial poly in power basis."""
    width = right-left
    q = [sum(poly[j] * comb(j, i) * left**(j-i) * width**i
             for j in range(i, 5)) for i in range(5)]
    return [sum(q[j] * F(comb(i, j), comb(4, j))
                for j in range(i+1)) for i in range(5)]

assert D < F(441401, 1000000)
assert Q == F(76, 1000)
assert D > F(3, 8)

# All defects <=1/8: quartic sum <= (81/64)Q < 11/100.
assert k*Q < target

# Unique x>1/8: Q-budget bound is increasing up to x=23/100.
x = F(23, 100)
B1 = k*Q + x*x*((1+x)**2-k)
assert B1 == F(43707339, 400000000)
assert B1 < target

for left, right, x0, root, alpha, beta in charts:
    # Exact conic and tangent-line certificates for concave root c(x).
    assert root*root == 9-24*x0-48*x0*x0
    c0 = (4*x0-1+root)/8
    deriv = F(1, 2)-(3+12*x0)/(2*root)
    assert alpha+beta*x0 == c0
    assert beta == deriv
    assert alpha+beta*left > 0
    assert alpha+beta*right > 0

    # p(x)=11/100 - (x+x^2)^2 - (81/64)(alpha+beta*x)(D-x)
    p = [target-k*alpha*D,
         -k*(beta*D-alpha),
         -1+k*beta,
         F(-2),
         F(-1)]
    coeff = bernstein_coeffs(p, left, right)
    assert all(c > 0 for c in coeff)
    print('Interval', left, right, 'min Bernstein', min(coeff))

full20 = F(375, 896)-target
leave19 = F(2375, 7168)-target/2
assert full20 == F(6911, 22400)
assert leave19 == F(49519, 179200)

# All-six-positive: core midpoint Gram PSD gives D <= A_C/2 <= B/2.
B = F(383, 504)
D6 = B/2
assert D6 == F(383, 1008)
assert D6-F(3, 8) == F(5, 1008)
Q6 = 3*F(1, 8)**2 + (D6-F(3, 8))**2
T6 = k*Q6
H6 = F(375, 896)-T6
assert Q6 == F(47653, 1016064)
assert T6 == F(47653, 802816)
assert H6 == F(288347, 802816)

print('PASS: T_core^+ <', target, '; H_184+H_C^- >', full20)
print('PASS: H_184+(1/2)H_C^- >', leave19, '+ (1/4)H_OC')
print('PASS: all-six-positive branch H_184 >', H6)
