#!/usr/bin/env python3
"""Exact checks of Type-E squared-safe and exceptional-core inequalities."""
from fractions import Fraction as F
from itertools import product
import sympy as s
M,Z,X,Y=s.symbols('M Z X Y',real=True)
assert s.expand(((M+Z)**2+(X+Y)**2+(M-Z)**2+(X-Y)**2)/2-(M*M+Z*Z+X*X+Y*Y))==0
vals=[F(k,8) for k in range(-4,5)]
n=0
for m,z,x,y in product(vals,repeat=4):
    ap=abs(m+z)+abs(x+y); am=abs(m-z)+abs(x-y)
    if ap>F(1,2) or am>F(1,2): continue
    n+=1
    h=F(1,2)-abs(z)
    R=(F(1,4)-ap*ap+F(1,4)-am*am)/2
    cross=abs(m+z)*abs(x+y)+abs(m-z)*abs(x-y)
    assert R>=0 and F(1,4)-z*z==m*m+x*x+y*y+cross+R
    assert x*x+y*y<=h*h+m*m
    r,t=abs(z),abs(m)
    assert x*x+y*y<=(F(1,2)-max(r,t))**2+min(r,t)**2
assert n==441
assert (F(1,2)*(1-F(1,16)),F(1,2)*(1-F(1,4)))==(F(15,32),F(3,8))
c=F(4,21)
assert (c/2)/F(15,32)==F(64,315)
for aa in product([F(0),F(1,16),F(1,8),F(1,4)],repeat=4):
    ac=sum(aa)
    assert sum(aa[i]*aa[j] for i in range(4) for j in range(i+1,4))<=F(3,8)*ac*ac
B=F(4,21); Dmin=F(1665618603949,2064772104192)
rhs=F(14297,3600)*B+F(79,64)*B*B+F(3,4)*B**3+F(1,8)*B**4
assert Dmin-rhs==F(4997736421,51619302604800)>0
print('PASS:',n,'exact rational safe-pair tuples; core and frame arithmetic checked')
print('OPEN: Type E not excluded; 40<=tau_5<=44 unchanged')
