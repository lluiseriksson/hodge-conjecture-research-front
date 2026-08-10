---
brick_id: B114
status: PROVED
base_field: C with finite-cover and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its original plane-net collision family, and the finite S3 root cover with semistable proper model
smoothness: X and the generic hyperplane fibers smooth; covered source semistable regular; target collision singular
projectivity: X, hyperplane family, finite cover, semistable model, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; collision support has positive base codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, perverse cohomology, strict support, finite-cover unit and trace, S3 invariants, and selected class coordinates
hodge_type: unit, trace, invariant projection, and full-support identification preserve rational Hodge subobjects and type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B063, B072, B074-B077, B081, B113, G042-G043, G075
claim: On the canonical relevant perverse-grade full-support summand, the S3-invariant covered nearby-cycle object is canonically the original downstairs object. A selected invariant covered class has nonzero full-support coordinate if and only if its descended downstairs coordinate is nonzero; the root cover and Reynolds projection cannot create that landing.
falsifier: failure of B074's invariant full-support isomorphism on the relevant perverse grade, a nonzero invariant covered full-support class descending to zero, or a zero downstairs class whose unit has nonzero invariant full-support coordinate
---

# B114 — Invariant full-support landing is the downstairs landing

**Status:** PROVED

Let (F) be the canonical relevant perverse-grade full-support object on the
original base and let (widetilde F) be the corresponding object after the
finite (S_3) root cover and proper pushdown. B074 gives an isomorphism of
rational Hodge objects

\[
 widetilde F^{S_3}\simeq F.
\]

B076 realizes this identification through nearby-cycle unit and normalized
trace maps

\[
 U:F\longrightarrow\widetilde F^{S_3},
 \qquad
 R:\widetilde F^{S_3}\longrightarrow F,
 \qquad
 R\circ U=\operatorname{id}_F.
\]

On the invariant full-support summand, B074 makes (U) and (R) inverse
isomorphisms. Therefore, for a selected class (xin F),

\[
 x\ne0\quad\Longleftrightarrow\quad Ux\ne0,
\]

and for an invariant selected covered class (widetilde x),

\[
 widetilde x\ne0\quad\Longleftrightarrow\quad R\widetilde x\ne0.
\]

All maps are rational Hodge morphisms. The same statement holds after
restricting to type ((0,0)) and to B081's canonical perverse grade.

## Consequence for G075

The root cover is a technically useful semistable model but not a source of
class-level full-support nonvanishing. G075's invariant coordinate is nonzero
exactly when the corresponding original selected specialization coordinate
is nonzero. B113 separately shows that the local (A_2) standard component
does not contribute to this invariant coordinate.

The remaining gate is thus downstairs: construct the selected original
specialization and prove its canonical full-support coordinate is nonzero.
G076 records this selected-excess formulation of G043; it is not a new
reduction.

## Scope guard

B114 proves an equivalence of coordinates. It constructs neither coordinate
and provides no algebraic cycle or general Hodge-class progress.
