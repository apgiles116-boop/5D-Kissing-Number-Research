"""Exact rational audit of the canonical Type-E safe-correlation threshold profile."""
from fractions import Fraction as F

Q0=F(8790283,317520)
core=F(57,32)
q=Q0-core
assert q==F(16449401,635040)
assert core==F(3,2)+F(1,4)+F(1,32)
expected={F(1,10):101,F(1,5):89,F(1,4):77,
          F(3,10):59,F(1,3):40,F(7,20):27}
for t,n in expected.items():
    r=(q-184*t*t)/(F(1,4)-t*t)
    lower=max(0,(r.numerator+r.denominator-1)//r.denominator)
    assert lower==n and r.denominator!=1
    assert 184*t*t+(n-1)*(F(1,4)-t*t)<q
    print(f"t={t}: N_t >= {n}; rational threshold={r}")
print("EXACT RATIONAL AUDIT PASSED")
