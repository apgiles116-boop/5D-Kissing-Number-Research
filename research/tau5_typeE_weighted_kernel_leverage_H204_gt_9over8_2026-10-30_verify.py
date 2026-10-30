"""Exact rational certificate for Type E weighted Q-kernel leverage H204 > 9/8.
Mathematical proof is in the companion .md. All calculations use Fraction.
"""
from fractions import Fraction as F

B=F(383,504)
t=F(13,8)
L=F(53,10)
ri=F(4,5)+15*F(1,5)+4*F(1,5)*t+F(1,5)
rc=(16*F(1,5)+F(1,5)+(F(4,5)+3*F(4,5))*t)/t
rv=F(4,5)+16*F(1,5)+4*F(1,5)*t
assert ri==rv==L and rc==F(344,65)<L

assert F(4,5)/L==F(8,53)
assert (2-F(1,4))*(1-F(1,4))**2==F(63,64)
xi=F(8,53)*F(63,64)
assert xi==F(63,424)
rank_coef=2-xi
assert rank_coef==F(785,424) and rank_coef*B<F(3,2)
coef=rank_coef-F(1,4)
assert coef==F(679,424)
assert F(27,32)-F(19,16)<0

D=B/2+B*B
assert D==F(243205,254016)
lo,hi=F(9,10),F(49,50)
assert lo*lo<D<hi*hi
base=F(27,448)*(7-coef*B)**2-(F(19,4)*B+B*B)/16-F(3,8)
g_lo=D/16-(B/2+F(11,32)*lo)**2+F(21,64)*B-F(49,1024)*D
assert g_lo<0
g_hi=D/16-(B/2+F(11,32)*hi)**2+F(21,64)*B-F(49,1024)*D
result=base+g_hi
assert result==F(2061191525172601,1826639216640000)
assert result-F(9,8)==F(6222406452601,1826639216640000)>0
print("Weighted row bounds:",ri,rc,rv)
print("Leverage Xi >= (63/424)A; scalar certificate:",result)
print("Strict margin over 9/8:",result-F(9,8))
print("PASS")
