"""Exact rational audit of the D5 20-line Q-Gram spectrum; no dependencies."""
from fractions import Fraction as F

def mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B,alpha=F(1)):
    return [[A[i][j]+alpha*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,a):
    return [[a*x for x in row] for row in A]
def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def trace(A):
    return sum((A[i][i] for i in range(len(A))),F(0))
def rank(A):
    A=[list(map(F,row)) for row in A]; m=len(A); n=len(A[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        t=A[r][j]; A[r]=[v/t for v in A[r]]
        for i in range(m):
            if i!=r and A[i][j]:
                t=A[i][j]; A[i]=[a-t*b for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

vectors=[]
edges=[]
for i in range(5):
    for j in range(i+1,5):
        edges.append((i,j))
        for s in (1,-1):
            v=[0]*5;v[i]=1;v[j]=s;vectors.append(v)
n=20; I=eye(n)
K=[[F(sum(a*b for a,b in zip(vectors[i],vectors[j]))**2,4)-F(1,5)
    for j in range(n)] for i in range(n)]
K2=mul(K,K)
K3=mul(K2,K)
# x(x-1)(x-3/2) = x^3 - (5/2)x^2 + (3/2)x
assert add(add(K3,K2,F(-5,2)),K,F(3,2))==[[F(0)]*n for _ in range(n)]
# Solve multiplicities using tr(K)=17, tr(K^2)=19 and sum multiplicities=20.
assert trace(K)==F(16)  # 10*1 + 4*(3/2) = 16
assert trace(K2)==F(19) # 10 + 4*9/4 = 19
assert rank(K)==14
P=add(add(I,K,F(-5,3)),K2,F(2,3))
assert mul(P,P)==P
assert mul(K,P)==[[F(0)]*n for _ in range(n)]
assert trace(P)==6
B=[[F(i in edge) for edge in edges] for i in range(5)]
assert rank(B)==5
print("PASS: spectrum 0(x6), 1(x10), 3/2(x4); kernel projector and incidence rank exact")
