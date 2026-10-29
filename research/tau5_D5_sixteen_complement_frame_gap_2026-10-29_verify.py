#!/usr/bin/env python3
"""Exact D5 complement ranks and radial frame-gap checks. Standard library only."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

roots=[]
for i in range(5):
    for j in range(i+1,5):
        for s in (1,-1):
            v=[0]*5;v[i]=1;v[j]=s;roots.append(v)

def rank(cols):
    m=[[F(v[i]) for v in cols] for i in range(5)]
    row=0
    for col in range(len(cols)):
        piv=next((i for i in range(row,5) if m[i][col]),None)
        if piv is None:continue
        m[row],m[piv]=m[piv],m[row]
        t=m[row][col];m[row]=[v/t for v in m[row]]
        for i in range(5):
            if i!=row and m[i][col]:
                t=m[i][col];m[i]=[a-t*b for a,b in zip(m[i],m[row])]
        row+=1
    return row

def frame(a):
    T=[[F(0) for _ in range(5)] for _ in range(5)]
    for idx,v in enumerate(roots):
        for i in range(5):
            for j in range(5):
                T[i][j]+=(1-a.get(idx,F(0)))*v[i]*v[j]/2
    return T

T=frame({})
assert T==[[F(4) if i==j else F(0) for j in range(5)] for i in range(5)]
count=Counter();examples={}
for J in combinations(range(20),4):
    r=rank([roots[j] for j in J]);count[r]+=1;examples.setdefault(r,J)
assert count==Counter({3:830,4:4015}),count
for r,J in examples.items():
    I=[i for i in range(20) if i not in J]
    a={j:F(3,16) for j in J}
    a[I[0]]=F(1,1000);a[I[1]]=F(1,1000)
    x=sum((a.get(i,F(0)) for i in I),F(0))
    A=sum(a.values(),F(0));T=frame(a);mu=(20-A)/5
    V=sum((T[i][j]-(mu if i==j else 0))**2 for i in range(5) for j in range(5))
    k=5-r
    assert V>=F(5*k,5-k)*max(F(0),A/5-x)**2
    print("k",k,"omitted",J,"V",V)
A=F(383,504);x=F(1,250);d=A/5-x
assert F(5,8)*d*d==F(86918329,6350400000)
assert F(5,3)*d*d==F(86918329,2381400000)
D=(F(2)-F(1,500)-F(1,100))**2-F(39,10)
assert D==F(3259,62500)
assert F(5,4)*D*D==F(10621081,3125000000)
print("PASS: 4845 exact ranks, frame and rational bounds")
