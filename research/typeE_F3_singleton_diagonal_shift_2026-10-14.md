# F3 singleton branch: exact diagonal-shift lemma

[PROVED EXACTLY, conditional on Type E setup.] For the all-singleton perfect matching P2, the four midpoint energies sum to C > 2 - sqrt(15)/2 = 0.0635083268963.

Proof: Orient P2 as (04),(71),(23),(56). The six residual signed mixed products have matrix K=I-ee^T with e=(1,1,-1,-1). Orthogonality m_i.z_i=0 allows replacing K by K+I=2I-ee^T, whose square is 4I. Summing six residual contact equations gives 1+Delta+(||sum m_i||^2+||sum z_i||^2)/2=-T, with Delta>0 and |T|<=2sqrt(C(4-C)). Thus C(4-C)>1/4, proving the claim. The double-contact branches retain the earlier bound C>2-sqrt(9+4sqrt(3))/2, so the uniform bound is unchanged.

[OPEN] Type E elimination, types C/D, generic e>=27, minimum-degree dependency. Global proved range remains 40<=tau_5<=44. Retain M(F3)<=89 and A<=383/504.
