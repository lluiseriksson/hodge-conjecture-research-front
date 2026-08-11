---
brick_id: G090
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational Hodge class zeta, and a sought high-power nodal member in |H^m|
smoothness: X is smooth; the member has only isolated ordinary double points; every labeled discriminant branch and the sought saturated simultaneous-node germ are smooth
projectivity: X and the full high-power hyperplane parameter space are projective
dimension: dim_C X=2n with n at least 2; the selected member has N nodes and smoothing-conormal rank R, while every scalable sequence must obey B141's superlinear floor
codimension: middle codimension n on X; the saturated parameter germ has codimension R_m and all branch intersections have codimension min(s,R_m)
coefficient_field: Q for Hodge classes, vanishing relations, and Saito pairings; C for deformation germs and evaluation matroids
cohomology_theory: Betti Hodge structures, nodal vanishing cycles, adjoint coherent defect, evaluation matroids, local intersection cohomology, and filtered Hodge modules
hodge_type: zeta and the selected local relation functional have type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B010, B026-B028, B054, B128, B134-B144, G008, G028, G088, and NG103
claim: For every specified nonzero primitive rational Hodge class, some sufficiently high nodal member has a uniform node set U_(R,N), a smooth codimension-R germ contained in every labeled node branch, positive adjoint defect, and a rational relation whose Saito ambient class pairs nontrivially with the specified class; any construction repeated along unbounded powers must obey B141's superlinear node floor.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class for which every high-power uniform nodal member either lacks a saturated smooth deepest germ, has zero adjoint or ambient rank, or has all relation images in zeta-perp
---

# G090 — Unanchored saturated-stratum incidence

## Falsifiable theorem

Fix

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}
\]

and a very ample \(H\). Construct \(m\), a nodal
\(Y\in|H^m|\), its labeled node branches
\(D_1,\ldots,D_N\), and a relation \(\beta\) such that:

1. the smoothing conormals have uniform matroid \(U_{R,N}\);
2. an actual smooth codimension-\(R\) germ
   \(F\subseteq\bigcap_iD_i\) is constructed without an algebraic
   representative of \(\zeta\);
3. the adjoint defect is positive and the canonical extra-to-primitive map
   has positive rank;
4. \(\langle\zeta,\gamma_\beta\rangle\ne0\).

B144 turns items 1-2 into the full Li-clean nonlinear arrangement. B054
then supplies the rational type-\((0,0)\) local relation channel, and B010
turns item 4 into singular-hyperplane detection. Universal G090 therefore
implies G008 and the rational Hodge Conjecture through B007.

For a scalable construction producing such members along \(m\to\infty\),
B141 additionally forces \(N_m/(mn-c)\to\infty\). That is a design
constraint on repeated high-power realizations, not an extra logical
quantifier needed for one detecting member.

This formulation is stronger than merely asking for one support point, but
it is more concrete than G028's clean-arrangement clause: the entire
nonlinear condition is reduced to construction of one saturated smooth
deepest germ.

## Positive special-family audit

B142-B143 prove all five conditions on
\(\mathbf P^n\times\mathbf P^n\), with

\[
 N=m^n,\qquad R=\binom{m+n}{n}-n,
\]

and \(F\) the moving-fiber incidence. This does not establish universal
G090 because the same algebraic fiber supplies both \(F\) and the nonzero
primitive ambient class.

## Attempt 1 — Use the canonical filtered section

B132 gives, without an algebraic representative,

\[
 0\ne h_m(\zeta)\in
 H^0\!\left(P_m,
 \mathcal H^{-d_m+1}
 \operatorname{gr}_{-n}^F\operatorname{DR}(M_m)\right).
\]

One might try to define \(F\) as its zero locus or its survival locus.
NG115 records the failure. Brogan's calculation identifies the displayed
sheaf with
\(H_{\mathrm{prim}}^{n,n}(X)\otimes\mathcal O_{P_m}\), and
\(h_m(\zeta)\) is the constant nonzero section corresponding to \(\zeta\).
Its zero locus is empty, not a discriminant stratum.

The locus where this filtered class survives to ordinary rational local
intersection cohomology is exactly the unknown support in G088/G008.
Assuming that locus nonempty would assume the terminal-equivalent step; and
even nonemptiness would not prove nodality, uniformity, smoothness, or the
codimension-\(R\) saturation required here.

## Current smallest obligation

Construct \(F\) directly from universal-incidence geometry, not from an
algebraic carrier and not by naming the unknown survival support. It must be
an actual simultaneous-node germ with the exact codimension matching its
uniform smoothing rank. Then prove that its unique or selected adjoint
relation has nonzero B134 functional. No audited theorem presently supplies
this object for arbitrary \((X,\zeta)\).
