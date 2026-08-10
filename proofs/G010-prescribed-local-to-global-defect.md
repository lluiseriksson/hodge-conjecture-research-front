---
brick_id: G010
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective X of dimension 2n, a specified primitive rational Hodge class, a global tube or quotiented-thimble detector, and a sought independent-node hyperplane member
smoothness: X and reference hyperplane fibers are smooth; the sought member has only ordinary double points imposing independent conditions
projectivity: X is projective and the hyperplane family comes from a sufficiently high very ample power of the polarization
dimension: dim_C X = 2n and the hyperplane fibers have dimension 2n-1
codimension: middle codimension n; the sought multi-node point lies in a higher-codimension discriminant stratum
coefficient_field: Q
cohomology_theory: primitive Betti homology and cohomology, Lefschetz thimbles, monodromy tubes, local Milnor lattices, nearby and vanishing cycles, intersection cohomology, and mixed Hodge structures
hodge_type: the input is primitive rational type (n,n), or type (0,0) after Tate twist; the sought local relation is rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010-B011, B015-B016, and B022-B025
claim: Every nonzero global tube or quotient-level thimble detector for a specified primitive rational Hodge class can be transferred by an algebraic topology-changing degeneration to a nonzero type-(0,0) kernel element of the local-to-global Milnor map at one independent-node member, with the resulting Saito ambient class retaining nonzero pairing with the specified Hodge class.
falsifier: a polarized smooth projective 2n-fold and primitive rational Hodge class with a nonzero global detector such that every independent-node local-to-global kernel class has zero Saito pairing with it
---

# G010 - Prescribed local-to-global defect

## Falsifiable theorem sought

Let

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}.
\]

Choose a global detector supplied by B011; in the complete-intersection
checkpoint it may be chosen in the quotiented thimble group by B024. Prove
that an algebraic topology-changing degeneration produces an
independent-node member \(Y_0\) and

\[
 0\ne\beta\in
 \ker\!\left(
   \bigoplus_{y\in\operatorname{Sing}Y_0}M_y\otimes\mathbf Q(n)
   \longrightarrow
   H_{2n-1}(Y_\infty,\mathbf Q(n))
 \right)^{(0,0)}
\]

such that

\[
 \langle\zeta,\gamma_\beta\rangle\ne0.
\]

B010 then gives nonzero restriction to \(Y_0\); B007 propagates the universal
statement to the rational Hodge Conjecture. Under universal quantification,
B016 also gives G009 directly.

## Why this is narrower than “collide the critical values”

B025 proves that the complete morsification basis of each isolated
singularity has no internal relation. Therefore the degeneration must force
noninjectivity only after the local Milnor lattices map into the global
nearby fiber. B022-B024 require the source class to survive the global
equator and base-locus quotients; B015 controls the target once an
independent-node member is supplied.

The exact missing morphism is therefore

\[
 \text{global quotient-level detector}
 \dashrightarrow
 \ker(\text{local Milnor}\to\text{global nearby fiber})^{(0,0)}
 \xrightarrow{\ \gamma\ }
 H_{2n}^{\mathrm{prim}}(X,\mathbf Q(n)),
\]

with nonzero pairing preserved end to end.

## Attempt 1 - Use one higher isolated singularity

Morsify the singularity and use all \(\mu\) vanishing cycles. B025 shows
that these cycles form a basis of its Milnor lattice, so the internal kernel
is zero. A relation can arise only from the global embedding map, which the
local singularity classification does not control. This attempt is NG-022.

## Re-entry condition

Construct a global algebraic incidence or degeneration in which the map from
the sum of local Milnor lattices to nearby-fiber homology has a prescribed
kernel vector; prove that the vector survives the B022 ambient quotients,
has rational type \((0,0)\), and maps to a Saito class pairing nontrivially
with \(\zeta\). A Milnor-number count or isolated singularity morsification
alone is insufficient.
