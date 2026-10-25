"""Exact identity and witness checks for the 2026-10-25 Type-E singleton midpoint-sum note.

Universal inequalities are proved in the companion note by Cauchy--Schwarz.
This verifier checks the key polynomial identity, the exact PSD witness,
the contact pattern, the zero-contact Walsh identity, and rational bounds.
"""
from fractions import Fraction
import sympy as s

t, d, a, c, r, p, q = s.symbols("t d a c r p q", real=True)
assert s.expand((t-2*d)*(1-t-2*d)-4*d*d - (t*(1-t)-2*d)) == 0
assert s.simplify((a+s.Rational(1,4))*(s.Rational(3,4)-a)/2 -
                  (s.Rational(3,32)+a/4-a*a/2)) == 0

B=Fraction(383,504)
C=B/2-B*B/4
assert C==Fraction(239375,1016064) and C<B/2

G=s.Matrix([[4,0,-3,-3],[0,28,3,19],[-3,3,4,0],[-3,19,0,28]])/32
assert G==G.T and G.det()==0
assert G.eigenvals()=={
    s.Integer(0):1,
    s.Rational(5,16):1,
    (27-s.sqrt(409))/32:1,
    (27+s.sqrt(409))/32:1,
}
assert 27**2>409
assert G[0,1]==0 and G[2,3]==0
assert G[0,0]==G[2,2]==s.Rational(1,8)
assert G[1,1]==G[3,3]==s.Rational(7,8)

# Endpoints i+,i-,j+,j- expressed in basis m_i,z_i,m_j,z_j.
E=s.Matrix([[1,1,0,0],[1,-1,0,0],[0,0,1,1],[0,0,1,-1]])
H=E*G*E.T
assert all(H[k,k]==1 for k in range(4))
assert H[0,1]==H[2,3]==-s.Rational(3,4)
cross=sorted(H[i,j] for i in (0,1) for j in (2,3))
assert cross==[-s.Rational(7,8),-s.Rational(1,2),
               s.Rational(1,2),s.Rational(1,2)]
assert all(H[i,j]<=s.Rational(1,2)
           for i in range(4) for j in range(i+1,4))
assert 2*s.Rational(3,32)==s.Rational(1,4)*(1-s.Rational(1,4))

cross_form=[c+r+p+q,c+r-p-q,c-r+p-q,c-r-p+q]
assert s.expand(sum(x*x for x in cross_form)-
                4*(c*c+r*r+p*p+q*q))==0
assert s.simplify(((p+q)**2+(p-q)**2)/2-(p*p+q*q))==0

print("PASS: exact singleton polynomial, rank-3 Gram witness,")
print("      endpoint kissing/deep pattern, Walsh identity, disjoint rational cap.")
print("Disjoint singleton cap:",C,"=",float(C))
print("Witness cross dots:",cross)
