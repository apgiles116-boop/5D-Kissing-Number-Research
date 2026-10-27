# Type E: exact frame-variance audit and strengthened conditional 17-line energy tradeoff

Date: 2026-10-27. Proof-status labels are strict. Companion exact verifier: `research/tau5_typeE_frame_variance_template_tradeoff_2026-10-27_verify.py`.

## [PROVED EXACTLY — UNIVERSAL] Frame-variance identity and stability caveat

For 20 vectors z_i in R^5, let a_i=1-||z_i||^2, A=sum a_i, F_z=sum z_i z_i^T. Expanding tr(F_z^2) gives the exact identity

sum_(i<j)(z_i.z_j)^2 = 30-3A+A^2/10-(1/2)sum_i a_i^2+(1/2)||F_z-(4-A/5)I||_F^2.

For normalized u_i=z_i/sqrt(1-a_i), likewise

sum_(i<j)(u_i.u_j)^2 = 30+(1/2)||sum_i u_i u_i^T-4I||_F^2 >=30.

Consequently the previously retained lower bound 17456771/635040 on the unnormalized squared-correlation sum is a weighted Welch lower bound, NOT a D5-closeness estimate. Even normalized equality 30 does not characterize D5: four copies of an orthonormal basis attain equality, but violate the Type-E safe-pair constraints. A D5 stability proof needs an upper frame-variance bound AND contact-pattern information.

## [PROVED EXACTLY — CONDITIONAL ON EXPLICIT 17-LINE TEMPLATE] Stronger energy floors

Assume the isolated center and the sixteen normalized outside-core directions equal the exact 17-line D16+center template of `tau5_typeE_17line_exact_covering_correction_2026-10-27.md`, up to rotation/relabeling/sign. Its covering radius has rho^2=8/(31-6sqrt(2)); set kappa=1/(4rho^2)=(31-6sqrt(2))/32.

Let A_O=sum_outside a_j, C=sum_four_core a_i, b=max_outside a_j. Since 0<=a_i<=1/4, we have 0<=b<=1/4 and A_O>=b. The prior covering inequality forces each core a_i>=1-kappa/(1-b). This is positive because 1-b>=3/4>kappa. Hence

C >= 4(1-4kappa/3) = sqrt(2)-7/6 = 0.247546895706... .

Also A=A_O+C >= f(b):=b+4(1-kappa/(1-b)). Since f'(b)=1-4kappa/(1-b)^2<0 for 0<=b<=1/4,

A >= f(1/4)=sqrt(2)-11/12 = 0.497546895706... .

This is a CONDITIONAL result, not a label-free Type-E energy improvement.

## [PROVED EXACTLY — CONDITIONAL TEMPLATE PLUS RETAINED UPPER BOUND] Outside-core interval

With U=383/504 and x=A_O, if x<1/4 then b<=x and A<=U imply
x+4(1-kappa/(1-x))<=U, equivalently
504x^2+1129x+320-378sqrt(2)>=0.

Thus x >= (sqrt(629521+762048sqrt(2))-1129)/1008 = 0.1761965718996... . If x>=1/4 the same bound is automatic. Moreover C>=sqrt(2)-7/6 gives
A_O <= 971/504-sqrt(2)=0.512373739214... .

## [OPEN] Ledger and next step

No theorem places arbitrary Type E into this 17-line template. The exact 20-line D5 template is incompatible with the isolated center. A label-free upper frame-variance/contact-stability estimate, or a finite optimization retaining all sixteen outside-core energies, is still required. No Type-E exclusion or global improvement is claimed.

Retain 40<=tau_5<=44; M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; prior label-free A>1/49; and the delta(G)>=1 caveat for sparse e=23/24 classification. Types C,D, generic e>=27 and non-isolated branches remain open.
