---
brick_id: B036
status: PROVED
base_field: C
variety: the U_(2,5) local smoothing-parameter slice of B035 for a projective nodal hyperplane-section family
smoothness: the parameter surface is smooth; the central projective fiber has five ordinary double points; nearby fibers are smooth; the blow-up boundary is simple normal crossing
projectivity: the calculation is local on the parameter surface; the motivating hyperplane-section family and its fibers are projective
dimension: parameter dimension 2; ambient projective variety dimension 2n; nearby fiber dimension 2n-1
codimension: discriminant branches have codimension 1, their common stratum has codimension 2, and downstream algebraic cycles have middle codimension n
coefficient_field: Q
cohomology_theory: symplectic Picard-Lefschetz vanishing homology and the degree-one monodromy complexes at the five resolved crossings
hodge_type: none asserted; the unresolved intermediate-extension comparison must still prove rational type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009, B035, the Picard-Lefschetz formula, and finite-dimensional symplectic linear algebra
claim: For five mutually disjoint nonzero ODP vanishing cycles, every resolved crossing of U_(2,5) has a one-dimensional degree-one monodromy cokernel, so their direct sum is Q^5, whereas the desired relation space is the kernel of the canonical surjection Q^5 -> span(delta_i); hence any exceptional gluing that realizes the desired kernel must impose exactly rank(span(delta_i)) independent constraints and realize that vanishing-cycle map up to target isomorphism.
falsifier: a uniform-sign symplectic Picard-Lefschetz system of five nonzero pairwise orthogonal vanishing cycles for which the exceptional logarithm does not surject onto their span, a resolved crossing cokernel has dimension other than one, or the relation-kernel codimension differs from the span rank
---

# B036 - Exceptional gluing rank

B035 leaves a global intermediate-extension calculation on an exceptional
\(\mathbf P^1\) with five marked crossings. This brick computes the exact
linear algebra that any successful gluing calculation must realize.

## Picard-Lefschetz setup

Let \((V,\langle\ ,\ \rangle)\) be the rational middle homology of a smooth
odd-dimensional fiber, with its nondegenerate alternating pairing. Let
\(\delta_1,\ldots,\delta_5\) be nonzero vanishing cycles supported in
disjoint Milnor balls. Then

\[
 \langle\delta_i,\delta_j\rangle=0\quad(1\le i,j\le5).
\]

After one common choice of Picard-Lefschetz sign, put

\[
 N_i(v)=\langle v,\delta_i\rangle\delta_i,
 \qquad N_E=\sum_{i=1}^5N_i.
\]

Let

\[
 \phi:\mathbf Q^5\longrightarrow W:=
 \operatorname{span}_{\mathbf Q}\{\delta_1,\ldots,\delta_5\},
 \qquad e_i\longmapsto\delta_i,
\]

and write \(R=\ker\phi\) and \(s=\dim W\). The desired B009/G015 target is
\(R\), of dimension \(5-s\).

## Rank of the exceptional logarithm

Define

\[
 A:V\longrightarrow\mathbf Q^5,
 \qquad A(v)=
 (\langle v,\delta_1\rangle,\ldots,
  \langle v,\delta_5\rangle).
\]

Nondegeneracy of the symplectic pairing gives

\[
 \operatorname{im}A=R^\perp,
\]

where orthogonality on \(\mathbf Q^5\) uses the standard positive-definite
rational form. Since \(R\cap R^\perp=0\), the restriction
\(\phi|_{R^\perp}\) is injective. Both its source and target have dimension
\(s\), so it is an isomorphism. As

\[
 N_E=\phi A,
\]

we obtain

\[
 \operatorname{im}N_E=W,
 \qquad \ker N_E=\ker A=igcap_{i=1}^5\ker N_i.
\]

This uses the uniform Picard-Lefschetz sign. Allowing arbitrary independent
sign changes would replace the positive-definite coefficient form by an
indefinite one and invalidate the \(R\cap R^\perp=0\) step; such signs are
not independent geometric choices.

## One crossing contributes one excess generator

At the marked point \(E\cap\widetilde H_i\), the resolved degree-one local
complex is

\[
 V\xrightarrow{\alpha_i}
 \operatorname{im}N_E\oplus\operatorname{im}N_i,
 \qquad
 v\longmapsto(N_Ev,N_iv).
\]

The first component is onto \(W\). Its kernel is contained in \(\ker N_i\),
so \(N_iv\) is determined by \(N_Ev\). Hence \(\operatorname{im}\alpha_i\)
is the graph of a linear map

\[
 W\longrightarrow\mathbf Q\delta_i.
\]

It has dimension \(s\) inside a target of dimension \(s+1\), and therefore

\[
 \dim\operatorname{coker}\alpha_i=1.
\]

The five crossing cokernels consequently form a five-dimensional direct sum
\(C\simeq\mathbf Q^5\), with one generator labeled by each branch.

## Exact missing differential

The full relation space has the tautological exact sequence

\[
 0\longrightarrow R\longrightarrow C\simeq\mathbf Q^5
 \xrightarrow{\phi}W\longrightarrow0.
\]

Thus a resolution calculation that merely adds the five crossing cokernels
overcounts by exactly \(s=\dim W\). If G015 is true in this model, the global
exceptional-divisor differential must have rank \(s\) and kernel \(R\); after
the branch labeling, it must agree with \(\phi:e_i\mapsto\delta_i\) up to an
automorphism of its target.

This is a falsifiable finite target for the remaining quiver computation.
It also strengthens NG-033: the omitted global differential is nonzero
whenever at least one vanishing cycle is nonzero.

## Scope guard

B036 does not prove that the actual intermediate-extension differential is
\(\phi\). It proves what its rank and kernel must be **if** the multipart
relation theorem holds. It does not establish the type-\((0,0)\) comparison,
global projective realizability of the \(U_{2,5}\) slice, or algebraicity of
any Hodge class.
