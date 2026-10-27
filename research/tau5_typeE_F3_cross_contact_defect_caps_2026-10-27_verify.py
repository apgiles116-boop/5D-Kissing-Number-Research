"""Exact SymPy verification of F3 cross-contact caps and quartic envelopes.
The near-antipodal inequalities are proved analytically in the companion note.
"""
import sympy as sp
from itertools import combinations, permutations

E={frozenset(p) for p in [(0,2),(0,4),(0,5),(1,4),(1,7),
                           (2,3),(2,7),(3,6),(5,6),(5,7)]}
P={'P1':[(0,2),(1,4),(3,6),(5,7)],
   'P2':[(0,4),(1,7),(2,3),(5,6)],
   'P3':[(0,5),(1,4),(2,7),(3,6)]}
for name,match in P.items():
    assert set(sum((list(t) for t in match),[]))==set(range(8))
    assert all(frozenset(t) in E for t in match)
    counts={}
    for a,b in combinations(match,2):
        cross=[(u,v) for u in a for v in b if frozenset((u,v)) in E]
        counts[(a,b)]=len(cross)
        if len(cross)==2:
            assert len({u for u,v in cross})==len({v for u,v in cross})==2
    if name=='P2':
        assert sorted(counts.values())==[1]*6
    else:
        assert sorted(counts.values())==[0,1,1,1,1,2]
        assert counts[((1,4),(3,6))]==0
        assert counts[((0,2),(5,7)) if name=='P1' else ((0,5),(2,7))]==2
cycles=set()
for a,b,c,d in permutations(range(8),4):
    if all(frozenset(pair) in E for pair in [(a,b),(b,c),(c,d),(d,a)]):
        cycles.add(frozenset((a,b,c,d)))
assert cycles=={frozenset((0,2,5,7))}

c=sp.sqrt(2)-sp.Rational(5,4)
D0=sp.Rational(1780062775,4032758016)
D6=sp.Rational(383,1008)
f=lambda d:(sp.Rational(1,2)+d)**2*d*(1+d)
assert sp.simplify(1/(6+4*sp.sqrt(2))-(sp.Rational(3,2)-sp.sqrt(2)))==0
assert sp.simplify(c-(sp.Rational(1,4)-1/(6+4*sp.sqrt(2))))==0
assert all(sp.N(x,50)>0 for x in [c,sp.Rational(1,4)-c,D0-2*c,3*c-D0,
    D0-sp.Rational(1,4)-c,sp.Rational(1,4)+2*c-D0,D6-2*c,3*c-D6,
    c-(D6-sp.Rational(1,4))])
P2=sp.expand(2*f(c)+f(D0-2*c))
P13=sp.expand(f(sp.Rational(1,4))+f(c)+f(D0-sp.Rational(1,4)-c))
P2six=sp.expand(2*f(c)+f(D6-2*c))
P13six=sp.expand(f(sp.Rational(1,4))+f(D6-sp.Rational(1,4)))
assert sp.simplify(P13six-sp.Rational(241638909745,1032386052096))==0
old=sp.expand(f(sp.Rational(1,4))+f(D0-sp.Rational(1,4)))
assert all(sp.N(old-v,50)>0 for v in [P2,P13,P2six,P13six])
assert sp.N(P2six,50)<sp.N(P2,50)
print("PASS: F3 cross-contacts, unique C4, radical caps, quartic envelopes")
for name,val in [('P2',P2),('P1/P3',P13),('P2 six-active',P2six),
                 ('P1/P3 six-active',P13six)]:
    print(name,sp.N(val,20))
