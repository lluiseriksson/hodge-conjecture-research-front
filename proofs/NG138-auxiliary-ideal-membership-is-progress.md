---
brick_id: NG138
status: NO-GO
base_field: C
variety: any analytic tracked critical-value germ equipped with a valid residue identity and an auxiliary residue term
smoothness: only a smooth analytic parameter germ is required
projectivity: irrelevant to the local-algebra obstruction; projective residue identities are subject to the same audit
dimension: N tracked functions of central differential rank R<N
codimension: the desired N-R lifted relation rows are not supplied by auxiliary ideal membership
coefficient_field: C
cohomology_theory: analytic syzygy modules and residue coefficient identities
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative
dependencies: B156, B172-B174, G100, G108
claim: The condition that the auxiliary residue rho_A belongs to the tracked ideal I_tau is a nontrivial obstruction whose vanishing produces adjusted analytic syzygies.
falsifier: the residue identity already gives rho_A=-c_A dot tau, while B174 identifies every alternative coefficient representation with a pre-existing syzygy
---

# NG138 — Auxiliary ideal membership is automatic and circular

For every admissible numerator, the global residue identity has the form

\[
 c_A\cdot\tau+\rho_A=0.
\]

It follows immediately that \(\rho_A\in I_\tau\). The quotient class
\([\rho_A]\in\mathcal O/I_\tau\) therefore vanishes identically and cannot
distinguish successful from unsuccessful critical-value germs.

Choosing coefficients \(b\) with \(b\cdot\tau=\rho_A\) does not repair
the problem. B174 gives the affine bijection

\[
 b\longmapsto b+c_A
\]

from all such choices to \(\operatorname{Syz}(\tau)\). The canonical
choice \(b=-c_A\) gives zero; every nonzero adjusted row is exactly a
syzygy already present.

The model \(\tau=(x,x+y^2)\) makes the circularity visible. Its auxiliary
identity can be manufactured for every \(c_A\), but all adjusted rows
vanish at the origin and cannot lift the central relation \((1,-1)\).

## Re-entry condition

An auxiliary residue route must construct a nonzero analytic syzygy by
independent geometric data, not merely assert ideal membership or choose an
unspecified representation. Such a construction is G100 itself and must
retain every detector clause.
