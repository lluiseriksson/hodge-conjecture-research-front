---
brick_id: B265
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) with k=3 or 4, and H=A^2
smoothness: Q^d and the seven reduced marked supports are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, a residual P^2 through u, selected good secant lines, normalized pair-line hyperplanes, and first infinitesimal neighborhood 2u are projective
dimension: dim X=d=2n>=14; the proposed planar combined rank d is false because every variable-edge product image is the same rank-(d-1) subspace
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the failed route was intended to exclude cubic/quartic equality inside G190
coefficient_field: Q for zeta and C for plane equations, square-zero local jets, normalized factors, products, annihilators, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B260-B264, B267, G190, NG222, S081
claim: The proposed route using different complementary unit jets for two planar variable edges does not supply rank d. B267 proves that the removed factor contributes the opposite first jet, all product spaces share the same generator j(P), and every image equals <j(P)> direct-sum Ann(U) of rank d-1. The earlier PROVED label and the claimed floor h_Z(1)>=7d+6 are retracted.
falsifier: a noncancelling complementary-unit term after the variable factor is restored, two planar edge product images that differ, or a combined rank at least d from the B265 spaces alone
---

# B265 — RETRACTED: planar unit separation cancels

- **Label:** NO-GO
- **Attempted route:** choose two distinct selected secants in B264's
  planar locus and compare the first jets of their complementary fixed
  products.
- **Omitted term:** the variable generator for edge \(e\) has jet
  \((1,\lambda_e)\), while its complementary product has jet
  \((1,\Lambda-\lambda_e)\).
- **Exact cancellation:** in the square-zero first-jet algebra,

  \[
  (1,\lambda_e)(1,\Lambda-\lambda_e)=(1,\Lambda)=j(P). \tag{1}
  \]

  Thus every edge image contains the same unit generator.
- **Derivative space:** all zero-value variations have differential in
  the same \(D=\operatorname{Ann}(U)\), of dimension \(d-2\).
- **Actual image:** for every selected planar edge,

  \[
  R_e=\langle j(P)\rangle\oplus D,
  \qquad \dim R_e=d-1. \tag{2}
  \]

- **Invalid inference:** distinct complementary unit jets yield distinct
  annihilator graph planes. They do not, because the removed variable
  factor restores exactly the missing \(\lambda_e\).
- **Consequence:** B265's former rank-\(d\) conclusion, cubic/quartic
  floor \(7d+6\), and G190-to-G191 transition are invalid.
- **Preserved results:** B264 remains valid outside the planar locus;
  B266's standard-polarization exclusion is independent and remains
  valid after its common-floor claims are removed.
- **Re-entry condition:** G190 must attack the planar locus using
  sections not contained in the single-factor edge-product span.
- **HC guard:** no detector, cycle, proof, or disproof of HC is produced.
