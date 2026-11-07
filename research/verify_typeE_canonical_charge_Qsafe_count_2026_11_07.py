"""Exact rational audit of canonical F3 endpoint-charge/Qsafe transfer."""
from fractions import Fraction as F

A0 = F(383,504)
P0 = F(8790283,317520)
D0 = F(1,4)
cap = F(1,8)
Qcore = 6*F(1,4) + D0 + 2*cap**2
assert Qcore == F(57,32)
Qsafe = P0-Qcore
assert Qsafe == F(16449401,635040)
def max_safe(K):
    return F(184-K,9)+F(K,4)
assert max_safe(39) < Qsafe <= max_safe(40)
print('canonical Qcore <=',Qcore)
print('canonical Qsafe >=',Qsafe,'=',float(Qsafe))
print('gap over K=39:',Qsafe-max_safe(39))
Qcenter = F(141813,5000)
Qsafe_center = Qcenter-Qcore
assert Qsafe_center == F(531627,20000)
assert max_safe(44) < Qsafe_center <= max_safe(45)
print('conditional center Qsafe >',Qsafe_center,'=',float(Qsafe_center))
print('gap over K=44:',Qsafe_center-max_safe(44))
print('EXACT RATIONAL AUDIT PASSED')
