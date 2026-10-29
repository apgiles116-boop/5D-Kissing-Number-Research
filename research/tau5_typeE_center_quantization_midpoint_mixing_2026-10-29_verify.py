"""Exact rational verification of Type-E center-contact/midpoint mixing.
The upstream global Type-E harmonic/signed-Gram certificates are not recertified.
"""
from fractions import Fraction as F
from random import Random

assert F(29,120)-F(1,16)==F(43,240)
assert F(1,16)/F(43,240)==F(15,43)
assert F(15,43)/4==F(15,172)
assert F(1,160)+F(1,60)==F(11,480)
assert F(480,11)*F(15,172)/60==F(30,473)
assert F(480,11)+F(480,473)<45

def check(pq):
    assert len(pq)==20
    assert all(abs(p+q)<=F(1,2) and abs(p-q)<=F(1,2) for p,q in pq)
    pq=sorted(pq,key=lambda t:2*(t[0]**2+t[1]**2),reverse=True)
    y=[2*(p*p+q*q) for p,q in pq]
    rho=sum(y)-F(13,2)
    if not F(2,5)<=rho<=F(7,15): return False
    delta=sum(abs(a-b) for a,b in zip(y,[F(1,2)]*13+[rho]+[F(0)]*6))
    B=sum(p*p for p,q in pq)
    if not (delta<=F(1,30) and B<=F(1,16)): return False
    top=sum(p*p for p,q in pq[:13])
    assert top<=F(15,172)*delta**2
    mix=sum((F(1,2)-yi)*p*p for yi,(p,q) in zip(y,pq))
    assert mix>=max(F(0),B-F(15,172)*delta**2)/60
    N0=7*sum((p+q)**2*(1-4*(p+q)**2)+(p-q)**2*(1-4*(p-q)**2) for p,q in pq)
    RN=N0-7*rho*(1-2*rho)+56*B-F(56,5)*B**2
    gap=sum(yi*(1-2*yi) for yi in y)-rho*(1-2*rho)
    assert RN==7*gap+112*mix+224*(sum(p**4 for p,q in pq)-B**2/20)
    assert RN/112>=((1-2*rho)*delta-delta**2)/16+max(F(0),B-F(15,172)*delta**2)/60
    return True

rng=Random(20261029)
checked=0
for _ in range(3000):
    pq=[]
    for j in range(13):
        cplus=F(1,2)-F(rng.randrange(5),10000)
        cminus=-F(1,2)+F(rng.randrange(5),10000)
        pq.append(((cplus+cminus)/2,(cplus-cminus)/2))
    q=F(rng.randrange(460,482),1000)
    p=F(rng.randrange(-10,11),1000)
    if abs(p+q)>F(1,2) or abs(p-q)>F(1,2): continue
    pq.append((p,q))
    pq.extend([(F(0),F(0))]*6)
    checked+=int(check(pq))
assert checked>500,checked
print("PASS: exact constants, identity, inequalities; %d admissible rational tests"%checked)
