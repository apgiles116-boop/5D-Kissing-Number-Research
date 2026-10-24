"""Exact rational subcertificate for the four-core K2,2 sign-stability theorem.

The analytic rank-one and length-variance arguments are in the companion note.
No numerical optimization is used here.
"""
from fractions import Fraction as F

# epsilon/C <= 1/64
assert F(79,10)**2 < 63
assert F(87,50)**2 > 3
assert (F(79,10)-F(87,50))/16 == F(77,200)
assert F(1,2)+F(87,50)/16 < F(61,100)
assert F(77,200)**2-F(1,16) > F(29,100)**2
assert 3*F(29,100)-F(61,100) > F(1,4)
pair_gap = F(29,100)**2-F(1,32)
assert pair_gap == F(1057,20000)>0
print("PASS: epsilon/C <= 1/64 forces 2+2 signs and K2,2 negative pairings")
print("PASS: pairwise |m_i.m_j| >",pair_gap,"* C")

# epsilon/C <= 1/100
assert F(99,100)**2 < F(99,100)
assert F(9,50)**2 > F(3,100)
assert (F(99,100)-F(9,50))/2 == F(81,200)
min_t_sq = F(81,200)**2-F(1,25)
assert min_t_sq == F(4961,40000)
normal_cap = F(1,25)/min_t_sq
assert normal_cap == F(1600,4961) < F(1,3)
print("PASS: epsilon/C <= 1/100 forces sum_i(v.z_i)^2 <",normal_cap)

# Optional retained F3 matching-uniform lower bound C>1/117.
assert pair_gap/F(117) == F(1057,2340000)
print("PASS: conditional projective raw-threshold margin >",pair_gap/F(117))
