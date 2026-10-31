"""Exact checks for tau5_typeE_center_walsh_normalization_2026-10-31.md.

The continuum and endpoint bounds are analytically proved in the note.
This script independently verifies the algebraic constants and examples.
"""
from itertools import combinations
import sympy as S

h=2/S.sqrt(3)
Cstar=18*S.sqrt(3)-S.Rational(53,2)
assert S.simplify(Cstar-(S.Rational(1,2)+27*(h-1)))==0
assert S.Rational(23,20)<h<S.Rational(7,6)
assert S.simplify(S.Rational(1,4)-S.Rational(3,2)*(h-1))>0
assert S.Rational(41,8)*(S.Rational(100,99)**2)<6
assert S.simplify(S.Rational(4,3)*(S.Rational(1,2)+27*(h-1))-6)>0

def T(masses):
    s=[S.Integer(1)]+[1/S.sqrt(1-S.sympify(a)) for a in masses]
    return S.simplify(sum((s[i]*s[j]-1)/2
             for i,j in combinations(range(len(s)),2)))

for k in (1,2,3):
    masses=[S.Rational(1,4)]*k+[S.Integer(0)]*(20-k)
    Tk=(S.binomial(k,2)*(h*h-1)+k*(21-k)*(h-1))/2
    assert S.simplify(T(masses)-Tk)==0
    assert S.simplify(Cstar-S.Rational(3,4)*Tk/(S.Rational(k,4)))>=0

r=S.Rational(5,504)
Tend=T([S.Rational(1,4)]*3+[r]+[0]*16)
assert S.N(S.Rational(3,4)*Tend/S.Rational(383,504),30)<S.N(Cstar,30)

# Representative exact safe Walsh equality examples.
for a,b,c in [(S.Rational(1,4),S.Rational(1,4),S.Integer(0)),
              (S.Rational(1,4),S.Rational(1,4),S.Rational(1,8)),
              (S.Rational(1,16),S.Rational(1,4),S.Rational(1,32))]:
    lam=S.sqrt((1-a)*(1-b));kap=(1-lam)/2;q=S.Rational(1,2)-c
    lhs=max(S.Integer(0),S.N(q/lam-S.Rational(1,2),30))
    rhs=max(S.Integer(0),S.N((kap-c)/lam,30))
    assert abs(lhs-rhs)<S.Float('1e-25')

# Cauchy-Schwarz squared residual is exactly (a-b)^2.
a,b=S.symbols('a b',real=True)
assert S.expand((a+b-2*a*b)**2-4*a*b*(1-a)*(1-b)-(a-b)**2)==0

print('PASS: exact constants, capped-mass extremizers, Walsh examples.')
print('C_* =',S.N(Cstar,18))
print('last-interval ratio =',S.N(S.Rational(3,4)*Tend/S.Rational(383,504),18))
print('STATUS: Type E open; global proved 40 <= tau_5 <= 44.')
