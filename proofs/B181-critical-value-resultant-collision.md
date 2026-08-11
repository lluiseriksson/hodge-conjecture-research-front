---
brick_id: B181
status: PROVED
base_field: C
variety: a one-variable polynomial Morse family with labelled tracked critical points and possible auxiliary critical points; this is the affine prototype of the full critical incidence
smoothness: all critical points are simple with nonzero Hessian; distinct tracked critical points may have the same critical value at the central parameter
projectivity: not used in the resultant identity; homogenization and transfer to arbitrary projective X require separate elimination and boundary audits
dimension: one spatial variable; r critical points; N at least 2 tracked critical values colliding at zero
codimension: the unlabelled critical-value resultant has root multiplicity at least N and therefore is not a simple implicit equation for any individual tracked branch
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: univariate resultants, finite étale critical-point covers, ODP critical values, and conormal escape modules
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157, B172, B179-B180, G113
claim: The resultant Res_z(f'_t(z),w-f_t(z)) is a unit times the product over all critical values w-tau_j(t). At a central member with N distinct tracked critical points of value zero it is divisible by w^N, so its w-derivative vanishes at the origin for N>=2 and it cannot serve as B180's simple labelled equation.
falsifier: failure of the standard resultant product formula, a simple w-root at a common value carried by at least two simple critical points, or recovery of individual labels from the unlabelled product without additional data
---

# B181 — Critical-value resultants collide the labels

Let \(f_t(z)\) be a degree-\(m\) polynomial whose derivative has simple
roots

\[
 p_1(t),\ldots,p_r(t),\qquad r=m-1,
\]

on the chosen parameter neighborhood. Put

\[
 \tau_j(t)=f_t(p_j(t)).
\]

If \(a(t)\) is the leading coefficient of \(f'_t\), the product formula
for the resultant gives

\[
 \mathcal R(t,w)
 =\operatorname{Res}_z(f'_t(z),w-f_t(z))
 =a(t)^m\prod_{j=1}^{r}(w-\tau_j(t)). \tag{1}
\]

The factor \(a(t)^m\) is a unit while the degree remains \(m\).

Suppose \(N\ge2\) distinct tracked critical points are nodes at the
central member. Then

\[
 \tau_1(0)=\cdots=\tau_N(0)=0,
\]

and (1) implies

\[
 w^N\mid\mathcal R(0,w). \tag{2}
\]

Consequently

\[
 \partial_w\mathcal R(0,0)=0. \tag{3}
\]

Thus \(\mathcal R(t,w)=0\) is an algebraic equation for the unordered
critical-value set, but it is not a simple implicit equation for any one
labelled branch at the multinodal collision. B180 cannot be applied to
it directly.

## Exact model

For

\[
 f(z)=(z^2-1)^2,
\]

the critical points are \(-1,0,1\), all Morse, with values \(0,1,0\).
Since \(f'(z)=4z(z^2-1)\), equation (1) gives

\[
 \operatorname{Res}_z(f'(z),w-f(z))
 =4^4w^2(w-1)=256w^2(w-1). \tag{4}
\]

The two tracked zero-value critical points are distinct, but the resultant
has only their doubled unlabelled value.

Taking the squarefree part after specialization changes (4) to a simple
factor \(w\), but collapses the two labels. Moreover squarefree
specialization does not produce analytic factors
\(w-\tau_1(t)\) and \(w-\tau_2(t)\) through a collision. A separating
critical-point coordinate is required.

## Scope guard

B181 does not prevent effective labelled elimination. It proves that G113
must first split the finite étale critical-point cover using data that
separate the critical points, then track the degree of the individual
critical-value branches.
