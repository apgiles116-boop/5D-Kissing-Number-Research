"""Exact F3 double-matching Walsh/SOS verification; Python 3 + SymPy."""
from itertools import product
from sympy import symbols, expand, Rational, simplify
F3={tuple(sorted(e)) for e in ((0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7))}
def matchings(V):
    if not V:
        yield ()
        return
    a=V[0]
    for b in V[1:]:
        if tuple(sorted((a,b))) in F3:
            for P in matchings(tuple(x for x in V if x not in (a,b))):
                yield ((a,b),)+P
M=list(matchings(tuple(range(8))))
assert len(M)==3
for P in M:
    idx={v:(i,1 if k==0 else -1) for i,p in enumerate(P) for k,v in enumerate(p)}
    cross=[]; count=[[0]*4 for _ in range(4)]
    for a,b in F3:
        i,si=idx[a]; j,sj=idx[b]
        if i==j: continue
        cross.append((i,j,si,sj));count[i][j]+=1;count[j][i]+=1
    assert len(cross)==6
    pattern=sorted(count[i][j] for i in range(4) for j in range(i+1,4))
    if pattern==[1]*6: continue
    assert pattern==[0,1,1,1,1,2]
    h=next((i,j) for i in range(4) for j in range(i+1,4) if count[i][j]==2)
    l=next((i,j) for i in range(4) for j in range(i+1,4) if count[i][j]==0)
    etas=[e for e in product((-1,1),repeat=4)
          if all(si*sj==e[i]*e[j] for i,j,si,sj in cross)]
    assert len(etas)==2
    eta=next(e for e in etas if any(
        ((i==h[0] and j==l[0] and si==e[i]) or
         (j==h[0] and i==l[0] and sj==e[j]))
        for i,j,si,sj in cross))
    signs={}
    for i,j,si,sj in cross:
        t=si//eta[i]
        assert t==sj//eta[j]
        signs.setdefault(tuple(sorted((i,j))),[]).append(t)
    assert sorted(signs[tuple(sorted(h))])==[-1,1]
    assert [signs[tuple(sorted((i,j)))][0]
            for i,j in ((h[0],l[0]),(h[0],l[1]),(h[1],l[0]),(h[1],l[1]))]==[1,-1,-1,1]
k={(i,j):symbols(f'k{i}{j}') for i in range(4) for j in range(i+1,4)}
c={(i,j):symbols(f'c{i}{j}') for i in range(4) for j in range(i+1,4)}
def K(i,j): return 1 if i==j else k[tuple(sorted((i,j)))]
def C(i,j): return c[tuple(sorted((i,j)))]
B=2*K(0,3)+K(0,1)+K(0,2)+K(3,1)+K(3,2)
T=C(0,1)-C(0,2)-C(3,1)+C(3,2)
R=3+B
H2=2+2*K(0,3)+K(0,1)+K(0,2)+K(3,1)+K(3,2)+(2+2*K(1,2))/4
assert expand(R-H2-(1-K(1,2))/2)==0
q=symbols('q',nonnegative=True)
Delta=-R-T
rho=Rational(1,2)-K(1,2)-q
assert expand(-T-Rational(1,4)-q/2-H2-rho/2-Delta)==0
t=symbols('t',positive=True)
assert simplify((t*t/(32*(t+3))).diff(t)-t*(t+6)/(32*(t+3)**2))==0
assert (t*t/(32*(t+3))).subs(t,1)==Rational(1,128)
print('PASS: 3 F3 matchings; 2 double patterns; formal SOS; energy corollary')
