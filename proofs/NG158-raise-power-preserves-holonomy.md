---
brick_id: NG158
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold with very ample H, a fixed G125 node scheme Z in degree m, and higher complete systems H^(m+a)
smoothness: the ambient variety and degree-m nodes are smooth/ODP; the obstruction concerns higher full-system first jets
projectivity: the variety, powers of H, fixed node schemes, and complete linear systems are projective
dimension: degree-m quotient dimension 2n; higher quotient dimension at least 2n r_a and eventually 2nN
codimension: multiplication by degree-a value sections introduces too many independent higher-degree gradient directions for one-node determination
coefficient_field: C for graded sections and first jets; Q detector data remain separate
cohomology_theory: graded coherent multiplication, point evaluation, first jets, and fixed-scheme Serre vanishing
hodge_type: no higher-degree rational detector is transported
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B195, G123-G126
claim: After constructing G125 at degree m, raise the polarization while keeping Z fixed and retain one-node determination, conformal Hessian holonomy, and the detector by positivity or multiplication.
falsifier: B195 injects E_a tensor V_m into V_(m+a), giving dimension at least 4n for every a>=1 and the full 2nN gradient target for a sufficiently large
---

# NG158 — Raising the power destroys the fixed-node holonomy

- **Route:** construct G125 once, replace \(H^m\) by \(H^{m+a}\) while
  keeping the node scheme, and use added positivity to stabilize or improve
  one-node determination and Hessian holonomy.
- **Valid input:** multiplication embeds the old degree-\(m\) sections into
  higher degrees and preserves their value vanishing on \(Z\).
- **Invalid inference:** the additional multiplier values preserve the
  \(2n\)-dimensional graph.
- **Precise obstruction:** B195 proves
  \[
  E_a\otimes V_m\hookrightarrow V_{m+a},\qquad
  q_{m+a}\ge r_aq_m.
  \]
  Since \(q_m=2n\) and \(r_a\ge2\),
  \[
  q_{m+a}\ge4n>2n.
  \]
  Hence no projection to one node gradient block can be injective. For
  \(a\gg0\), value evaluation on fixed \(Z\) is surjective and
  \(q_{m+a}=2nN\), the entire gradient target.
- **Scope guard:** a wholly new node scheme at a higher degree is not
  excluded, but it requires a new class-directed primitive-birth proof and
  no detector transport is automatic.
- **Re-entry condition:** close B186's complete finite Kuranishi ladder and
  every detector clause at the original birth degree, as demanded by G126,
  or rebuild all data from scratch for a new node scheme.
