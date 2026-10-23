"""Exact rational finite certificate for D5 contact-frame stability."""
from itertools import combinations,product
from fractions import Fraction as F
from sympy import Matrix,Rational,eye
import random
V=[]
for a,b in combinations(range(5),2):
 for s in (-1,1):
  v=[0]*5;v[a]=1;v[b]=s;V.append(Matrix(v))
assert len(V)==20
N=[j for j in range(20) if j!=0 and abs(V[0].dot(V[j]))==1]
assert len(N)==12
assert all(sum(j!=i and abs(V[i].dot(V[j]))==1 for j in range(20))==12 for i in range(20))
T=sum((V[j]*V[j].T/2 for j in N),Matrix.zeros(5))
assert T==Matrix.diag(3,3,2,2,2)
mins=[None]*5
for rem in combinations(N,3):
 S=T-sum((V[j]*V[j].T/2 for j in rem),Matrix.zeros(5))
 H=S-Rational(3,8)*eye(5)
 for k in range(1,6):
  d=H[:k,:k].det()
  assert d>0,(rem,k,d)
  if mins[k-1] is None or d<mins[k-1]:mins[k-1]=d
assert mins==[Rational(9,8),Rational(189,64),Rational(13,512),Rational(169,4096),Rational(2197,32768)]
rng=random.Random(20261023)
count=0
for _ in range(25000):
 a,b,c,d=[F(rng.randint(-20,20),40) for j in range(4)]
 f=[a+s*b+t*c+s*t*d for s,t in product((-1,1),repeat=2)]
 if not all(-F(1,2)<=v<=F(1,2) for v in f):continue
 x,y=abs(a),abs(d)
 assert x+y<=F(1,2)
 assert b*b+c*c<=(F(1,2)-max(x,y))**2+min(x,y)**2
 assert b*b+c*c<=2*(F(1,2)-y)**2
 count+=1
assert count>500
rho=F(1,525)
upper=960*rho*rho/(F(3,8)-24*rho)
assert upper==F(512,48405)
assert F(5313,500000)-upper==F(235153,4840500000)>0
B=F(383,504)
smax=F(3,16)+(B-F(3,4))**2
assert smax==F(47653,254016)
floor=30-3*B+B*B/10-smax/2-F(3,2)-B-B*B/4
assert floor==F(128429963,5080320)
assert floor+F(1,4250)==F(54583242307,2159136000)
print('PASS 220 exact D5 cases,',count,'safe rational chambers, energy and Q fractions')
