---
brick_id: B051
status: PROVED
base_field: C
variety: the wonderful resolution of an arbitrary central representable nodal discriminant arrangement, normally sliced along every arrangement stratum
smoothness: the parameter base and wonderful resolution are smooth, all arrangement strata are smooth, and the resolved boundary is simple normal crossing
projectivity: the wonderful morphism and every normal central fiber are projective
dimension: arbitrary parameter dimension d; a support of codimension c has normal wonderful fiber dimension c-1
codimension: every proper arrangement support has codimension c at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational perverse direct images, normal-fiber hypercohomology, Verdier duality, and polarizable Hodge modules
hodge_type: the bound is coefficient-insensitive after B050; any surviving degree-one full-support group remains type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B039-B050, G019-G023, Saito S037, and Li S038
claim: Every non-full-support strict-support summand in the proper direct image of an arbitrary wonderful nodal resolution begins in ordinary stalk degree at least two; consequently the resolved ordinary-degree-one group descends canonically to the full-support downstairs intersection-complex stalk.
falsifier: a codimension-c support with perverse degree below -(c-2), a normal wonderful fiber with hypercohomology above 2c-2, failure of the dual lower bound, or a support intersection-complex normalization producing negative ordinary degrees
---

# B051 - Universal strict-support bound

This brick proves G023. The proof is coefficient-sensitive: it uses B050's
two cohomology sheaves rather than a constant-sheaf semismall shortcut.

## Normal-fiber amplitude

Let (S) be an arrangement stratum of codimension (c\ge2), and take a
normal slice at its generic point. The restricted wonderful map has a
projective central fiber (E_S) of dimension (c-1). By B050, the
unshifted intermediate-extension restriction (A|_{E_S}) has

\[
 \mathcal H^0=K_{E_S},\qquad
 \mathcal H^1=\bigoplus_D (i_D)_*W_D,\qquad
 \mathcal H^{\ge2}=0,
\]

where every (D) is a divisor of dimension (c-2). Therefore

\[
 H^q(E_S,K)=0\quad(q>2c-2),
\]

and

\[
 H^{q-1}(D,W_D)=0\quad(q-1>2c-4).
\]

The coefficient row thus vanishes already for (q>2c-3), while the
constant row gives the sharp combined bound

\[
 \mathbb H^q(E_S,A|_{E_S})=0\qquad(q>2c-2).
\]

This uses only cohomological dimension; no degeneration of the
hypercohomology spectral sequence is assumed.

## Perverse shift audit

Put (P=A[c]) on the normal (c)-fold. Proper base change shifts the
preceding bound to stalk degrees at most (c-2) for (R\pi_*P). Applying
the same calculation to the Verdier-dual geometric variation and using
(D R\pi_*P\simeq R\pi_*DP) gives the matching costalk bound. Hence the
perverse cohomology capable of having strict support (S) lies only in

\[
 -(c-2)\le j\le c-2.
\]

Saito's projective direct-image and strict-support decomposition applies
over (mathbf Q). A summand with strict support of codimension (c) in
perverse degree (j) occurs, after undoing the ambient shift, first in
ordinary degree

\[
 c+j\ge c-(c-2)=2.
\]

The closures of the strata are smooth linear flats. Their normalized
intermediate extensions have ordinary cohomology sheaves only in
nonnegative degrees, by the same normal-crossing complex beginning in degree
zero. Specializing further inside a support can therefore increase, but
cannot decrease, this first ordinary degree. Disconnected normal
arrangements and nested products obey the same dimension bounds.

## Descent in degree one

The wonderful map is an isomorphism away from the arrangement singular
strata, so it has exactly one full-support summand, the downstairs
intersection complex. Every other summand begins in ordinary degree at
least two. Proper base change consequently gives a canonical isomorphism

\[
 H^1(IC_B(L_{\mathbf Q})_0)
 \simeq \mathbb H^1(E_{\mathcal B},A|_{E_{\mathcal B}}).
\]

## Scope guard

B051 proves descent only. The resolved degree-one hypercohomology still has
to be computed globally from B049's divisor classes and B050's coefficient
sheaves. That residue calculation is the next gate. No cycle is constructed
and actual progress toward the standard rational Hodge Conjecture is zero.
