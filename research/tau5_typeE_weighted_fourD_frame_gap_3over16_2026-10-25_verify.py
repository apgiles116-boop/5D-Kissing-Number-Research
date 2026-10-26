"""Exact symbolic checks for the Type-E outside-sixteen frame gap 3/16.

The written proof supplies the global majorization, monotonicity and
Gegenbauer-positive-definiteness arguments. These checks verify algebra
and rational certificates, not an independent global optimization.
"""
from sympy import Matrix, diag, Rational as Q, symbols, expand, factor, diff, simplify

t = symbols("t")
assert expand(Q(1,16)+Q(1,8)*(4*t*t-1)
              +Q(1,16)*(16*t**4-12*t*t+1)) == t**4-t*t/4
print("PASS: weighted S^3 Gegenbauer polynomial")

r = Q(383,504)-Q(3,4)
a = Q(1,4)
assert r == Q(5,504)
K = Matrix([[2*a,(a+r)/2,12*a/2],
            [3*(a+r)/2,0,12*r/2],
            [3*a/2,r/2,0]])
D = diag(3,1,12)
assert D*K == K.T*D
S = D*(Q(27,25)*Matrix.eye(3)-K)
minors = [factor(S[:k,:k].det()) for k in (1,2,3)]
assert minors == [Q(87,50), Q(121870727,70560000),
                  Q(22005127,73500000)]
assert all(v > 0 for v in minors)
print("PASS: 3x3 rational spectral certificate", minors)

p,c,dlt = symbols("p c dlt")
expr = (Q(1,2)+p)**4-(c-dlt)*(Q(1,2)+p)**2/4
rhs = (1-c)/16+dlt/16+(Q(1,2)-c/4)*p+dlt*p/4
rhs += (Q(3,2)-c/4)*p**2+dlt*p**2/4+2*p**3+p**4
assert expand(expr-rhs) == 0
print("PASS: pairwise quartic expansion")

A,S2,S3,S4 = symbols("A S2 S3 S4")
C1,C2,C4 = 16-A,16-2*A+S2,16-4*A+6*S2-4*S3+S4
Dexpr = C2**2/32-Q(3,8)*C4-(120-(C1**2-C2)/2)/16
Dtarget = (64-46*A+5*A**2-4*A*S2-41*S2+S2**2+48*S3-12*S4)/32
assert simplify(Dexpr-Dtarget) == 0

ai,aj = symbols("ai aj")
partial = lambda u: (diff(Dtarget,A)+2*u*diff(Dtarget,S2)
                     +3*u*u*diff(Dtarget,S3)+4*u**3*diff(Dtarget,S4))
quotient = factor((partial(ai)-partial(aj))/(ai-aj))
claim = (-8*A+4*S2-82+144*(ai+aj)
         -48*(ai**2+ai*aj+aj**2))/32
assert simplify(quotient-claim) == 0
print("PASS: deficit polynomial and Schur-concavity identity")

aa = [Q(1,4)]*3+[Q(5,504)]+[Q(0)]*12
subs = {A:sum(aa),S2:sum(x**2 for x in aa),
        S3:sum(x**3 for x in aa),S4:sum(x**4 for x in aa)}
Dmin = Dtarget.subs(subs)
assert Dmin == Q(1665618603949,2064772104192)
B = symbols("B")
C = Q(15,16)+Q(15,8)+Q(27,100)+Q(8,9)
assert C == Q(14297,3600)
upper = C*B+Q(3,2)*B**2+Q(3,4)*B**3+B**4/8
assert upper.subs(B,Q(3,16)) == Q(31554331,39321600)
margin = Dmin-upper.subs(B,Q(3,16))
assert margin == Q(870478520203,206477210419200) and margin>0
print("PASS: exact positive contradiction margin", margin)
print("PROVED with analytic lemmas: F_O strictly exceeds (3/16) I_5")
print("TYPE E conditional: H_184 > (3/32) A for A>0")
