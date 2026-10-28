#!/usr/bin/env python3
"""Exact D5 16/17-line Walsh atlas and improved full-20 stress-gap checks.
Requires SymPy. No floating-point rank or eigenvalue decisions.
"""
from itertools import combinations, permutations, product
from collections import Counter
from fractions import Fraction as F
from sympy import Matrix, eye, symbols
from sympy.polys.matrices import DomainMatrix

SUPPORTS=list(combinations(range(5),2))
ROOTS=[]
for a,b in SUPPORTS:
    for s in (1,-1):
        v=[0]*5;v[a]=1;v[b]=s;ROOTS.append(tuple(v))
INDEX={v:i for i,v in enumerate(ROOTS)}
assert len(INDEX)==20

def canonical(v):
    s=next(z for z in v if z)
    return tuple(s*x for x in v)

GROUP=set()
for p in permutations(range(5)):
    for s4 in product((1,-1),repeat=4):
        sg=s4+(s4[0]*s4[1]*s4[2]*s4[3],)
        perm=[]
        for v in ROOTS:
            w=[0]*5
            for i in range(5):w[p[i]]=sg[i]*v[i]
            perm.append(INDEX[canonical(w)])
        GROUP.add(tuple(perm))
assert len(GROUP)==1920

def orbits(k):
    unseen=set(combinations(range(20),k));out=[]
    while unseen:
        rep=min(unseen)
        orb={tuple(sorted(p[i] for i in rep)) for p in GROUP}
        assert orb<=unseen
        unseen-=orb;out.append((rep,len(orb)))
    assert sum(sz for _,sz in out)=={3:1140,4:4845}[k]
    return out

def walsh(chosen):
    n=len(chosen);vs=[ROOTS[i] for i in chosen];rows=[]
    for i in range(n):
        row=[0]*(5*n);row[5*i:5*i+5]=vs[i];rows.append(row)
    for i,j in combinations(range(n),2):
        sig=sum(vs[i][t]*vs[j][t] for t in range(5))
        if abs(sig)==1:
            row=[0]*(5*n)
            row[5*i:5*i+5]=[sig*t for t in vs[j]]
            row[5*j:5*j+5]=vs[i]
            rows.append(row)
    return Matrix(rows)

def pd_bareiss(B):
    A=[list(map(int,B.row(i))) for i in range(B.rows)]
    n=len(A);prev=1
    for k in range(n-1):
        pivot=A[k][k]
        if pivot<=0:return False
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(i,n):
                q,r=divmod(A[i][j]*pivot-aik*A[j][k],prev)
                assert r==0
                A[i][j]=q
            A[i][k]=0
        for i in range(k+1,n):
            for j in range(i+1,n):A[j][i]=A[i][j]
        prev=pivot
    return A[-1][-1]>0

def pattern(omitted):
    return sorted(Counter(SUPPORTS[i//2] for i in omitted).values(),reverse=True)

def doubled(omitted):
    return set(SUPPORTS)-{SUPPORTS[i//2] for i in omitted}

def triangle(E):
    return any(set(combinations(t,2))<=E for t in combinations(range(5),3))

def exceptional_four_singles(omitted):
    edge_sign={SUPPORTS[i//2]:(1 if i%2==0 else -1) for i in omitted}
    missing=set(edge_sign)
    deg=Counter(t for e in missing for t in e)
    if max(deg.values())==4:return True
    for tri in combinations(range(5),3):
        edges=set(combinations(tri,2))
        if edges<=missing:
            rem=missing-edges
            if len(rem)==1 and set(next(iter(rem))).isdisjoint(tri):
                return all(e in edge_sign for e in edges) and \
                       edge_sign[tuple(sorted((tri[0],tri[1])))]* \
                       edge_sign[tuple(sorted((tri[0],tri[2])))]* \
                       edge_sign[tuple(sorted((tri[1],tri[2])))]==1
    return False

counts={}
for k in (3,4):
    O=orbits(k)
    assert len(O)=={3:7,4:17}[k]
    hist=Counter();no_triangle=0
    for omitted,size in O:
        chosen=tuple(i for i in range(20) if i not in omitted)
        L=walsh(chosen)
        rank=DomainMatrix.from_Matrix(L).rank()
        nullity=5*len(chosen)-rank
        p=pattern(omitted);E=doubled(omitted)
        no_triangle+=size*(not triangle(E))
        if k==3:
            assert p in ([1,1,1],[2,1])
            expected=0 if p==[1,1,1] else 3
        elif p==[2,2]:expected=6
        elif p==[2,1,1]:expected=3
        else:
            assert p==[1,1,1,1]
            expected=1 if exceptional_four_singles(omitted) else 0
        assert nullity==expected,(k,omitted,rank,expected)
        hist[nullity]+=size
        if nullity==0:
            K=L.T*L
            if k==3:assert pd_bareiss(17*K-2*eye(K.rows))
            else:assert pd_bareiss(11*K-eye(K.rows))
    counts[k]=(hist,no_triangle)
assert counts[3]==(Counter({0:960,3:180}),0)
assert counts[4]==(Counter({0:3200,1:160,3:1440,6:45}),160)
print("PASS: 7 three-root omission orbits; 17-line ranks and gap >2/17")
print("PASS: 17 four-root omission orbits; 16-line ranks and gap >1/11")
print("PASS: all 17-line and 4685/4845 sixteen-line subsets have doubled D3 triangles")

V=Matrix(ROOTS);D=V*V.T
adj=Matrix(20,20,lambda i,j:int(i!=j and abs(D[i,j])==1))
S=D-2*eye(20)
assert V.T*V==8*eye(5)
assert adj.eigenvals()=={12:1,2:4,-4:5,0:10}
assert S.eigenvals()=={6:5,-2:15}
assert all(sum(S[i,j]*V[j,t] for j in range(20))==6*V[i,t]
           for i in range(20) for t in range(5))
tri_ids=[i for i in range(20) if SUPPORTS[i//2] in {(0,1),(0,2),(1,2)}]
VT=Matrix([ROOTS[i] for i in tri_ids]);DT=VT*VT.T
ST=DT-2*eye(6)
AT=Matrix(6,6,lambda i,j:int(i!=j and abs(DT[i,j])==1))
assert ST.eigenvals()=={2:3,-2:3}
assert AT.eigenvals()=={4:1,-2:2,0:3}
assert sum(AT)==24
print("PASS: full-D5 and local-D3 signed and unsigned stress spectra")

x=symbols("x")
p=x**3-24*x**2+146*x-48
lo=F(5902,10000);b=F(50991,10000);c=F(141422,100000)
assert p.subs(x,F(1,3))<0<p.subs(x,F(7,20))
assert p.subs(x,lo*lo)<0
assert p.diff(x).subs(x,F(7,20))>0
assert b*b>26 and c*c>2
assert 913*lo*lo>(b+9*c)**2
print("PASS: improved conditional full-20 midpoint gap A=0 or A>1/913")
print("ALL EXACT CERTIFICATES PASSED")
