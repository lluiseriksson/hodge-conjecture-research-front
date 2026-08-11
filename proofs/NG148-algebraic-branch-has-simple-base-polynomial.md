---
brick_id: NG148
status: NO-GO
base_field: C
variety: a one-dimensional smooth base and a rank-two finite etale algebra with two centrally separated labelled points whose numerator values collide
smoothness: the base is smooth and the cover lambda squared equals 1+u is etale at both points over u=0
projectivity: irrelevant to the local algebraic obstruction; the example is an affine etale prototype for a labelled critical algebra
dimension: one base coordinate, one etale coordinate, and one numerator function
codimension: the numerator branch has order one but admits no polynomial relation simple in its value coordinate at the origin
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: finite etale algebras, algebraic analytic branches, minimal polynomials, and implicit equations
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B180-B184, G113-G117
claim: Every algebraic analytic labelled numerator over the original basis germ admits a polynomial relation P(u,z) with nonzero z derivative at its central value.
falsifier: epsilon(u)=u sqrt(1+u) is analytic on the etale branch lambda(0)=1, but its minimal polynomial z squared minus u squared times (1+u) has zero z derivative at the origin and divides every polynomial relation
---

# NG148 — Algebraic branches need not have simple base equations

Consider the finite étale algebra

\[
 A=\mathbf C[u,\lambda]/(\lambda^2-1-u).
\]

Over \(u=0\), the two points have separator values \(\lambda=1,-1\), and
the derivative (2\lambda) is nonzero at both. On the analytic branch
\(\lambda(0)=1\), put

\[
 \epsilon(u)=u\lambda(u)=u\sqrt{1+u}. \tag{1}
\]

This is an algebraic analytic function of order one. Its conjugate is
(-u\sqrt{1+u}), so both values specialize to zero. The minimal polynomial
over \(\mathbf C(u)\) is

\[
 M(u,z)=z^2-u^2(1+u). \tag{2}
\]

It is irreducible because \(1+u\) is not a square in \(\mathbf C(u)\).
If \(P\in\mathbf C[u,z]\) satisfies \(P(u,\epsilon(u))=0\), then \(M\)
divides \(P\) by minimality and Gauss's lemma. Writing \(P=MQ\),

\[
 \partial_zP(0,0)
 =\partial_zM(0,0)Q(0,0)+M(0,0)\partial_zQ(0,0)=0. \tag{3}
\]

Thus no polynomial relation for this labelled numerator is simple in \(z\)
at the origin, despite the critical algebra being étale and the separator
values being distinct.

## Consequence

Effective elimination can compute equations, but it cannot turn this
multiple specialized value into B180's simple equation. G116's
simple-polynomial-over-the-original-base formulation is therefore too
strong.

## Re-entry condition

G117 works on the pointed étale algebraic carrier itself. There the
numerator \(u\lambda\) is a regular polynomial, and B184 bounds its local
order using carrier and numerator degrees without eliminating \(\lambda\).
The full-incidence carrier, its degrees, all required jets, and every Hodge
detector clause remain unproved.
