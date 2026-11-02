#!/usr/bin/env python3
"""Exact rational R^3 F3 witnesses for two canonical three-defect paths.
No floating point or external packages are used for verification.
"""
from fractions import Fraction as Q
from itertools import combinations

DEEP = {(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
P = ((0,4),(7,1),(2,3),(5,6))
HALF = Q(1,2)
CAP = Q(383,504)

# Each row (pivot p, sign s, integer pair (t1,t2)) defines a rational
# unit vector by stereographic projection at scale N.
WITNESSES = {
    (0,2,1,3): {
        'N': 100,
        'rows': [
            (2,-1,(31,-30)),
            (2, 1,(28,-33)),
            (2, 1,(2,18)),
            (2,-1,(-30,-32)),
            (1, 1,(-23,11)),
            (2, 1,(-33,-27)),
            (1, 1,(27,-12)),
            (2,-1,(-1,17)),
        ],
        'min_contact_margin': Q(1,60),
        'min_defect_margin': Q(1,40),
        'core_energy_upper': Q(7,20),
    },
    (0,2,3,1): {
        'N': 1000,
        'rows': [
            (1, 1,(251,-168)),
            (0, 1,(-324,-202)),
            (1,-1,(144,372)),
            (2,-1,(60,87)),
            (0,-1,(-233,181)),
            (2,-1,(-226,-384)),
            (2, 1,(-44,77)),
            (1, 1,(-158,181)),
        ],
        'min_contact_margin': Q(1,2000),
        'min_defect_margin': Q(1,3000),
        'core_energy_upper': Q(7,16),
    },
}

def vector(row,N):
    p,s,nums = row
    assert p in range(3) and s in (-1,1) and len(nums)==2
    t=[Q(a,N) for a in nums]
    r=sum(x*x for x in t)
    v=[Q(0)]*3
    v[p]=s*(1-r)/(1+r)
    for j,x in zip((j for j in range(3) if j!=p),t):
        v[j]=2*x/(1+r)
    return v

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def run():
    for path,rec in WITNESSES.items():
        U=[vector(row,rec['N']) for row in rec['rows']]
        assert len(U)==8
        assert all(dot(u,u)==1 for u in U)
        margins=[]
        for i,j in combinations(range(8),2):
            d=dot(U[i],U[j])
            margin=-HALF-d if (i,j) in DEEP else HALF-abs(d)
            margins.append(margin)
            assert margin>rec['min_contact_margin'],(path,(i,j),'endpoint')
        m=[[(U[i][k]+U[j][k])/2 for k in range(3)] for i,j in P]
        w=[[(U[i][k]-U[j][k])/2 for k in range(3)] for i,j in P]
        assert all(dot(m[i],w[i])==0 for i in range(4))
        core_energy=sum(dot(x,x) for x in m)
        assert core_energy<rec['core_energy_upper']<CAP
        defects={tuple(sorted(e)) for e in zip(path,path[1:])}
        defect_margins=[]
        for i,j in combinations(range(4),2):
            d=dot(w[i],w[j])
            if (i,j) in defects:
                margin=-HALF-d
                defect_margins.append(margin)
                assert margin>rec['min_defect_margin'],(path,(i,j),'defect')
            else:
                assert abs(d)<HALF,(path,(i,j),'unexpected defect')
        assert len(defect_margins)==3
        print('PATH',path,'PASS: exact rational unit vectors in R^3')
        print('  endpoint margin >',rec['min_contact_margin'],
              '; defect margin >',rec['min_defect_margin'])
        print('  C <',rec['core_energy_upper'],'< 383/504; all nonpath pairs safe')
        print('  diagnostics only: C=',float(core_energy),
              'min endpoint=',float(min(margins)),
              'min defect=',float(min(defect_margins)))
    print('PASS: both surviving canonical paths locally realizable in R^3.')

if __name__=='__main__':
    run()
