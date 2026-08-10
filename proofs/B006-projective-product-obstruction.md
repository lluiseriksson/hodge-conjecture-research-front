---
brick_id: B006
status: PROVED
base_field: C
variety: product X x P^r with an lci product cycle Z x point or Z x P^r
smoothness: X smooth; Z lci; projective-space factors smooth
projectivity: X and all products projective
dimension: dim(X)=n and r>=0 arbitrary
codimension: codim(Z,X)=q; product codimension q+r for Z x point and q for Z x P^r
coefficient_field: C for obstruction groups; Q for associated cycle classes
cohomology_theory: coherent cohomology controlling embedded lci deformations
hodge_type: product cycle classes of type (q+r,q+r) or (q,q)
cycle_class_map: rational Chow cycle class into Betti cohomology of X x P^r
cycle_equivalence: rational equivalence
scope: absolute
dependencies: product normal-bundle splitting and coherent-cohomology Kunneth formula
claim: The B001 low-degree product Z x point acquires an extra obstruction summand H^1(O_Z)^r, whereas Z x P^r has the same H^1 normal space as Z.
falsifier: failure of the product normal-bundle splitting or of the stated Kunneth decompositions
---

# B006 - Projective-product obstruction audit

## Statement

Let \(X/\mathbf C\) be smooth projective, let \(Z\subset X\) be lci of
codimension \(q\), and let \(r\ge0\).

### Point product

For \(W=Z\times\{t\}\subset Y=X\times\mathbf P^r\),

\[
 N_{W/Y}\simeq N_{Z/X}\oplus\mathcal O_Z^{\oplus r}
\]

and hence

\[
 H^1(W,N_{W/Y})\simeq
 H^1(Z,N_{Z/X})\oplus H^1(Z,\mathcal O_Z)^{\oplus r}.
\]

### Full projective-space product

For \(W'=Z\times\mathbf P^r\subset Y\),

\[
 N_{W'/Y}\simeq\operatorname{pr}_Z^*N_{Z/X}
\]

and Kunneth plus \(H^1(\mathbf P^r,\mathcal O)=0\) gives

\[
 H^1(W',N_{W'/Y})\simeq H^1(Z,N_{Z/X}).
\]

## Proof

The conormal sequence for a product regular embedding splits into the conormal
bundles from the two factors. Dualizing gives

\[
 N_{Z\times L\,/\,X\times\mathbf P^r}
 \simeq \operatorname{pr}_Z^*N_{Z/X}
 \oplus \operatorname{pr}_L^*N_{L/\mathbf P^r}.
\]

For \(L=\{t\}\), its normal bundle is the vector space
\(T_t\mathbf P^r\) pulled back to \(Z\), hence
\(\mathcal O_Z^{\oplus r}\). For \(L=\mathbf P^r\), the second summand is
zero. The displayed cohomology identities follow from Kunneth and
\(H^0(\mathbf P^r,\mathcal O)=\mathbf C\),
\(H^1(\mathbf P^r,\mathcal O)=0\). QED.

## Consequence for the vertical map

B001's case \(2p\le n\) multiplies the class by the top hyperplane class and
therefore geometrically uses point products. Even if a presentation on \(X\)
is semiregular, its point-product presentation has new potential obstruction
directions \(H^1(\mathcal O_Z)^{\oplus r}\). Injectivity of the old
semiregularity map says nothing about those directions.

Thus semiregularity is not automatically stable under the very product used
in the low-degree half of B001. This does not refute G004: the product class
might have a different presentation, or the new directions might be detected
by the product semiregularity map. Both require a separate proof.

