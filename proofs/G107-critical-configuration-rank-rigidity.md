---
brick_id: G107
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational middle Hodge class zeta, a high-power complete linear system, and an ordered moving critical-point configuration in fixed local Morse gauges
smoothness: X and the complete-linear-system chart are smooth; the central member has exactly the tracked ODPs and the moving spatial Hessians remain nondegenerate
projectivity: X and the universal hypersurface family are projective
dimension: N tracked nodes; central uniform value rank R<N; moving evaluation maps from the full affine tangent W to N value lines
codimension: the rank-at-most-R evaluation degeneracy locus must contain the full critical-configuration image germ; the resulting simultaneous-node germ has codimension R
coefficient_field: C for evaluation ranks and analytic critical values; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: coherent value evaluation, analytic ODP deformation theory, rational vanishing cycles, Saito local intersection cohomology, and primitive Betti Hodge structures
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B170, G090-G106, NG118-NG134
claim: Construct carrier-free class-directed full-linear-system nodal data and fixed local Morse gauges for which the complete moving critical-point configuration remains inside the rank-at-most-R value-evaluation degeneracy locus, while retaining the superlinear uniform matroid, isolated exhaustive ODPs, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: one nearby parameter where moving critical-point evaluation has rank greater than R, an untracked singularity, failure of the uniform matroid or adjoint/ambient conditions, or zero specified pairing
---

# G107 — Keep the moving critical configuration rank deficient

Let \(W\) be the affine tangent space of the full complete linear system
and

\[
 p:(W,0)\longrightarrow\operatorname{Conf}_N(X)
\]

the ordered critical-point map supplied by the tracked Morse charts. Let
\(\mathcal D_R\) denote the determinantal locus of configurations whose
value evaluation by \(W\) has rank at most \(R\).

G107 asks for the germwise containment

\[
 p(W,0)\subseteq\mathcal D_R. \tag{1}
\]

B170 identifies the moving evaluation map with \(d\tau\). Since the
central rank is \(R\), (1) makes that rank constantly \(R\), forces
\(H_\tau=0\), and closes the geometric clauses of G100--G106.

The construction must simultaneously retain:

1. B141's superlinear uniform value matroid;
2. isolated exhaustive ODPs and the multipart partition;
3. positive adjoint defect and nonzero primitive ambient image;
4. rational type \((0,0)\) and the specified nonzero Saito pairing with
   \(\zeta\).

Condition (1) is intentionally stronger than necessary: a factorized
critical-value ideal can have Jacobian rank jump away from its zero germ.
Its advantage is falsifiability by a single nonzero \((R+1)\)-minor and
its direct expression in the global geometry of moving point evaluations.
The off-discriminant extension \(p\) depends on the chosen local frames;
G107 therefore includes those gauges as data. The resulting implication
to \(H_\tau=0\) is invariant even though the sufficient rank certificate
is not.
NG134 shows that affine-linearity of the hypersurface family does not
establish (1); an actual full-system determinantal mechanism is required.
