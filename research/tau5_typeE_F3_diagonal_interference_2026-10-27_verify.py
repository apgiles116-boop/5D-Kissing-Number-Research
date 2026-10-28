#!/usr/bin/env python3
"""Exact rational audit of the Type-E F3 diagonal interference bound.
The Cauchy/PSD inequalities themselves are proved in the accompanying note.
"""
from fractions import Fraction as F
from itertools import combinations, product

edges = {frozenset(e) for e in ((0,2),(0,4),(0,5),(1,4),(1,7),
                               (2,3),(2,7),(3,6),(5,6),(5,7))}
matchings = (
    ((0,2),(1,4),(3,6),(5,7)),
    ((0,4),(1,7),(2,3),(5,6)),
    ((0,5),(1,4),(2,7),(3,6)),
)
def f(d):
    return (F(1,2)+d)**2*(d+d*d)
def h(d):
    return f(d)+F(7,64)*(d+d*d)

assert f(F(1,4)) == F(45,256)
assert h(F(1,4)) == F(215,1024)
assert h(F(3,16))+h(F(1,8)) == F(13101,65536) < F(215,1024)
assert h(F(1,6)) == F(2233,20736)
assert h(F(1,8)) == F(9,128)
assert 2*h(F(1,8)) == F(9,64)
assert (h(F(1,6))/F(1,6)*(F(1,6)-F(1,4)/3-F(1,4)**2/3)
        +h(F(1,8))/F(1,8)*F(1,4)) == F(10009,55296) < F(215,1024)
assert f(F(3,16))+f(F(1,8)) == F(10497,65536)
assert f(F(1,6)) == F(7,81)
assert f(F(1,6))/F(1,6) == F(14,27)
assert f(F(1,8))/F(1,8) == F(225,512)
assert F(7,81)+(F(225,512)-F(14,81))*F(1,4)-F(14,81)*F(1,4)**2 == F(7867,55296)
assert F(7867,55296) < F(45,256)
assert F(10497,65536) < F(45,256)
assert 2*f(F(1,8)) == F(225,2048) < F(45,256)

for number, matching in enumerate(matchings,1):
    cross = {}
    forced_sign = {}
    for i,j in combinations(range(4),2):
        contacts = [(s,t) for s,u in enumerate(matching[i])
                   for t,v in enumerate(matching[j])
                   if frozenset((u,v)) in edges]
        cross[i,j] = contacts
        if contacts:
            signs = {-(1-2*s)*(1-2*t) for s,t in contacts}
            assert len(signs)==1
            forced_sign[i,j] = signs.pop()
    switches = [eps for eps in product((-1,1),repeat=4)
                if all(sign == -eps[i]*eps[j]
                       for (i,j),sign in forced_sign.items())]
    assert switches, (number,'no switching')
    count = sorted(len(v) for v in cross.values())
    assert count == ([0,1,1,1,1,2] if number!=2 else [1]*6)
    if number!=2:
        diag = next(k for k,v in cross.items() if len(v)==2)
        zero = next(k for k,v in cross.items() if len(v)==0)
        remaining = set(range(4))-set(diag)
        assert set(zero)==remaining
        for k1 in [k for k,v in cross.items() if len(v)==1]:
            assert len(set(k1)&remaining)==1
        for k1,k2 in combinations([k for k,v in cross.items() if len(v)==1],2):
            if len(set(k1)&set(k2)&remaining)==1:
                triangle = (diag,k1,k2)
                assert len(set().union(*map(set,triangle)))==3
                assert forced_sign[diag]*forced_sign[k1]*forced_sign[k2] == -1
    print('P%d: contacts=%s, switching=%s' % (number,count,switches[0]))
print('Exact rational bounds: diagonal-only',f(F(1,4)))
print('diagonal + one cap',f(F(3,16))+f(F(1,8)))
print('diagonal + two cap',F(7867,55296))
print('uniform P1/P3',F(45,256),'P2',F(225,2048))
print('harmonic-positive caps P1/P3',F(215,1024),'P2',F(9,64))
print('PASS')
