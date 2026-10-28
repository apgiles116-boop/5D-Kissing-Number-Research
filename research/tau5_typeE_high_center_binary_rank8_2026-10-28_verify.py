"""Exact rational regression for high-center Type-E binary/rank-8 reduction.

This checks the arithmetic and Walsh isometry. The conditional geometric
arguments are stated in the accompanying Markdown note.
"""
from fractions import Fraction as Q
from itertools import product

B = Q(5, 64)
xc = Q(1, 2500)

def D(x):
    return 196*x - 644*x*x + 896*x**3 - 448*x**4

def g(d):
    return Q(7,4)*d*(1+d)*(21*d*d - 49*d + 20)

def f(t):
    return 7*t*t*(1-4*t*t)

assert D(xc) > B
assert g(Q(1,400)) > B
assert f(Q(1,9)) > B
assert f(Q(12,25)) > B
assert Q(12,25)-Q(1,9) > Q(1,25)
assert Q(8,7)*B == Q(5,56)
assert Q(4,21)*B == Q(5,336)

signs = list(product((1,-1), repeat=2))
H = [[1,s,t,s*t] for s,t in signs]
assert all(sum(H[k][i]*H[k][j] for k in range(4)) == (4 if i==j else 0)
           for i in range(4) for j in range(4))

welch_floor = Q(88,5) - Q(11,5)*xc - Q(2,5)*xc**2
assert 7*(1-4*Q(1,9)**2) == Q(539,81)
low_Q_upper = Q(81,4*539)*B
assert welch_floor > Q(70,4)+low_Q_upper
assert welch_floor <= Q(71,4)+low_Q_upper
assert low_Q_upper == Q(405,137984)
assert welch_floor == Q(274986249,15625000)

assert Q(5,336)+xc**2 < Q(1,64)
for k in range(9,18):
    # Squared version of determinant bound, no floating-point arithmetic.
    lhs = ((Q(k)+Q(9,32))/5)**10 * Q(1,64*(k-5))**(k-5)
    rhs = Q(1,2**(2*k))
    assert lhs < rhs, (k, lhs/rhs)

print("PASS: high-center rational thresholds, Welch e>=71, Walsh isometry, rank<=8.")
print("Welch floor:", welch_floor)
print("Low-pair squared-mass cap:", low_Q_upper)
print("Gap excluding e<=70:", welch_floor-(Q(70,4)+low_Q_upper))
print("Frobenius squared cap:", Q(5,336)+xc**2)
