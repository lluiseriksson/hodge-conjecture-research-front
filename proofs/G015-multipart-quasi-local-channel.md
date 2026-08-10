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
dependencies: B009-B010, B028, B034-B042, G012-G014, Green-Griffiths S021, and Saito S022/S037
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

## Attempt 4 - Locate the exceptional Postnikov class

B037 computes the cohomology sheaves of the resolved complex on
\(E\simeq\mathbf P^1\): the constant sheaf
\(K=\ker N_E\) in degree zero and five rank-one skyscrapers in degree one.
Therefore

\[
 \mathbb H^1(E,\mathcal B_E^\bullet)
 =\ker\!\left(d_2:\mathbf Q^5\to H^2(E,K)\simeq K\right).
\]

The topological subgate is now the residue calculation
\(d_2(e_i)=\delta_i\). Even if this is proved, B035's downstairs IC-summand
identification remains. In addition, S035's face algebra is formulated over
\(\mathbf C\) and carries no mixed-Hodge-module structure, so the quiver
calculation alone cannot establish rationality or type \((0,0)\). This
separate mismatch is NG-034.

## Attempt 5 - Compute the residue transgression

B038 uses the Green–Griffiths logarithmic residue complex and the residue
sequence on the five-marked exceptional \(\mathbf P^1\) to prove

\[
 d_2(a_1,\ldots,a_5)=\sum_i a_i\delta_i.
\]

Thus the **resolved exceptional contribution** in the minimal three-block
model is exactly the full rational relation kernel. The comparison is made
on the rational Betti side; the universal \(2\pi i\) de Rham normalization is
not miscounted as a Hodge-type proof.

This closes the residue subgate but not G015. The next obligation is to
separate this group from point-supported summands in the proper direct image
and identify it with the downstairs intermediate-extension stalk. Only then
may the mixed-Hodge type and general multipart arrangement be addressed.

## Attempt 6 - Descend through the blow-up

B039 applies proper base change and Saito's projective direct-image theorem
with the actual geometric rational variation as coefficient. A direct
stalk/costalk amplitude calculation shows that the shifted direct image is
perverse. Strict-support decomposition then has the form

\[
 R\pi_*IC_{\widetilde B}(L_{\mathbf Q})
 \simeq IC_B(L_{\mathbf Q})\oplus i_{0*}H_0[-2].
\]

The point-supported term occurs in ordinary degree two because the base is
a surface. It therefore cannot change degree one. Consequently B038's
resolved relation kernel is canonically the degree-one stalk of the
downstairs intermediate extension.

This closes the topological/intersection-cohomology calculation for the
minimal \(U_{2,5}\) arrangement. It does not close G015: the next falsifiable
obligation is to compute the Hodge structure and Tate normalization of this
specific relation kernel. Only after that comparison succeeds is extension
to arbitrary multipart arrangements justified.

## Attempt 7 - Compute the Tate type

B040 applies Saito Proposition 1.7 at the five resolved crossings. With the
explicit \(\mathbf Q(n)\) normalization from B010, every local crossing group
is \(\mathbf Q(0)\). The B038 transgression is a morphism of rational mixed
Hodge structures, so its kernel is a sub-Hodge structure of
\(\mathbf Q(0)^5\), hence is pure of type \((0,0)\). B039 transfers that
structure to the downstairs IC stalk.

Thus the full rational topological and Hodge-theoretic statement is proved
for the minimal \(U_{2,5}\) model. G015 remains open because this rank-two
calculation does not control wonderful resolutions of higher-rank
arrangements or their additional exceptional-stratum differentials. The
next falsifiable subgate is to generalize first to \(U_{2,r}\), where the
exceptional locus is still a single marked \(\mathbf P^1\), before allowing
higher arrangement rank.

## Attempt 8 - Uniform rank-two generalization

B041 checks that no step in B035-B040 depends on \(r=5\). For every
\(U_{2,r}\), one blow-up produces a marked exceptional \(\mathbf P^1\), the
residue transgression is

\[
 (a_i)\longmapsto\sum_i a_i\delta_i,
\]

point-supported direct-image summands occur only in ordinary degree two,
and the source is \(\mathbf Q(0)^r\). Hence the downstairs degree-one IC
stalk is the full type-\((0,0)\) relation kernel for every \(r\ge3\).

The narrowest unresolved higher-rank gate is \(U_{3,7}\). Its exceptional
\(\mathbf P^2\) contains seven pairwise-transverse lines and their
pair-intersection strata, so the marked-curve two-row argument no longer
applies without a new incidence spectral-sequence computation.

## Attempt 9 - First higher-rank incidence calculation

B042 computes that spectral sequence, uniformly for \(U_{3,r}\). At a
pair-intersection point, the local degree-one group is canonically the
direct sum of the two incident line generators. Thus

\[
 \mathcal H^1(A|_{\mathbf P^2})
 =\bigoplus_i\mathbf Q_{L_i},
\]

with no additional skyscraper term. The logarithmic residue sequence on
\(\mathbf P^2\) again gives \(d_2(e_i)=\delta_i\).

The threefold blow-up is not semismall, but its direct image has perverse
amplitude \([-1,1]\). After undoing the dimension-three shift, all
point-supported summands lie in ordinary degrees \(2,3,4\), so degree one
still descends to the full-support IC summand. Saito's normal-crossing
calculation makes the resulting kernel pure type \((0,0)\).

The calculation suggests a dimension-uniform pattern for simple uniform
arrangements. The next falsifiable subgate is to prove or refute that pattern
for \(U_{d,r}\) in arbitrary rank, including the exact perverse-amplitude
bound for the blow-up of a \(d\)-fold at the origin.

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
