#!/usr/bin/env python3
"""Exact rational audit of the robust Type-E disjoint-pair Gram obstruction."""
from fractions import Fraction as F

B=F(383,504)
D0=F(1780062775,4032758016)
a0=F(244473,1000000)
b0=B/2-a0
c0=D0-B/2
h=F(1,100000)
k=F(6,7)

assert F(0)<a0-h<a0+h<F(1,4)
assert F(0)<b0-h<b0+h<F(1,4)
assert F(0)<c0-h<c0+h<F(1,4)
assert F(1,300)**2>h
assert F(1,600)**2>(a0+h)*h+h*h/4
assert F(1,800)**2>(b0+h)*h+h*h/4

a_min,b_min,c_min=a0-h,b0-h,c0-h
L_min=(1-k)/2+(1+k)*c_min-(k/2)*F(1,300)
U3=1-b_min+F(1,800)
U12=(1+k*k)*(1-a_min+F(1,600))-k*(1+2*a_min)
assert L_min>0 and U3>0 and U12>0
gap=L_min*L_min-U3*U12
assert gap==F(311094683363205057250829161,194554131729736464000000000000)
assert gap>0

L0=(1-k)/2+(1+k)*c0
R0=(1-b0)*((1+k*k)*(1-a0)-k*(1+2*a0))
assert L0*L0>R0
assert a0+F(3,2)*c0>=F(1,4)
bessel_gap=4*c0*c0-(1-4*a0)*(F(2,3)-b0)
assert bessel_gap>0

print("PASS: exact rational exclusion box")
print("alpha0, beta0, gamma0 =",a0,b0,c0)
print("strict box gap =",gap,"~",float(gap))
print("saturation Cauchy gap ~",float(L0*L0-R0))
print("saturation Bessel gap ~",float(bessel_gap))
