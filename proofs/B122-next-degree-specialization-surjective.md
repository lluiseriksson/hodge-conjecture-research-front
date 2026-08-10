---
brick_id: B122
status: PROVED
base_field: C with rational coefficients
variety: the original plane-net incidence family restricted to a transverse marked collision disk with smooth total space and central fiber having finitely many isolated hypersurface singularities
smoothness: disk pullback total space and punctured fibers smooth; central fiber has isolated hypersurface singularities
projectivity: the original incidence family and disk base change are projective/proper
dimension: hyperplane fibers d=2n-1; disk base dimension 1; total space dimension d+1
codimension: middle cycle codimension n; collision point has disk codimension one
coefficient_field: Q
cohomology_theory: singular Betti cohomology, nearby and vanishing cycles, isolated-singularity Milnor cohomology, and proper specialization
hodge_type: no Hodge type is needed for surjectivity; the resulting lift is rational
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083-B084, B120-B121, S022, S037
claim: For the transverse original collision disk, specialization H^(d+1)(Y_p,Q)->H^(d+1)(Y_t,Q) is surjective because isolated hypersurface vanishing cohomology is concentrated in degree d; hence every rational class in H^0(i^*Psi K_Delta) has an ordinary special lift and is cyclic-monodromy invariant.
falsifier: nonzero isolated hypersurface vanishing cohomology in degree d+1, or a rational degree-(d+1) nearby class outside the specialization image
---

# B122 — Every next-degree disk class has an ordinary lift

**Status:** PROVED

Let \(g:Y_\Delta\to\Delta\) be B120's transverse original disk family and
put

\[
 K_\Delta=Rg_*\mathbf Q_{Y_\Delta}[d+1].
\]

For an isolated hypersurface singularity of a complex \(d\)-fold, S022
Proposition 2 identifies the reduced local vanishing cohomology as zero
outside degree \(d\). The special/nearby/vanishing long exact sequence in
raw degree \(d+1\) therefore contains

\[
 H^{d+1}(Y_p,\mathbf Q)
 \longrightarrow
 H^{d+1}(Y_t,\mathbf Q)
 \longrightarrow 0.
\]

Thus specialization is surjective.

After the disk normalization this is exactly

\[
 H^0(i_p^*K_\Delta)
 \twoheadrightarrow
 H^0(i_p^*\Psi K_\Delta).
\]

Every rational \(t_\Delta\) in the target therefore has a rational ordinary
special lift. Equivalently, its B083 canonical vanishing-cycle obstruction
is zero. Since every specialization image is locally monodromy invariant,
surjectivity also shows that the cyclic monodromy acts trivially on the
entire degree-\((d+1)\) nearby group.

## Exact boundary

This theorem removes the need to make a *raw thimble representative*
monodromy invariant. Such a representative can still acquire a defect in a
B022 kernel; only its image in the actual degree-\((d+1)\) nearby group is
used by the special/nearby triangle.

B122 supplies an ordinary lift, not a lift in B107's relation filtration
step \(S_0\). B121 shows why that distinction is essential: the lift may lie
entirely in the constant \(E_\infty^{-2,1}\) grade. The unresolved condition
remains

\[
 t_\Delta\in u_\Delta(S_0),
\]

equivalently vanishing of B108's filtered obstruction.
