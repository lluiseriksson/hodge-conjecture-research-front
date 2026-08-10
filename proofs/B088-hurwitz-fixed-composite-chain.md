---
brick_id: B088
status: PROVED
base_field: C for the Lefschetz family; Q for homology
variety: a family of Lefschetz-meridian factorizations with fixed smooth reference fiber, fixed composite detector loop, and fixed transported fiber class
smoothness: all fibers along the detector loops are smooth and enclosed critical fibers are Morse
projectivity: the hyperplane family is projective; the Hurwitz calculation is topological
dimension: arbitrary Lefschetz-fiber dimension; ambient dimension 2n in the Hodge application
codimension: middle codimension n; meridians encircle discriminant divisors
coefficient_field: Q
cohomology_theory: Picard-Lefschetz monodromy, relative thimble homology, path-extension cocycles, and Hurwitz moves
hodge_type: no new Hodge type is inferred; the B058 ambient class retains its previously established type
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the downstream application
scope: relative and fiberwise
dependencies: B023, B057, S028-S029
claim: If collision-parameter monodromy changes a Lefschetz-meridian factorization only by Hurwitz moves while preserving its composite loop g, the reference-fiber identification, and the class alpha, then the B057 geometric extension chain tau_g(alpha) is fixed; consequently its nilpotent collision residue is zero.
falsifier: a Hurwitz move preserving the composite path and transported input class but changing the relative homology class of extension along that composite path
---

# B088 — Pure Hurwitz motion fixes the composite extension chain

**Status:** PROVED

Let

\[
 g=\ell_r\cdots\ell_1,
 \qquad g\alpha=\alpha,
\]

and let $t=\tau_g(\alpha)$ be the B057 extension chain. A Hurwitz move
changes two adjacent factors while preserving their product. For example,
at the monodromy level,

\[
 (M_1,M_2)
 \longmapsto
 \left(M_2,M_2M_1M_2^{-1}\right)
\]

preserves the ordered composite because

\[
 (M_2M_1M_2^{-1})M_2=M_2M_1.
\]

B057's path-composition formula expresses the ordered thimble sum as the
single geometric extension $\tau_g(\alpha)$. Therefore a sequence of
Hurwitz changes may alter the thimble basis and coefficient coordinates,
but it cannot alter the relative homology class of the extension along the
same composite path with the same input class.

Hence, if a loop in the collision parameter induces only this Hurwitz
change and the chosen trivialization returns both $g$ and $\alpha$ exactly,

\[
 M_{\mathrm{coll}}t=t.
\]

For unipotent monodromy this is equivalent to $Nt=0$, so G051's residue
class vanishes without a kernel adjustment.

## Exact boundary

B088 is conditional on fixing the composite loop, reference-fiber
identification, and input class. A collision loop can instead conjugate the
detector loop or act nontrivially on the reference fiber. Hurwitz invariance
of the factorization type alone does not rule this out. G052 asks for the
required marked collision model; NG064 records the shortcut.
