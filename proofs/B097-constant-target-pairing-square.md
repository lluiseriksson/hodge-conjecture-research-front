---
brick_id: B097
status: PROVED
base_field: C with rational Hodge structures
variety: the special/nearby stalk data of a projective collision for an arbitrary polarized smooth projective complex 2n-fold, with constant primitive ambient homology target
smoothness: generic hyperplane fiber smooth; special target clean nodal; proof is exact rational linear algebra on the induced maps
projectivity: collision and ambient family projective in the application
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: nearby-cycle exact sequence, rational Hodge structures, B022 quotient homology, primitive ambient homology, and Hodge pairing
hodge_type: all maps and targets restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B022, B058, B083, B096
claim: If special and nearby detector maps q_S:S->V and q_P:P->V to constant primitive ambient homology satisfy q_S=q_P composed with u and q_P(t_psi)=c, then the detector functional annihilates the ambiguity boundary and its descended value equals the nonzero B058 pairing with c.
falsifier: a commutative constant-target square with q_P(t_psi)=c but nonzero detector functional on ker(u) or descended value different from the pairing with c
---

# B097 — A quotient-compatible constant target closes the pairing square

**Status:** PROVED

Let

\[
 W\xrightarrow d S\xrightarrow u P
\]

be B096's exact segment and let $V$ be the constant primitive ambient Hodge
homology. Suppose the actual collision constructs rational type-$(0,0)$ maps

\[
 q_S:S\to V,
 \qquad q_P:P\to V,
 \qquad q_S=q_P\circ u,
\]

after both B022 quotient stages. Assume also that the specified nearby
detector satisfies

\[
 q_P(t_\psi)=c,
\]

where $c$ is B058's chosen ambient tube class. Define
$F=\langle\zeta,q_S(-)\rangle$. Exactness gives $u\circ d=0$, hence

\[
 F\circ d
 =\langle\zeta,q_Pud(-)\rangle
 =0.
\]

Moreover $F=u^*\lambda$ for
$\lambda=\langle\zeta,q_P(-)\rangle$, and

\[
 \lambda(t_\psi)
 =\langle\zeta,q_P(t_\psi)\rangle
 =\langle\zeta,c\rangle
 \ne0
\]

by B058. Thus B096's second branch closes automatically.

## Boundary

B097 is a sufficient naturality lemma. It does not construct $q_S,q_P$ or
prove that raw proper pushforward descends through the equator-extension and
base-locus quotients. G061 is precisely that construction; NG073 blocks
assuming it from properness alone.
