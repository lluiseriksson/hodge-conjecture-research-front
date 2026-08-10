---
brick_id: B117
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a sufficiently high generic plane net of hyperplanes, and its original incidence family h:Y->B
smoothness: X smooth; the plane-net base locus is regular so the incidence total space is smooth; a generic point of every tested discriminant divisor has exactly one ordinary quadratic singularity and admits a transverse Lefschetz disk
projectivity: X, the plane net B, the incidence total space Y, and h are projective
dimension: dim_C X = 2n; hyperplane fibers have dimension d = 2n-1; dim_C B = 2; a transverse disk has dimension 1
codimension: middle cycle codimension n; tested strict support has base codimension one
coefficient_field: Q
cohomology_theory: singular Betti cohomology, proper direct image, Picard-Lefschetz theory, perverse cohomology, noncharacteristic normal slices, and polarizable rational Hodge modules
hodge_type: no class is selected; the support multiplicity vanishes over Q and hence in every rational Hodge type
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008, B056-B058, B077, B080-B081, B089, B116, G076-G078, NG093, S037, S052
claim: For the original smooth plane-net incidence pushdown K=Rh_*Q_Y[2n+1], the perverse Hodge module pH^0(K) has no strict-support summand on any discriminant divisor whose generic transverse degeneration is Lefschetz with nonzero vanishing cohomology.
falsifier: a nonzero divisor-strict-support multiplicity in pH^0(K), equivalently a nonzero punctual pH^0 summand after a generic transverse Lefschetz slice, despite constancy of R^(2n) on that slice
---

# B117 — Lefschetz discriminant divisors carry no perverse-degree-zero support

**Status:** PROVED

Let

\[
 d=2n-1,
 \qquad
 K_B=Rh_*\mathbf Q_{\mathcal Y}[d+2]
\]

for the original incidence family over the plane net \(B\). Let \(D\) be a
discriminant divisor and choose a general smooth point \(p\in D\), away
from every other stratum. By the generic-plane and clean-nodal hypotheses,
the fiber at \(p\) has one ordinary quadratic singularity. Choose a disk
\(a:\Delta\hookrightarrow B\) transverse to \(D\) at \(p\), and write
\(g:\mathcal Y_\Delta\to\Delta\) for the pullback.

The shifted normal-slice object is

\[
 K_\Delta=a^*K_B[-1]
 =Rg_*\mathbf Q_{\mathcal Y_\Delta}[d+1].
\]

The shift by \(-1\) is essential: a divisor-strict-support perverse summand
\(IC_D(M_D)=M_D[1]\) restricts to a punctual perverse summand
\(M_{D,p}[0]\) of \({}^pH^0(K_\Delta)\).

## Lefschetz calculation

Otwinowska--Saito S052, equations (2.2.1)--(2.2.5), treat exactly a
Lefschetz family of hyperplane sections. Put their ambient dimension
\(m=2n=d+1\). Under nonzero vanishing cohomology, the restriction to the
rank-one Milnor group is surjective. The vanishing-cycle long exact sequence
then makes the cospecialization map

\[
 H^{d+1}(Y_p,\mathbf Q)
 \longrightarrow
 H^{d+1}(Y_t,\mathbf Q)
\]

an isomorphism. Consequently S052 equation (2.2.3) says that

\[
 R^{d+1}g_*\mathbf Q
\]

is constant across \(p\). The same passage also gives equation (2.2.5):
\(R^d g_*\mathbf Q\) is the intersection-complex extension of its
restriction to \(\Delta^*\).

Now apply the projective decomposition theorem to \(K_\Delta\). On a disk,
write the strict-support decomposition

\[
 {}^pH^0(K_\Delta)
 =IC_\Delta(R^d g_*\mathbf Q|_{\Delta^*})
 \oplus i_{p*}V.
\]

Because the derived decomposition is a direct sum, the punctual term
\(i_{p*}V\) contributes a punctual direct summand \(i_{p*}V\) to

\[
 \mathcal H^0(K_\Delta)=R^{d+1}g_*\mathbf Q.
\]

But this sheaf is constant by the preceding Lefschetz calculation. A
constant sheaf on the disk has no nonzero direct summand supported only at
\(p\). Therefore

\[
 V=0.
\]

## Return to the plane base

Strict-support multiplicity is generically detected by a transverse normal
slice. Any nonzero \(D\)-supported summand of \({}^pH^0(K_B)\) would yield
the punctual \(V\ne0\) just excluded. Hence no such divisor summand exists.
The argument is rational and the decomposition is compatible with
polarizable Hodge modules, so there is no coefficient or Hodge-type gap.

For G076 this means that, once the selected class has a nonzero canonical
\(E_\infty^{-1,0}\) coordinate in the original incidence pushdown, that
coordinate is automatically full-support. No selected divisor projection
remains to calculate.

## Scope guard

This theorem concerns the original smooth incidence pushdown. A semistable
alteration or resolution can create exceptional divisor-supported summands
in its own pushdown; B117 neither excludes nor needs them for the original
downstairs landing. It also does not construct the selected collision class,
prove that its relevant perverse grade is nonzero, or produce an algebraic
cycle.
