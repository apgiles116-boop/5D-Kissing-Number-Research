#!/usr/bin/env python3
"""Exact Fraction audit of the 21-line six-exception rank-slack theorem."""
from fractions import Fraction as F
from itertools import combinations

B = F(383,504)
c0 = F(64,625)
target = F(4833,100000)
assert F(9*(21-14),32) == F(63,32)
assert F(9*(17-14),32) == F(27,32)
assert F(49,18) + F(1,9) == F(17,6)
assert F(9,4) - F(49,324) == F(170,81)
assert F(63,32) - F(6,16) == F(51,32)

def f17(t):
    return (1-t)**2*(F(27,32)-F(361,648)*t-F(49,324)*t*t)

def g21(c):
    return (1-B)**2*(F(51,32)-F(17,24)*B-F(49,324)*B*B
                     -F(170,81)*(c/F(2)+c*c))

large_core = f17(B-c0)
small_core = g21(c0)
assert large_core > target and small_core > target
assert large_core == F(22025252761259802036053,455710657500000000000000)
assert small_core == F(11278777913463577,233323856640000000)
print("B:",B,"core split:",c0)
print("large-core bound:",large_core,"margin:",large_core-target)
print("small-core bound:",small_core,"margin:",small_core-target)
print("UNIFORM H204 >",target,"=",float(target))

# Verify all three F3 perfect matchings and their safe parity channels.
E={tuple(sorted(e)) for e in [
    (0,2),(0,4),(0,5),(1,4),(1,7),
    (2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[
    [(0,2),(1,4),(3,6),(5,7)],
    [(0,4),(1,7),(2,3),(5,6)],
    [(0,5),(1,4),(2,7),(3,6)]
]
counts=[]
for M in matchings:
    M=[tuple(sorted(e)) for e in M]
    assert len(set(sum((list(e) for e in M),[])))==8
    assert all(e in E for e in M)
    bad=0
    multiplicities=[]
    for edge1,edge2 in combinations(M,2):
        parities=[]
        for s,v in enumerate(edge1):
            for t,w in enumerate(edge2):
                if tuple(sorted((v,w))) in E:
                    parities.append((s+t)%2)
        assert len(set(parities))<=1
        bad+=bool(parities)
        multiplicities.append(len(parities))
    counts.append(bad)
    assert sorted(multiplicities) in ([0,1,1,1,1,2],[1,1,1,1,1,1])
assert counts==[5,6,5]
print("F3 bad parity channel counts:",counts)

# Sharp scalar exceptional normalized positive defect coefficient 3/2.
a=b=F(1,4)
w=(1-a)*(1-b)
d=F(3,4)
delta=d*d/w-F(1,4)
assert delta==F(3,4)==F(3,2)*(a+b)
print("Sharp exceptional coefficient: 3/2")
print("PASS")
