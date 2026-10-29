"""Exact Fraction verifier for three-zone center-contact coercivity.
Upstream global Type-E mass/harmonic/signed-Gram certificates are NOT recertified.
"""
from fractions import Fraction as F
from random import Random

c=F(15,172)
assert F(41,1320)>F(31,1000)
assert F(1,30)-F(1,440)==F(41,1320)
assert F(1,240)-F(1,3520)==F(41,10560)
assert F(10560,41)<260
assert F(1,160)+F(31,1000)==F(149,4000)
assert F(31,1000)*c==F(465,172000)
assert F(67600,57600)==F(169,144)
assert F(4000,149)*(1+F(465,172000)*F(169,144))==F(8282195,307536)
assert F(8282195,307536)<27
assert c*F(169,144)==F(845,8256)
assert c*67600==F(253500,43)
assert F(1,160)+F(1,2)-F(1,440)>F(1,2)
assert F(1,160)+F(1,30)==F(19,480)

def check(ys, ps2):
    assert len(ys)==len(ps2)==20 and ys==sorted(ys,reverse=True)
    assert all(F(0)<=yi<=F(1,2) for yi in ys)
    assert all(F(0)<=p2<=yi/2 for yi,p2 in zip(ys,ps2))
    # Squared version of |p_i+q_i|,|p_i-q_i| <= 1/2:
    assert all(p2*(yi/2-p2)<=(F(1,2)-yi)**2/16 for yi,p2 in zip(ys,ps2))
    rho=sum(ys)-F(13,2)
    assert F(2,5)<=rho<=F(7,15)
    delta=sum(abs(yi-target) for yi,target in zip(ys,[F(1,2)]*13+[rho]+[F(0)]*6))
    B=sum(ps2)
    if delta>F(1,30) or B>F(1,16): return False
    BH=sum(ps2[:13]); BR=ps2[13]; BT=sum(ps2[14:])
    h=F(1,2)-rho-delta/2
    assert BH<=c*delta**2
    mix=sum((F(1,2)-yi)*p2 for yi,p2 in zip(ys,ps2))
    assert mix>=h*BR+(F(1,2)-delta/2)*BT
    assert mix>=h*max(F(0),B-c*delta**2)+rho*BT
    gap=sum(yi*(1-2*yi) for yi in ys)-rho*(1-2*rho)
    assert gap>=(1-2*rho)*delta-delta**2
    return True

rng=Random(2026102909)
passed=0
for _ in range(3000):
    D=[F(rng.randrange(0,5),20000) for _ in range(13)]
    E=[F(rng.randrange(0,4),20000) for _ in range(6)]
    rho=F(rng.randrange(400,467),1000)
    y=[F(1,2)-d for d in D]+[rho+sum(D)-sum(E)]+E
    y.sort(reverse=True)
    ps2=[]
    for yi in y:
        bound=min(yi/4,(F(1,2)-yi)**2/(8*(yi+F(1,100))))
        ps2.append(bound*F(rng.randrange(0,4),10))
    if check(y,ps2): passed+=1
assert passed>500,passed
print("PASS: exact constants and three-zone inequalities;",passed,"rational diagnostic cases")
