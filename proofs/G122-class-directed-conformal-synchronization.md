---
brick_id: G122
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system ordered-node incidence of an arbitrary polarized smooth projective complex 2n-fold with a specified primitive rational middle Hodge class
smoothness: the ambient variety and tracked singularities are smooth/ODP; the final simultaneous-node germ must be reduced and smooth
projectivity: every value, gradient, Hessian, and detector datum must come from the full projective universal family
dimension: N nodes, value rank R<N, and one common conditional-gradient space conformally embedded in all 2n-dimensional node blocks
codimension: force the multiplier vector into the value image so that the complete quadratic relation-Hessian tensor vanishes
coefficient_field: C for synchronization and Hessian linear algebra; Q for the Hodge class, vanishing-cycle detector, and specified pairing
cohomology_theory: coherent first-jet interpolation, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B190, G013, G090-G121, and NG106-NG153
claim: Construct from arbitrary (X,zeta) full-incidence ordered ODP data whose entire conditional-gradient image is conformally synchronized as in B190, whose multiplier vector lies in the no-coloop rank-R value image, and which retains positive adjoint defect, nonzero primitive image, a rational type-(0,0) detector, and nonzero specified Saito pairing.
falsifier: synchronization only in a restricted subfamily, any additional full-system conditional-gradient direction, nonconformal node Hessians, multiplier vector outside the value image, a value coloop, or failure of any detector clause
---

# G122 — Construct class-directed conformal synchronization

B190 supplies a concrete sufficient route through G121 and the full
quadratic gate G119. Starting from arbitrary \((X,\zeta)\), construct a
nodal member in a full complete linear system for which:

1. the value image \(S\subset\bigoplus_iL|_{p_i}\) has rank \(R<N\) and
   no coloop;
2. the **entire** conditional-gradient image, not the image of a chosen
   subfamily, is a synchronized graph of one space \(Q\);
3. the inverse-Hessian restrictions on that graph are conformally equal,
   with multiplier vector \(\lambda\);
4. \(\lambda\in S\);
5. the configuration retains positive adjoint defect, nonzero primitive
   image, a rational type-\((0,0)\) detector, and nonzero specified Saito
   pairing with \(\zeta\).

Items 1--4 imply \(H(U)\subset S\) by B190. Hence every value relation
annihilates the quadratic Kuranishi tensor, while the no-coloop condition
supplies a full-support relation. This is stronger than G121 and is a
genuine sufficient precursor to G119.

B189 adds an immediate audit: for every node \(i\), the isolated-gradient
map

\[
 H^0(X,I_{\Theta_i}\otimes L)\longrightarrow
 T_{p_i}^*X\otimes L|_{p_i}
\]

must have inverse-Hessian isotropic image of dimension at most \(n\). In
the exact graph model that image is zero when \(N>1\).

Even success at G122 would close only the quadratic Kuranishi rung. The
cubic and higher obligations of B186 remain, as do smooth integration and
the terminal cycle construction. B191/G123 give the intrinsic coherent
form of this gate. NG154 shows that the B142-B143 moving-fiber witness does
not satisfy it: its full conditional-gradient image is too large to be
determined by any one node.
