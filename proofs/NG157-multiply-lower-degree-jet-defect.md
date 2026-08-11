---
brick_id: NG157
status: NO-GO
base_field: C
variety: a smooth projective complex variety with a very ample H, at least two distinct prospective nodes Z, a lower power H^k, and a target power H^m with k<m
smoothness: the variety and point supports are smooth; target singularities are intended to be ODPs, but the obstruction occurs already in first jets
projectivity: the variety, powers of H, point schemes, and complete linear systems are projective
dimension: arbitrary positive dimension; in the Hodge route dim X=2n and the target conditional-gradient quotient has dimension at most 2n
codimension: any nonzero lower-degree conditional gradient produces, after point-separating multiplication, a target deformation with gradient zero at one node and nonzero at another
coefficient_field: C for multiplication and coherent jets; Q detector data remain separate
cohomology_theory: graded section rings, coherent first jets, and very ample point separation
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B194, G123-G125
claim: Start with a nonzero lower-degree conditional-gradient quotient V_k, multiply its sections by H^(m-k), and thereby construct one-node determination and conformal holonomy in the full degree-m system.
falsifier: B194 proves one-node determination in degree m forces V_k=0 for every k<m; a point-separating multiplier converts any nonzero lower jet into an explicit violation
---

# NG157 — Multiplication cannot inherit the one-node jet defect

- **Route:** construct a useful node-gradient defect in a lower power
  \(H^k\), multiply its sections by degree \(m-k\) polarization sections,
  and claim the resulting degree-\(m\) full system satisfies G123/G124.
- **Valid input:** multiplication preserves value vanishing on \(Z\), and
  at a node the product derivative is the multiplier value times the lower
  derivative.
- **Invalid inference:** this preserves one-node determination.

Suppose

\[
 0\ne[s]\in
 V_k=H^0(I_ZH^k)/H^0(I_{2Z}H^k). \tag{1}
\]

Then \(ds(p_i)\ne0\) for some node \(p_i\). Choose a second node \(p_j\)
and a section \(h\in H^0(H^{m-k})\) with

\[
 h(p_j)=0,\qquad h(p_i)\ne0. \tag{2}
\]

The target section \(hs\) vanishes on all of \(Z\), but

\[
 d(hs)(p_j)=0,qquad d(hs)(p_i)=h(p_i)ds(p_i)\ne0. \tag{3}
\]

Thus its gradient at one node does not determine the remaining gradients.
The violation lies inside the full degree-\(m\) complete system, so it
cannot be repaired by enlarging a selected multiplication subfamily.

- **Precise obstruction:** B194 proves the converse universal statement:
  target one-node determination forces \(V_k=0\) for every \(k<m\).
- **Re-entry condition:** G125 must construct a genuinely primitive first-
  jet birth at degree \(m\), with every lower quotient zero, then establish
  Hessian holonomy and the rational detector independently.
