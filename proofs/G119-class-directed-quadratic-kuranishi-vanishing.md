---
brick_id: G119
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system incidence of an arbitrary smooth projective complex variety with a proposed class-directed ordered ODP configuration
smoothness: the projective variety, labelled ODP critical incidences, and B185 basis carrier are smooth; smoothness of the full simultaneous-node germ is not assumed
projectivity: every tangent, gradient, Hessian, and value map comes from the full projective universal family
dimension: arbitrary projective and parameter dimensions; N nodes; value rank R<N; first nonautomatic conormal order one
codimension: force K_B into m^3, equivalently kill the quadratic Kuranishi tensor in coker(E) tensor Sym^2((ker E)^*)
coefficient_field: C for Hessian and Kuranishi tensors; Q for the specified rational Hodge class and detector
cohomology_theory: second-order ODP deformation theory, finite conormal jets, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B186, G013, G090-G118, NG106-NG150
claim: Construct the class-directed full-incidence ODP data so that B146's complete relation-Hessian obstruction vanishes, equivalently K_B is contained in m^3 and the order-one conormal jet is zero, while retaining the uniform matroid, adjoint defect, primitive image, rational type, and specified nonzero pairing.
falsifier: a nonzero B146 relation-Hessian pairing, nonzero pure class Omega_Q in the synchronized branch, loss of class direction or any detector clause, or substitution of tangent rank for quadratic vanishing
---

# G119 — Kill the first nonautomatic Kuranishi rung

B186 decomposes G118 into the finite ladder

\[
 \kappa_2,\kappa_3,\ldots,\kappa_{D_{\mathrm{car}}}.
\]

The tangent-rank choice already gives \(K_B\subset\mathfrak m^2\), so the
constant conormal jet vanishes automatically. The first new obligation is

\[
 K_B\subset\mathfrak m^3
 \quad\Longleftrightarrow\quad
 \kappa_2=0
 \quad\Longleftrightarrow\quad
 j^1\beta_{K_B}=0. \tag{1}
\]

By B146, (1) says that every value relation annihilates the inverse-Hessian
quadratic form on every conditional-gradient direction. In the synchronized
branch, B153/G097 decompose it into the mixed Hessian condition and
\(\Omega_Q=0\).

G119 asks for this vanishing from arbitrary \((X,\zeta)\), in the actual
full linear system, while retaining the uniform node matroid, positive
adjoint defect, nonzero primitive image, rational type \((0,0)\), and
specified nonzero Saito pairing.

Even success at G119 would close only the quadratic rung. NG150 proves that
the cubic rung does not follow formally.

## First linear-algebra precursor after B187

For a no-coloop value matroid, B187 selects a full-support relation and
forces \(\operatorname{rank}D\le nN\). G120 isolates the weaker precursor
of realizing one such global Lagrangian channel with the class-directed
detector. NG151 shows that this global condition does not provide the
nodewise split Lagrangian core used by anchored constructions.
