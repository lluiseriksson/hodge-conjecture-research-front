---
brick_id: B190
status: PROVED
base_field: C
variety: finite value, conditional-gradient, and inverse-Hessian data of an ordered ODP configuration intended to arise from a full projective linear system
smoothness: every gradient block carries a nondegenerate ODP inverse-Hessian form; no nonlinear incidence smoothness is inferred
projectivity: inherited from the intended full projective incidence; the theorem itself is finite-dimensional linear algebra
dimension: N value lines, value rank R<N, and one common conditional-gradient space conformally embedded in every 2n-dimensional node block
codimension: conformal synchronization with its multiplier vector in the value image makes the entire Hessian-pairing span lie in the value image
coefficient_field: C for the sufficient quadratic mechanism; Q remains required for the rational Hodge detector and specified pairing
cohomology_theory: ODP second-order deformation theory, value matroids, and symmetric bilinear algebra
hodge_type: none asserted; downstream detector data must be rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146-B153, B187-B189, and G119-G121
claim: If the full conditional-gradient image is a common space conformally synchronized across all node Hessians and the vector of conformal multipliers lies in the value image S, then H(U) is contained in S. Thus every value relation makes U isotropic, the augmented map has image S of rank R<N, and a full-support relation exists whenever the value matroid has no coloop.
falsifier: a conformally synchronized image whose Hessian-pairing span is not contained in the multiplier line, a multiplier vector in S but H(U) not contained in S, a value relation with nonzero quadratic form on U, or a no-coloop value matroid with no full-support relation
---

# B190 — Conformal synchronization is sufficient for the quadratic rung

Let

\[
 S=\operatorname{im}E\subset\mathcal T=\bigoplus_{i=1}^N\mathcal T_i,
 \qquad \operatorname{rank}E=R<N.
\]

Assume there are a vector space \(Q\), a nonzero symmetric pairing
\(B_Q:Q\times Q\to\mathbf C\), and injective maps

\[
 \phi_i:Q\longrightarrow G_i
\]

such that the **full** conditional-gradient image is the synchronized graph

\[
 U=\{(\phi_1q,\ldots,\phi_Nq):q\in Q\}, \tag{1}
\]

and, after choosing local frames of the value lines,

\[
 B_i(\phi_iq,\phi_iq')=\lambda_i B_Q(q,q') \tag{2}
\]

for one multiplier vector
\(\lambda=(\lambda_1,\ldots,\lambda_N)\in\mathbf C^N\).

## Hessian span

For \(u=\phi(q)\) and \(v=\phi(q')\), B188's map is

\[
 h_U(u\odot v)=B_Q(q,q')\lambda. \tag{3}
\]

Therefore

\[
 H(U)\subseteq\mathbf C\lambda. \tag{4}
\]

If \(B_Q\ne0\), equality holds. Suppose now that

\[
 \lambda\in S. \tag{5}
\]

Then \(H(U)\subset S\), so the augmented map of B188 has

\[
 \operatorname{im}A_U=S+H(U)=S,
 \qquad \operatorname{rank}A_U=R<N. \tag{6}
\]

More strongly, for every value relation \(c\in S^\perp\),

\[
 q_c(u,v)=c(h_U(u\odot v))=0. \tag{7}
\]

Thus (1), (2), and (5) kill B146's complete quadratic relation-Hessian
tensor, not merely one selected relation. They provide a finite sufficient
mechanism for G119's quadratic rung.

## Full support

If the value matroid has no coloop, no value line \(\mathcal T_i\) is
contained in \(S\). Equivalently, no coordinate vanishes identically on
\(S^\perp\). Since \(S^\perp\ne0\) and \(\mathbf C\) is infinite, the
finite-union argument gives a full-support relation in \(S^\perp\).
Together with (6), this also solves the finite B188/G121 condition.

For example, take distinct \(t_1,\ldots,t_N\), let \(S\) be the rank-
\(R\) Vandermonde evaluation space of polynomials of degree below \(R<N\),
take \(\lambda=(1,\ldots,1)\in S\), and use identical \(B_i\) and diagonal
\(\phi_i\). This realizes the mechanism in finite linear algebra for every
\(1\le R<N\).

## Scope guard

B190 does not prove that the full conditional-gradient image of an
arbitrary projective complete linear system has form (1). It constructs no
adjoint defect, primitive image, rational detector, specified pairing,
higher Kuranishi vanishing, smooth integration, or algebraic cycle. B191
recasts every hypothesis intrinsically on the full coherent jet quotient;
there is no freedom to replace that quotient by a smaller family.
