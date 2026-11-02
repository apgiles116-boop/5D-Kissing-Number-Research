# Type E: endpoint-Perron correction, exact singleton mixed-Walsh signs, improved Q floor (2026-11-02)

**[AUDIT CORRECTION / WITHDRAWN]** The earlier endpoint-Perron proof substituted an average of two opposite endpoint inner products for an individual endpoint inner product. This omits mixed Walsh terms. Its Perron obstruction, exclusion of four positive F3 defects, canonical `D_raw<1/4` and `D_raw<=(sqrt(2)-1)/2`, alternative double-free `D_raw<1/4`, and derived 45/46 safe-pair counts are **NOT PROVED and must not be used**. The old file now carries an explicit withdrawal banner. This does not construct a full F3 counterexample; it identifies an invalid inference. Earlier triangle-free support and C4 mass/defect certificates are independent and remain retained.

## 1. Exact error and rational witness [PROVED EXACTLY]

For selected deep edges `u_i^sigma=m_i+sigma z_i`, `u_j^tau=m_j+tau z_j`, define `h=m_i·m_j`, `d=z_i·z_j`, `p=m_i·z_j`, `q=z_i·m_j`. The exact Walsh identity is

    u_i^sigma·u_j^tau = h + sigma*tau*d + tau*p + sigma*q.

Averaging the `++` and `--` contacts yields `h+d`, but the individual contacts differ by `+(p+q)` and `-(p+q)`. The previous Perron proof used the average as an individual endpoint correlation.

An exact Gram counterexample, in order `(m_i,z_i,m_j,z_j)`, is

    [[1/10, 0,    0,    1/10],
     [0,    9/10, 1/10, 0   ],
     [0,    1/10, 1/10, 0   ],
     [1/10, 0,    0,    9/10]].

This is positive definite. The four cross-endpoint contacts `(++),(--),(+-),(-+)` are `1/5,-1/5,0,0`, all safe. Both selected internal edge contacts equal `-4/5` (deep). Yet `h+d=0` while the individual `++` contact is positive `1/5`. This refutes the *local inference*, not the F3 global conclusion.

## 2. Singleton mixed-Walsh sign theorem [PROVED EXACTLY]

Suppose exactly one of the four cross-endpoint contacts is deep and the other three are two-sided safe in `[-1/2,1/2]`; selected deep edges have `a_i=||m_i||²<1/4`, `a_j<1/4`. Reorient the `z` vectors so the unique deep cross-contact is `++`. If `delta=(|d|-1/2)_+>0`, then

    d = -1/2-delta,
    h <= -delta - |p-q|,
    p <= -delta,       q <= -delta.                         (1)

**Proof.** Averaging both opposite-sign safe contacts and using their lower bounds gives `h-d>=-1/2`. All four upper bounds give `h+|d|<=1/2`. If `d>1/2`, these imply `h>=delta` and `h<=-delta`, impossible. Hence `d=-1/2-delta`. The opposite-sign safe *upper* bounds give `h+delta+|p-q|<=0`. The safe `--` *lower* bound gives `p+q<=h-delta`. Thus `p+q<=-2delta-|p-q|`, equivalent to both `p<=-delta` and `q<=-delta`.

For a unique deep sign pair `(sigma,tau)`, the orientation-free version is `tau*(m_i·z_j)<=-delta` and `sigma*(z_i·m_j)<=-delta`. Therefore

    (m_i·z_j)^2 + (z_i·m_j)^2 >= 2 delta^2.              (2)

**Local sharpness.** For `0<t<1/2`, set `a_i=a_j=t/2`, `delta=t(1-t)/2`, and `h=p=q=-delta`, `d=-1/2-delta`. The resulting four-vector Gram is PSD: its symmetric block has determinant zero and its antisymmetric block has determinant `t(3-2t)/2>0`. The four cross contacts are `-1/2-4delta,-1/2,1/2,1/2`, and (1)-(2) are sharp. This is the earlier sharp singleton mass-defect witness.

**Double-contact exception.** For two opposite deep cross contacts, the mixed-sign conclusion fails. The exact PSD example `a_i=a_j=1/5`, `h=-1/10`, `d=-3/5`, `p=q=0` gives `++=--=-7/10` and `+-=-+=1/2`: positive defect `1/10` but zero mixed terms. Apply (1)-(2) only to singleton-contact pairs.

## 3. Improved universal 20-line Q-frame floor [PROVED EXACTLY]

For 20 selected deep edges in dimension five, `a_i<1/4`, `A=sum a_i<=383/504`, `z_i` are projected vectors, and `Q=sum_(i<j)(z_i·z_j)^2`, the exact frame inequality gives

    Q >= 30-3A+A^2/10-(1/2)sum_i a_i^2.

For fixed `0<=A<1`, convex mass concentration with `a_i<1/4` yields

    sum_i a_i^2 <= k/16+(A-k/4)^2,   k=floor(4A),

with strict inequality at the relevant endpoint because the maximizing configuration requires three entries equal to `1/4`. The lower-bound function is strictly decreasing on each interval: its derivative is `-3+A/5-(A-k/4)<0`. At `A=383/504`, `k=3`, residual `5/504`. Hence

    Q > 30-3*(383/504)+(383/504)^2/10
          -(1/2)*(3/16+(5/504)^2)
      = 8790283/317520
      = 27.684186822877... .                              (3)

This exceeds the previous assumption-light baseline `17456771/635040` by exactly `131/672` and retains at least `92.2806%` of the exact D5 squared-correlation value 30. **[LIMITATION]** This is weaker than the separately retained, stronger center-sensitive `Q_total>28.3626` certificate; it improves the unconditional-on-harmonic baseline, not that later bound.

## Proof-status ledger

**[PROVED EXACTLY]** The Walsh endpoint identity, explicit rational PSD counterexample to the Perron substitution, singleton mixed-sign lemma and its local sharpness, double-contact exception, and improved global Q floor.

**[WITHDRAWN / UNVERIFIED]** The endpoint-Perron-based four-defect exclusion, `D<1/4`, `D<=(sqrt(2)-1)/2`, alternative double-free `D<1/4`, and 45/46 safe-pair counts. These require independent new proofs.

**[RETAINED, NOT RE-PROVED]** F3 positive-defect support triangle-free (four defects would form a C4); C4 mass-variance and joint defect budgets; raw defect `<=1780062775/4032758016`, homogeneous defect `<=5792292955405/4129544208384`; star `<=70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, 20-edge mass `>=2137/6`, `A<=383/504`, audited Musin/Boyvalenkov 21-line zero-midpoint exclusion. Stronger harmonic and Q certificates retain their separate upstream conditions.

**[OPEN]** Type E (canonical C4 and alternative double-positive), C, D, generic `e>=27`, non-isolated branches. Sparse `e=23/24` classification assumes `delta(G)>=1`. Global proved range remains `40<=tau_5<=44`.

**Next:** exploit signed mixed-Walsh constraints around a canonical C4 jointly with the two opposite safe pairings and the rank-five endpoint Gram; do not reuse endpoint Perron without controlling mixed terms.

Companion checker: `research/tau5_typeE_Walsh_mixed_audit_2026-11-02_verify.py`.
