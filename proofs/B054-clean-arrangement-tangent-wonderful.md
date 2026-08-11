---
brick_id: B054
status: PROVED
base_field: C
variety: a nonlinear nodal discriminant germ whose smooth branch intersections form a Li arrangement of subvarieties, its wonderful resolution, and the wonderful model of its representable tangent arrangement
smoothness: the base, all arrangement strata, all building centers, and all iterated transforms are smooth; intersections are clean and the final boundary is simple normal crossing
projectivity: the motivating nodal family and all blow-ups are projective; the comparison is local analytic transverse to each stratum
dimension: arbitrary finite parameter dimension and any dimension-scaled number of smoothing blocks
codimension: arbitrary clean arrangement strata of codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational Picard-Lefschetz intermediate extensions, wonderful-model logarithmic residues, perverse direct images, and polarizable mixed Hodge modules
hodge_type: the downstairs degree-one channel is pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B049-B053, B134, Li Definitions 2.1-2.3 and Proposition 2.8/Lemma 2.9 (S038), and Saito S022/S037
claim: The labelled central fiber of every nonlinear clean wonderful discriminant resolution is canonically the wonderful model of its tangent arrangement; residues and the degree-one rational IC/MHS channel agree, with polarized homological model the full type-(0,0) vanishing-cycle relation kernel and cohomological stalk its dual.
falsifier: an iterated center whose intersection with the central fiber is not the corresponding transformed projectivized normal flat, a clean transform not preserved by Li's induction, a higher-jet-dependent boundary valuation, or disagreement of the residue/support complexes
---

# B054 - Clean arrangements have tangent wonderful fibers

This brick proves G027 and closes G015 under its explicit multipart
clean-arrangement hypothesis.

## Initial normal fiber

Let \(\mathcal S\) be a Li arrangement of smooth discriminant strata in a
smooth base \(Y\), let \(\mathcal G\) be a building set, and let \(F_0\) be
the deepest stratum through the point under study. Blow up \(F_0\). The
exceptional divisor is

\[
 E_0=\mathbf P(N_{F_0/Y}).
\]

For every stratum \(S\supset F_0\), its strict transform meets \(E_0\) in

\[
 \mathbf P(N_{F_0/S})
 =\mathbf P(TS|_{F_0}/TF_0).
\]

Li's proof of Lemma 2.9(iii) identifies intersections inside the exceptional
divisor by

\[
 \mathbf P(N_{F_0/S_1})\cap\mathbf P(N_{F_0/S_2})
 =\mathbf P(N_{F_0/(S_1\cap S_2)}),
\]

where clean intersection is exactly what identifies the tangent-space
intersection. Fiberwise over the chosen point, these are the projective
linear flats of the representable tangent arrangement, with the same labelled
intersection poset.

## Induction through the building set

Use an inclusion-compatible order. Proposition 2.8 says that after blowing a
minimal building element, the dominant transforms again form an arrangement
with the induced building set. Lemma 2.9 preserves clean intersections and
separates incomparable centers when their intersection has already been
blown up.

Suppose inductively that the current central fiber is the corresponding
partial wonderful model of the tangent arrangement. A later center meets the
fiber transversally in the current transform of its projectivized normal flat.
For a transverse square, restricting the ambient blow-up to the fiber is the
blow-up of the fiber along that intersection. Hence the next fiber is the
next tangent wonderful blow-up. Induction gives a canonical labelled
isomorphism

\[
 E_{\mathcal G}^{\rm nonlinear}
 \simeq E_{\mathcal G}^{\rm tangent}.
\]

This comparison is intrinsic and therefore independent of permissible
order by Li Theorem 1.3. It does not assert that neighborhoods of the two
divisors are analytically equivalent; NG036 shows that stronger statement is
false.

## Residues and the IC channel

At the generic point of a center \(F\), a smooth branch \(D_i\) contains it
with order one exactly when \(F\subset D_i\). The boundary valuation and
Picard-Lefschetz residue are therefore

\[
 N_F=\sum_{F\subset D_i}N_i,
\]

with no dependence on higher jets. The labelled tangent comparison preserves
the origin residue, every branch residue, every \(N_F\), and every boundary
support.

B049-B052 now apply verbatim on the common labelled fiber: the intrinsic
divisor matrix is triangular, the coefficient sheaf has only degrees zero
and one, lower strict supports start in degree two, and the sole degree-one
transgression has kernel

\[
 \ker\!\left(\mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}
 \operatorname{span}_{\mathbf Q}\{\delta_i\}\right).
\]

This kernel is the polarized homological model; the cohomological IC stalk
is its dual by B134. The comparison is rational and every coefficient is \(\mathbf Q(0)\) after
the \(\mathbf Q(n)\) normalization, so it preserves the pure type-\((0,0)\)
mixed Hodge structure.

## Consequence for G015 and scope

For G015, “multipart quasi-local” is now made explicit: the discriminant
branches and all their relevant intersections must form a Li clean
arrangement, while each block is independently smoothable. The tangent
matroid is representable by the actual smoothing covectors. B054 and B052
then prove the full relation channel for every number of blocks.

Block independence alone does not construct such a clean nodal incidence,
does not force positive adjoint defect or ambient detector rank, and does not
select a relation pairing nontrivially with a specified Hodge class. Those
remain the upstream geometric obligations. No algebraic cycle is produced,
and actual general-Hodge progress remains zero.
