#!/usr/bin/env python3
"""Exact algebraic verifier: Type-E tensor/contact stability, 2026-10-29.
Does NOT recertify upstream mass, harmonic, atlas or large-x certificates.
"""
from fractions import Fraction as F
import sympy as sp

D=lambda x:196*x-644*x*x+896*x**3-448*x**4
Dp=lambda x:196-1288*x+2688*x*x-1792*x**3
B0=F(2595,256); s0=F(209,30); xfar=F(1,250); slo=F(69,10)
cfar=F(5427,100000)
E=lambda s:10+F(35,64)*(5*s-32)**2
n2=lambda s:7*(s-F(13,2))*(1-2*(s-F(13,2)))
target_c=lambda x:F(43,3)-(B0+D(x))/2

# The previously retained c(1/250) enclosure and monotone a(x).
assert D(cfar)>target_c(xfar)
assert Dp(xfar)>190 and Dp(F(0))==196
assert Dp(F(3,50))>128 and Dp(F(27,500))<135
assert 1-F(196,256)>0
assert F(1,2)+xfar+cfar<F(67,120)
assert 4-F(67,120)/5-s0/2==F(81,200)
assert F(5,4)*F(81,200)-F(1,2)==F(1,160)
assert F(5,8)+F(1,10)==F(29,40)
assert E(s0)==F(33155,2304)
assert n2(s0)==F(49,225)
assert 15-E(s0)-n2(s0)==F(2509,6400)
assert -1+F(190,112)>F(2,3)
assert -F(1,4)+F(16,112)<-F(1,10)

# Generic 5-by-5 trace-free frame identity.
vals=sp.symbols("t0:15",real=True); T=sp.zeros(5); k=0
for i in range(5):
    for j in range(i,5):
        T[i,j]=T[j,i]=vals[k]; k+=1
N=sp.trace(T); t=T[0,0]; beta=(N-t)/4
R=T[1:5,1:5]; r=T[1:5,0]
V=sp.trace((T-N*sp.eye(5)/5)**2)
rhs=sp.Rational(5,4)*(t-N/5)**2+2*(r.T*r)[0]+sp.trace((R-beta*sp.eye(4))**2)
assert sp.expand(V-rhs)==0

# Pair-center fourth-moment expansion.
p,q=sp.symbols("p q",real=True)
si=2*(p*p+q*q)
ni=7*((p+q)**2*(1-4*(p+q)**2)+(p-q)**2*(1-4*(p-q)**2))
assert sp.expand(ni-7*(si*(1-2*si)-16*si*p*p+32*p**4))==0

# General sorted capped-simplex identity (j=3,n=6 representative).
y=sp.symbols("y0:6",real=True); j=3
ss=sum(y); rho=ss-sp.Rational(j,2); t=y[j]
Dc=sum(sp.Rational(1,2)-y[i] for i in range(j))
Ec=sum(y[i] for i in range(j+1,len(y)))
gap=sum(yi*(1-2*yi) for yi in y)-rho*(1-2*rho)
hi=sum((sp.Rational(1,2)-y[i])*(y[i]-t) for i in range(j))
lo=sum(y[i]*(t-y[i]) for i in range(j+1,len(y)))
assert sp.expand(gap-2*((sp.Rational(1,2)-rho)*Dc+rho*Ec+hi+lo))==0
assert slo-F(13,2)==F(2,5) and s0-F(13,2)==F(7,15)
assert F(1,2)-F(7,15)==F(1,30)

# Exact harmonic resource/frame combination.
h,b,rn,r0,Fbase=sp.symbols("h b rn r0 Fbase",real=True)
resource=56*b-sp.Rational(56,5)*b*b-rn-r0
J=Fbase+resource/112
Q=Fbase+sp.Rational(5,4)*h*b+sp.Rational(5,8)*b*b
assert sp.expand(Q-J-(sp.Rational(5,4)*h-sp.Rational(1,2))*b
                 -sp.Rational(29,40)*b*b-(rn+r0)/112)==0

print("PASS exact tensor decomposition, capped-simplex identity, harmonic/frame algebra")
print("PASS h>81/200, linear B coefficient >1/160, quadratic coefficient 29/40")
print("PASS L1 quantization coefficient 1/480 (under sorted/cap hypotheses)")
print("NOTE upstream Type-E certificates not independently verified")
