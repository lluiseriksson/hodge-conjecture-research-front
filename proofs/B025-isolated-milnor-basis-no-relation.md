---
brick_id: B025
status: PROVED
base_field: C
variety: the germ of an isolated complex hypersurface singularity f:(C^{m+1},0)->(C,0), its morsification, and its Milnor fiber; in the Hodge application the germ is embedded in a singular projective hyperplane section
smoothness: the central hypersurface germ is singular only at the origin; a morsification has only nondegenerate critical points with distinct critical values; the Milnor fiber is smooth with boundary
projectivity: not assumed for the local theorem; projectivity is required only for the later global hyperplane-family application
dimension: the Milnor fiber has complex dimension m and its vanishing cycles lie in middle homology H_m
codimension: local hypersurface codimension 1; the global Hodge application concerns middle codimension n on an ambient 2n-fold
coefficient_field: Z for the Milnor lattice and Q for relation kernels
cohomology_theory: reduced singular homology of the Milnor fiber, Milnor lattice, morsification, Picard-Lefschetz vanishing cycles, and local-to-global homology
hodge_type: no Hodge type is asserted locally; rational type (0,0) is a separate condition on a global Saito relation
cycle_class_map: not involved locally; the global application uses CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: not applicable locally; rational equivalence in the global projective application
scope: fiberwise
dependencies: Brieskorn Appendix and Ebeling Theorem 3/Corollary 4 (S030), and B009-B010 for the global relation channel
claim: The vanishing cycles of a distinguished morsification of one isolated hypersurface singularity form an integral basis of its Milnor lattice, so they have no nontrivial internal rational relation; any Saito relation in a projective singular fiber must come from the kernel of the map from the direct sum of local Milnor lattices to global nearby-fiber homology.
falsifier: a distinguished morsification whose vanishing cycles satisfy a nonzero rational relation in the Milnor lattice, or whose number differs from the Milnor-lattice rank
---

# B025 - Isolated Milnor bases have no internal relation

Let

\[
 f:(\mathbf C^{m+1},0)\longrightarrow(\mathbf C,0)
\]

have an isolated hypersurface singularity with Milnor number \(\mu\). Its
Milnor fiber \(F\) has reduced middle homology

\[
 M=\widetilde H_m(F,\mathbf Z),
\]

a free module of rank \(\mu\). Brieskorn's appendix proves this rank by a
morsification with \(\mu\) nondegenerate
critical points with distinct critical values. Ebeling's Theorem 3, citing
Brieskorn, states that the associated distinguished vanishing cycles

\[
 (\delta_1,\ldots,\delta_\mu)
\]

form a \(\mathbf Z\)-basis of \(M\). Corollary 4 gives the same conclusion
for a weakly distinguished system. In the original appendix Brieskorn also
states that the \(\mu\) transported integral cycles generate the free
rank-\(\mu\) middle homology, which yields the same basis conclusion.

Consequently the map

\[
 \mathbf Q^\mu\longrightarrow M\otimes\mathbf Q,
 \qquad e_i\longmapsto\delta_i
\]

is an isomorphism. Its kernel is zero. No choice of distinguished paths,
Hurwitz moves, or orientations can produce a nonzero rational relation
among the complete local morsification basis.

## Consequence for collision strategies

Replacing several Morse critical values by one higher isolated singularity
does not create the required relation **inside that singularity's Milnor
lattice**. In a projective singular hyperplane with singular points \(y\),
the relevant relation space must instead be a kernel of the global map

\[
 \bigoplus_y M_y\otimes\mathbf Q
 \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n)).
\]

Thus the non-invertible content sought in G007/G009 is global embedding
defect: local basis elements from one or more singularities must become
dependent only after mapping into the nearby projective fiber.

## Scope guard

The theorem does not say the local-to-global map is always injective. Nodal
defect and Saito relations are precisely failures of that map to be
injective. It says only that such failures cannot be inferred from the
internal Milnor topology of a single isolated singularity or from its Milnor
number alone.
