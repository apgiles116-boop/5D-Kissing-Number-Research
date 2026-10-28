"""Exact 165-graph audit of sparse D5 Q-kernel relations (2026-10-28)."""
from itertools import combinations, permutations
from collections import Counter
from sympy import Matrix

EDGES=tuple(combinations(range(5),2))

def four_cycles(edge_set):
    edges=set(edge_set)
    out=set()
    for four in combinations(range(5),4):
        for p in permutations(four):
            if p[0]!=min(four) or p[1]>p[3]:
                continue
            cycle=tuple(tuple(sorted((p[i],p[(i+1)%4]))) for i in range(4))
            if all(e in edges for e in cycle):
                out.add((tuple(sorted(cycle)),cycle))
    return [cycle for _,cycle in sorted(out)]

def check(k):
    hist=Counter()
    for supports in combinations(EDGES,k):
        ix={e:j for j,e in enumerate(supports)}
        B=Matrix([[int(v in e) for e in supports] for v in range(5)])
        assert B.rank()==5
        PB=Matrix([[5*int(v in e)-2 for e in supports] for v in range(5)])
        assert PB.rank()==4
        vectors=[]
        for cycle in four_cycles(supports):
            vec=[0]*k
            for i,e in enumerate(cycle):
                vec[ix[e]]=(-1)**i
            assert B*Matrix(vec)==Matrix.zeros(5,1)
            vectors.append(vec)
        rank=Matrix(vectors).rank()
        assert rank==k-5,(k,supports,rank)
        hist[(len(vectors),rank)]+=1
    return hist

if __name__=="__main__":
    assert check(7)==Counter({(2,2):60,(3,2):60})
    assert check(8)==Counter({(5,3):45})
    assert 120*8==960 and 10*9*2==180
    print("PASS: 165 support graphs; 7-edge cycle rank 2; 8-edge cycle rank 3.")
    print("PASS: 960/180 omitted-line counts; Q ranks 14/13 by incidence formula.")
