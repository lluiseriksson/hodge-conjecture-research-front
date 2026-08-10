---
brick_id: B016
status: PROVED
base_field: C
variety: a fixed polarized smooth projective X of dimension 2n and any specified collection of singular hyperplane members across powers of the polarization
smoothness: X is smooth; members in the detector collection may be singular and must satisfy the hypotheses needed for their Saito relation classes
projectivity: X is projective and L is ample, with singular members drawn from very ample powers mL
dimension: dim X = 2n and singular hyperplane fibers have dimension 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: primitive singular Betti cohomology and homology, Poincare duality, polarization, and vanishing-cycle mixed Hodge structures
hodge_type: primitive type (0,0) after Tate twist on both cohomological test classes and homological detector classes
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no surjectivity is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010 for Saito detector classes; Hodge-Riemann bilinear relations and Poincare duality
claim: For any collection C of singular members, every nonzero primitive rational Hodge class is detected by some Saito relation in C if and only if the associated detector classes span the primitive rational Hodge homology of X.
falsifier: a detector collection for which pointwise nonzero pairing holds but the detector span is proper, or whose span is full but some nonzero primitive Hodge class pairs trivially with every generator
---

# B016 - Detector-span equivalence

Let

\[
 H_{\mathrm{Hdg}}=
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}
\]

and let \(H_{\mathrm{Hdg}}^\vee\) denote the type-\((0,0)\) primitive rational
homology under Poincare duality. The polarization pairing

\[
 \langle-,-\rangle:
 H_{\mathrm{Hdg}}\times H_{\mathrm{Hdg}}^\vee\longrightarrow\mathbf Q
\]

is perfect. Indeed, the primitive Hodge-Riemann bilinear relations make its
restriction to the real \((0,0)\) subspace definite up to the conventional
sign, hence nondegenerate; rationality then gives the stated perfect pairing.

Fix any collection \(\mathcal C\) of singular hyperplane members, possibly
over several powers of \(L\), together with all relations
\(\beta\in R(Y)_1^{(0,0)}\) to which B010 applies. Define

\[
 D_{\mathcal C}=
 \operatorname{span}_{\mathbf Q}
 \{\gamma_\beta:(Y,\beta)\in\mathcal C\}
 \subseteq H_{\mathrm{Hdg}}^\vee.
\]

Then the following are equivalent:

1. every \(0\ne\zeta\in H_{\mathrm{Hdg}}\) satisfies
   \(\langle\zeta,\gamma_\beta\rangle\ne0\) for some
   \((Y,\beta)\in\mathcal C\);
2. \(D_{\mathcal C}=H_{\mathrm{Hdg}}^\vee\).

If (2) holds, perfection of the pairing supplies a detector for each nonzero
\(\zeta\); if every generator paired trivially, every element of their span
would as well. Conversely, (1) says the annihilator of \(D_{\mathcal C}\) in
\(H_{\mathrm{Hdg}}\) is zero. Perfection implies
\(\dim D_{\mathcal C}=\dim H_{\mathrm{Hdg}}^\vee\), proving (2).

## Two choices of collection

- If \(\mathcal C\) contains every singular member in every sufficiently high
  power, B007 and B010 identify (1), hence (2), with the terminal universal
  singularity statement.
- If \(\mathcal C\) contains only independent-node members covered by B015,
  equality of spans is a stronger sufficient theorem. No converse from the
  Hodge Conjecture to this restricted equality is claimed without an
  additional incidence theorem.

## Scope guard

This brick is finite-dimensional Hodge linear algebra. It does not show that
any detector class exists, that the restricted detector span is nonzero, or
that it exhausts the Hodge subspace.
