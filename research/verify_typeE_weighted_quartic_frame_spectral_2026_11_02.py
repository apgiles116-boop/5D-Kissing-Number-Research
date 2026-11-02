"""Exact rational verifier for weighted quartic Type-E frame certificates.

The accompanying note proves the Jensen, Loewner and Karamata steps.
This checks polynomial identities, rational relaxations, monotonicity,
and the five exact contradiction gaps.
"""
import sympy as s

A,E,D=s.symbols('A E D',nonnegative=True)
A0=s.Rational(383,504)
Dglobal=s.Rational(1780062775,4032758016)
Dpath=s.Rational(366383,1016064)
S2max=s.Rational(3,16)+s.Rational(5,504)**2
assert S2max==s.Rational(47653,254016)
assert (s.Rational(27,10)-A0)**2-20*S2max==s.Rational(75821,6350400)>0
assert s.Rational(576,25)>23
print('PASS: capped mass spectral and joint moment relaxations')

u=s.symbols('u')
P2=(4*u*u-1)/3
P4=(16*u**4-12*u*u+1)/5
assert s.expand(s.Rational(3,8)*u**2*(4*u**2-1)-
    (s.Rational(3,32)+s.Rational(9,16)*P2+s.Rational(15,32)*P4))==0
print('PASS: S3 Gegenbauer identity')

J=s.Rational(27,20)*E+s.Rational(17,5)*E**2+E**3/2
allB=19*A+57*E+s.Rational(19,10)*E**2
coreB=3*A+9*E+2*E**2
pathB=2*A+s.Rational(21,4)*E+E**2
qalt=(3+2*E)**2/16
qsingle=(5+4*E)**2/64
def L(q,coeff,defectB):
    return s.expand(allB/4+(1+E/2)*J+
                    (q-s.Rational(1,4))*defectB+q*coeff*D)
Lalt=L(qalt,5+4*E,coreB)
Lsingle=L(qsingle,s.Rational(9,2)+4*E,coreB)
Lpath=L(qsingle,s.Rational(9,2)+4*E,pathB)
for name,p in [('alt',Lalt),('single',Lsingle),('path',Lpath)]:
    for var in (A,E,D):
        assert all(c>=0 for c in s.Poly(s.diff(p,var),A,E,D).coeffs()),(name,var)
print('PASS: upper polynomial monotonicity')

U0=16+2*s.Rational(3,4)**4+s.Rational(499,504)**4+(s.Rational(3,4)-E)**4
R0=s.expand((20-A0-E)**4/3200-s.Rational(3,2)*U0)
assert s.Rational(18)**3/800>6
cases=[
 ('general-no-global-D',s.Rational(37,200),s.Rational(3,2),Lalt,
  s.Rational(170756865083663731,5040947520000000000)),
 ('general-global-D',s.Rational(297,1000),Dglobal,Lalt,
  s.Rational(232166826351874649779,12602368800000000000000)),
 ('singleton-basic',s.Rational(63,200),s.Rational(3,4),Lsingle,
  s.Rational(65464532636720153,2520473760000000000)),
 ('singleton-global',s.Rational(343,1000),Dglobal,Lsingle,
  s.Rational(102410241566713858021,3150592200000000000000)),
 ('canonical-path',s.Rational(3,8),Dpath,Lpath,
  s.Rational(300860069611,12904825651200)),
]
for name,e0,d0,bound,expected in cases:
    gap=s.factor(R0.subs(E,e0)-bound.subs({A:A0,E:e0,D:d0}))
    assert gap==expected and gap>0,(name,gap,expected)
    print('PASS:',name,'lambda_min >',e0,'gap',gap)
assert s.Rational(13,8)**2-s.Rational(13,8)-1>0
t=s.symbols('t',positive=True)
f=s.sqrt(t*(1-t))
assert s.simplify(s.diff(f,t,2)+1/(4*(t*(1-t))**s.Rational(3,2)))==0
print('PASS: Jensen concavity, path bound, all certificates')
