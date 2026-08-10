---
brick_id: B111
status: PROVED
base_field: C with all comparison classes over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, one selected B058 detector, and a proposed projective collision
smoothness: X and generic hyperplane fibers smooth; proposed target clean nodal; no smoothness is needed for the logical sufficiency statement
projectivity: X, the hyperplane family, and collision projective in the application
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; comparison classes have middle degree 2n
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: relative thimble homology, nearby and special stalks, relative bordism, B022 quotients, and perverse-filtered rational vector spaces
hodge_type: selected source, nearby, lift, and ambient classes rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B083, B104, B109-B110, G067-G073, NG080, NG086
claim: To define and test the filtered obstruction for one selected B058 detector, it is sufficient to construct one collision-certified nearby class t_psi, one ordinary lift s with u(s)=t_psi, and the class-specific B022 and pairing compatibilities; a morphism on the entire distributed thimble complex is not necessary.
falsifier: a step in B083, B109, or the terminal class-specific pairing criterion that requires images of distributed classes other than the selected detector, or failure of B104's one-class relative-bordism sufficiency
---

# B111 — One selected realization is sufficient

**Status:** PROVED

Fix the B057 detector class $t$. The input needed by B109 consists of

\[
 t_\psi\in P_\psi,
 \qquad
 s\in S,
 \qquad
 u(s)=t_\psi,
\]

together with a geometric certificate that $t_\psi$ realizes this selected
$t$. B109 then forms

\[
 [s]\in S/(S_0+\ker u)
\]

without referring to any other class in $H(C_{\mathrm{dist}})$. B083's
ordinary lift criterion is equally class-specific: it asks only whether
$\operatorname{can}(t_\psi)=0$.

The two B022 quotient checks and the final pairing are evaluations on this
same selected class. Hence the required source datum may be a marked
comparison chain, a relative bordism, or another collision-certified
correspondence defined only for $t$; it need not extend to a natural
morphism on the whole distributed complex.

B104 proves the corresponding downstream statement at chain level. Once the
selected detector and one target lift are placed in a collision total-space
pair, one relative bordism between them suffices for compatible ambient
equality. NG080 already excludes a full map on every thimble as a necessary
condition.

## Consequence for G073

The displayed map

\[
 \rho:H(C_{\mathrm{dist}})\to P_\psi
\]

in the first version of G073 was sufficient but stronger than required.
The corrected gate asks for a class-specific realization certificate

\[
 t\rightsquigarrow t_\psi,
\]

ordinary liftability, rational Hodge type, survival through both B022
quotients, and nonzero prescribed pairing. It does not ask for images of
unrelated thimble classes.

## Scope guard

B111 is a quantifier reduction. It neither constructs the selected
realization nor proves its liftability, Hodge type, or pairing, and therefore
does not advance the general Hodge Conjecture.
