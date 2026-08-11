---
brick_id: B180
status: PROVED
base_field: C
variety: a smooth analytic basis-node germ equipped with local algebraic coordinates and escape functions given as simple implicit algebraic branches
smoothness: the basis-node germ is smooth; each implicit polynomial is unramified in its branch variable at the origin
projectivity: not used in the local degree lemma; the intended source of the algebraic presentations is the projective full-linear-system critical incidence
dimension: arbitrary basis-node dimension q=d-R; finitely many N-R escape functions; polynomial degree bound D
codimension: a nonzero escape ideal has conormal defect visible by jet order at most D-1
coefficient_field: C for polynomial equations and analytic branches; Q remains required only for downstream Hodge detectors
cohomology_theory: algebraic implicit functions, vanishing order, conormal modules, and ODP critical-value deformation theory
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B158-B159, B178-B179, G112
claim: If every escape generator epsilon_i is a simple analytic branch of a polynomial P_i(u,z) of total degree at most D, then either epsilon_i=0 or ord_0(epsilon_i)<=D. Consequently, if K_B is nonzero, beta_K_B has a nonzero coefficient of order at most D-1; checking beta through jet order D-1 is sufficient under this explicit presentation hypothesis.
falsifier: a nonzero simple implicit branch of degree at most D and vanishing order greater than D, or a nonzero escape ideal with every conormal coefficient vanishing through order D-1
---

# B180 — Effective order bound for algebraic escape branches

Let \(u=(u_1,\ldots,u_q)\), and suppose

\[
 P(u,z)=\sum_{k=0}^s a_k(u)z^k\in\mathbf C[u,z]
\]

has total degree at most \(D\), with

\[
 P(0,0)=0,
 \qquad
 \partial_zP(0,0)=a_1(0)\ne0. \tag{1}
\]

Let \(\epsilon\in\mathbf C\{u\}\) be the unique analytic branch with
\(\epsilon(0)=0\) and

\[
 P(u,\epsilon(u))=0. \tag{2}
\]

## Branch-order theorem

Either \(\epsilon=0\), or

\[
 \operatorname{ord}_0\epsilon\le D. \tag{3}
\]

If \(a_0=0\) identically, then

\[
 P(u,z)=z\bigl(a_1(u)+a_2(u)z+\cdots+a_s(u)z^{s-1}\bigr).
\]

The factor in parentheses is a unit at the origin by (1), so (2) forces
\(\epsilon=0\).

Assume \(a_0\ne0\), and put \(m=\operatorname{ord}_0\epsilon\ge1\).
The term \(a_1\epsilon\) has order exactly \(m\), while every term
\(a_k\epsilon^k\) for \(k\ge2\) has order at least \(2m>m\). Equation
(2) therefore gives

\[
 \operatorname{ord}_0 a_0=m. \tag{4}
\]

But \(a_0\) is a nonzero polynomial of degree at most \(D\), so its
vanishing order is at most \(D\). This proves (3).

## Finite conormal certificate under a degree bound

Suppose each escape generator \(\epsilon_i\) of \(K_B\) has a
presentation satisfying (1)--(2) with degree at most \(D\). If
\(K_B\ne0\), let \(m\) be the smallest order of a nonzero generator.
The minimal order of a nonzero element of \(K_B\) is also \(m\), and
(3) gives \(m\le D\).

Some partial derivative of a generator of order \(m\) has order
\(m-1\). It cannot lie in \(K_B\), whose nonzero elements all have order
at least \(m\). Hence B179's conormal map has a nonzero coefficient of
order at most

\[
 m-1\le D-1. \tag{5}
\]

Therefore, under the stated simple algebraic presentations,

\[
 j^{D-1}\beta_{K_B}=0
 \Longrightarrow
 \beta_{K_B}=0
 \Longrightarrow
 H_\tau=0. \tag{6}
\]

## Scope guard

B180 does not construct the polynomials \(P_i\) for the full critical
incidence and does not bound their degrees after restriction to \(F_B\).
Those elimination and coordinate bounds are the new geometric obligation.
Without an explicit \(D\), (6) is not a finite proof certificate.
