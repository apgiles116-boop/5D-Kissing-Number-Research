"""Exact symbolic and 220-case D5 deletion verification.

The universally quantified inequalities are proved in the companion note;
this checker verifies the polynomial identities and finite spectral certificate.
"""
import itertools
from collections import Counter
import sympy as s

A, Ac, sc, Sraw, sumasq = s.symbols("A Ac sc Sraw sumasq", real=True)
B=s.Rational(383,504)
assert 1-B/5==s.Rational(2137,2520)
assert s.expand((20-A)*A/5-(3*Ac-Ac**2+sc) -
    (A*(1-A/5)+3*(A-Ac)+Ac**2-sc))==0
assert s.expand((20-2*A+sumasq+2*Sraw)-(20-A)**2/5 -
    (2*Sraw-60+6*A-A**2/5+sumasq))==0

V=[]
for i in range(5):
    for j in range(i+1,5):
        for sign in (1,-1):
            w=s.zeros(5,1); w[i]=1; w[j]=sign
            V.append(w/s.sqrt(2))
root=V[0]
N=[j for j in range(20) if j!=0 and
   abs((root.T*V[j])[0])==s.Rational(1,2)]
assert len(N)==12
S0=sum((V[j]*V[j].T for j in N),s.zeros(5))
assert S0==s.diag(3,3,2,2,2)
x=s.symbols("x")
expected={
s.expand((x-2)*(2*x*x-8*x+7)*(2*x*x-6*x+3)/4):96,
s.expand((x-1)*(2*x-5)*(2*x-3)*(2*x*x-8*x+7)/8):48,
s.expand((x-3)*(x-2)**2*(x-1)**2):24,
s.expand((x-2)**2*(x-1)*(2*x*x-8*x+7)/2):24,
s.expand((x-3)*(2*x-3)**2*(2*x*x-6*x+3)/8):16,
s.expand((x-2)**3*(x*x-3*x+1)):12}
assert len(expected)==6
observed=Counter()
for D in itertools.combinations(N,3):
    S=S0-sum((V[j]*V[j].T for j in D),s.zeros(5))
    observed[s.expand(S.charpoly(x).as_expr())]+=1
assert observed==Counter(expected)
assert sum(observed.values())==220
gamma=(3-s.sqrt(5))/2
assert gamma>0
assert (3-s.sqrt(3))/2>gamma
assert 2-s.sqrt(2)/2>gamma
assert s.Rational(1)>gamma
assert s.simplify(4/(3*gamma)-2*(3+s.sqrt(5))/3)==0
print("PASS: mixed-frame identities and all 220 exact D5 deletion spectra")
print("gamma =", gamma, "~", float(gamma))
print("polynomial multiplicities =", sorted(observed.values()))
