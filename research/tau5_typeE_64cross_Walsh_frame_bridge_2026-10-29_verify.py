"""Exact Fraction checks for 2026-10-29 Type-E 64-cross Walsh/frame bridge.
Analytic arguments are in the companion markdown; no float tolerances.
"""
from fractions import Fraction as F
from random import Random

B=F(383,504); rB=B-F(3,4)
gB=F(3,16)+rB*rB
L=F(8790283,317520)
assert rB==F(5,504)
assert L==30-3*B+B*B/10-gB/2
assert B+F(4,5)*B*B-gB==F(1313651,1270080)
assert F(1,125)<F(1,11)**2
assert F(1313651,1270080)-B/11==F(13485001,13970880)

def cap(A):
 k=min(int(4*A),19)
 return [F(1,4)]*k+[A-F(k,4)]+[F(0)]*(19-k)
def sq(v):return sum(x*x for x in v)

rng=Random(20261029)
for _ in range(8500):
 A=B*F(rng.randrange(1,10000),10000)
 raw=[F(rng.randrange(1,200),rng.randrange(200,500)) for i in range(20)]
 a=sorted([A*x/sum(raw) for x in raw],reverse=True)
 assert max(a)<=F(1,4)
 b=cap(A); delta=sum(abs(x-y) for x,y in zip(a,b))
 gap=sq(b)-sq(a)
 assert gap>=F(5,64)*delta*delta
 if A>=F(3,4):
  r=A-F(3,4)
  assert gap>=r*delta-delta*delta/2
 assert 30-3*A+A*A/10-sq(a)/2>=L+F(57,20)*(B-A)+F(5,128)*delta*delta

# All four two-sided safe contacts imply the mixed Walsh inequalities.
vals=[F(i,8) for i in range(-4,5)]
n=0
for c in vals:
 for b in vals:
  for d in vals:
   for e in vals:
    if all(abs(c+t*b+s*d+s*t*e)<=F(1,2)
           for s in (-1,1) for t in (-1,1)):
     n+=1
     assert abs(d)+abs(e)<=F(1,2)
     assert abs(b)+abs(e)<=F(1,2)
assert n==441

for _ in range(3000):
 a=[F(rng.randrange(0,251),1000) for j in range(4)]
 y=sum(a);U=sq(a)
 assert sum(a[j]*(1-a[k]) for j in range(4) for k in range(4)
            if j!=k)==3*y-y*y+U

eps=F(1,300000)
rmin=rB-F(20,57)*eps
assert rmin>0 and rmin*rmin>F(128,5)*eps
print("PASS: exact constants, 8500 cap cases, 441 Walsh cases, 3000 core identities, bootstrap")
