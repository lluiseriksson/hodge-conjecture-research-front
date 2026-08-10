---
brick_id: NG037
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold and one connected equisingular clean nodal incidence component
smoothness: X and the incidence stratum are smooth enough for the rational relation groups and canonical ambient maps to be local systems
projectivity: X and the hyperplane family are projective
dimension: dim_C X = 2n; nodal fibers have dimension 2n-1
codimension: middle codimension n; the incidence component has arbitrary fixed codimension
coefficient_field: Q
cohomology_theory: nodal relation local systems, monodromy, Saito ambient maps, and primitive Betti homology
hodge_type: relation vectors may have type (0,0) after Q(n), but type does not defeat the rigidity obstruction
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B016, B033, B055, and G028
claim: Whenever the canonical Saito maps assemble as B055's morphism to constant primitive homology, monodromy within one connected equisingular nodal incidence component cannot sweep one nonzero ambient image through new primitive directions.
falsifier: a connected component satisfying B055's local-system hypotheses whose monodromy transports one ambient image to a genuinely different subspace of the fixed primitive homology
---

# NG037 - Equisingular monodromy cannot enlarge the ambient image

## Route tested

Start with one clean \(q\)-block nodal member having
\(\operatorname{rank}\Phi_Y>0\). Use large monodromy on its nodes or relation
space to generate enough translates of \(\operatorname{im}\Phi_Y\) to span
primitive rational Hodge homology and close G028 through B016.

## Precise obstruction

On a connected equisingular component, the relation spaces form a local
system \(\mathcal E\). Whenever the canonical ambient maps assemble as the
required morphism

\[
 \mathcal E\longrightarrow
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\otimes\mathbf Q_S,
\]

B055 gives \(\Phi_s\rho(g)=\Phi_s\) for every loop \(g\). The image in the
fixed ambient homology is constant. Monodromy may permute nodes and alter
vectors inside the kernel, but it cannot manufacture a second ambient
direction.

## Re-entry condition

A viable route must compare distinct incidence components or cross a
topology-changing boundary where one local-system description no longer
applies. It must construct a specialization map on the B022 quotient-level
thimble class, identify the resulting clean nodal relation, and prove that
the specified Hodge pairing remains nonzero. G029 records this boundary
transport gate.
