---
brick_id: G007
status: EXPLORATORY
base_field: C
variety: arbitrary polarized smooth projective X of dimension 2n, its high-power hyperplane family, and a specified nonzero primitive rational Hodge class
smoothness: X and the tube family's fibers are smooth; the sought terminal fiber is singular, preferably nodal
projectivity: X projective and L ample with a sufficiently high very ample power
dimension: dim X = 2n and hyperplane fibers have dimension 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: singular Betti homology/cohomology, monodromy and tube classes, vanishing cycles, limit mixed Hodge structures, and local intersection cohomology
hodge_type: primitive (n,n) input; the sought local relation has type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B008, B010-B013, B015, and B019-B025
claim: Every nonzero primitive rational Hodge class detected by a global Schnell tube is also detected by a type-(0,0) Saito relation concentrated at one singular hyperplane member.
falsifier: a polarized smooth projective 2n-fold and primitive rational Hodge class with a nonzero global tube detector but orthogonal to every Saito local relation class for every singular member of every polarization power
---

# G007 - Tube-to-local-relation bridge

## Falsifiable theorem sought

For \(X/\mathbf C\), \(L\), and
\(0\ne\zeta\in H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}\),
B011 produces \(g\in G\) and
\(\alpha\in\ker(g-1)\) whose tube detects \(\zeta\). The required bridge is:

> There exist a singular member \(Y_0\in|L^m|\) and
> \(\beta\in R(Y_0)_1^{(0,0)}\) such that
> \(\langle\zeta,\gamma_\beta\rangle\ne0\).

By B010, this makes \(Y_0\) a generalized Thomas hyperplane section for
\(\zeta\); B007 then propagates to the rational Hodge Conjecture. The theorem
is therefore a sufficient and terminal-equivalent universal gate, not a
proved weakening of HC.

## Attempt: fill and concentrate the tube loop

1. Express \(g\) as a product of Picard-Lefschetz meridians around the
   discriminant. B013 computes the resulting distributed relation exactly.
2. Fill the loop in the full projective parameter space. A generic filling
   meets the discriminant at several smooth points.
3. Try to collide those intersections into one higher discriminant stratum,
   so that the global cancellation becomes a relation among the vanishing
   cycles of one singular fiber.
4. Prove that the resulting local relation has type \((0,0)\) and that its
   Saito class \(\gamma_\beta\) retains nonzero pairing with \(\zeta\).

Steps 3-4 are not consequences of the Picard-Lefschetz factorization. A
generic filling sees only smooth discriminant points, whose rational local
intersection-cohomology groups vanish by B008. B015 proves that a nodal
member with independently imposed nodes has exactly the required
normal-crossing collision geometry, but it starts with that member. No
audited theorem constructs it from the tube while preserving the tube class,
its nonzero pairing, and its Hodge type.

B012 sharpens the dimension obstruction: the class-specific local support has
complex codimension at least two. Thus a generic real filling disk for the
loop misses it. Passing to a complex two-parameter net creates enough
dimension to meet a nonempty codimension-two component but does not prove
that the component exists.

## Exact kernel mismatch

Schnell's global datum is

\[
 \alpha\in\ker(g-1:V\to V)
\]

for a product \(g\) of monodromies. Saito's local datum is

\[
 \beta\in\ker\!\left(
 \bigoplus_y H_{2n-1}(Z_{y,\infty},\mathbf Q(n))
 \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n))\right)^{(0,0)}_1
\]

at one fiber. Neither kernel includes in the other, and the audited sources
provide no natural transformation carrying the first to the second. Treating
them as identical is NG-010.

## Exact thimble quotient obstruction

B022 shows, in the generic projective-hypersurface pencil model, that even
the local-looking condition \(\sum_i a_i\delta_i=0\) is only the first
stage. The corresponding thimble combination represents an ambient class
only after passing through

\[
 \ker\partial
 \longrightarrow
 \mathcal T(Y)=\ker\partial/\operatorname{im}\tau_\infty
 \longrightarrow
 H_n(X)/\iota_*H_n(X_b),
\]

and the second map has the explicit base-locus kernel \(K\). A collision
comparison must therefore preserve a nonzero class through both quotients;
preserving a kernel vector alone is NG-019.

B023 also removes pure Hurwitz basis change as a repair mechanism. Hurwitz
moves within one fixed fibration act invertibly and preserve the dimension of
the relation kernel. They cannot identify the rank-at-most-one matching
boundary map (whose kernel is nonzero) with the rank-two cusp boundary map
(whose kernel is zero). Any viable collision must change the
complex non-invertibly or introduce additional vanishing directions; this is
NG-020.

## Complete-intersection checkpoint

B024 proves that for a smooth projective complete intersection, every
nonzero primitive class has a nonzero detector already at the final
quotient level \(\mathcal T(Y)/K\simeq PH_n(X)\). Thus the global thimble
construction and both quotient nonvanishing tests can be passed in that
special setting.

The remaining arrow is still exactly the open one:

\[
 \text{nonzero global quotient-level thimble detector}
 \dashrightarrow
 \text{one-fiber type-}(0,0)\text{ Saito detector}.
\]

B024 gives no concentration, Hodge-type, or algebraicity theorem, and its
complete-intersection scope has no proved reduction from arbitrary smooth
projective varieties. Promoting the topological surjection to HC is NG-021.

## Re-entry condition

Construct an algebraic two-parameter degeneration whose boundary realizes a
tube detector and whose discriminant intersections specialize to one
higher-codimension point; then prove, through the vanishing-cycle exact
sequence, that the specialized relation maps to a Saito class with the same
nonzero \(\zeta\)-pairing. Ordinary double points would make the type
\((0,0)\) condition automatic by B010, while B015 supplies the local
normal-crossing geometry if their independent-incidence hypothesis is met.
The specialization datum must include the equator-extension quotient and
the base-locus projection of B022, not only a map of vanishing-cycle kernels.

This is now a proposed geometric mechanism for the exact support gate G008.
