"""Exact rational audit of canonical F3-to-isolated-16 mass transfer."""
from fractions import Fraction as F

# sqrt(6)+sqrt(2) < 58/15 follows from sqrt(3)<391/225.
assert F(391,225)**2 > 3
A0=F(383,504)
b=A0-F(1,15)
assert b==F(1747,2520)
assert F(1,2)<b<F(3,4)
Umax=F(1,8)+(b-F(1,2))**2
Q=F(88,5)-F(11,5)*b+b*b/10-Umax/2
assert Q==F(254678471,15876000)
old=F(5046067,317520)
assert Q-old==F(113101,756000)
# F'(B)=-11/5-4B/5+k/4 <0 for B in [k/4,(k+1)/4], k=0,1,2.
for k in range(3):
    upper=min(b,F(k+1,4))
    assert -F(11,5)-F(4,5)*F(k,4)+F(k,4)<0
    assert upper>=F(k,4)
for t,n in [(F(1,5),54),(F(1,4),46),(F(3,10),33),
            (F(1,3),20),(F(7,20),11)]:
    assert 120*t*t+(n-1)*(F(1,4)-t*t)<Q
    print('threshold',t,'minimum',n)
print('EXACT RATIONAL AUDIT PASSED:',Q)
