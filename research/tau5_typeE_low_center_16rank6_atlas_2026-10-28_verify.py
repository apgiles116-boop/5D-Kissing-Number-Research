#!/usr/bin/env python3
"""Exact 16-vertex rank-six Schur atlas. Dependencies: networkx, numpy, sympy.
Uses exact small-integer matrices and rational Descartes root counts.
The upstream 6-basis screening theorem is a retained prerequisite.
"""
from collections import Counter
from itertools import product
from math import comb
import networkx as nx
import numpy as np
import sympy as sp

def charpoly_int(A):
    n=A.shape[0];B=np.eye(n,dtype=np.int64);I=B.copy();out=[1]
    for k in range(1,n+1):
        P=A@B;tr=int(np.trace(P));assert tr%k==0
        c=-(tr//k);out.append(c);B=P+c*I
    return tuple(out)

def roots_above(poly,p,q):
    n=len(poly)-1;asc=poly[::-1];signs=[]
    for j in range(n,-1,-1):
        v=sum(asc[k]*comb(k,j)*p**(k-j)*q**(n-k+j) for k in range(j,n+1))
        if v:signs.append(v>0)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def screen(poly):
    while poly[-1]==0:poly=poly[:-1]
    assert len(poly)==7
    return roots_above(poly,-1,4)==6 and roots_above(poly,1,4)<6

atlas=[g for g in nx.graph_atlas_g() if len(g)==6]
assert len(atlas)==156
cols=np.array(list(product((-1,0,1),repeat=6)),dtype=np.int64)
bases=0;signings=0;cliques=0;basis_counts=Counter();poly_counts=Counter()
for g in atlas:
    edges=sorted(tuple(sorted(e)) for e in g.edges())
    fixed=set(tuple(sorted(e)) for e in nx.minimum_spanning_tree(g).edges())
    free=[e for e in edges if e not in fixed]
    B=2*np.eye(6,dtype=np.int64)
    for i,j in fixed:B[i,j]=B[j,i]=1
    for signs in product((-1,1),repeat=len(free)):
        for (i,j),s in zip(free,signs):B[i,j]=B[j,i]=s
        signings+=1
        p6=charpoly_int(B)
        if p6[-1]==0 or not screen(p6):continue
        bases+=1
        mat=sp.Matrix(B.tolist());det=int(mat.det());adj=np.array(mat.adjugate()).astype(np.int64)
        q=np.einsum('ij,jk,ik->i',cols,adj,cols)
        selected=cols[q==2*det]
        surviving=[]
        for c in selected:
            M7=np.zeros((7,7),dtype=np.int64)
            M7[:6,:6]=B;M7[:6,6]=c;M7[6,:6]=c;M7[6,6]=2
            if screen(charpoly_int(M7)):surviving.append(c)
        if len(surviving)<10:continue
        surviving=np.array(surviving,dtype=np.int64)
        cross=surviving@adj@surviving.T
        graph=nx.Graph();graph.add_nodes_from(range(len(surviving)))
        for i in range(len(surviving)):
            for j in range(i+1,len(surviving)):
                num=int(cross[i,j])
                if num%det!=0 or abs(num)>abs(det):continue
                t=num//det
                M8=np.zeros((8,8),dtype=np.int64)
                M8[:6,:6]=B;M8[:6,6]=surviving[i];M8[6:,:6]=surviving[i]
                M8[:6,7]=surviving[j];M8[7,:6]=surviving[j]
                M8[6,6]=M8[7,7]=2;M8[6,7]=M8[7,6]=t
                if screen(charpoly_int(M8)):graph.add_edge(i,j)
        maxlen=0
        for clique in nx.find_cliques(graph):
            maxlen=max(maxlen,len(clique))
            if len(clique)!=10:continue
            C=surviving[clique].T;Dn=C.T@adj@C
            assert np.all(Dn%det==0)
            M16=np.zeros((16,16),dtype=np.int64)
            M16[:6,:6]=B;M16[:6,6:]=C;M16[6:,:6]=C.T;M16[6:,6:]=Dn//det
            poly=charpoly_int(M16)
            assert poly[-10:]==(0,)*10
            poly6=poly[:7]
            assert roots_above(poly6,1,2)==6
            cliques+=1;basis_counts[bases]+=1;poly_counts[poly6]+=1
        assert maxlen<=10
assert (signings,bases,cliques)==(4562,246,4096)
assert sorted(basis_counts.values())==[1024,1024,2048]
assert poly_counts==Counter({(1,-32,411,-2676,9091,-14484,7161):4096})
print('PASS: 4562 signed six-bases; 246 spectral survivors')
print('PASS: exactly 4096 maximal 10-cliques across 3 bases')
print('PASS: one exact nonzero characteristic polynomial, all roots > 1/2')
print('CONDITIONAL: previous 6-/7-basis atlas completeness and Type-E mass inputs assumed')
