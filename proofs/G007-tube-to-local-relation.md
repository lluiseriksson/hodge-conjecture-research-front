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
dependencies: B010 and B011
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
   discriminant. The equation \(g\alpha=\alpha\) records a global cancellation
   after transporting \(\alpha\) around the entire loop.
2. Fill the loop in the full projective parameter space. A generic filling
   meets the discriminant at several smooth points.
3. Try to collide those intersections into one higher discriminant stratum,
   so that the global cancellation becomes a relation among the vanishing
   cycles of one singular fiber.
4. Prove that the resulting local relation has type \((0,0)\) and that its
   Saito class \(\gamma_\beta\) retains nonzero pairing with \(\zeta\).

Steps 3-4 are not consequences of the Picard-Lefschetz factorization. A
generic filling sees only smooth discriminant points, whose rational local
intersection-cohomology groups vanish by B008. No audited theorem permits
coalescing the meridians into one algebraic hyperplane section while
preserving the tube class and its Hodge type.

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

## Re-entry condition

Construct an algebraic two-parameter degeneration whose boundary realizes a
tube detector and whose discriminant intersections specialize to one
higher-codimension point; then prove, through the vanishing-cycle exact
sequence, that the specialized relation maps to a Saito class with the same
nonzero \(\zeta\)-pairing. Ordinary double points would make the type
\((0,0)\) condition automatic by B010.
