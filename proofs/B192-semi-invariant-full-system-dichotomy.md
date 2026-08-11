---
brick_id: B192
status: PROVED
base_field: C
variety: a smooth projective complex variety with a very ample G-linearized line bundle and a finite group G acting on the polarized variety
smoothness: the variety is smooth; the representation theorem itself does not assert existence or smoothness of a nodal divisor
projectivity: the very ample complete linear system embeds the projective variety equivariantly
dimension: arbitrary variety dimension; a prospective ordered node set contains a nontrivial finite G-orbit of size N>1
codimension: every character-semi-invariant section space is a strict subspace of the complete section space when G moves a point
coefficient_field: C for finite-group representations, sections, jets, and projective embeddings; Q remains required for downstream Hodge detectors
cohomology_theory: linearized line bundles, complete linear systems, finite-group representations, and coherent jets
hodge_type: none asserted; rational type (0,0) and the specified Hodge pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B189-B191, G122-G123, and the equivariant very ample embedding
claim: If a finite group G acts nontrivially on X and L is a very ample G-linearized line bundle, then H0(X,L) cannot consist entirely of sections transforming by one character. In particular, if G transitively permutes more than one prospective node, every character-semi-invariant space is a strict subspace of the full complete linear system, so synchronization proved only there is not full-system synchronization.
falsifier: a nontrivial polarized automorphism moving a point while acting by a scalar character on all global sections of a very ample linearized line bundle, or a transitive orbit of size greater than one with a character-isotypic space equal to H0(X,L)
---

# B192 — Semi-invariant synchronization is never the full very ample system

Let a finite group \(G\) act on a smooth projective variety \(X\), and let
\(L\) be a very ample \(G\)-linearized line bundle. The linearization gives
a representation

\[
 \rho:G\longrightarrow\operatorname{GL}(H^0(X,L)). \tag{1}
\]

For a character \(\chi:G\to\mathbf C^*\), write

\[
 H^0(X,L)_\chi
 =\{s:\rho(g)s=\chi(g)s\text{ for every }g\in G\}. \tag{2}
\]

Sections in one space (2) have equivariantly related values and jets along
a \(G\)-orbit. This is the legitimate source of many diagonal or conformal
patterns in a selected family.

## Scalar action forces trivial action on the variety

Suppose for some \(\chi\) that

\[
 H^0(X,L)_\chi=H^0(X,L). \tag{3}
\]

Then \(\rho(g)=\chi(g)\operatorname{id}\) for every \(g\). Hence the induced
action on

\[
 \mathbf P(H^0(X,L)^*)
\]

is trivial. The very ample morphism

\[
 \iota_L:X\hookrightarrow\mathbf P(H^0(X,L)^*) \tag{4}
\]

is a closed immersion and is \(G\)-equivariant. Therefore

\[
 \iota_L(gx)=g\iota_L(x)=\iota_L(x) \tag{5}
\]

for every \(x\in X\). Injectivity of (4) gives \(gx=x\). Thus every
element of \(G\) acts trivially on \(X\).

Taking the contrapositive, if some group element moves a point, then

\[
 H^0(X,L)_\chi\subsetneq H^0(X,L) \tag{6}

for every character \(\chi\).

## Consequence for a nodal orbit

If \(G\) acts transitively on distinct prospective nodes
\(p_1,\ldots,p_N\) with \(N>1\), its action on \(X\) is nontrivial.
Therefore (6) holds. A construction that uses only invariant sections or
one character-semi-invariant component works in a strict linear subfamily.

The omitted isotypic components can change the value map, the full
conditional-gradient quotient

\[
 H^0(I_ZL)/H^0(I_{2Z}L),
\]

and B191's Hessian tensor. Equivariance alone does not put those omitted
components into \(H^0(I_{2Z}L)\).

B192 does not rule out every equivariant full-system construction: several
isotypic components might conceivably combine to satisfy B191. It rules out
only the common shortcut of proving synchronization in a single
semi-invariant family and silently replacing that family by \(|L|\).
