"""Exact rational verifier for the Type-E outside-16 Schur-convex spectral gap.
The mathematical proof of Schur-convexity and Gegenbauer positivity is in the note.
"""
from fractions import Fraction as Q
import sympy as s

def F(a):
    one=Q(1)
    return sum((one/((one-x)**2*(one-y)**2)
                -one/((one-x)*(one-y)))/8
               for i,x in enumerate(a) for y in a[i+1:])

B=Q(383,504)
a=[Q(1,4)]*3+[B-Q(3,4)]+[Q(0)]*12
assert len(a)==16 and sum(a)==B
V=F(a)
assert V==Q(18211220,6723027)
assert 4-V==Q(8680888,6723027)>0
assert F([Q(1,4)]*4+[Q(0)]*12)==Q(100,27)<4

lam=Q(1,31)
c=Q(3,4)-lam
K=1/(2*c)+1/(4*c*c)
q=(Q(1,2)+lam/2)/c
D=4*q**3-q/2
assert (c,K,q,D)==(Q(89,124),Q(9362,7921),Q(64,89),Q(795104,704969))
assert D>Q(1,3)  # larger than absolute value at the interior critical points
margin=4-V-30*K*D*lam
assert margin==Q(44313384250232,37541782445232123)>0

x,y=s.symbols("x y",positive=True)
aa,bb=s.symbols("a b")
g=1/((1-aa)**2*(1-bb)**2)-1/((1-aa)*(1-bb))
assert s.factor(s.diff(g,aa).subs({aa:1-1/x,bb:1-1/y})-(2*x**3*y**2-x**2*y))==0
assert s.factor(s.diff(g,aa,2).subs({aa:1-1/x,bb:1-1/y})-2*x**3*y*(3*x*y-1))==0
P2=(4*x*x-1)/3
P4=(16*x**4-12*x*x+1)/5
assert s.expand((1+6*P2+5*P4)/16-(x**4-x*x/4))==0

print("PASS: exact capped-simplex, Schur derivatives, Gegenbauer expansion and >1/31 gap")
print("Fmax =",V, "margin =",margin)
