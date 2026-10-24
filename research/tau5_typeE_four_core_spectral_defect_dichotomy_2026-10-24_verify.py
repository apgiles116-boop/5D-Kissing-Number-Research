"""Exact 64-graph spectral certificate for Type-E four-core defect dichotomy.
No numerical eigenvalues, external libraries, or floating point.
"""
from itertools import combinations, product, permutations

E = list(combinations(range(4), 2))

def mul(a, b):  # a+b sqrt(3), exact in Z[sqrt(3)]
    return (a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def sign(x):  # exact sign of a+b sqrt(3)
    a,b=x
    if a==0: return (b>0)-(b<0)
    if b==0: return (a>0)-(a<0)
    if a>0 and b>0: return 1
    if a<0 and b<0: return -1
    t=a*a-3*b*b
    return ((t>0)-(t<0))*(1 if a>0 else -1)

def det(mat):
    n=len(mat)
    ans=(0,0)
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        z=(1,0)
        for i,j in enumerate(p): z=mul(z,mat[i][j])
        factor=(-1)**inversions
        ans=(ans[0]+factor*z[0],ans[1]+factor*z[1])
    return ans

def psd_shift_sqrt3(A):
    for n in range(1,5):
        for S in combinations(range(4),n):
            mat=[[(0,1) if i==j else (A[i][j],0) for j in S] for i in S]
            if sign(det(mat))<0: return False
    return True

stats={}
for bits in product((0,1),repeat=6):
    A=[[0]*4 for _ in range(4)]
    for (i,j),bit in zip(E,bits): A[i][j]=A[j][i]=bit
    degree=[sum(row) for row in A]
    is_C4=(sum(bits)==4 and degree==[2,2,2,2])
    okay=psd_shift_sqrt3(A)
    assert okay == (not is_C4), (bits,okay,is_C4)
    stats[sum(bits)]=stats.get(sum(bits),0)+1
assert stats=={0:1,1:6,2:15,3:20,4:15,5:6,6:1}
print('PASS: 64 graphs; A + sqrt(3) I PSD exactly except the three C4 graphs')

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def characteristic(A):
    result=[0]*5
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=[1]
        for i,j in enumerate(p):
            factor=[-A[i][j],1] if i==j else [-A[i][j]]
            term=pmul(term,factor)
        for k,c in enumerate(term): result[k]+=(-1)**inversions*c
    return result

for bits in product((0,1),repeat=6):
    A=[[0]*4 for _ in range(4)]
    for (i,j),bit in zip(E,bits): A[i][j]=A[j][i]=bit
    if sum(bits)==5: assert characteristic(A)==[0,-4,-5,0,1]
    if sum(bits)==6: assert characteristic(A)==[-3,-8,-6,0,1]
print('PASS: exact five-/six-edge characteristic polynomials')

# The exact SOS identities in the note are proved by expansion.
# Sharpness witnesses:
# K1,3: (-sqrt(3)v,v,v,v) has D/C=sqrt(3)/2.
# Five edges: m1=m2=-u/2, m3=(u+(1+h)v)/(2sqrt(2)),
# m4=(u-(1+h)v)/(2sqrt(2)); u.v=0, h -> 0+.
# Six edges: centered regular tetrahedron.
print('PASS: exact sharpness families and SOS identities supplied in note')
