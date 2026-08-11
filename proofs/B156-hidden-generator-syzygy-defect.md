---
brick_id: B156
status: PROVED
base_field: C
variety: the analytic parameter germ of an ordered-node hypersurface deformation, with critical-value map tau and differential rank R<N
smoothness: the parameter germ is smooth; the central spatial singularities are ordinary double points; smoothness of the simultaneous-node germ is characterized algebraically
projectivity: no projectivity is used in the local-algebra theorem; the intended application is the projective complete-linear-system germ
dimension: smooth parameter dimension d; N critical-value branches; differential rank R; linear relation space dimension N-R
codimension: desired simultaneous-node codimension R; the hidden-generator defect has dimension mu(I_tau)-R
coefficient_field: C
cohomology_theory: convergent analytic local rings, cotangent spaces, Nakayama lemma, syzygy modules, and ordinary-double-point critical values
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B155, Nakayama lemma, and elementary exact-sequence algebra
claim: For a rank-R critical-value germ tau, smooth reduced codimension-R excess is equivalent to each of the following: the ideal I_tau has exactly R minimal generators; the inclusion I_tau/m I_tau -> m/m^2 is injective; every linear relation among the differentials d tau_i(0) lifts to an analytic syzygy among the tau_i; and there are N-R such syzygies with independent values at the origin. The canonical cokernel of syzygy evaluation is the hidden-generator module ker(I_tau/m I_tau -> m/m^2), of dimension mu(I_tau)-R.
falsifier: a rank-R germ satisfying one condition but not the others, or failure of the exact sequence from evaluated analytic syzygies to linear differential relations and then to the hidden-generator module
---

# B156 — The all-order obstruction is a syzygy-lifting defect

Let \((\mathcal O,\mathfrak m)\) be the convergent analytic local ring of a
smooth parameter germ and let

\[
 \tau=(\tau_1,\ldots,\tau_N)\in\mathfrak m^N,
 \qquad I=(\tau_1,\ldots,\tau_N),
 \qquad \operatorname{rank}d\tau_0=R<N.
\]

Write

\[
 K=\operatorname{Syz}_{\mathcal O}(\tau)
 =\left\{a\in\mathcal O^N:\sum_i a_i\tau_i=0\right\}
\]

and let

\[
 L=\left\{c\in\mathbf C^N:\sum_i c_i\,d\tau_i(0)=0\right\}.
\]

Evaluation at the origin maps \(K\) into \(L\). Define the hidden-generator
space

\[
 H_\tau=\ker\left(I/\mathfrak m I\longrightarrow
                    \mathfrak m/\mathfrak m^2\right).
\]

The arrow is induced by \(I\subset\mathfrak m\); it is well defined because
\(\mathfrak m I\subset\mathfrak m^2\).

## Exact defect sequence

There is a canonical exact sequence

\[
 0\longrightarrow \operatorname{ev}_0(K)
 \longrightarrow L\longrightarrow H_\tau\longrightarrow0. \tag{1}
\]

Indeed, the surjection

\[
 \pi:\mathbf C^N\longrightarrow I/\mathfrak m I,
 \qquad c\longmapsto\left[\sum_i c_i\tau_i\right]
\]

has kernel exactly \(\operatorname{ev}_0(K)\). One inclusion is immediate.
For the other, if \(\sum c_i\tau_i\in\mathfrak m I\), write it as
\(\sum b_i\tau_i\) with every \(b_i\in\mathfrak m\). Then \(c-b\in K\)
and \((c-b)(0)=c\). Restricting \(\pi\) to \(L\) lands in \(H_\tau\),
and every hidden-generator class has a constant-coefficient lift in
\(\mathbf C^N\). This proves (1).

The image of

\[
 I/\mathfrak m I\longrightarrow\mathfrak m/\mathfrak m^2
\]

is the span of the first-order parts of the \(\tau_i\), hence has dimension
\(R\). If \(\mu(I)=\dim_{\mathbf C}I/\mathfrak m I\), then

\[
 \dim H_\tau=\mu(I)-R. \tag{2}
\]

## Equivalent all-order certificates

The following are equivalent.

1. The simultaneous-node scheme is reduced and smooth of codimension \(R\).
2. \(\mu(I)=R\).
3. \(H_\tau=0\).
4. Evaluation \(K\to L\) is surjective.
5. There is an \((N-R)\times N\) analytic matrix \(S\), of row rank
   \(N-R\) at the origin, such that \(S\tau=0\).
6. B155's factorization \(\tau=A f\) exists with \(f\) submersive to
   \(\mathbf C^R\) and \(A(0)\) of rank \(R\).

Equivalence of 2 and 3 is (2), while 3 and 4 follow from (1). Conditions 4
and 5 are equivalent by choosing a basis of \(L\) and analytic syzygy lifts.
If 5 holds, a unit maximal minor of \(S\) makes \(\ker S\) a free analytic
rank-\(R\) subbundle. Choose an analytic frame \(A\) of that kernel. Since
\(S\tau=0\), there is an analytic column \(f\) with \(\tau=A f\).
Differentiation gives

\[
 d\tau_0=A(0)df_0.
\]

Both \(d\tau_0\) and \(A(0)\) have rank \(R\), so \(df_0\) has rank \(R\).
Thus 5 implies 6. Conversely, the analytic left-kernel bundle of a
rank-\(R\) matrix \(A\) supplies 5. B155 gives equivalence of 1 and 6.

For completeness, 2 also implies 1 directly. Choose a basis of
\(I/\mathfrak m I\). Nakayama lifts it to generators
\(f_1,\ldots,f_R\) of \(I\); injectivity into
\(\mathfrak m/\mathfrak m^2\) makes their differentials independent. Hence
\(f=0\) is reduced and smooth of codimension \(R\).

## The NG125 family in this language

For \(\tau_m=(x,x+y^m)\),

\[
 I=(x,y^m),\qquad \mu(I)=2,qquad R=1,
\]

and \(H_{\tau_m}\) is one-dimensional, represented by \(y^m\). The linear
relation \((1,-1)\in L\) does not lift to a syzygy nonzero at the origin.
Thus the first-order relation exists, but its exact all-order lift fails.
