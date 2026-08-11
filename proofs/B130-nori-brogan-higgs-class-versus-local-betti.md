---
brick_id: B130
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex variety X of dimension 2r with r at least 2 and its universal sufficiently high hyperplane family
smoothness: X is smooth; the incidence family is smooth over P_sm and may be singular over the discriminant
projectivity: X and the full parameter space P are projective; P_sm is quasi-projective
dimension: dim_C X=2r; hyperplane fibers have dimension 2r-1; dim P=d
codimension: middle codimension r on X; the desired local support has parameter codimension at least two
coefficient_field: Q for Betti cohomology, complexified for filtered D-modules and de Rham complexes
cohomology_theory: singular and relative cohomology, variations of Hodge structure, filtered regular holonomic D-modules, de Rham and Higgs complexes, and hypercohomology
hodge_type: primitive type (r,r), equivalently rational type (0,0) after Q(r)
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B012, B128-B132, G008, G086-G088, NG103-NG105, S037, S053 Theorem 1.1, Corollary 4.1, Corollary 5.2, and pp. 13-14
claim: In the universal high-power family, Nori connectivity and Brogan's filtered D-module calculation place every primitive (r,r) component in H^(-d+1)gr_F^(-r)DR(M), but on the smooth locus H^(-d+1)DR(M) is zero; hence Higgs-graded nonvanishing does not imply a local Betti invariant, and the Leray incidence map is not proved in the source to equal the abstract decomposition-theorem map.
falsifier: failure of Brogan's index specialization k=2r, b=r, or nonzero degree-minus-d-plus-one ordinary de Rham cohomology sheaf of a local system shifted by d on P_sm
---

# B130 — Nori-Brogan Higgs class versus local Betti support

**Status:** PROVED

Write the ambient dimension as \(2r\), with \(r\ge2\). In S053/Brogan's
notation the hyperplane dimension is

\[
 n_B=2r-1.
\]

For \(m\gg0\), Theorem 1.1 restates Nori connectivity as

\[
 H^k(P^{\rm sm}\times X,\mathbf Q)
 \xrightarrow{\sim}H^k(\mathcal X^{\rm sm},\mathbf Q)
 \qquad(k<2n_B).
\]

At the incidence degree \(k=2r\), the inequality
\(2r<2(2r-1)\) holds for \(r\ge2\). Thus the smooth universal incidence
restriction is an isomorphism in the degree containing \(q^*\zeta\).

Let \(M\) be the minimal-extension Hodge module of the vanishing-cohomology
variation. Specialize Brogan Corollary 4.1 to

\[
 k=n_B+1=2r,\qquad b=r.
\]

Its hypotheses become \(2r<4r-2\) and \(r<2r-1\), and its degree is
\(-d-n_B+k=-d+1\). The direct sum has only \(j=n_B+1\), so it gives

\[
 H^{r,r}_{\rm prim}(X)\otimes\mathcal O_P
 \simeq
 \mathcal H^{-d+1}\operatorname{gr}^{F}_{-r}\operatorname{DR}(M).
\]

This is a genuine incidence-specific calculation and contains the complex
Hodge component of a primitive rational Hodge class.

## Why it does not give the B128 edge class

On \(P^{\rm sm}\), \(M\) is the flat vanishing-cohomology bundle \(V\), and
Riemann-Hilbert identifies

\[
 \operatorname{DR}(M)|_{P^{\rm sm}}\simeq V_{\mathbf C}[d].
\]

Therefore

\[
 \mathcal H^{-d+1}\operatorname{DR}(M)|_{P^{\rm sm}}=0,
\]

even though the displayed Higgs-graded cohomology sheaf can be nonzero.
Consequently

\[
 \mathcal H^{-d+1}\operatorname{gr}^{F}\operatorname{DR}(M)
 \not\simeq
 \operatorname{gr}^{F}\mathcal H^{-d+1}\operatorname{DR}(M)
\]

in the required sense: the primitive Higgs class is cancelled by filtered
de Rham differentials on the smooth locus.

There is a second typing guard. On p. 14 Brogan constructs a map from a
primitive class using the Leray filtration of the universal incidence and
states that it seems likely to be the Corollary 4.1 map, but that the
coincidence was not checked. It therefore cannot be silently identified with
\([q^*\zeta]_{00}\).

NG105 further audits the smooth-open globalization used in the proof of
Corollary 5.2: (H^0(P^{\rm sm},\mathcal O)) is not generally
(\mathbf C), and projective filtered strictness cannot be invoked on that
open base in the displayed way. B131 proves the rational first-Leray
nonvanishing independently. B132 repairs the filtered identification on the
full projective (P), starting from the canonical incidence class rather
than a chosen decomposition splitting.

## Consequence

Nori connectivity proves smooth-family incidence control, and Brogan
computes its Higgs-graded avatar. B131-B132 now canonically attach that avatar
to the incidence class on full projective (P). None of these results proves
survival in the ordinary rational local cohomology sheaf at a discriminant
point. That exact residual obligation is G088.

## Scope guard

B130 constructs no local support point and no algebraic cycle. It applies in
middle codimension \(r\ge2\); the divisor case \(r=1\) is already covered by
the Lefschetz \((1,1)\)-theorem and is not used to infer the general case.
