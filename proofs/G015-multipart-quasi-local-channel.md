---
brick_id: G015
status: EXPLORATORY
base_field: C
variety: a local family of hyperplane sections of a smooth projective complex 2n-fold with a central nodal fiber and a node partition into q independently smoothable blocks
smoothness: the ambient variety and nearby fibers are smooth; the central fiber has only ordinary double points; each block satisfies the audited independent-smoothing hypotheses
projectivity: the ambient family is projective, although the channel calculation is local on its parameter space
dimension: ambient dimension 2n, fiber dimension 2n-1, and q at least 3 in the new case
codimension: middle codimension n on the ambient variety; nodes have codimension 2n
coefficient_field: Q for monodromy, intersection cohomology, vanishing relations, and Hodge data
cohomology_theory: Picard-Lefschetz vanishing cycles, local monodromy Koszul complexes, local intersection cohomology, and limit mixed Hodge structures
hodge_type: the sought relation channel must retain rational type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009, B028, B034-B036, G012-G014, and Green-Griffiths S021
claim: The B009 quasi-local identification of the degree-one local intersection-cohomology channel with the full rational vanishing-cycle relation space extends from two independently smoothable blocks to q blocks.
falsifier: a q-block transverse nodal local model whose blocks are separately independently smoothable but whose degree-one local intersection-cohomology channel is not the full rational relation kernel or does not carry the required type-(0,0) comparison
---

# G015 - Multipart quasi-local relation channel

## Falsifiable theorem sought

Let a nodal central fiber have node set

\[
 \Delta=J_1\sqcup\cdots\sqcup J_q,\qquad q\ge3,
\]

where every \(J_a\) imposes independent smoothing conditions in the local
linear system. Let \(\delta_p\) be the vanishing cycle at \(p\in\Delta\).
Under a multipart analogue of B009's quasi-local normal-crossing
hypotheses, prove a canonical rational isomorphism

\[
 \mathcal H_{\mathrm{loc}}^1
 \simeq
 \ker\!\left(
 \mathbf Q^\Delta\longrightarrow H_{2n-1}(Y_t,\mathbf Q),
 (a_p)\longmapsto\sum_pa_p\delta_p
 \right),
\]

compatible with the limit mixed Hodge structure and Saito's ambient map.

The number \(q\) must be allowed to depend on \(n\). B034 proves that the
fixed-carrier high-power construction requires asymptotically at least
\(n!\) blocks; using any fixed \(q<n!\) cannot recover that route.

## Why the existing theorem does not suffice

B009 imports two cases from Green-Griffiths:

1. the elementary normal-crossing case in which every node is independently
   smoothable;
2. a quasi-local case with a bipartition
   \(\Delta=J\sqcup K\), each part independent.

Neither statement covers a partition into \(q\ge3\) independent blocks when
no union of \(q-1\) blocks is independent.

## Attempt 1 - Induct on the number of blocks

Apply the two-block theorem to \(J_1\) and
\(J_2\cup\cdots\cup J_q\), then repeat. This is invalid: the hypothesis gives
independence of each \(J_a\), not of their union. B034's density calculation
is precisely the regime in which a large union must be dependent. The
induction cannot make its first application. This is NG-032.

## Required calculation

Build the local monodromy complex for the multipart incidence, including all
higher intersections of block discriminants, and compute its degree-one
cohomology before comparing it with local intersection cohomology. A proof
must show that additional Čech/Koszul terms do not quotient out cross-block
relations or add spurious classes. It must then verify rationality and the
type-\((0,0)\) comparison used by B010.

## Attempt 2 - Resolve the smallest three-block arrangement

B035 identifies the minimal simple model as five distinct lines through the
origin of a two-dimensional smoothing slice, with matroid \(U_{2,5}\) and
block sizes \(2+2+1\). Blowing up the origin gives an SNC star whose center
is an exceptional \(\mathbf P^1\) meeting the five strict transforms.

For disjoint ordinary double points, Picard-Lefschetz gives

\[
 N_E=\sum_{i=1}^5N_i,\qquad N_EN_i=0.
\]

Thus every degree-two Koszul term at an individual resolved crossing
vanishes. This does **not** finish the computation. Proper base change leaves
the hypercohomology of the intermediate extension over the entire marked
exceptional \(\mathbf P^1\), followed by isolation of the downstairs IC
summand. Replacing that global calculation by the separate crossing stalks
is NG-033.

The current falsifiable subgate is therefore the explicit \(U_{2,5}\)
calculation: determine the marked-\(\mathbf P^1\) intermediate-extension
quiver for a Picard-Lefschetz representation, and test whether its downstairs
degree-one IC summand is exactly the full five-cycle relation kernel with the
required rational type \((0,0)\).

## Attempt 3 - Determine the missing gluing rank

B036 computes each marked crossing exactly. If
\(W=\operatorname{span}\{\delta_1,\ldots,\delta_5\}\) has dimension \(s\),
then every crossing cokernel is one-dimensional, so their direct sum is
\(C\simeq\mathbf Q^5\). The desired relation space has the exact sequence

\[
 0\longrightarrow R\longrightarrow C
 \xrightarrow{e_i\mapsto\delta_i}W\longrightarrow0.
\]

Therefore the exceptional gluing must impose exactly \(s\) independent
constraints. Up to an isomorphism of its target, the missing differential
has to be the vanishing-cycle map \(e_i\mapsto\delta_i\). What remains is no
longer a dimension guess: derive this map from the Bapat
induction-to-coinduction intermediate-extension module (S035), then compare
its rational mixed-Hodge structure with B010.

## Propagation

G015 alone proves no Hodge class algebraic. If it holds, the fixed-carrier
and unanchored incidence programs may replace the dimensionally impossible
two-block constraint by Edmonds' \(q\)-block inequalities

\[
 |S|\le q\,r_A(S)\qquad(S\subseteq\Delta).
\]

One must still construct positive adjoint defect, positive ambient rank, and
a class-specific nonzero pairing. Failure of G015 would show that the
two-block local channel is a genuine topological bottleneck rather than a
mere combinatorial choice.
