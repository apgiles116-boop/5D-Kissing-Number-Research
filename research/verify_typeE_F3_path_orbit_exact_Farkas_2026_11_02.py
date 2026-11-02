#!/usr/bin/env python3
"""Exact F3 canonical path-orbit exclusion, no third-party dependencies.

Each listed constraint is of the form A_k dot x <= b_k, where
x=(u_i dot u_j)_(i<j) for eight unit endpoints.
The listed positive integer weights satisfy sum weight*A_k=0,
sum weight*b_k<0. PSD constraints are v.T*G*v >= 0.
"""
from itertools import permutations

DEEP = {(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
P = ((0,4),(7,1),(2,3),(5,6))
PAIRS = tuple((i,j) for i in range(8) for j in range(i+1,8))
INDEX = {p:i for i,p in enumerate(PAIRS)}
PATH = ((0,1),(1,2),(2,3))

# Exact rational Farkas certificate; weights are positive integers.
# A 'sos' vector enforces v.T G v >= 0 by Gram PSD.
CERTIFICATE = [
    ('safe_hi', [0, 1], 60483007662782953824),
    ('deep', [0, 2], 323821202842520245524),
    ('deep', [0, 4], 25010543121392523120),
    ('deep', [0, 5], 228950092250384262444),
    ('safe_lo', [1, 3], 178161633044319364980),
    ('safe_hi', [1, 6], 18286128339274298226),
    ('deep', [1, 7], 17550447216943027590),
    ('deep', [2, 3], 56396034889107947064),
    ('safe_hi', [2, 6], 219408384975357757920),
    ('safe_hi', [3, 4], 22075189297188086940),
    ('safe_hi', [3, 5], 50601253948641950004),
    ('safe_hi', [3, 7], 15588826810170083472),
    ('safe_lo', [4, 6], 6307977503272421490),
    ('safe_hi', [4, 7], 190241051639352127530),
    ('deep', [5, 6], 12314528466037267260),
    ('deep', [5, 7], 353905019602515565296),
    ('path', [0, 1], 792193743575236888368),
    ('path', [1, 2], 658520995922894034144),
    ('path', [2, 3], 773359990594231623600),
    ('sos', [10, -1, 10, 6, 0, 8, 5, 8], 467184955447478928),
    ('sos', [10, 5, 10, 2, 13, 2, -1, 0], 229703769521079207),
    ('sos', [-9, 5, -6, 6, 0, -12, -3, -9], 325874616305195414),
    ('sos', [5, -11, 9, 10, -6, -2, 6, -3], 487443656747446836),
    ('sos', [-3, -12, -3, 2, -7, -10, 0, -10], 299933498063155860),
    ('sos', [1, -12, 5, -4, -12, 5, -1, 6], 28214231153337528),
    ('sos', [10, -8, 9, -6, -1, 5, -8, 5], 547659296602663848),
    ('sos', [0, -11, 0, -8, -9, -4, -10, -5], 137427137607340599),
    ('sos', [1, -2, 1, -2, -7, 12, 7, 12], 208859852755575792),
    ('sos', [1, -1, 1, -12, -5, 9, -6, 10], 350865904958236794),
]

def row(kind, data):
    A=[0]*28
    if kind=='sos':
        v=data
        for (i,j),k in INDEX.items():
            A[k]=-8*v[i]*v[j]
        b=4*sum(t*t for t in v)
    elif kind=='path':
        i,j=data
        a,b0=P[i];c,d=P[j]
        for x,y,sgn in ((a,c,1),(a,d,-1),(b0,c,-1),(b0,d,1)):
            A[INDEX[tuple(sorted((x,y)))]]+=sgn
        b=-2
    else:
        i,j=data
        A[INDEX[(i,j)]]=4 if kind in ('deep','safe_hi') else -4
        b=-2 if kind=='deep' else 2
        assert (i,j) in DEEP if kind=='deep' else (i,j) not in DEEP
    return A,b

assert all(w>0 for kind,data,w in CERTIFICATE)
assert len(CERTIFICATE)==29
acc=[0]*28
const=0
for kind,data,w in CERTIFICATE:
    a,b=row(kind,data)
    for k in range(28):acc[k]+=w*a[k]
    const+=w*b
assert all(t==0 for t in acc),acc
assert const==-12164187608516934784, const
print('EXACT FARKAS CONTRADICTION: sum of 29 nonnegative weighted slacks =',const)

# The endpoint deep-contact graph has an orientation-preserving
# automorphism action on the four matched pairs.
PSET={frozenset(pair) for pair in P}
assert all(tuple(sorted(pair)) in DEEP for pair in P)
match={frozenset(pair):i for i,pair in enumerate(P)}
paths=set()
valid=0
for perm in permutations(range(8)):
    if {tuple(sorted((perm[i],perm[j]))) for i,j in DEEP}!=DEEP:continue
    if {frozenset((perm[i],perm[j])) for i,j in P}!=PSET:continue
    quotient=[]
    for a,b in P:
        k=match[frozenset((perm[a],perm[b]))]
        assert (perm[a],perm[b])==P[k] # all automorphisms preserve orientations
        quotient.append(k)
    q=tuple(quotient)
    path=q
    paths.add(min(path,path[::-1]))
    valid+=1
assert valid==8
assert paths=={(0,1,2,3),(0,1,3,2),(1,0,2,3),(1,0,3,2)}
print('EXACT GRAPH AUDIT: all four paths in one canonical orbit excluded.')
print('PASS')
