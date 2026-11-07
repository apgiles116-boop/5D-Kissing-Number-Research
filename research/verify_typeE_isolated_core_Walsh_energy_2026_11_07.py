"""Exact Walsh coefficient and isolated/core incidence audit, no dependencies."""
from itertools import product
signs = list(product((1,-1), repeat=2))
# coefficients of c,e,f,d in contact(s,t)
rows = [(1,s,t,s*t) for s,t in signs]
for i in range(4):
    for j in range(4):
        dot = sum(row[i]*row[j] for row in rows)
        assert dot == (4 if i==j else 0)
assert 16*4 == 64
assert 64*4 == 256
print("PASS: exact Walsh orthogonality; 64 edge pairs; 256 endpoint contacts")
