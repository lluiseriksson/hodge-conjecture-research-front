---
brick_id: NG155
status: NO-GO
base_field: C
variety: a smooth projective complex variety with a very ample finite-group-linearized polarization and a prospective nodal divisor whose distinct nodes form a nontrivial group orbit
smoothness: the ambient variety is smooth and the proposed nodes are ODPs; the failure concerns the full parameter space rather than local singularity type
projectivity: the variety, very ample embedding, complete linear system, and semi-invariant subfamilies are projective
dimension: arbitrary even dimension 2n; node orbit size N>1; the full section representation contains more than the selected character component
codimension: semi-invariant synchronization controls only a strict subspace of H0(X,L), leaving uncontrolled value and conditional-gradient directions
coefficient_field: C for representations, jets, Hessians, and ranks; Q detector data remain separate
cohomology_theory: finite-group equivariance, coherent first jets, ODP Hessian deformation theory, and complete-linear-system incidence
hodge_type: none produced; no rational type-(0,0) detector or specified pairing follows from symmetry
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B189-B192, G119-G123, NG153
claim: Force G123 one-node determination and conformal Hessian rank one by taking invariant or character-semi-invariant sections along a transitive finite group orbit, then count that synchronized subfamily as the full complete-linear-system incidence.
falsifier: B192 proves the selected character component is strict whenever the orbit has more than one point; omitted isotypic components are full-system deformations not controlled by the synchronized calculation
---

# NG155 — Semi-invariant symmetry synchronizes only a strict subfamily

- **Route:** choose a finite group acting transitively on the nodes and use
  invariant, alternating, or more generally \(\chi\)-semi-invariant
  sections. Equivariance transports their gradients and Hessians between
  nodes, suggesting B190's conformal graph.
- **Valid input:** within one character component, values and jets at an
  orbit are related by the group action and the linearization. A central
  semi-invariant divisor can have a group-stable node set.
- **Invalid inference:** the selected character component is the full
  complete linear system, or every omitted component vanishes to first
  order at all nodes.
- **Precise obstruction:** B192 shows that for a very ample polarization
  and an orbit of size \(N>1\),
  \[
  H^0(X,L)_\chi\subsetneq H^0(X,L)
  \]
  for every character \(\chi\). Otherwise the group acts projectively
  trivially on the very ample embedding and fixes every point, contradicting
  the nontrivial orbit.

The full conditional-gradient quotient is computed from all of
\(H^0(I_ZL)\), not from its chosen semi-invariant part. An omitted isotypic
component may add node-isolated directions, increase \(q\), or raise the
rank of B191's Hessian flattening. Symmetry supplies no automatic inclusion

\[
 H^0(I_ZL)_{\mathrm{omitted}}
 \subset H^0(I_{2Z}L). \tag{1}
\]

- **Relation to NG153:** NG153 excludes an arbitrary selected high-power
  subfamily; NG155 proves that a nontrivial nodal symmetry cannot make the
  single-character selection equal to a very ample full system.
- **Re-entry condition:** an equivariant route must compute every isotypic
  contribution to \(H^0(I_ZL)/H^0(I_{2Z}L)\), prove the one-node kernel
  equalities and rank-one Hessian tensor for their total, and retain the
  rational detector. Otherwise G123 requires a nonsymmetry construction.
