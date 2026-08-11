---
brick_id: NG169
status: NO-GO
base_field: C
variety: a smooth projective complex variety with finite smooth node scheme Z, a degree-m value relation, and lower double sections
smoothness: X and Z are smooth and the central Hessians are nondegenerate; no relation among second jets is assumed
projectivity: X, H^m, H^k, point evaluations, and quadratic profiles are projective coherent data
dimension: arbitrary dim X=d; the failure occurs for two nodes and one symmetric tangent coefficient
codimension: a relation among values of global degree-m sections gives no relation among Hessian contractions of lower double sections
coefficient_field: C; the exact linear countermodel is defined over Q
cohomology_theory: finite point evaluation and coherent second jets
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B205-B207 and G135-G137
claim: Infer that ell_(r,e,b,c) vanishes on W_k by differentiating the value relation r in S_m^perp.
falsifier: r annihilates values of global degree-m sections, while e times a lower double section has zero values at Z and its Hessian contraction is not constrained by that zero-order relation
---

# NG169 — A value relation cannot be differentiated across the nodes

- **Route:** start from \(r\in S_m^\perp\), differentiate the identity that
  \(r\) annihilates global degree-\(m\) values, and conclude
  \(\ell_{r,e,b,c}|_{W_k}=0\).
- **Valid input:** for every global \(h\in H^0(H^m)\),
  \(\langle r,h|_Z\rangle=0\).
- **Invalid inference:** the same relation annihilates independently chosen
  second jets at the distinct points of \(Z\).

If \(s\in H^0(I_Z^2H^k)\) and \(e\in H^0(H^{m-k})\), then \(es\) is a
global degree-\(m\) section, but its value on \(Z\) is already zero. Applying
\(r\) yields only \(0=0\). The value relation has no parameter along which
the distinct marked points and their inverse-Hessian directions can be
differentiated coherently.

In the two-node model

\[
 S_m=E_{m-k}=\mathbf Q(1,1),\qquad
 r=(1,-1),
\]

an exact permitted contracted profile \((1,2)u^2\) gives
\(\ell=-1\), despite \(r\) annihilating every vector in \(S_m\). This is a
countermodel to the formal inference, not a projective counterexample.

- **Precise obstruction:** zero-order evaluation relations do not prolong
  automatically to second-jet relations.
- **Re-entry condition:** construct G137's coherent dual preimage or a
  genuine global differential comparison that produces it.
