# Exact deep-edge cap improves the universal Type-E Q-frame floor (2026-10-28)

**[PROVED EXACTLY — CONDITIONAL ONLY ON RETAINED TYPE-E ENERGY CEILING]**
For each of the twenty selected deep edges, write unit endpoints
u_i^+,u_i^- and midpoint m_i=(u_i^++u_i^-)/2. Because their
inner product is strictly below -1/2,
\[
0\le a_i=\|m_i\|^2=(1+u_i^+\cdot u_i^-)/2<1/4.
\]
Let A=sum a_i<=383/504 and U=sum a_i^2. For j=floor(4A), j=0,1,2,3,
convexity gives the sharp envelope
\[
U\le j/16+(A-j/4)^2.
\]
The supremum is attained in the closure by j coordinates at 1/4,
one at the residual, all others zero. At A*=383/504,
j=3, residual=5/504, and
\[
U\le3/16+(5/504)^2=47653/254016.
\]

For z_i=(u_i^+-u_i^-)/2, let
V=||sum z_i z_i^T-(20-A)I_5/5||_F^2>=0.
The exact five-dimensional frame identity is
\[
\sum_{i<j}(z_i\cdot z_j)^2
=30-3A+A^2/10-U/2+V/2.
\]
On each interval j/4<=A<(j+1)/4 the lower-envelope derivative is
-3-4A/5+j/4<0, so evaluating at A* yields
\[
\boxed{\sum_{i<j}(z_i\cdot z_j)^2
\ge8790283/317520=27.684186822877296\ldots.}
\]
This is an **exact improvement by 131/672** over the older universal
scalar floor 17456771/635040; it retains 92.2806% of the exact
D5 squared-correlation mass 30. It is weaker than separately retained
*conditional center-sensitive* floors (~28.3956) and does not replace them.

## Exact translation to the 184 safe pairings

For the six F3 core pairings put
d_ij=(|z_i.z_j|-1/2)_+, d=sum d_ij, d2=sum d_ij^2,
and hminus=sum (1/4-(z_i.z_j)^2)_+.
The identity
\[
S_{\rm safe}=57/2-3A+A^2/10-U/2+V/2-d-d2+hminus
\]
is exact. Using the retained raw-defect cap
D=1780062775/4032758016, and the retained negative-Gram theorem
d2<=(C^2-||W||^2)/4, where C=sum_{core}||m_i||^2<=A
and W=sum_{core}||m_i||m_i, gives the label-free consequence
\[
\boxed{S_{\rm safe}\ge64520136179/2520473760
+V/2+hminus+||W||^2/4.}
\]
The rational constant is 25.598416140225955...
and equals 8790283/317520 -3/2 -D -(383/504)^2/4.

**[RETAINED, NOT REPROVED]** Type-E mass and A ceiling, six-exception
defect cap, and negative-Gram theorem.
**[OPEN]** This lower bound is not yet incompatible with a proven
incidence-sensitive upper bound. Type E and all other outstanding
branches remain open; global proved range remains 40<=tau_5<=44.

Exact verifier: research/tau5_typeE_deep_edge_cap_Q_floor_2026-10-28_verify.py.
