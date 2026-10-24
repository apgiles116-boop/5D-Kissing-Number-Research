"""Exact arithmetic certificate for the 2026-10-24 D5 center/subset cap note.
The geometry and Taylor argument are proved in the paired Markdown note.
"""
from fractions import Fraction as F
from sympy import sqrt, simplify, N

T = F(1, 500)
alpha = 25*(sqrt(2)-1)/16
B0 = F(9,2)-3*sqrt(2)
Bnew = B0+alpha/1000
assert simplify(Bnew-(B0+(sqrt(2)-1)/640)) == 0
assert simplify(F(27,100)-Bnew) > 0

# All radical outward comparisons are exact integer-square comparisons.
assert F(9,200)**2 > T
assert F(39,100)**2 < F(31,200)
assert F(2236,1000)**2 < 5
assert F(1414,1000)**2 < 2
assert F(7417,1000)**2 > 55
assert F(173,100)**2 < 3  # kappa=4-2sqrt(3)<27/50

# Taylor remainder bound for x_j=u_j^2 near 1/5.
remainder = T/(8*F(31,200)*F(39,100))
assert remainder == F(5,1209)
L1 = F(2236,1000)-remainder
assert L1 == F(674581,302250)

# c_max<7/10, since x_j+x_l<2/5+2*(9/200)=49/100.
assert F(2,5)+2*F(9,200) == F(49,100)
Nlower = 4*F(1414,1000)*L1-5-F(7417,1000)
Dupper = 2*F(27,50)*F(7,10)
assert Nlower == F(31195943,151125000)
assert Dupper == F(189,250)
assert Nlower/Dupper == F(31195943,114250500)
assert Nlower/Dupper > F(27,100)

print("PASS exact rational certificate")
print("center-only:",N(B0,20))
print("full-endpoint template lower bound:",N(Bnew,20))
print("improvement:",N(alpha/1000,20))
