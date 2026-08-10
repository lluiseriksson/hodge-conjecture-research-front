---
brick_id: G068
status: EXPLORATORY
base_field: C with collision chains and comparison maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its specified B058 detector, and an actual projective collision to a clean isolated nodal hyperplane fiber
smoothness: X and nearby fibers smooth; target has finitely many ordinary double points; collision total space stratified as needed for relative chains
projectivity: X, plane-net family, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; detector and target classes degree 2n; bordism degree 2n+1
codimension: middle codimension n; special singular support finite
coefficient_field: Q
cohomology_theory: collision total-space relative homology, B057 thimbles, Saito relative cycles, lift torsors, good retraction, B022 quotients, and primitive ambient homology
hodge_type: local relation and primitive ambient target rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B081-B083, B093-B105, G047-G067, G069, NG069-NG081, S022
claim: Construct a collision total-space pair (W,N) receiving the specified detector class and Saito nearby pair, define the B104 obstruction coset for beta=r_H(beta_sp), prove the coset vanishes, and prove the ambient realization through (W,N) restricts to B098's value c and Saito's good-retraction map.
falsifier: undefined collision pair or inclusions, nonzero obstruction coset, wrong marked boundary, failure of rational type, or incompatible primitive ambient realization
---

# G068 — Kill the selected detector's relative-bordism obstruction

**Status:** EXPLORATORY

For the actual class-specific collision, construct a topological pair $(W,N)$
and maps that place:

1. B057's selected detector in $H_{2n}(W,N;\mathbf Q(n))$ as $t_W$; and
2. Saito's pair $(Y_c,Z_c)$ in $(W,N)$ by a map $j$.

Set $\beta=r_H(\beta_{\mathrm{sp}})$, choose any relative lift $\gamma_0$ of
$\beta$, and form B104's lift-independent coset

\[
 \overline\Omega(t,\beta)=
 [t_W-j_*\gamma_0]\pmod{j_*A},
 \qquad
 A=\operatorname{im}\!\left(
 H_{2n}(Y_c)\longrightarrow H_{2n}(Y_c,Z_c)
 \right).
\]

Prove

\[
 \overline\Omega(t,\beta)=0.
\]

Finally construct the ambient chain realization through $(W,N)$ and verify
that it restricts to B098's nearby map on $t_W$ and to Saito's
good-retraction map on the target. B104 then produces one target lift with
primitive ambient value $c$; B100 removes dependence on that lift.

This is a class-specific sufficient gate. It asks for one detector-specific
bordism and one exact coset calculation, not a natural comparison on all
thimble classes.

## Endpoint correction

B105/NG081 show that this gate is sufficient but still stronger than the
terminal Saito criterion. It is retained as a possible geometric mechanism,
not as the active minimal obligation. G069 only asks for the exact scalar
inequality obtained after primitive ambient realization and pairing with the
specified class.
