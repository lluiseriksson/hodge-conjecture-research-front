---
brick_id: G104
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and the proper universal hypersurface family base-changed to a basis-node germ F_B
smoothness: X and F_B are smooth; the central hyperplane has exactly N tracked ordinary double points and no other nearby singularities
projectivity: the family is the proper base change of the full projective complete-linear-system incidence
dimension: hyperplane dimension 2n-1; N tracked nodes; value rank R<N; microsupport lies in T^*F_B
codimension: F_B has codimension R in the full linear system; zero internal microsupport forces every extra node branch to contain it
coefficient_field: Q for constructible sheaves, Hodge modules, and zeta
cohomology_theory: rational proper direct images, microsupport, regular holonomic D-modules, Saito mixed Hodge modules, local intersection cohomology, and rational Betti cohomology
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B164, G090-G103, and NG118-NG129
claim: Construct carrier-free full-linear-system nodal data and a basis-node germ F_B such that the proper direct image K_B of the base-changed hypersurface family has microsupport contained in the zero section of T^*F_B, with exhaustive tracked-Morse control, while retaining the superlinear uniform matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: any nonzero internal microsupport covector, an untracked singularity, loss of full-linear-system scope, zero adjoint or ambient rank, or zero specified pairing
---

# G104 — Prove zero microsupport inside the basis-node germ

Let \(i:F_B\hookrightarrow |L|\) and let \(h:\mathcal U\to|L|\) be the
universal hypersurface family. Proper base change gives

\[
 K_B=Li^*Rh_*\mathbf Q_{\mathcal U}
     \simeq Rg_*\mathbf Q_{\mathcal U\times_{|L|}F_B}.
\]

B163 makes the persistence part of G103 exactly

\[
 SS(K_B)\subseteq T^*_{F_B}F_B, \tag{1}
\]

the zero section of the internal cotangent bundle.

G104 asks for (1) without a carrier, together with:

1. B141's superlinear uniform value matroid;
2. isolated multipart nodes and exhaustive singularity control;
3. positive adjoint defect and nonzero primitive ambient image;
4. rational type \((0,0)\) and nonzero pairing with the specified
   \(\zeta\).

Under Riemann--Hilbert, (1) may be tested as absence of nonzero
characteristic covectors for the regular holonomic object underlying the
base-changed Hodge-module direct image. This connects the persistence gate
to the repository's filtered \(D\)-module machinery without identifying
the two distinct obligations: zero escape microsupport and nonzero
relation-channel pairing.

B164/NG130 show that projective decomposition and semisimplicity do not
imply (1). A proof must exclude every positive-codimension strict support or
nontrivial local-system singularity **inside \(F_B\)** for the complete
direct image, not just isolate one favorable summand.
