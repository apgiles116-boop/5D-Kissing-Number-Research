"""Exact rational finite audit of F3 signed triangle obstruction and quartic caps."""
from fractions import Fraction as Q
from itertools import combinations
from math import prod

E = {frozenset(e) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),
                             (2,3),(2,7),(3,6),(5,6),(5,7)]}
P = {
 'P1': [(0,2),(1,4),(3,6),(5,7)],
 'P2': [(0,4),(1,7),(2,3),(5,6)],
 'P3': [(0,5),(1,4),(2,7),(3,6)],
}
D0 = Q(1780062775,4032758016)
f = lambda d: (Q(1,2)+d)**2*(d+d*d)
assert Q(3,8)<D0<Q(1,2)
expected = {
 'P1': f(Q(1,4))+f(Q(1,8))+f(D0-Q(3,8)),
 'P2': 3*f(Q(1,8))+f(D0-Q(3,8)),
 'P3': f(Q(1,4))+f(Q(1,8))+f(D0-Q(3,8)),
}
for name, match in P.items():
    assert len(set(sum((list(x) for x in match), [])))==8
    assert all(frozenset(x) in E for x in match)
    pairs = list(combinations(range(4),2))
    cross_count, forced_sign = {}, {}
    for i,j in pairs:
        cross = []
        for u in match[i]:
            for v in match[j]:
                if frozenset((u,v)) in E:
                    sigma_i = 1 if u==match[i][0] else -1
                    sigma_j = 1 if v==match[j][0] else -1
                    cross.append(-sigma_i*sigma_j)
        assert len(cross)<=2
        assert len(set(cross))<=1 # when 2, both are disjoint and opposite-aligned
        cross_count[(i,j)] = len(cross)
        if cross: forced_sign[(i,j)] = cross[0]
    triangles = []
    for vertices in combinations(range(4),3):
        sides = frozenset(combinations(vertices,2))
        if all(cross_count[e] for e in sides):
            assert prod(forced_sign[e] for e in sides)==-1
            triangles.append(sides)
    if name=='P2':
        assert sorted(cross_count.values())==[1]*6
        assert len(triangles)==4
    else:
        assert sorted(cross_count.values())==[0,1,1,1,1,2]
        assert len(triangles)==2
    best = Q(-1)
    best_support = None
    max_active = 0
    # All 64 labeled possible active subsets: omit zero-cross and forbidden triangles.
    for mask in range(64):
        active = frozenset(pairs[i] for i in range(6) if mask&(1<<i))
        if any(cross_count[e]==0 for e in active): continue
        if any(t.issubset(active) for t in triangles): continue
        max_active = max(max_active,len(active))
        # Majorization: convex f is maximized by filling largest caps first.
        caps = sorted((Q(cross_count[e],8) for e in active), reverse=True)
        remaining = D0
        allocation=[]
        for cap in caps:
            d = min(cap,remaining)
            allocation.append(d)
            remaining -= d
        value = sum((f(d) for d in allocation),Q(0))
        if value>best:
            best, best_support = value, active
    assert max_active==4
    assert best==expected[name], (name,best,expected[name])
    print(name, 'max active=',max_active,'best rational=',best,'decimal=',format(float(best),'.15f'),'support=',sorted(best_support))
assert expected['P2']<expected['P1']
assert expected['P1']<Q(1,1)
print('PASS: 3 matchings, all signed triangles, all 64 subsets each, exact quartic bounds.')
