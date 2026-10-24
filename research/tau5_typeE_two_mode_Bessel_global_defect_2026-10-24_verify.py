#!/usr/bin/env python3
from fractions import Fraction as F
D=F(1780062775,4032758016); B=F(383,504); b=B/2; r=D-b
T=F(122237,500000); e=F(1,100000); h=F(1,10000); q=F(40949,500000)
a0=F(244473,1000000); beta0=b-a0; g0=r; te=2*e
P=lambda p,c:p+c+4*(p*p+c*c-p*c)-F(1,2)
FF=lambda p:p*p+(b-p)**2+r*r
G1=lambda p,c:p*p+(b-p)**2+r*c
assert 0<D/3<b/2<T-e<T<T+e<F(1,4)
assert D+F(1,4)<B and D*D/3<q and b*b/2+r*r<q
assert FF(T-e)<q and 8*T-12*F(1,16)>1 and 1+B-4*D<0
assert D-T<F(1,5) and P(T,F(1,16))>0
cu=F(61385,1000000)
assert P(T+e,cu)>0 and G1(T+e,cu)<q
cm=F(6149,100000)
assert P(T-e,cm)>0 and cm-r>e and D-T-cm>0
ym=D-T-cm
assert max(T*T+cm*(D-T),T*T+ym*ym+cm*cm,
           T*T+(b-T-e)**2+(r+e)**2)<q
c0=F(61437,1000000)
assert P(T,c0)>0 and c0<r
penalty=2*(b-F(1,4))-F(1,16)
assert penalty>0 and F(3,40)<q
assert G1(T,c0)-e*penalty+e*e<q
assert r>h>e
assert (T+e)**2+(b-T-e)**2+(r-h)*(r+e)<q
sa=F(23,10000); sb=F(17,10000)
assert sa*sa>(a0+h)*te+te*te/4
assert sb*sb>(beta0+h)*te+te*te/4
xmin=F(1,2)+g0-h; ymax=F(1,2)-(g0-h)+sb
cmin=F(1,2)+a0-h; nmax=1-(a0-h)+sa
assert cmin*xmin>nmax*ymax and F(1,2)-2*(a0+h)>0
dd=2*(g0-h)-sb
assert dd>0
lb=1/(3+2*sa)+dd*dd/(1-4*(a0-h)+2*sa)
ub=1-(beta0-h)+sb
assert lb-ub==F(2603293159010046381219438287,404239298123534816332656000000)>0
assert T-a0==F(1,1000000)
assert e+F(1,1000000)<h and 2*e+F(1,1000000)<h
L=F(8790283,317520)
K=L-F(3,2)-D-q
assert K==F(1616939870490713,63011844000000)
assert F(819,10000)-q==F(1,500000)
print("PASS exact Type-E Q <",q)
print("PASS exact safe-pair floor >",K)
