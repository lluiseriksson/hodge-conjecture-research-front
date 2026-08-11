---
brick_id: B270
status: PROVED
base_field: C
variety: the projective plane Pi with six distinct reduced supports P6, a seventh point u, and a cubic through P6 that is a unit at u; downstream Pi is an isotropic plane in a split quadric Q^d
smoothness: Pi and all seven reduced supports are smooth; no divisor, ODP, or incidence germ is asserted
projectivity: the cubic and sextic plane linear systems and their first-jet restrictions are projective coherent data
dimension: dim Pi=2; a rank-one residual sextic first-jet image forces the residual cubic first-jet image to have rank one
codimension: six simple base conditions occur in degree three and six double base conditions in degree six; the result is a reduction of the planar cubic equality branch, not a Hodge codimension claim
coefficient_field: C for plane sections and first jets; Q remains separately required for the downstream detector
cohomology_theory: coherent restriction to reduced and double finite schemes and the square-zero first-jet algebra at u
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)) only downstream; no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B261, B264, B268, G190
claim: If C0 is a plane cubic through P6 with C0(u) nonzero and the image of H0(I_(2P6)(6)) in O_(2u) has rank one, then the image of H0(I_(P6)(3)) in O_(2u) also has rank one. Equivalently, every cubic through P6 union {u} is singular at u.
falsifier: a cubic C through P6 whose first jet is independent of C0's jet while every sextic double at P6 has first jet proportional to the jet of C0 squared
---

# B270 — Sextic equality forces anticanonical jet collapse

Let

\[
 V=H^0\bigl(\Pi,I_{P_6}(3)\bigr),\qquad
 W=H^0\bigl(\Pi,I_{2P_6}(6)\bigr), \tag{1}
\]

and let \(j_u\) denote restriction to the square-zero algebra
\(O_{2u}\). Choose \(C_0\in V\) with \(C_0(u)\ne0\). Then
\(j_u(C_0)\) is a unit.

For every \(C\in V\), the product \(CC_0\) vanishes doubly at \(P_6\),
so it lies in \(W\). If \(j_u(W)\) has rank one, it contains the unit
\(j_u(C_0^2)\) and therefore

\[
 j_u(CC_0)\in\langle j_u(C_0^2)\rangle. \tag{2}
\]

Multiplication by \(j_u(C_0)^{-1}\) in \(O_{2u}\) gives

\[
 j_u(C)\in\langle j_u(C_0)\rangle \qquad(C\in V). \tag{3}
\]

Thus \(j_u(V)\) has rank one. After subtracting the appropriate scalar
multiple of \(C_0\), every cubic in \(V\) that vanishes at \(u\) has
zero first jet there. Equivalently,

\[
 H^0\bigl(I_{P_6\cup\{u\}}(3)\bigr)
 \subset H^0\bigl(I_{P_6}I_u^2(3)\bigr), \tag{4}
\]

so every cubic through the seven reduced points is singular at \(u\).

In the cubic branch of G190, B260's good-edge perfect matching supplies
\(C_0\) as a product of three pair lines avoiding \(u\). B270 constructs
no marked scheme, ODP package, rational detector, specified pairing,
cycle, proof, or disproof of HC.
