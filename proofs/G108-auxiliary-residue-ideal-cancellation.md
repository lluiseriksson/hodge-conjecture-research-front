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
dependencies: B156, B172-B174, G100, NG136-NG138
claim: Construct, independently of any pre-existing tracked-value syzygy, coefficient representations of the auxiliary residues whose adjusted rows span ker(d tau_0)^*, then retain the uniform matroid, primitive ambient image, rational type, and specified nonzero pairing.
falsifier: B174 proves that the space of all coefficient representations is an affine torsor under the pre-existing syzygy module, so the stated independent construction is exactly G100 rather than a weaker residue gate
---

# G108 — Auxiliary cancellation is terminal-equivalent, not a new gate

For an admissible numerator \(f_tA\), B172 gives

\[
 \sum_i \frac{A(p_i(t))}{J_i(t)}\tau_i(t)+\rho_A(t)=0.
\]

B173 and NG137 close the special case \(\rho_A=0\): a complete analytic
selector frame is then equivalent to G107. For \(\rho_A\ne0\), the residue
identity already gives the coefficient representation

\[
 \rho_A=-\sum_i\frac{A(p_i(t))}{J_i(t)}\tau_i(t). \tag{1}
\]

Thus \([\rho_A]=0\) in \(\mathcal O/I_\tau\) for every admissible
numerator. The resulting adjusted row is zero.

B174 proves more: all representations
\(\rho_A=\sum_i b_i\tau_i\) form an affine torsor under
\(\operatorname{Syz}(\tau)\), and

\[
 b\longmapsto
 \left(\frac{A(p_i)}{J_i}+b_i\right)_i
\]

is an affine bijection from that torsor to the analytic syzygy module.
Consequently producing adjusted rows spanning
\(\ker(d\tau_0)^*\) is exactly the G100 syzygy-lifting problem.

G108 is retained as a terminal-equivalent formulation for audit history,
not as a smaller residue gate. NG138 forbids counting bare ideal membership
or an unspecified coefficient representation as progress.
