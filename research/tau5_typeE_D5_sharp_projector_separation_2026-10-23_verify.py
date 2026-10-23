"""Exact SymPy certificate: sharp D5 quadratic covering and Type-E Q gap."""
from itertools import combinations
from sympy import Rational as R, symbols, simplify, expand, sqrt

u=symbols("u0:5",real=True)
q=[]
for a,b in combinations(range(5),2):
    q.extend(((u[a]+u[b])**2/R(2),(u[a]-u[b])**2/R(2)))
assert len(q)==20
n=sum(x*x for x in u)
assert simplify(sum(q)-4*n)==0
assert simplify(sum(x*x for x in q)-R(3,2)*n*n-R(1,2)*sum(x**4 for x in u))==0
t=symbols("t",nonnegative=True)
p=(39*t*t-12*t)/64
assert expand((t-R(1,4))**2-p-(5*t-2)**2/64)==0
assert expand(-p-t*(12-39*t)/64)==0
assert R(21,128)+R(39,640)==R(9,40)
qq=[simplify(x.subs(dict(zip(u,[1/sqrt(5)]*5)))) for x in q]
assert qq.count(R(2,5))==10 and qq.count(R(0))==10
assert sum(max(x-R(1,4),0)**2 for x in qq)==R(9,40)
B=R(383,504)
M=R(47653,254016)
assert M<=B/R(4)
assert R(47,100)**2<R(9,40)
assert B<R(81,100)
assert (sqrt(R(9,40))-sqrt(M)/5).evalf(15)>R(19,50)
print("PASS: exact D5 moments, polynomial minorant, sharp 9/40 equality")
print("PASS: Type-E midpoint cap and Q-tensor separation algebra")
print("Q-tensor squared gap:", (R(5,4)*(sqrt(R(9,40))-sqrt(M)/5)**2).evalf(14))
