---
brick_id: B187
status: PROVED
base_field: C
variety: the second-order ordered-node deformation data of a hypersurface on a smooth projective complex 2n-fold with N labelled ODPs and value rank R<N
smoothness: the ambient variety and nodes are smooth/ordinary double points; the quadratic isotropy conclusion is necessary for a smooth excess incidence
projectivity: inherited from the full projective linear system; the proof is finite-dimensional linear algebra after the ODP Hessian calculation
dimension: N nodal gradient blocks of dimension 2n; value rank R<N; conditional-gradient image dimension at most nN
codimension: a no-coloop value matroid supplies a full-support relation, forcing conditional-gradient corank at least nN and full first-jet defect at least (n+1)N-R
coefficient_field: C for relation spaces and Hessian forms; Q remains required for downstream Hodge detectors
cohomology_theory: second-order ODP deformation theory, value matroids, nondegenerate quadratic forms, and coherent first-jet evaluation
hodge_type: none asserted; downstream relation functionals must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B153, B186, G119
claim: If no node coordinate is a coloop of the rank-R value matroid, in particular for U_(R,N), the value-relation space contains a full-support relation. Its B146 Hessian form is nondegenerate on the 2nN-dimensional gradient target. Therefore quadratic Kuranishi vanishing forces the conditional-gradient image to have dimension at most nN, giving full first-jet rank at most R+nN and defect at least (n+1)N-R.
falsifier: a no-coloop relation space contained in the union of coordinate hyperplanes, a full-support relation whose weighted direct-sum inverse-Hessian form is degenerate, or a totally isotropic conditional-gradient image of dimension greater than nN
---

# B187 — A full-support relation gives a global Lagrangian ceiling

Retain B146's notation

\[
 E:W\longrightarrow\mathcal T=\bigoplus_{i=1}^N L|_{p_i},
 \qquad
 K=\ker E^*,
\]

and let

\[
 D:\ker E\longrightarrow
 G=\bigoplus_{i=1}^N
 (T_{p_i}^*X\otimes L|_{p_i})
\]

be the conditional-gradient map. Each block \(G_i\) has dimension \(2n\)
and carries the nondegenerate inverse-Hessian symmetric form \(B_i\).

## A full-support relation exists

Assume that no coordinate functional vanishes identically on \(K\). This
is exactly the statement that every node occurs in some value relation;
it holds for the uniform matroid \(U_{R,N}\).

For each \(i\), the subspace

\[
 H_i=\{c\in K:c_i=0\}
\]

is then a proper hyperplane of \(K\). Since \(\mathbf C\) is infinite, the
finite union \(\bigcup_iH_i\) cannot cover \(K\). Choose

\[
 c=(c_1,\ldots,c_N)\in K,\qquad c_i\ne0\text{ for every }i. \tag{1}
\]

## Nondegenerate relation form

In local frames, B146's polarized relation form is

\[
 q_c(\lambda,\mu)
 =\sum_{i=1}^N c_i B_i(\lambda_i,\mu_i). \tag{2}
\]

Every coefficient \(c_i\) is nonzero and every \(B_i\) is nondegenerate,
so \(q_c\) is nondegenerate on the \(2nN\)-dimensional space \(G\).

If the quadratic Kuranishi tensor vanishes, B146 gives

\[
 q_c(Da,Db)=0
 \qquad(a,b\in\ker E).
\]

Thus \(U=\operatorname{im}D\) is totally isotropic for a nondegenerate
symmetric form. Over \(\mathbf C\), its dimension is at most half:

\[
 \operatorname{rank}D=\dim U\le nN. \tag{3}
\]

Equivalently, the conditional-gradient corank is at least \(nN\). This
strictly strengthens B146's earlier \(n(R+1)\) floor whenever
\(R+1<N\).

## Full first-jet consequence

The value part has rank \(R\), so evaluation on the first infinitesimal
neighborhood of the \(N\) nodes has rank at most

\[
 R+nN. \tag{4}
\]

Since its target has dimension \((2n+1)N\), its defect is at least

\[
 (2n+1)N-(R+nN)=(n+1)N-R. \tag{5}
\]

The ceiling is sharp as linear algebra: choosing one maximal isotropic
\(\Lambda_i\subset G_i\) at every node gives
\(\bigoplus_i\Lambda_i\) of dimension \(nN\). Sharpness does not imply that
every equality case splits nodewise; NG151 gives a nonsplit equality
example.

## Coefficient guard

The finite-union argument chooses \(c\) in the complex value-relation
space \(\ker E^*\). It need not be a rational vanishing-cycle relation and
is not the Saito detector. B187 uses \(c\) only to prove the complex
conditional-gradient rank ceiling. Rational type and the specified pairing
remain independent downstream obligations.

## Scope guard

B187 is a necessary condition for G119, not a construction. It supplies no
class-directed node configuration, no Hodge type or pairing, and no
quadratic or higher Kuranishi vanishing.
