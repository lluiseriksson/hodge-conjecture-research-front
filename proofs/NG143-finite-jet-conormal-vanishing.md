---
brick_id: NG143
status: NO-GO
base_field: C
variety: the B159 family of projectively realizable ordered ODP critical-value germs with uniform conormal matroid and high-order basis-node escape
smoothness: the parameter germ, every branch, and every intersection of at most R basis branches are smooth; the full simultaneous germ has a hidden generator
projectivity: B157-B159 provide sufficiently ample projective finite-jet realization over a generally nonlinear analytic base, not a full-system impossibility theorem
dimension: arbitrary R<N and arbitrary prescribed finite jet order q; the decisive escape occurs on one transverse coordinate y
codimension: the conormal defect vanishes through order q but is nonzero and the simultaneous ideal has one hidden generator
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: analytic conormal modules, finite jets, uniform evaluation matroids, and ODP critical-value deformation theory
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B159, B176-B179, G112
claim: Vanishing of the conormal escape defect beta_K_B to one fixed finite jet order forces beta_K_B=0 and H_tau=0.
falsifier: for m at least q+2, K_m=(y^m) has beta([y^m])=m y^(m-1)dy, whose q-jet is zero but which is nonzero modulo y^m
---

# NG143 — Finite conormal jets do not close persistence

Fix any finite jet order \(q\ge0\), and choose \(m\ge q+2\). In B159's
uniform high-order escape family, restriction to a basis-node germ gives

\[
 K_m=(y^m).
\]

B179 computes

\[
 \beta_{K_m}([y^m])
 =m y^{m-1}dy\pmod {y^m}. \tag{1}
\]

Because \(m-1\ge q+1\), the \(q\)-jet of the coefficient in (1) is zero.
Nevertheless (1) is nonzero in

\[
 \Omega^1_{\mathbf C\{y\}}\otimes
 \mathbf C\{y\}/(y^m),
\]

and \(K_m\ne0\). Thus \(H_\tau\ne0\).

The counterfamily retains B159's uniform conormal matroid and all smooth
rank-\(R\) branch intersections, so adding those finite data does not
repair the inference.

## Re-entry condition

G112 must prove the analytic module morphism \(\beta_{K_B}\) is
identically zero, or provide a separate Noetherian mechanism with a
uniformly proved order bound depending on all full-system geometry. No
such bound is known, and every detector clause remains separate.
