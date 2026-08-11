---
brick_id: B093
status: PROVED
base_field: C with rational coefficients
variety: the plane-net hyperplane family of a smooth projective complex 2n-fold and a clean nodal parameter H
smoothness: ambient and generic hyperplane fibers smooth; H has the nodal/quasi-local hypotheses of B009/B052
projectivity: universal hyperplane family and plane net projective
dimension: ambient 2n; hyperplane fibers 2n-1; parameter base 2
codimension: middle codimension n; H is a point of the plane base and lies on a positive-codimension nodal stratum
coefficient_field: Q
cohomology_theory: rational intermediate extension, perverse sheaves, mixed Hodge modules, local intersection cohomology, and the perverse filtration
hodge_type: the nodal relation group is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B009-B010, B052, B080-B081, B134
claim: On the plane base, if L=R^(2n-1)h_*Q on the smooth locus and P=j_!*L[2], then H^(-1)(i_H^*P) is canonically the dual of the nodal relation group; inside a proper direct image it is reached only through the canonical E_infinity^(-1,0) perverse grade and the full-support strict-support summand.
falsifier: a different perverse shift for L on the plane base, or a clean nodal model where H^(-1)(i_H^*P) is not canonically dual to the B009/B052 relation group
---

# B093 — The local relation is the full-support perverse stalk

**Status:** PROVED

Let $U$ be the smooth locus of the plane-net hyperplane family and put

\[
 L=R^{2n-1}h_*\mathbf Q|_U,
 \qquad P=j_{!*}L[2].
\]

Because the base has complex dimension two, $P$ is perverse. B080 gives the
exact shift identity

\[
 H^1(j_{!*}L)_H=H^{-1}(i_H^*P).
\]

B009 and B134 identify the left side with the dual of the rational relation
space among the nodal vanishing cycles, and B052 proves the same rank and
type $(0,0)$ for the clean arrangement channel. Thus

\[
 R(H)_1^{(0,0),\vee}\simeq H^{-1}(i_H^*P)^{(0,0)}
\]

canonically, with the Tate twist understood. A polarization can model this
dual by a kernel, but a specified cohomological class remains a functional
on relations.

If $P$ occurs inside a proper pushdown complex $K$, B081 supplies the exact
access route: first pass the total class in $H^{-1}(i_H^*K)$ to the canonical
$E_\infty^{-1,0}$ associated grade; then take the unique full-support
strict-support summand of ${}^pH^0(K)$. There is no canonical total derived
projection $K\to P$ supplied by the decomposition theorem.

## Consequence

G056's proposed arbitrary edge map from the total special stalk is the wrong
object. The corrected gate G057 asks whether the specified lift has a nonzero
canonical associated-grade/full-support coordinate in the displayed group.
