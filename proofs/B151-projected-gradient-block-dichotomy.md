---
brick_id: B151
status: PROVED
base_field: C
variety: the finite conditional-gradient data of a G093-G094 ordered N-node configuration on a smooth projective complex 2n-fold
smoothness: the ambient variety and node supports are smooth; no nonlinear incidence smoothness is inferred
projectivity: inherited from the downstream projective linear system; the theorem itself is finite-dimensional linear algebra
dimension: every projected-gradient block Q_i has dimension n and the total projected rank is at most n
codimension: either one local block has positive corank, or all block kernels coincide and have codimension n in ker E
coefficient_field: C
cohomology_theory: first-jet nodal deformation theory and finite-dimensional linear algebra
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B148-B150, G093-G094, and rank-nullity
claim: If P=(P_i):V -> direct_sum_i Q_i has rank at most n with every Q_i n-dimensional, then either some P_i is not surjective, or rank P=n and every P_i descends from the same n-dimensional quotient V/ker P through an isomorphism. In the second branch all kernels ker P_i equal ker P and the node blocks are mutually synchronized.
falsifier: total rank at most n, all n-dimensional blocks surjective, and either total rank below n, unequal block kernels, or failure of the induced quotient maps to be isomorphisms
---

# B151 — Low projected rank is local defect or global synchronization

Write G093's projected conditional-gradient map as

\[
 P=(P_1,\ldots,P_N):
 V=\ker E_Z\longrightarrow\bigoplus_{i=1}^N Q_i,
 \qquad \dim Q_i=n,
\]

and assume \(\operatorname{rank}P\le n\).

There are exactly two branches.

## Local-defect branch

Some block has

\[
 \operatorname{rank}P_i<n.
\]

Then even the \(n\) oriented derivative conditions at that single node fail
conditional interpolation. This is a local first-jet defect and must be
constructed and integrated explicitly.

## Synchronized branch

Assume every \(P_i\) is surjective. Then

\[
 n=\operatorname{rank}P_i
 \le\operatorname{rank}P\le n,
\]

so \(\operatorname{rank}P=n\). Put \(Q=V/\ker P\). Each \(P_i\) factors
through a surjection

\[
 \overline P_i:Q\longrightarrow Q_i.
\]

Both sides have dimension \(n\), so every \(\overline P_i\) is an
isomorphism. Consequently

\[
 \ker P_i=\ker P
\]

for all \(i\), and after choosing node \(1\),

\[
 P_i=\phi_iP_1,\qquad
 \phi_i=\overline P_i\overline P_1^{-1}:Q_1\xrightarrow{\sim}Q_i.
\]

Thus all \(nN\) oriented gradients are synchronized by a single
\(n\)-dimensional quotient. B148's product-fiber example lies in this
branch: transversality makes every local \(d\sigma_i\) invertible, and the
common quotient is carrier motion. B151 does not turn the abstract quotient
into an algebraic carrier or prove B146's relation quadrics.
