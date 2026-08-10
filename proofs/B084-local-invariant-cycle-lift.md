---
brick_id: B084
status: PROVED
base_field: C
variety: a proper algebraic map f from a complex algebraic variety X to a base Y, with a boundary point u of an open locus U where R^q f_* IC_X is locally constant
smoothness: X may be singular and is handled by IC_X; U is a local-system locus; the special fiber over u may be singular
projectivity: proper is sufficient for the cited theorem; the Hodge application is projective
dimension: arbitrary; the Hodge application has ambient dimension 2n and hyperplane-fiber dimension 2n-1
codimension: arbitrary boundary stratum; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational intersection cohomology, proper direct image, local monodromy invariants, nearby cycles, and vanishing cycles
hodge_type: the restriction map is Hodge-theoretic in the projective setting, but this brick asserts a rational lift only and does not select a type-(0,0) lift
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B083, S037
claim: For a proper map of complex algebraic varieties with IC_X coefficients, every locally monodromy-invariant nearby class is the image of a special-fiber intersection-cohomology class; equivalently, its canonical vanishing-cycle obstruction in B083 is zero.
falsifier: a class fixed by all monodromy in a sufficiently small punctured neighborhood that is not in the image of the special-fiber restriction/retraction map
---

# B084 — Local invariant cycles kill the lift obstruction

**Status:** PROVED

Let $f:X\to Y$ be proper and let $U\subseteq Y$ be a Zariski-open locus
on which $R^qf_*IC_X$ is locally constant. For a boundary point
$u\in\overline U$, let $B_u$ be the intersection of $U$ with a sufficiently
small Euclidean ball centered at $u$.

De Cataldo-Migliorini Theorem 1.7.1(2) states that

\[
 H^q(f^{-1}(u),IC_X)
 \longrightarrow
 H^0(B_u,R^qf_*IC_X)
\]

is surjective. The target is exactly the subspace of a nearby-fiber group
fixed by the local fundamental group of $B_u$.

Consequently, if a class $t_\psi$ is invariant under the local collision
monodromy, it has a rational special-fiber lift. In B083's exact triangle
this is equivalent to

\[
 \mathrm{can}(t_\psi)=0.
\]

This is stronger than the formal relation
$\mathrm{var}\circ\mathrm{can}=T-I$: it uses properness and the
decomposition theorem to turn monodromy invariance into actual liftability.

## Exact boundary

The theorem is stated for a proper map of varieties with $IC_X$
coefficients. Applying it to G048 requires placing the specified B057 class
in such a proper collision model, or proving the corresponding stack
extension. It also requires invariance under the collision-parameter
monodromy. B057 proves invariance under the detector loop $g$ in the
hyperplane complement; those are different actions. G049 isolates both
remaining obligations. Finally, surjectivity alone does not choose a lift or
prove that a lift has the required type and pairing.
