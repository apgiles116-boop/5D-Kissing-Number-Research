"""Exact SymPy regression for Type-E frame/mixing coercivity.
Universal validity follows from the polynomial identity in the companion note.
This test does not construct a Type-E spherical code.
"""
import sympy as sp

n = 20
I = sp.eye(5)
e = [I[:, k] for k in range(5)]
m = [sp.Rational(1, 10)*e[i % 5] for i in range(n)]
z = [sp.sqrt(99)/10*e[(i + 1) % 5] for i in range(n)]
dot = lambda x, y: (x.T*y)[0]
a = [dot(x, x) for x in m]
r = [dot(x, x) for x in z]
assert all(sp.simplify(a[i]+r[i]-1) == 0 and dot(m[i],z[i]) == 0 for i in range(n))
A = sum(a)
U = sum(x*x for x in a)
R2 = sum(x*x for x in r)
C = range(4)
K = {(i,j) for i in C for j in C if i < j}
R = [(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in K]
assert len(K) == 6 and len(R) == 184

Fw = sum((r[i]*z[i]*z[i].T for i in range(n)), sp.zeros(5))
Fz = sum((z[i]*z[i].T for i in range(n)), sp.zeros(5))
E = Fw-R2/sp.Integer(5)*I
W = sp.trace(E*E)
B = sum((a[i]*m[i]*m[i].T for i in range(n)), sp.zeros(5))
B0 = B-U/sp.Integer(5)*I
Uc = sum(a[i]**2 for i in C)
T = sp.simplify(sum((1-r[i]*r[j])*(dot(m[i],z[j])**2+dot(z[i],m[j])**2) for i,j in R))
J1 = sp.simplify(sum(((1-r[i]*r[j])-a[i])*dot(m[i],z[j])**2
                    +((1-r[i]*r[j])-a[j])*dot(z[i],m[j])**2 for i,j in R))
J2 = sp.simplify(sp.trace(B*(Fz-Fw)))
J3 = sp.simplify(3*Uc-sum(a[i]*dot(m[i],z[j])**2
                            +a[j]*dot(z[i],m[j])**2 for i,j in K))
LHS = sp.Rational(5,24)*W+T/4
RHS = (U*R2/20-sp.Rational(3,4)*Uc
       -sp.Rational(3,40)*sp.trace(B0*B0)
       +sp.Rational(5,24)*sp.trace((E+sp.Rational(3,5)*B0)**2)
       +(J1+J2+J3)/4)
assert sp.simplify(LHS-RHS) == 0
assert J1 >= 0 and J2 >= 0 and J3 >= 0
assert LHS >= U*(sp.Rational(1,4)-A/10-U/100)
Amax = sp.Rational(383,504)
c = sp.Rational(1,4)-Amax/10-Amax/400
assert c == sp.Rational(34697,201600)
assert A <= Amax and all(x <= sp.Rational(1,4) for x in a)
assert LHS >= c*U
print("PASS: exact frame/mixing identity and coercivity")
print("A =",A,"U =",U,"W =",W,"T_R =",T,"c =",c)
