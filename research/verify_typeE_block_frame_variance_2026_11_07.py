"""Exact rational audit of the isolated/core five-dimensional frame identities."""
from fractions import Fraction as F

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))
def add(A,B):
    return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def op(vs):
    return [[sum(v[i]*v[j] for v in vs) for j in range(5)] for i in range(5)]
def frob(A,B):
    return sum(a*b for ra,rb in zip(A,B) for a,b in zip(ra,rb))
def traceless(A):
    t=sum(A[i][i] for i in range(5))
    return [[A[i][j]-(t/F(5) if i==j else 0) for j in range(5)] for i in range(5)]

v=[[F(x) for x in row] for row in [
    (1,0,0,0,0),(0,2,0,0,0),(1,1,1,0,0),(0,0,1,2,0),
    (0,0,0,1,1),(1,0,1,0,1)]]
I,C=v[:4],v[4:]
ZI,ZC=op(I),op(C)
EI,EC=traceless(ZI),traceless(ZC)
TI=sum(dot(x,x) for x in I)
TC=sum(dot(x,x) for x in C)
VI,VC=frob(EI,EI),frob(EC,EC)
Delta=frob(add(EI,EC),add(EI,EC))
QII=sum(dot(x,y)**2 for i,x in enumerate(I) for y in I[i+1:])
QCC=sum(dot(x,y)**2 for i,x in enumerate(C) for y in C[i+1:])
QIC=sum(dot(x,y)**2 for x in I for y in C)
assert VI==2*QII+sum(dot(x,x)**2 for x in I)-TI**2/F(5)
assert VC==2*QCC+sum(dot(x,x)**2 for x in C)-TC**2/F(5)
assert QIC==TI*TC/F(5)+(Delta-VI-VC)/2
assert (QIC-TI*TC/F(5))**2 <= VI*VC
assert VC >= TC**2/F(20)
assert (F(1633,504)**2)/20==F(2666689,5080320)
print("PASS: exact rational identities, Cauchy bound, rank floor and Type-E constant")
