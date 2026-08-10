---
brick_id: B055
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X and a connected equisingular incidence stratum of clean nodal hyperplane members
smoothness: X is smooth; the incidence stratum is connected and locally path connected; the relation groups and canonical ambient maps are assumed to assemble as local systems
projectivity: X and the hyperplane family are projective
dimension: dim_C X = 2n; nodal fibers have dimension 2n-1
codimension: middle codimension n; incidence codimension is arbitrary but locally constant on the stratum
coefficient_field: Q
cohomology_theory: rational local systems, nodal vanishing-cycle relations, Saito ambient classes, and primitive Betti homology
hodge_type: none asserted by the rigidity theorem; a downstream relation must separately have rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B016, B022-B023, and functoriality of parallel transport
claim: If the nodal relation spaces on a connected equisingular incidence stratum form a local system E and their canonical ambient maps form a morphism E -> H_(2n)(X,Q(n))_prim tensor Q_S, then the ambient image subspace is independent of the fiber and monodromy inside that stratum cannot generate any new primitive direction.
falsifier: a path in such a stratum along which the canonically identified image subspace changes despite the ambient maps forming a morphism to the constant local system
---

# B055 - Equisingular ambient images are rigid

Let \(S\) be connected and locally path connected, let \(\mathcal E\) be a
finite-rank rational local system on \(S\), and let

\[
 \Phi:\mathcal E\longrightarrow V_S
\]

be a morphism to the constant local system with fiber \(V\). In the nodal
application, \(\mathcal E_s\) is the rational relation or extra-homology
space and

\[
 V=H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}.
\]

## Path calculation

For a path \(c:[0,1]\to S\), denote parallel transport in \(\mathcal E\) by
\(T_c\). Naturality of a local-system morphism gives

\[
 \Phi_{c(1)}T_c=\Phi_{c(0)},
\]

because parallel transport in \(V_S\) is the identity. Since \(T_c\) is an
isomorphism,

\[
 \operatorname{im}\Phi_{c(1)}
 =\operatorname{im}\Phi_{c(0)}
 \subseteq V.
\]

Connectedness makes this subspace independent of \(s\in S\). For a loop
with monodromy \(\rho(g)\), the same identity reads

\[
 \Phi_s\rho(g)=\Phi_s.
\]

Thus even arbitrarily large permutation or relation monodromy acts
trivially after passage to the fixed ambient image.

## Nodal consequence

On any connected clean equisingular incidence stratum where Saito's
canonical maps assemble into the displayed morphism, transporting node
labels or relation vectors cannot sweep out more primitive ambient homology
than the image already present at one fiber. Full symmetric monodromy may
prove uniform postulation, as in B033, but it cannot by itself create a new
ambient detector direction.

This is a rigidity statement, not a vanishing theorem. Distinct incidence
components may have different images, and a topology-changing boundary
specialization need not be governed by one local system. Those are precisely
the remaining possibilities.

## Scope guard

The theorem does not prove that the relation spaces form a local system
across collisions, that specialization preserves Saito's map, or that the
union of images over different components is proper. It constructs no
algebraic cycle and proves no Hodge class algebraic.
