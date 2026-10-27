"""Exact Type-E four-core active-graph spectral certificate (SymPy)."""
import itertools
import sympy as S

edges=list(itertools.combinations(range(4),2))
rho={0:S.Integer(0),1:S.Integer(1),2:S.sqrt(2),
     3:S.sqrt(3),4:S.Integer(2),
     5:(S.sqrt(17)-1)/2,6:S.Integer(1)}

# All 64 labelled four-vertex graphs. A+rho[k]I must be PSD.
# Verify every principal minor symbolically, and sharpness by determinant zero.
count={k:0 for k in range(7)}
sharp={k:False for k in range(7)}
for mask in range(64):
    A=S.zeros(4)
    for h,(i,j) in enumerate(edges):
        if mask&(1<<h):
            A[i,j]=A[j,i]=1
    k=mask.bit_count()
    B=A+rho[k]*S.eye(4)
    for d in range(1,5):
        for ix in itertools.combinations(range(4),d):
            det=S.simplify(B.extract(ix,ix).det())
            assert det.is_nonnegative is True,(mask,k,ix,det)
    count[k]+=1
    if S.simplify(B.det())==0:
        sharp[k]=True
assert count=={0:1,1:6,2:15,3:20,4:15,5:6,6:1}
assert all(sharp.values())

Amax=S.Rational(383,504)
dbar=Amax/12
corrbar=S.Rational(1,2)+dbar
assert dbar==S.Rational(383,6048)
assert corrbar==S.Rational(3407,6048)

# Earlier exact rational D5 flex: all six projected core defects equal.
flexcorr=S.Rational(491137,821762)
flexd=S.simplify(flexcorr-S.Rational(1,2))
assert flexd==S.Rational(40128,410881)
assert 12*flexd>Amax

# Six-active convex fixed quartic cap versus the earlier all-pattern cap.
f=lambda d:(S.Rational(1,2)+d)**2*(d+d*d)
P6=S.factor(f(S.Rational(1,4))+f(Amax/2-S.Rational(1,4)))
assert P6==S.Rational(241638909745,1032386052096)
D0=S.Rational(1780062775,4032758016)
Pold=S.factor(f(S.Rational(1,4))+f(D0-S.Rational(1,4)))
assert P6<Pold

# Sharpness of the k=4 coefficient for unconstrained midpoint vectors:
# two +t and two -t vectors have four negative cross-pairs.
t=S.symbols('t',positive=True)
M=[S.Matrix([t,0,0,0,0]),S.Matrix([t,0,0,0,0]),
   S.Matrix([-t,0,0,0,0]),S.Matrix([-t,0,0,0,0])]
Acore=sum((v.dot(v) for v in M),S.Integer(0))
negative=sum((S.Max(0,-M[i].dot(M[j])) for i,j in edges),S.Integer(0))
assert S.simplify(negative-Acore)==0

print('PASS: 64 exact PSD graph checks and all sharp coefficients')
print('rho:',rho)
print('six-active mean excess bound:',dbar,'~',float(dbar))
print('six-active common correlation bound:',corrbar)
print('flex minimum Acore:',12*flexd,'~',float(12*flexd))
print('six-active quartic bound:',P6,'~',float(P6))
print('prior all-pattern quartic bound:',Pold,'~',float(Pold))
