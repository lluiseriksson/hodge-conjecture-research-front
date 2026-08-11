---
brick_id: NG137
status: NO-GO
base_field: C
variety: reduced no-infinity gradient complete intersections of degree-m affine polynomial families, with ordered tracked and auxiliary critical points
smoothness: all critical points and parameter sections are smooth and Morse
projectivity: the homogenized gradient scheme is projective in P^d; no statement is made for arbitrary projective varieties
dimension: d spatial variables; selector degree e=d(m-1)-d-1-m>=0; N tracked points; central evaluation rank R<N
codimension: N-R exact residue selectors are required to lift every central tracked-value relation
coefficient_field: C
cohomology_theory: residual Cayley-Bacharach duality, evaluation codes, and Grothendieck residues
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic cycle or Hodge detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B170-B173, G100, G107, S070
claim: A full analytic frame of maximal-degree Jacobi selectors vanishing on every auxiliary critical point supplies a route to G100 that is weaker than moving critical-evaluation rank rigidity.
falsifier: B173 identifies the weighted selector space with the dual kernel of degree-m tracked evaluation at every fiber, making an analytic N-R selector frame equivalent to constant rank R
---

# NG137 — Exact Jacobi selectors do not bypass G107

B172 left open the possibility that global residues might directly lift
the \(N-R\) central critical-value relations. The most natural
implementation is to choose degree-\(e\) numerators that vanish at every
auxiliary critical point, where

\[
 e=d(m-1)-d-1-m
\]

is the largest degree for which \(f_tA\) remains in Jacobi's vanishing
range.

B173 proves fiberwise that the Hessian-weighted rows of all such selectors
are exactly

\[
 \ker\!\left(\operatorname{ev}_{T_t}^{\,m}\right)^*.
\]

Therefore \(N-R\) independent analytic selector rows exist near the
central fiber exactly when the moving degree-\(m\) evaluation rank stays
\(R\). By B170 this is G107 in the full polynomial coefficient family.

The exact-selector residue route is consequently a dual presentation of
G107, not a weaker proof of \(H_\tau=0\). This does not refute the existence
of constant-rank configurations and does not close G100.

## Re-entry

A residue route can still differ from G107 only by using input outside
B173's equality, most directly:

1. allow a nonzero auxiliary residue \(\rho_A\) whose class vanishes in
   \(\mathcal O/I_\tau\);
2. use a compact/projective residue duality whose complementary space is
   not the full moving value-evaluation space; or
3. prove G107 itself, with all detector clauses.

The first option is isolated as G108.
