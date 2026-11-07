"""Exact-rational verification of the isolated-16 Welch count consequences."""
from fractions import Fraction as F

A0 = F(383,504)
Umax = F(3,16) + F(5,504)**2
q0 = F(88,5) - F(11,5)*A0 + A0*A0/10 - Umax/2
assert q0 == F(5046067,317520)
# Derivative -11/5+B/5 is negative for all B in [0,A0].
assert -F(11,5)+A0/5 < 0

thresholds = [(F(1,5),53),(F(1,4),45),(F(3,10),32),
              (F(1,3),19),(F(7,20),10)]
for t,n in thresholds:
    # n-1 pairs above threshold cannot carry enough squared energy.
    assert 120*t*t+(n-1)*(F(1,4)-t*t) < q0
    # n pairs are not excluded by this scalar argument alone.
    assert q0 <= 120*t*t+n*(F(1,4)-t*t)
    print(str(t), 'at least', n)
print('PASS:',q0,'=',float(q0))
