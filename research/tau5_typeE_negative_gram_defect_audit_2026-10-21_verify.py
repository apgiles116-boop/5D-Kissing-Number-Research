"""Exact rational verifier for Type E negative-Gram defect audit (2026-10-21).
The dimension-free Gram inequality is proved analytically in the companion note.
"""
from sympy import Rational as Q, symbols, simplify
Dstar=Q(1780062775,4032758016)
R0=Q(56719845779369,2000000000000)
Ccap=Q(557185,1000000)
A=Q(566926,1000000)
A2=Q(128271,1000000)
V=Q(926958807369,5000000000000)
D=lambda a:196*a-644*a*a+896*a**3-448*a**4
assert D(Q(57185,1000000))>Q(28,3)-Q(35,512)
assert R0==30-3*A+A*A/10-A2/2+V/2
t=symbols('t')
assert simplify((1-t)/2-t*t-(1+t)*(1-2*t)/2)==0
L=R0-Q(3,2)-Dstar-Ccap*Ccap/4
assert L==Q(1659789202653287342993,63011844000000000000)
assert L-Q(421,16)==Q(1790057403287342993,63011844000000000000)
threshold=Q(63,500)
assert L-(25+84*threshold*threshold)==Q(461515684391342993,63011844000000000000)
print("PASS: exact rational brackets, safe floor, 1/8 and 63/500 census")
print("R_safe >",L,"=",float(L))
