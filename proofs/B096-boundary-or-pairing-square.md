---
brick_id: B096
status: PROVED
base_field: C with rational Hodge structures
variety: the type-(0,0) stalk sequence of a projective collision for an arbitrary polarized smooth projective complex 2n-fold and its B058 detector
smoothness: generic hyperplane fiber smooth; special target clean nodal; proof uses the resulting finite-dimensional exact sequence
projectivity: collision and ambient family projective in the application
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: nearby and vanishing-cycle long exact sequence, dual rational Hodge structures, perverse grade, B022 quotients, and Saito pairing
hodge_type: restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B058, B083, B095
claim: For the exact segment W->S->P containing the special-to-nearby map u and detector functional F, the nonzero-cokernel branch of B095 is exactly F composed with the preceding map being nonzero; if that composition vanishes, a pairing-compatible descended square identifying lambda(t_psi) with the nonzero B058 ambient pairing proves the second branch.
falsifier: exact rational data where [F] in coker(u^*) is nonzero but F composed with the preceding map is zero, or a commuting pairing square with nonzero B058 value but zero descended evaluation
---

# B096 — Either the ambiguity boundary detects, or the pairing square does

**Status:** PROVED

Take the type-$(0,0)$ part of the B083 long exact sequence around degree
$-1$:

\[
 W\xrightarrow{d}S\xrightarrow{u}P.
\]

Exactness gives $\operatorname{im}d=\ker u$. Dualizing finite-dimensional
rational vector spaces gives

\[
 \operatorname{im}u^*=\ker d^*.
\]

Hence the first branch of B095 has the concrete form

\[
 [F]\ne0\text{ in }\operatorname{coker}u^*
 \quad\Longleftrightarrow\quad
 d^*F=F\circ d\ne0.
\]

If $F\circ d=0$, then $F=u^*\lambda$ and the detector value is the
well-defined scalar $\lambda(t_\psi)$. Suppose the actual collision
comparison proves the pairing square

\[
 \lambda(t_\psi)=\langle\zeta,c\rangle,
\]

where $c$ is B058's selected ambient tube class. B058 gives
$\langle\zeta,c\rangle\ne0$, so the second B095 branch holds.

Thus G059 reduces to an exhaustive alternative: either the ambiguity-boundary
functional $F\circ d$ is nonzero, or it vanishes and the displayed
pairing-square identity closes the gate.

## Boundary

B096 does not prove the square commutes for a topology-changing collision.
That is G060. It also does not infer $F\circ d=0$ from liftability of
$t_\psi$; NG072 records that invalid implication.
