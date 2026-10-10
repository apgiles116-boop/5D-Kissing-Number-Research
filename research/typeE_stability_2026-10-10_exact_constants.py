from fractions import Fraction as F

def certify(c, k):
    # K(c)=1024-96*c+128*sqrt(10*c*(4-c)) < k
    r = k-1024+96*c
    assert r>0
    assert r*r>128**2*10*c*(4-c)

certify(F(1), 1630)
certify(F(383,504), 1587)
certify(F(120709,200000), 1546)
print("PASS: exact rational K(c) comparisons")
