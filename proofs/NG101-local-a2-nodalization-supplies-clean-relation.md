---
brick_id: NG101
status: NO-GO
base_field: C
variety: a detecting suspended A2 hyperplane singularity and its local miniversal two-parameter deformation
smoothness: total deformation space smooth; generic discriminant fiber nodal
projectivity: local analytic-algebraic statement; downstream global family projective
dimension: arbitrary suspended fiber dimension; base dimension 2
codimension: cusp discriminant codimension one; desired multinode target absent
coefficient_field: Q
cohomology_theory: local singularity theory, Milnor vanishing cycles, and Saito nodal relation spaces
hodge_type: no type conclusion because the required multinode relation does not exist
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) downstream; no algebraic representative assumed
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B025, B064, B126, G032, G084, NG040
claim: A detecting A2 support point can always be moved inside its local miniversal deformation to one clean multipart nodal fiber carrying a nonzero relation.
falsifier: absence of every two-node fiber in the local miniversal base
---

# NG101 — Local A2 nodalization does not supply a clean relation

**Status:** NO-GO

- **Route:** start at an \(A_2\) support point and use its miniversal
  deformation to obtain one nearby fiber with several nodes and a Saito
  relation.
- **Valid input:** the \(A_2\) Milnor number is two and a morsification has
  two distinguished Morse critical points across the family.
- **Invalid inference:** those critical points occur simultaneously in one
  fiber.
- **Precise obstruction:** B126 proves the cusp normalization
  \(x\mapsto(-3x^2,2x^3)\) is injective. Every noncentral discriminant fiber
  has exactly one node; the central fiber has one \(A_2\) singularity. No
  local parameter has two nodes, so the required one-fiber relation channel
  is absent.
- **Re-entry condition:** use a global topology-changing deformation that
  adds or recollides distinct critical points outside the single local
  versal germ, and prove that the specified restriction/pairing survives.
  This remains G084/G032.
