#!/usr/bin/env python3
"""Exact rational regression for the Type-E Walsh edge-frame identity."""
from fractions import Fraction as Q
from itertools import combinations
SUPPORTS=list(combinations(range(5),2))
LABELS=[(p,q,s) for p,q in SUPPORTS for s in (1,-1)]
CORE=[i for i,(p,q,s) in enumerate(LABELS) if p==0 and s==1]
K=set(combinations(CORE,2))
SAME=set();DISJOINT=set();MEETING=set()
for i,j in combinations(range(20),2):
    a=set(LABELS[i][:2]);b=set(LABELS[j][:2])
    if a==b:SAME.add((i,j))
    elif a.isdisjoint(b):DISJOINT.add((i,j))
    else:MEETING.add((i,j))
R=MEETING-K;ORTHO=SAME|DISJOINT
assert (len(SAME),len(DISJOINT),len(MEETING),len(K),len(R))==(10,60,120,6,114)

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def outer(x):return [[x[i]*x[j] for j in range(5)] for i in range(5)]
def zeros():return [[Q(0) for j in range(5)] for i in range(5)]
def add(X,Y):return [[X[i][j]+Y[i][j] for j in range(5)] for i in range(5)]
def normsq(X):return sum(X[i][j]**2 for i in range(5) for j in range(5))

def rational_test():
    m=[];z=[]
    for p,q,sign in LABELS:
        mm=[Q(0)]*5;zz=[Q(0)]*5
        mm[p]=Q(13,85);zz[q]=Q(sign*84,85)
        m.append(mm);z.append(zz)
    a=[dot(x,x) for x in m]
    assert all(dot(m[i],z[i])==0 and a[i]+dot(z[i],z[i])==1 for i in range(20))
    A=sum(a);U=sum(x*x for x in a)
    assert A<Q(567,1000)
    S=[add(outer(m[i]),outer(z[i])) for i in range(20)]
    F=zeros()
    for x in S:F=add(F,x)
    V=normsq([[F[i][j]-(4 if i==j else 0) for j in range(5)] for i in range(5)])
    W={}
    for i,j in combinations(range(20),2):
        W[i,j]=sum((dot(x,y)**2 for x,y in
                    ((m[i],m[j]),(m[i],z[j]),(z[i],m[j]),(z[i],z[j]))),Q(0))
        assert W[i,j]==sum(S[i][k][l]*S[j][k][l] for k in range(5) for l in range(5))
        contacts=[dot([m[i][k]+si*z[i][k] for k in range(5)],
                      [m[j][k]+sj*z[j][k] for k in range(5)])
                  for si in (1,-1) for sj in (1,-1)]
        assert sum(t*t for t in contacts)==4*W[i,j]
    assert sum(W.values())==30+A-U+V/2
    W70=sum(W[e] for e in ORTHO)
    X6=sum(W[e]-Q(1,4) for e in K)
    S114=sum(Q(1,4)-W[e] for e in R)
    assert W70+X6==A-U+V/2+S114
    print("PASS non-D5 rational frame/Walsh identity; A =",A)

def D5_test():
    W={};F=zeros()
    for p,q,s in LABELS:
        S=zeros();S[p][p]=S[q][q]=Q(1,2)
        S[p][q]=S[q][p]=Q(s,2)
        F=add(F,S)
    assert normsq([[F[i][j]-(4 if i==j else 0) for j in range(5)] for i in range(5)])==0
    for i,j in combinations(range(20),2):
        p,q,s=LABELS[i];r,t,u=LABELS[j]
        vi=[0]*5;vj=[0]*5
        vi[p]=1;vi[q]=s;vj[r]=1;vj[t]=u
        W[i,j]=Q(dot(vi,vj)**2,4)
    assert sum(W.values())==30
    assert all(W[e]==0 for e in ORTHO)
    assert all(W[e]==Q(1,4) for e in MEETING)
    print("PASS exact D5 saturation and 70/120 incidence")

if __name__=="__main__":
    rational_test()
    D5_test()
    print("ALL EXACT CHECKS PASSED; Type E remains OPEN")
