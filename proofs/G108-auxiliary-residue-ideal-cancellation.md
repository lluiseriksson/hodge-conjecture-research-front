---
brick_id: G108
status: EXPLORATORY
base_field: C
variety: a full affine polynomial coefficient family with a reduced no-infinity gradient complete intersection, ordered tracked nodes, and all auxiliary critical points
smoothness: the parameter germ and all critical-point sections are smooth; every critical point is Morse
projectivity: only the homogenized gradient scheme is projective; transfer to arbitrary smooth projective varieties remains a separate obligation
dimension: d spatial variables; N tracked nodes; central tracked-value rank R<N; admissible residue degrees are bounded by s=d(m-1)-d-1
codimension: construct N-R adjusted residue syzygies whose central rows span ker(d tau_0)^*
coefficient_field: C
cohomology_theory: global Grothendieck residues and analytic local algebra of I_tau
hodge_type: must ultimately be rational type-(0,0); none is yet constructed
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) remains downstream; no algebraic cycle may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156, B172-B173, G100, NG136-NG137
claim: Find N-R admissible analytic numerators whose auxiliary residue classes vanish in O/I_tau and whose adjusted central tracked rows span ker(d tau_0)^*, without assuming constant moving critical-evaluation rank, then retain the uniform matroid, primitive ambient image, rational type, and specified nonzero pairing.
falsifier: a theorem showing every spanning family with auxiliary residue in I_tau forces constant moving evaluation rank, or a nonzero obstruction class for every admissible numerator in a candidate family
---

# G108 — Can auxiliary residues cancel inside the tracked ideal?

For an admissible numerator \(f_tA\), B172 gives

\[
 \sum_i \frac{A(p_i(t))}{J_i(t)}\tau_i(t)+\rho_A(t)=0.
\]

B173 and NG137 close the special case \(\rho_A=0\): a complete analytic
selector frame is then equivalent to G107. The remaining residue-specific
possibility is

\[
 \rho_A\ne0,\qquad [\rho_A]=0
 \ \text{in}\ \mathcal O/I_\tau. \tag{1}
\]

Writing \(\rho_A=\sum_i b_i\tau_i\) turns the displayed residue identity
into an adjusted analytic syzygy. G108 asks for \(N-R\) such adjusted rows
spanning every central relation while the raw moving evaluation rank is
allowed to jump.

This is falsifiable: compute the linear map from admissible numerators to
\(\mathcal O/I_\tau\), including every auxiliary critical section, and
test whether its kernel maps surjectively to
\(\ker(d\tau_0)^*\). A positive result is still only an affine mechanism;
promotion toward G100 also requires the full projective and detector
clauses in the metadata.
