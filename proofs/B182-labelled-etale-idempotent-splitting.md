---
brick_id: B182
status: PROVED
base_field: C
variety: a finite étale analytic critical-point algebra over a smooth parameter germ, equipped with an element separating all central tracked critical points
smoothness: the parameter germ is smooth and the critical algebra is finite étale; equivalently all tracked critical points remain Morse
projectivity: not used in the analytic splitting theorem; the intended algebra is obtained by localizing the full projective critical incidence
dimension: arbitrary parameter dimension q and finite critical-algebra rank r; N tracked labels may be a subset of the r factors
codimension: labelled splitting exists even when several critical-value functions coincide; effective degree control is not asserted
coefficient_field: C for Hensel factorization and analytic idempotents; Q remains required only for downstream Hodge detectors
cohomology_theory: finite étale algebras, characteristic polynomials, analytic implicit functions, Chinese remainders, and ODP critical values
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157, B180-B181, G113-G114
claim: Over a convergent analytic local C-algebra, any finite étale critical algebra with a separator whose central values are pairwise distinct splits uniquely into labelled rank-one factors. Explicit Lagrange idempotents recover each critical-value branch even when the values coincide. This closes analytic existence of the labelled splitting but not effective degree or denominator bounds.
falsifier: failure of simple central roots to lift analytically, failure of the Lagrange elements to be orthogonal idempotents, or loss of a critical-value label after splitting
---

# B182 — Labelled idempotents split the étale critical algebra

Let

\[
 O=\mathbf C\{u_1,\ldots,u_q\}
\]

and let \(A\) be a finite étale \(O\)-algebra of rank \(r\). Its central
fiber is

\[
 A/\mathfrak m_OA\simeq\mathbf C^r.
\]

Choose \(\lambda\in A\) whose values

\[
 \lambda_1^0,\ldots,\lambda_r^0
\]

on those \(r\) points are pairwise distinct.

Let \(Q(u,T)\) be the characteristic polynomial of multiplication by
\(\lambda\). It is monic of degree \(r\), and

\[
 Q(0,T)=\prod_{i=1}^r(T-\lambda_i^0). \tag{1}
\]

Every root in (1) is simple. The analytic implicit-function theorem lifts
it uniquely to \(\lambda_i(u)\in O\), and monicity gives

\[
 Q(u,T)=\prod_{i=1}^r(T-\lambda_i(u)). \tag{2}
\]

The map

\[
 O[T]/(Q)\longrightarrow A,
 \qquad T\longmapsto\lambda, \tag{3}
\]

is an isomorphism. Indeed, modulo \(\mathfrak m_O\) it is the evaluation
isomorphism for \(r\) distinct scalars, and both sides are free of rank
\(r\); Nakayama makes (3) invertible.

## Explicit labelled idempotents

Define

\[
 e_i=prod_{j\ne i}
 \frac{\lambda-\lambda_j(u)}{\lambda_i(u)-\lambda_j(u)}\in A. \tag{4}
\]

Every denominator in (4) is a unit because its central value is nonzero.
Equations (2)--(3), or direct evaluation at the roots, give

\[
 e_i^2=e_i,\qquad e_ie_j=0\ (i\ne j),
 \qquad \sum_i e_i=1. \tag{5}
\]

Therefore

\[
 A=\prod_{i=1}^r e_iA\simeq O^r. \tag{6}
\]

For any critical-value element \(v\in A\), its labelled analytic branches
are the components

\[
 \tau_i=e_iv\in e_iA\simeq O. \tag{7}
\]

The separator values \(\lambda_i\), not the possibly coincident values
\(\tau_i\), retain the labels.

## Quartic collision revisited

For \(f=(z^2-1)^2\), take

\[
 A=\mathbf C[z]/(z(z^2-1)),\qquad\lambda=z.
\]

The labelled idempotents are

\[
 e_{-1}=\frac{z(z-1)}2,qquad
 e_0=1-z^2,qquad
 e_1=\frac{z(z+1)}2. \tag{8}
\]

Modulo \(z^3-z\), the critical-value element is

\[
 f(z)=1-z^2=e_0,
\]

so (7) recovers the labelled values \((0,1,0)\), including the two
distinct zero-value factors.

## Scope guard

B182 closes existence of the analytic labelled splitting once a separator
is supplied. It does not bound the algebraic degrees of the lifted roots,
the inverse separator discriminant, the idempotents, or the branch values.
Those effective bounds remain necessary for B180's finite certificate.
