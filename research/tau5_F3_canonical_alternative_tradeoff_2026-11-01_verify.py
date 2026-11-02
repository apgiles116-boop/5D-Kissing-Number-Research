"""Exact SymPy regression: sharp F3 canonical/alternative matching tradeoff.
Only standalone algebra and rational brackets are verified here; upstream
Type-E scalar/harmonic theorems are retained, not independently re-proved.
"""
import sympy as s

t, lam, y = s.symbols("t lambda y", positive=True)
H = s.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
assert H*H.T == s.eye(4)

# Weighted adjacency and its four 2x2 Hadamard PSD blocks.
A=[0,2,5,7]; B=[4,3,6,1]
P0=[(0,4),(1,7),(2,3),(5,6)]
P1=[(0,2),(1,4),(3,6),(5,7)]
P2=[(0,5),(1,4),(2,7),(3,6)]
locA={u:i for i,u in enumerate(A)}
locB={u:i for i,u in enumerate(B)}
AA=s.zeros(4); BB=s.zeros(4); AB=s.zeros(4)
for matching,weight in [(P0,lam),(P1,s.Integer(1)),(P2,s.Integer(1))]:
    for i,j in matching:
        if i in locA and j in locA:
            AA[locA[i],locA[j]]+=weight
            AA[locA[j],locA[i]]+=weight
        elif i in locB and j in locB:
            BB[locB[i],locB[j]]+=weight
            BB[locB[j],locB[i]]+=weight
        else:
            ia=locA[i] if i in locA else locA[j]
            ib=locB[i] if i in locB else locB[j]
            AB[ia,ib]+=weight
assert AB==lam*s.eye(4)
assert H*AA*H.T==s.diag(2,0,0,-2)
assert H*BB*H.T==s.diag(2,-2,-2,2)
for ec,ej,det in [(2,1,4*(y+4)),(0,-1,0),(0,-1,0),(-2,1,0)]:
    K=s.Matrix([[ec+(y+4)/2,lam],[lam,2*ej+y+2]])
    assert s.factor(K.det().subs(lam**2,y*(y+4)/2)-det)==0
    assert K[0,0].subs(y,s.Rational(1,2))>0
    assert K[1,1].subs(y,s.Rational(1,2))>0

# Rational parameterization and symbolic Gram orbit correlations.
v=4*t**2*(4-t**2)/(4-t**4)
w=4-v
yt=4*t**2/(2-t**2)
lt=4*t/(2-t**2)
assert s.factor(yt*(yt+4)-2*lt**2)==0
assert s.factor(v/t**2+t**2*w/4-4)==0
q={
    "A_cycle":-w/4,
    "A_opposite":(w-v)/4,
    "B_opposite":(-v/t**2+t**2*w/4)/4,
    "B_other":-t**2*w/16,
    "AB_matched":-(v/t+t*w/2)/4,
    "AB_cycle":t*w/8,
    "AB_opposite":v/(4*t)-t*w/8
}
want={
    "A_cycle":-4*(1-t**2)/(4-t**4),
    "A_opposite":1-v/2,
    "B_opposite":-(t**4-2*t**2+4)/(4-t**4),
    "B_other":-t**2*(1-t**2)/(4-t**4),
    "AB_matched":-3*t/(2+t**2),
    "AB_cycle":2*t*(1-t**2)/(4-t**4),
    "AB_opposite":t/(2-t**2)
}
for k in q:
    assert s.factor(q[k]-want[k])==0,k
assert s.factor(2+2*q["AB_matched"]-(2-6*t/(2+t**2)))==0
assert s.factor(4+2*q["A_cycle"]+2*q["B_opposite"]-6*t**2/(2+t**2))==0

# Rational interval proof of strict deepness and two-sided safety.
lo,hi=s.Rational(27,50),s.Rational(14,25)
vl,vh=s.Rational(11,10),s.Rational(6,5)
wl,wh=s.Rational(14,5),s.Rational(29,10)
assert s.factor(s.diff(v,t))==32*t*(t**4-2*t**2+4)/((t**2-2)**2*(t**2+2)**2)
assert vl<v.subs(t,lo) and v.subs(t,hi)<vh
assert -wl/4<-s.Rational(1,2)
assert -s.Rational(1,2)<1-vh/2<1-vl/2<s.Rational(1,2)
assert (-vl/hi**2+hi**2*wh/4)/4<-s.Rational(1,2)
assert -s.Rational(1,2)<-hi**2*wh/16<0
assert -(vl/hi+lo*wl/2)/4<-s.Rational(1,2)
assert 0<hi*wh/8<s.Rational(1,2)
assert 0<vl/(4*hi)-hi*wh/8
assert vh/(4*lo)-lo*wl/8<s.Rational(1,2)

# Rational rank-three Gram, all 28 exact endpoint checks.
G=s.zeros(8)
for i in range(4):
    for j in range(4):
        a=(v/2)*(H[1,i]*H[1,j]+H[2,i]*H[2,j])+w*H[3,i]*H[3,j]
        b=(v/(2*t**2))*(H[1,i]*H[1,j]+H[2,i]*H[2,j])+(t**2*w/4)*H[3,i]*H[3,j]
        z=-(v/(2*t))*(H[1,i]*H[1,j]+H[2,i]*H[2,j])-(t*w/2)*H[3,i]*H[3,j]
        G[A[i],A[j]]=a
        G[B[i],B[j]]=b
        G[A[i],B[j]]=G[B[j],A[i]]=z
G=G.subs(t,s.Rational(11,20)).applyfunc(s.factor)
assert G==G.T and G.rank()==3 and all(G[i,i]==1 for i in range(8))
deep={tuple(sorted(x)) for x in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
for i in range(8):
    for j in range(i+1,8):
        if (i,j) in deep: assert G[i,j]<-s.Rational(1,2)
        else: assert -s.Rational(1,2)<=G[i,j]<=s.Rational(1,2)
C=lambda P:sum((1+G[i,j])/2 for i,j in P)
assert C(P0)==s.Rational(174,307)
assert C(P1)==C(P2)==s.Rational(121,307)
S=C(P1)+C(P2)
assert s.factor((2-C(P0))**2+S**2/2-3*S)==0

# Retained harmonic cap: independent exact rational root bracketing.
D=lambda a:196*a-644*a*a+896*a**3-448*a**4
rl,rh=s.Rational(27143,10**6),s.Rational(27144,10**6)
sl,sh=s.Rational(39781,10**6),s.Rational(39782,10**6)
assert D(rl)<s.Rational(1245,256)<D(rh)
assert D(sl)<s.Rational(41,6)<D(sh)
assert s.Rational(1,2)+rl+sl>s.Rational(566924,10**6)
cap=s.Rational(1,2)+rh+sh
assert cap==s.Rational(566926,10**6)
c=lambda x:2-6*x/(2+x*x)
assert c(hi)<s.Rational(566924,10**6)<cap<c(lo)
# Conditional sum >271/200 and alternative sum >7879/10000.
R=9-2*(2-cap)**2
b=3+cap-s.Rational(271,200)
assert b>0 and b*b>R
cap2=s.Rational(567,1000)
R2=9-2*(2-cap2)**2
b2=3-s.Rational(7879,10000)
assert b2>0 and b2*b2>R2
assert (2-cap)**2>s.Rational(3,2)

print("PASS exact Hadamard PSD, F3 strict rank-three witness, all 28 contacts,")
print("matching tradeoff, root brackets, and conditional rational corollaries")
print("C0 =",C(P0),"; C1=C2 =",C(P1))
