---
brick_id: NG095
status: NO-GO
base_field: Q inside the category of rational pure Hodge structures
variety: abstract Hodge-theoretic countermodel for the special-to-nearby lift in the clean nodal collision route
smoothness: not applicable to the exact countermodel; downstream geometric scope is B119's smooth projective original incidence family
projectivity: not applicable to the exact countermodel; downstream application is projective
dimension: arbitrary Hodge-theoretic model; downstream ambient dimension 2n
codimension: middle codimension n downstream
coefficient_field: Q
cohomology_theory: rational pure Hodge structures and a type-(0,0) morphism
hodge_type: relevant quotient Q(0); total source Q(0) direct-sum Q(-1)
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B093, B108, B117-B119, G080, S022
claim: Requiring an ordinary special lift to be type (0,0) as a total vector is not necessary for the Hodge route; a rational lift can have an irrelevant non-(0,0) component while its nonzero relevant relation-grade image is type (0,0).
falsifier: a theorem showing that the downstream conclusion fails whenever the total lift has any non-(0,0) component, even though its canonical relevant coordinate is nonzero and type (0,0)
---

# NG095 — The total lift need not be a Hodge class

**Status:** NO-GO

- **Route:** demand that the entire ordinary special-stalk lift \(\beta\) be
  rational type \((0,0)\) before testing its canonical relation grade.
- **Valid input:** the eventual Saito relation coordinate must be rational
  type \((0,0)\) after \(\mathbf Q(n)\).
- **Invalid inference:** every Hodge component of the total lift must have
  that type.
- **Precise obstruction:** take

  \[
  S=\mathbf Q(0)e_0\oplus\mathbf Q(-1)e_1,
  \qquad P=\mathbf Q(0)f,
  \]

  and the Hodge morphism \(u:S\to P\) given by

  \[
  u(e_0)=f,
  \qquad u(e_1)=0.
  \]

  The rational vector \(\beta=e_0+e_1\) is not of type \((0,0)\) as a
  total vector, while \(u(\beta)=f\ne0\) is type \((0,0)\). Thus an
  irrelevant Hodge component of a lift does not contaminate its relevant
  quotient.
- **Geometric closure:** once G083 supplies a lift in $S_0$, B118 removes its
  lower point grade and B117 makes its nonzero
  \(E_\infty^{-1,0}\) coordinate full-support. B093 and S022 identify that channel, for a
  clean nodal target, with a direct sum of \(\mathbf Q(0)\)'s after the Tate
  normalization. B119 makes the required coordinate type automatic.
- **Re-entry condition:** construct G083's selected relation-filtered lift.
  A type condition on the total lift may still matter in a
  different route whose relevant quotient is not already pure Tate.
