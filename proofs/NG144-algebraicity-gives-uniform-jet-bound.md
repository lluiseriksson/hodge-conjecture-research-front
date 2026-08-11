---
brick_id: NG144
status: NO-GO
base_field: C
variety: algebraic ODP critical-value germs, including B157 projective realizations over nonlinear analytic bases
smoothness: the parameter germ and ODP Hessians are smooth and nondegenerate; the escape order is unrestricted
projectivity: B157 realizes each polynomial escape after sufficient twisting, but not with one fixed embedding-independent degree bound on the full-system germ
dimension: already fails on a one-dimensional basis-node germ with one escape generator
codimension: nonzero algebraic escape ideals can begin at arbitrarily high order as their algebraic degree grows
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: algebraic implicit functions, finite jets, ODP deformation theory, and conormal modules
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B159, B179-B180, G113
claim: The mere fact that every escape germ is algebraic or Nash supplies one uniform finite jet order, independent of its defining degree and the polarization, that detects conormal vanishing.
falsifier: epsilon_m(y)=y^m satisfies the simple polynomial P_m(y,z)=z-y^m of degree m and has nonzero conormal defect first visible in degree m-1
---

# NG144 — Algebraicity alone gives no uniform jet order

For every \(m\ge2\), the algebraic escape function

\[
 \epsilon_m(y)=y^m
\]

is the unique simple branch of

\[
 P_m(y,z)=z-y^m,
 \qquad
 \partial_zP_m=1. \tag{1}
\]

Its defining degree is \(m\), its vanishing order is \(m\), and B179
gives

\[
 \beta_{(y^m)}([y^m])=m y^{m-1}dy\pmod {y^m}. \tag{2}
\]

Thus the first visible conormal coefficient occurs in degree \(m-1\),
which is unbounded as the algebraic degree grows. B157 can realize each
such polynomial germ in projective ODP charts after sufficient twisting,
while keeping local Milnor data fixed.

## Re-entry condition

G113 must track an explicit degree bound for the actual full critical
incidence, including restriction to \(F_B\) and every étale coordinate or
elimination step. “Algebraic,” “Nash,” “Noetherian,” or “projective” without
that bound does not produce a finite certificate. The resulting jet
vanishing and every Hodge detector clause remain to be proved.
