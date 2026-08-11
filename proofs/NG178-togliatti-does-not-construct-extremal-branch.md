---
brick_id: NG178
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds in G145 versus special projected Veronese or smooth toric varieties arising from Togliatti systems
smoothness: the audited examples may be smooth, but their general-point osculating defect does not imply G145's marked common-osculator equality or nodal-incidence smoothness
projectivity: both settings are projective; the audited Togliatti mechanism is confined to special linear systems and projections of Veronese varieties
dimension: arbitrary 2n in G145; audited classifications are restricted to special cubic monomial systems or specified projected Veronese families
codimension: failure of WLP corresponds to smaller-than-expected osculating dimension, not equality of the full second osculators at all marked nodes
coefficient_field: characteristic-zero algebraically closed fields in the audited WLP mechanism; C in G145 and Q for its detector
cohomology_theory: artinian graded multiplication, apolarity, and osculating spaces in the audited sources; primitive rational cohomology and Saito pairing are absent
hodge_type: no arbitrary rational type-(0,0) detector or specified Hodge-class pairing is supplied
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not addressed by the audited Togliatti theorems
cycle_equivalence: rational equivalence remains the terminal relation and is absent from the audited construction
scope: absolute
dependencies: B216, G145, S077
claim: Invoke the existence or classification of Togliatti systems, WLP failures, or Laplace equations as a construction of G145 for arbitrary (X,zeta).
falsifier: S077 proves only an equivalence for special degree-d artinian systems and projected Veronese varieties, with osculating dimension deficient at a general point; it supplies neither a common full marked osculator nor any class-directed nodal detector clause.
---

# NG178 — Togliatti defect does not construct the equality branch

- **Route:** identify B216's common-osculator rigidity with the classical
  Laplace-equation/Togliatti mechanism and import its examples.
- **Valid input:** S077 relates failure of a Weak Lefschetz multiplication
  map to deficient \((d-1)\)-osculating spaces of an apolar projected
  Veronese variety. Smooth toric cubic cases provide explicit examples.
- **Invalid inference:** a deficient osculator at a general point is a
  common *full* second osculator at all nodes of one marked scheme.

The Togliatti sources start with special artinian ideals or monomial cubic
systems. They do not take an arbitrary smooth projective \(X\), do not
construct ordinary double points with the G143 central profile, and do not
produce a rational type-\((0,0)\) detector pairing nontrivially with a
specified arbitrary primitive Hodge class.

- **Precise obstruction:** mismatch of variety, quantifiers, osculating
  condition, and detector data.
- **Re-entry condition:** prove a comparison theorem that transports a
  Togliatti construction to arbitrary \((X,\zeta)\), yields (1)-(2) of
  G145 at every marked node, and preserves all profile and detector clauses.
