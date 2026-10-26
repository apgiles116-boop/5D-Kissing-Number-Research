"""Exact rational checks for the Huber 21-line gap and Type-E A>1/90."""
from fractions import Fraction as F

def g(k):
    c=F(k,4)-F(16,5)
    l=F(3,10)
    return c*c if abs(c)<=l/2 else l*abs(c)-l*l/4

assert g(12)==F(3,80) and g(13)==F(1,400)
assert all(g(k-1)-2*g(k)+g(k+1)>=0 for k in range(1,20))
assert 5*g(12)+16*g(13)==F(91,400)
assert 3*g(12)+18*g(13)==F(63,400)

p=F(1,72)
assert F(24,5)*p==F(1,15)
assert 24*p==F(1,3)
assert F(24,5)+4*p==F(437,90)
assert F(91,400)-F(3,10)*F(1,3)==F(51,400)
assert F(63,400)-F(3,10)*F(1,3)==F(23,400)
assert F(51,400)/(F(437,90)-1)==F(459,13880)>F(2,65)
assert F(23,400)/(F(437,90)-1)==F(207,13880)>F(1,70)

A=F(1,90)
P0=(24*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)
P15=(19*A+11*A*A+7*A**3+A**4)/(16*(1-A)**4)
assert P0==F(17585731,1003875856)
assert P15==F(13940731,1003875856)
assert F(4,5)-24*P0>0
assert (F(4,5)-24*P0)**2-F(96,25)*P0==F(6047104267847453,78731776114041620)>0
assert F(1,72)-P15==F(17903,9034882704)>0

for C in [F(0),F(1,100),F(1,4),F(3,4)]:
    core=C/4+F(5,16)*C*C+C**3/4+C**4/16
    extra=F(3,8)*C*C+F(3,16)*C**3
    assert core+extra==C/4+F(11,16)*C*C+F(7,16)*C**3+C**4/16

print("PASS: universal exact 21-line gap P>1/72")
print("PASS: conditional Type-E midpoint-energy floor A>1/90")
print("exact margin:",F(1,72)-P15)
