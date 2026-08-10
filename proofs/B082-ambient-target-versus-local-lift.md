---
brick_id: B082
status: PROVED
base_field: C
variety: an arbitrary smooth projective complex 2n-fold, its plane-net hyperplane family, a smooth detector loop, and a prospective singular collision fiber
smoothness: X and the detector-loop fibers are smooth; the prospective collision fiber may be singular
projectivity: X and the hyperplane family are projective
dimension: ambient 2n, hyperplane fibers 2n-1, and plane-net base 2
codimension: middle codimension n; prospective proper supports have base codimension one or two
coefficient_field: Q
cohomology_theory: singular relative homology, Lefschetz thimbles, intersection cohomology, perverse stalks, and primitive homology
hodge_type: the B058 ambient target is rational type (0,0) after Q(n); no local lift inherits this type without a comparison theorem
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081, S029
claim: B022 and B057-B058 provide forward maps from a chosen local or thimble relation to ambient primitive homology and an ambient target c, but they provide no canonical reverse map from c to a collision stalk; entering B081's perverse filtration requires a collision-dependent lift constructed before any associated-grade projection.
falsifier: a cited canonical morphism from primitive ambient homology to the local relation stalk that is a right inverse to both B022 quotients and specializes the B057 chain independently of collision data
---

# B082 — An ambient target is not a local collision class

**Status:** PROVED

For a fixed collision fiber at $p$, write $R_p$ for its rational local
relation group. In the audited pencil model, B022 gives only forward arrows

\[
 R_p\longrightarrow \ker\partial
 \twoheadrightarrow \mathcal T(Y)
 \twoheadrightarrow PH_{2n}(X,\mathbf Q(n)).
\]

The first arrow depends on identifying the local relation with a thimble
combination. The second quotient kills equator extensions; the third has the
base-locus kernel $K$. Neither exact sequence supplies a reverse arrow.

B058 chooses

\[
 c\in PH_{2n}(X,\mathbf Q(n))^{(0,0)},
 \qquad \langle\zeta,c\rangle\ne0,
\]

and B057 realizes $c$ by a distributed smooth-locus extension chain. This
does not produce an element of $R_p$ for any single collision point $p$.
Indeed, a lift through the two B022 quotients is nonunique when either kernel
is nonzero, and membership of $c$ in the image of a fixed local detector
space is an additional condition. B059 shows that even nonzero pairing with
some local detector does not force the preselected $c$ itself to lie in that
detector space.

Therefore the expression “the nearby specialization of $c$ in
$H^{-1}(i_p^*K)$” has no meaning from B022/B057/B058 alone. One must first
construct collision data and a relative thimble or nearby-cycle class whose
generic realization is the B057 chain. Only its special boundary class may
then be placed in B081's canonical perverse filtration.

## Boundary

B082 does not prove that such collision data exist. G047 is the exact lift
obligation. It permits preservation of nonzero pairing rather than the
strictly stronger equality with the preselected ambient class $c$.
