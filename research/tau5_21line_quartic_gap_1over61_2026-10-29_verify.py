"""Exact SymPy rational/surd verifier for universal 21-line quartic gap P>1/61.
Mathematical proof: tau5_21line_quartic_gap_1over61_2026-10-29.md
"""
import sympy as s

t=s.symbols("t")
P2=(5*t*t-1)/4
P4=(21*t**4-14*t*t+1)/8
assert s.expand(t**4-t*t/4-(s.Rational(1,28)+P2/3+s.Rational(8,21)*P4))==0

P=s.Rational(1,61)
Vmax=s.Rational(24,5)*P
Vstar=s.Rational(9,2440)
assert Vstar==s.Rational(24,5)*(P-s.Rational(1,64))
assert P<s.Rational(1,32)
assert Vmax<s.Rational(1,10)
assert 2*(4*P+s.Rational(1,4))<s.Rational(7,10)
assert s.Rational(4,5)-Vmax>s.Rational(7,10)

def G(E):
    assert 0<=E<s.Rational(1,32)
    if E<=s.Rational(1,64):
        return s.Rational(1,8)-s.sqrt(s.Rational(1,64)-E)
    return s.Rational(1,4)-s.sqrt(s.Rational(1,32)-E)

def L(V):
    assert 0<=V<=Vmax
    return 4*P+G(P-s.Rational(5,24)*V)

H={134:s.Rational(91,400),135:s.Rational(63,400)}
threshold={134:s.Rational(31,1000),135:s.Rational(37,2500)}

for K in (134,135):
    v=threshold[K]
    assert 0<Vstar<v<Vmax
    for V in (s.Rational(0),Vstar,v):
        gap=s.simplify(H[K]-(s.Rational(24,5)+4*P)*V-s.Rational(3,5)*L(V))
        assert gap.is_positive is True,(K,V,gap)
    agap=s.simplify(v+s.Rational(1,5)-2*L(v)) if K==134 else s.simplify(s.Rational(3,10)-v-2*L(v))
    assert agap.is_positive is True,(K,agap)

assert 2500*3100935-88007**2==7105451>0
assert s.Rational(81,256)*P==s.Rational(81,15616)
assert s.Rational(81,256)*s.Rational(320,81)==s.Rational(5,4)
assert s.Rational(81,256)*s.Rational(16,9)==s.Rational(9,16)

def huber(c):
    lam=s.Rational(3,10)
    return c*c if abs(c)<=lam/2 else lam*abs(c)-lam*lam/4
c12=s.Rational(12,4)-s.Rational(16,5)
c13=s.Rational(13,4)-s.Rational(16,5)
assert 5*huber(c12)+16*huber(c13)==H[134]
assert 3*huber(c12)+18*huber(c13)==H[135]
print("PASS: exact universal P>1/61 certificate, eight strict surd inequalities")
