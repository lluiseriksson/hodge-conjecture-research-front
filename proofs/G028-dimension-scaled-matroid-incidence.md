---
brick_id: G028
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective 2n-fold and a high-power nodal hyperplane member with node-smoothing evaluation matroid
smoothness: the ambient variety and nearby hyperplane sections are smooth; the selected central member has only ordinary double points and the sought incidence strata form a clean arrangement
projectivity: the ambient variety and hyperplane family are projective
dimension: ambient dimension 2n, with a number q of smoothing blocks allowed to scale with n
codimension: middle codimension n; node conditions have their standard first-jet codimension
coefficient_field: Q
cohomology_theory: node-smoothing evaluation matroids, adjoint defect, rational vanishing-cycle relations, and Saito detector classes
hodge_type: the selected relation must have type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B010, B016, B028, B034, B054, G012-G015, and G019
claim: For every specified nonzero primitive rational Hodge class, some high-power nodal member has a clean node incidence whose smoothing matroid partitions into a dimension-scaled number q of independent blocks, has positive adjoint defect and positive extra-to-primitive rank, and contains a rational type-(0,0) relation pairing nontrivially with the class.
falsifier: a polarized smooth projective variety and primitive rational Hodge class for which every clean q-block nodal relation at every high power either violates the q-matroid partition inequalities, has zero adjoint/ambient rank, or has zero class pairing
---

# G028 - Dimension-scaled class-paired nodal incidence

B054 removes the multipart local-topology obstruction. The next gate returns
to geometry and the specified Hodge class.

For a node set \(\Delta\) with smoothing-evaluation rank function \(r_A\),
Edmonds' \(q\)-matroid partition criterion requires

\[
 |S|\le q\,r_A(S)\qquad(S\subseteq\Delta).
\]

The sought member must satisfy these inequalities for some \(q=q(n)\), have
positive adjoint corank, and have a relation whose canonical
extra-to-primitive image pairs nontrivially with the specified class. Its
discriminant intersections must satisfy B054's clean-arrangement hypothesis.

B034 shows why \(q\) must scale at least factorially in the fixed-carrier
model. B054 proves that increasing \(q\) causes no further local IC loss. It
does not supply the member, the positive ambient map, or the class-specific
pairing. Choosing an algebraic carrier with the desired class would be
circular and remains forbidden.
