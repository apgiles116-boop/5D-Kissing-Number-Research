"""Exact rational audit for the Type-E joint safe-pair/core-Gram gap.
The analytic vector inequalities are proved in the companion Markdown note.
"""
from fractions import Fraction as F
from itertools import combinations, product
from sympy import symbols, expand, sqrt

c0 = F(541, 1000)
B = F(383, 504)
assert B < 2*(4-2*sqrt(3))
assert F(17321,10000)**2 > 3
assert F(827,100)**2 > 64+8*c0
assert F(3,4)**2 > c0
assert 4-2*F(17321,10000)-c0/2 == F(2653,10000)
assert 2*F(827,100)+F(3,4) == F(1729,100)

large = c0*c0/1242
small = F(2653,10000)**2 / F(1729,100)**2
assert large == F(292681,1242000000)
assert small == F(143641,610090000)
assert large > F(1,4250) and small > F(1,4250)
assert F(1,96) > F(1,4250)

# The core identity 4(C-d)=||sum m||^2+sum E_ij,
# checked in all 64 sign chambers as an exact polynomial.
a = symbols('a0:4')
pairs = list(combinations(range(4),2))
s = symbols('s0:6')
C = sum(a)
snorm = C + 2*sum(s)
for signs in product((-1,1),repeat=6):
    abs_s = sum(signs[k]*s[k] for k in range(6))
    d = (abs_s-sum(s))/2
    E = 3*C-2*abs_s
    assert expand(4*(C-d)-snorm-E)==0

edges={tuple(sorted(e)) for e in
       [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[x for x in combinations(sorted(edges),4)
           if len(set(v for edge in x for v in edge))==8]
assert len(matchings)==3
expected={tuple(sorted(x)) for x in
          [((0,2),(1,4),(3,6),(5,7)),
           ((0,4),(1,7),(2,3),(5,6)),
           ((0,5),(1,4),(2,7),(3,6))]}
assert set(matchings)==expected
print('PASS: rational bounds, 64 sign chambers, and three F3 matchings')
print('large-C floor:', large, float(large))
print('small-C floor:', small, float(small))
print('uniform floor: 1/4250 =', float(F(1,4250)))
