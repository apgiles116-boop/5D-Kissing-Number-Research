"""Exact SymPy verifier: Type-E variance-aware quartic noncollapse (2026-11-02)."""
import sympy as s

A,E,D,B,U2,U3,U4=s.symbols("A E D B U2 U3 U4", nonnegative=True)
A0=s.Rational(383,504)
Dg=s.Rational(1780062775,4032758016)
Dp=s.Rational(366383,1016064)
F=s.expand((20-2*B+U2)**2/8-s.Rational(3,2)*(20-4*B+6*U2-4*U3+U4))
Fexact=20-4*B+B**2/2-(4+B/2)*U2+U2**2/8+6*U3-s.Rational(3,2)*U4
assert s.expand(F-Fexact)==0
print("PASS: coupled second/fourth moment expansion")

B0=A0+E
q=s.Rational(1,4)+E
C=s.Rational(1,8)+(6-s.Rational(3,2)*q)/B0
R=20-4*B0+B0**2/2-(4+B0/2)**2/(4*C)
assert s.factor(s.diff(C,E))<0
assert B0.subs(E,s.Rational(2149,5000))<4
assert q.subs(E,s.Rational(2149,5000))<4
assert s.simplify(C-(s.Rational(1,8)+(s.Rational(45,8)-s.Rational(3,2)*E)/B0))==0
print("PASS: lower-bound monotonicity prerequisites")

J=s.Rational(27,20)*E+s.Rational(17,5)*E**2+E**3/2
Ball=19*A+57*E+s.Rational(19,10)*E**2
Bcore=3*A+9*E+2*E**2
Bpath=2*A+s.Rational(21,4)*E+E**2
qa=(3+2*E)**2/16
qs=(5+4*E)**2/64
def L(q,coefficient,exceptionB):
    return s.expand(Ball/4+(1+E/2)*J+(q-s.Rational(1,4))*exceptionB+q*coefficient*D)
La=L(qa,5+4*E,Bcore)
Ls=L(qs,s.Rational(9,2)+4*E,Bcore)
Lp=L(qs,s.Rational(9,2)+4*E,Bpath)
for upper in (La,Ls,Lp):
    for v in (A,E,D):
        assert all(c>=0 for c in s.Poly(s.diff(upper,v),A,E,D).coeffs())
print("PASS: retained upper polynomial monotonicity")

cases=[
("general-coarse",s.Rational(213,1000),s.Rational(3,2),La,
 s.Rational(2068181855076531043,344643516000000000000)),
("general-global",s.Rational(843,2500),Dg,La,
 s.Rational(11637056493033844209773651,3622627761942656250000000000)),
("singleton-coarse",s.Rational(179,500),s.Rational(3,4),Ls,
 s.Rational(38581113578514221,41497800750000000000)),
("singleton-global",s.Rational(3901,10000),Dg,Ls,
 s.Rational(347727676502590567436420711,149315820383520000000000000000)),
("canonical-path",s.Rational(2149,5000),Dp,Lp,
 s.Rational(84433297068480293813057,256498966710000000000000000))
]
for name,e0,d0,upper,expected in cases:
    gap=s.factor(R.subs(E,e0)-upper.subs({A:A0,E:e0,D:d0}))
    assert gap==expected and gap>0,(name,gap,expected)
    print("PASS:",name,"lambda_min >",e0,"gap",gap)

u=s.symbols("u")
P2=(4*u**2-1)/3
P4=(16*u**4-12*u**2+1)/5
assert s.expand(s.Rational(3,8)*u**2*(4*u**2-1)-
 (s.Rational(3,32)+s.Rational(9,16)*P2+s.Rational(15,32)*P4))==0
print("PASS: S^3 Gegenbauer identity")
