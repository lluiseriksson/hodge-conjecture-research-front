---
brick_id: G049
status: EXPLORATORY
base_field: C with the detector and comparison maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 plane-net detector, and a proper one-parameter topology-changing collision model
smoothness: X and generic detector fibers smooth; endpoint singular; IC coefficients allow a singular proper total space
projectivity: collision model must be proper/projective
dimension: ambient 2n, hyperplane fibers 2n-1, plane-net base 2, and collision parameter 1
codimension: middle codimension n; collision endpoint has parameter codimension one and plane-base codimension at least one
coefficient_field: Q
cohomology_theory: relative thimble homology, rational intersection cohomology, nearby cycles, local monodromy, and the local invariant-cycle theorem
hodge_type: the nearby class and selected special lift must be rational and ultimately retain type-(0,0) pairing after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022-B023, B057-B059, B083-B085, G047-G048, NG059-NG062
claim: Construct a proper collision model realizing the B057 ordered extension chain as a rational nearby intersection-cohomology class t_psi and prove t_psi is fixed by the collision-parameter local monodromy; B084 then supplies a rational special-fiber lift.
falsifier: failure of chain realization in nearby intersection cohomology, nontrivial collision monodromy on the specified class, or inability to place the comparison in the proper-variety IC setting of B084
---

# G049 — Collision-monodromy invariance of the specified chain

**Status:** EXPLORATORY  
**Parent gate:** G048

Construct a proper algebraic degeneration $f:\mathfrak X\to T$ and a class

\[
 t_\psi\in H^{-1}(i_p^*\Psi_fIC_{\mathfrak X})
\]

whose chain realization is the ordered B057 extension
$t=\tau_g(\alpha)$. Then compute the local collision monodromy and prove

\[
 T_{\mathrm{coll}}t_\psi=t_\psi.
\]

B084 then gives

\[
 \mathrm{can}(t_\psi)=0
\]

and at least one rational special-fiber lift. The remaining part of G048 is
to control the lift ambiguity, Hodge type, B022 quotient image, and pairing.

B085/NG062 refine the fixed-vector requirement. Constancy of the ambient
class makes $M_{\mathrm{coll}}t-t$ kernel-valued but need not make it zero.
G050 is the exact current subgate: compute its class in
$\operatorname{coker}(M_J-I)$ and kill it by an explicit kernel adjustment.

## First concrete calculation

Choose a curve transverse to a boundary divisor in the deformation space of
plane nets. Express its braid action on the ordered Lefschetz thimbles and
apply that action to B057's exact coefficient vector

\[
 c_i=\varepsilon\langle\alpha_{i-1},\delta_i\rangle.
\]

It is insufficient to prove that the thimble module or relation subspace is
preserved; the specified vector must be fixed after both B022 quotient
identifications. B023 guarantees only invertible transport within a fixed
Morse fibration and does not supply this fixed-vector calculation.
