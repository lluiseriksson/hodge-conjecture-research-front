---
brick_id: B144
status: PROVED
base_field: C
variety: a smooth analytic parameter germ carrying labeled nodal discriminant hypersurface germs and a proposed simultaneous-node stratum
smoothness: the parameter germ, every labeled branch, and the saturated deepest stratum are smooth; the conclusion proves smoothness and clean intersection for all branch intersections
projectivity: not needed for the local analytic lemma; downstream universal hyperplane applications are projective
dimension: arbitrary finite parameter dimension; N labeled branches have uniform conormal rank R with 1 at most R at most N
codimension: an s-branch intersection has codimension min(s,R); the saturated deepest stratum has codimension R
coefficient_field: C for analytic germs and conormal matroids; Q only in the downstream Hodge application
cohomology_theory: local analytic deformation theory, conormal matroids, clean arrangements, and downstream rational local intersection cohomology through B054
hodge_type: none asserted by the analytic criterion; B054 supplies type (0,0) only after the nodal Hodge hypotheses are added
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; no cycle is constructed or assumed by this lemma
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B054, B143, the analytic implicit-function theorem, and elementary representable-matroid rank
claim: Smooth labeled hypersurface germs with uniform conormal matroid U_(R,N) form a Li clean arrangement whenever their total intersection contains a smooth codimension-R germ F; every intersection of at least R branches then equals F as a germ.
falsifier: a subset of fewer than R branches with singular or nontransverse intersection, an R-subset whose intersection strictly contains F, a deeper intersection different from F, or failure of tangent-space cleanliness
---

# B144 — A saturated deepest stratum forces clean incidence

Let \((S,0)\) be a smooth complex analytic germ and let

\[
 D_1,\ldots,D_N\subset(S,0)
\]

be smooth hypersurface germs. Write \(\ell_i\in T_0^*S\) for their
conormals. Assume:

1. the representable conormal matroid is uniform \(U_{R,N}\);
2. there is a smooth codimension-\(R\) germ
   \(F\subseteq\bigcap_{i=1}^N D_i\).

The second hypothesis is the saturation condition. It is geometric, not a
dimension count: an actual smooth germ \(F\) must already have been
constructed.

## Small intersections

If \(I\subseteq\{1,\ldots,N\}\) has \(|I|<R\), uniformity makes the
conormals \(\{\ell_i:i\in I\}\) independent. The analytic implicit-function
theorem gives

\[
 D_I:=\bigcap_{i\in I}D_i
\]

smooth of codimension \(|I|\), with

\[
 T_0D_I=\bigcap_{i\in I}T_0D_i.
\]

The same conclusion holds for \(|I|=R\): \(D_I\) is smooth of
codimension \(R\).

## Saturation at rank

Fix \(I\) with \(|I|=R\). Since \(F\subseteq D_I\) and both are smooth
codimension-\(R\) germs through the origin, the inclusion has equal
dimension and hence

\[
 D_I=F
\]

as analytic germs.

Now let \(|J|>R\) and choose \(I\subset J\) of size \(R\). Then

\[
 F\subseteq D_J\subseteq D_I=F,
\]

so \(D_J=F\). Therefore every branch intersection is smooth and

\[
 \operatorname{codim}_S D_J=\min\{|J|,R\}.
\]

For \(|J|\ge R\), uniformity says that the intersection of the conormal
hyperplanes has codimension \(R\). Since \(F\subseteq D_i\) for every
\(i\), this gives

\[
 T_0F=\bigcap_{i\in J}T_0D_i.
\]

Thus every intersection is clean. The distinct intersection germs are the
uniform flats of ranks below \(R\), together with the single saturated
deepest germ \(F\), and they are closed under intersection. They form a Li
clean arrangement.

## Propagation and limitation

When the \(D_i\) are the labeled branches of a nodal discriminant, B054
applies and identifies the local rational type-\((0,0)\) relation channel.
Hence a G028 construction no longer needs a separate nonlinear
linearization theorem if it supplies:

- a uniform smoothing-conormal matroid;
- an actual saturated smooth codimension-\(R\) simultaneous-node germ;
- positive adjoint and ambient ranks and a nonzero specified pairing.

B144 constructs none of those inputs. In particular, choosing \(F\) as an
incidence of divisors containing an algebraic carrier retains the
circularity of NG-029 for arbitrary Hodge classes. The criterion separates
the clean-geometry obligation from the class-directed construction; it does
not resolve the latter. B145 subsequently identifies \(F\) intrinsically as
the image of a rank-smooth excess component of the ordered-node incidence,
reducing its construction to G091.
