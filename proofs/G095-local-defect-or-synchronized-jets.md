---
brick_id: G095
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and G094 oriented half-double data on N prospective nodes
smoothness: X and support points are smooth; the final nodes must be ordinary double points and the integrated excess germ reduced and smooth
projectivity: X, the oriented scheme, and the linear system are projective
dimension: dim_C X=2n; every projected derivative block has dimension n; total projected rank at most n
codimension: either a local projected block has corank at least one or all N blocks share one codimension-n kernel; final smoothing height R<N
coefficient_field: C for jets, schemes, Hessians, and deformation germs; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: coherent interpolation, local nodal deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final Saito functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146-B151, G092-G094, NG118-NG121, and S062-S064
claim: Realize one B151 branch from (X,zeta) without an algebraic carrier: either a local projected-gradient block defect, or surjective node blocks synchronized through a common n-dimensional quotient; then verify common Hessian isotropy, integrate to a reduced smooth height-R nodal germ, and prove the nonzero specified Saito pairing.
falsifier: generic maximal-rank interpolation, projected rank greater than n, failure of either B151 branch, failure of common relation quadrics or smooth integration, or zero specified pairing
---

# G095 — Realize local jet defect or carrier-free synchronization

B151 splits G094's first-order obligation into two falsifiable cases.

1. **Local defect:** construct a node \(p_i\) for which the projected
   conditional-gradient block has rank \(<n\), while the Hessian remains
   nondegenerate and the global value matroid, defect, primitive image, and
   specified pairing survive.
2. **Synchronization:** make every local block surjective but prove that all
   blocks factor through one common \(n\)-dimensional quotient, without that
   quotient being supplied by motion of a preselected algebraic carrier.

S062/B150 and NG121 exclude general projective-space data. S063 does not
apply after splitting the \(n\) coalesced jets at each support. S064 permits
special degenerations but supplies only an upper-bound mechanism; any
candidate must verify flatness, the exact oriented limit, Hessian
compatibility, B146's common relation quadrics, nonlinear integration, and
the nonzero rational pairing.

The synchronized branch matches the only scalable anchored model currently
known. The local-defect branch is geometrically more singular and has no
known smooth-excess realization. Neither branch is solved.
