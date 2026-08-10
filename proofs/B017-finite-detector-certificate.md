---
brick_id: B017
status: PROVED
base_field: C
variety: a fixed polarized smooth projective X of dimension 2n and a chosen sequence of singular-member detector collections across polarization powers
smoothness: X is smooth; singular members satisfy the hypotheses defining their Saito detector classes
projectivity: X is projective and L is ample
dimension: dim X = 2n
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: finite-dimensional primitive rational Betti homology with its Hodge subspace
hodge_type: primitive type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraicity conclusion is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B016 and finite-dimensional linear algebra
claim: The cumulative Saito detector spans across polarization powers stabilize, and full detector generation for a fixed X is equivalent to the existence of a finite list of detector classes forming a basis of primitive rational Hodge homology.
falsifier: an increasing sequence of cumulative detector subspaces in finite-dimensional primitive Hodge homology that never stabilizes, or a full union with no finite spanning subcollection
---

# B017 - Finite detector certificate

Let \(H_{\mathrm{Hdg}}^\vee\) be the finite-dimensional primitive rational
Hodge homology of a fixed \(X\). For each positive integer \(m\), let \(D_m\)
be the span of a specified class of Saito detectors arising in \(|mL|\), and
define the cumulative span

\[
 D_{\le M}=\sum_{m\le M}D_m\subseteq H_{\mathrm{Hdg}}^\vee.
\]

Then

\[
 D_{\le1}\subseteq D_{\le2}\subseteq\cdots
\]

is an increasing sequence of subspaces of a finite-dimensional vector space.
Its dimension can increase only finitely many times. Hence there is an
\(M_0\), not effectively bounded by this argument, such that

\[
 D_{\le M}=D_{\le M_0}\qquad(M\ge M_0).
\]

Moreover,

\[
 \sum_{m\ge1}D_m=H_{\mathrm{Hdg}}^\vee
\]

if and only if finitely many individual detector classes
\(\gamma_{\beta_1},\ldots,\gamma_{\beta_h}\), drawn from finitely many powers,
form a basis of \(H_{\mathrm{Hdg}}^\vee\). Combined with B016, this finite
list is a complete detector certificate for the fixed polarized variety.

## Scope guard

The stabilization is non-effective and may occur at a proper subspace. It
does not bound \(M_0\), produce any detector, compare the non-cumulative
spaces \(D_m\), or prove the certificate exists for arbitrary \(X\).
