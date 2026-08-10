---
brick_id: B104
status: PROVED
base_field: C with rational chains
variety: an abstract collision total-space pair (W,N) receiving the chosen B057 detector and Saito's nearby-fiber pair (Y_c,Z_c), downstream attached to an arbitrary smooth projective complex 2n-fold X
smoothness: no smoothness needed for the chain theorem; downstream W comes from a collision with smooth nearby fiber and isolated nodal target
projectivity: not needed for the chain theorem; downstream collision and X projective
dimension: detector and Saito relative classes have degree 2n; bordisms have degree 2n+1
codimension: middle codimension n in the terminal application
coefficient_field: Q
cohomology_theory: relative singular chain complexes, long exact sequence of a pair, relative bordism, lift torsors, and primitive ambient homology
hodge_type: no Hodge type is created; downstream beta and c are rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B098-B103, elementary relative homology
claim: For a fixed detector class t and local boundary beta, the difference between t and a chosen Saito relative lift defines a lift-independent obstruction coset modulo the image of absolute nearby-fiber homology; this coset vanishes exactly when some lift of beta is relatively bordant to t in the collision pair, and one such bordism suffices for the ambient equality when the ambient realization factors through the pair.
falsifier: dependence of the quotient coset on the chosen lift, vanishing without any bordant lift, or a compatible ambient chain map sending bordant classes to different primitive ambient values
---

# B104 — The single-detector comparison is one obstruction coset

**Status:** PROVED

Let $(W,N)$ be a collision total-space pair. Suppose the selected B057 class
has an image

\[
 t_W\in H_{2n}(W,N;\mathbf Q(n)),
\]

and the inclusion of Saito's nearby pair induces

\[
 j_*:H_{2n}(Y_c,Z_c;\mathbf Q(n))
 \longrightarrow H_{2n}(W,N;\mathbf Q(n)).
\]

Fix a local relation $\beta$ and one lift
$\gamma_0\in H_{2n}(Y_c,Z_c)$ with $\partial\gamma_0=\beta$. Put

\[
 A=\operatorname{im}\!\left(
 H_{2n}(Y_c)\longrightarrow H_{2n}(Y_c,Z_c)
 \right).
\]

All lifts of $\beta$ are exactly the affine space $\gamma_0+A$. Define

\[
 \overline\Omega(t,\beta)=
 [t_W-j_*\gamma_0]
 \in H_{2n}(W,N)/j_*A.
\]

Replacing $\gamma_0$ by $\gamma_0+a$ changes the representative by
$-j_*a$, so the coset is independent of the chosen lift.

The coset vanishes if and only if there is $a\in A$ such that

\[
 t_W=j_*(\gamma_0+a)
 \quad\text{in }H_{2n}(W,N).
\]

Equality of these relative homology classes is equivalent to a relative
$(2n+1)$-chain in $(W,N)$ whose boundary is the difference of cycle
representatives. Hence vanishing is exactly the existence of one
class-specific relative bordism between the detector and a lift of $\beta$.

If a chain-level ambient realization through $(W,N)$ restricts to B098's
map on the source and Saito's good-retraction map on the target, bordant
classes have equal primitive ambient images. Since B098 sends $t$ to $c$,
the chosen Saito lift also maps to $c$. B100 shows that the primitive target
value is then independent of the remaining lift choice.

## Scope guard

B104 does not construct $(W,N)$, its two inclusions, or prove
$\overline\Omega(t,\beta)=0$. It proves that a full chain map on every
distributed thimble is stronger than the class-specific terminal argument
requires.
