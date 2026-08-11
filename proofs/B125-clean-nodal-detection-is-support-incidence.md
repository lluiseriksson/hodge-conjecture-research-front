---
brick_id: B125
status: PROVED
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X and its sufficiently high universal hyperplane systems
smoothness: X smooth; the tested parameter has a nodal hyperplane fiber whose discriminant branches form a Li-clean arrangement
projectivity: X and the universal incidence family projective
dimension: dim_C X=2n; hyperplane fibers have dimension 2n-1; parameter dimension arbitrary
codimension: middle cycle codimension n; class-specific local support has parameter codimension at least two
coefficient_field: Q
cohomology_theory: intersection cohomology, local Green-Griffiths invariants, Saito vanishing-cycle relations, and primitive Betti homology
hodge_type: zeta primitive rational type (0,0) after Q(n); every rational nodal relation type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence in the terminal application
scope: absolute
dependencies: B007, B010, B012, B054, G031, S022 Theorems 1 and 3, S024 Corollary 3.10
claim: For a fixed nonzero primitive rational Hodge class zeta, G031 is equivalent to nonemptiness of the intersection between zeta's local restriction support and the Li-clean multipart nodal locus in some sufficiently high hyperplane system; once a point of this intersection is found, existence and type of a detecting relation are automatic.
falsifier: a clean nodal support point with nonzero restriction but no type-(0,0) relation pairing nontrivially with zeta, or such a pairing at a point outside the restriction support
---

# B125 — Clean-nodal detection is exactly a support incidence

**Status:** PROVED

For the parameter space \(P_m=|L^m|\), define

\[
 \Sigma_{\zeta,m}
 =\{p\in P_m:\zeta|_{Y_p}\ne0\}
\]

using B012's local intersection-cohomology restriction, and let
\(C_m^{\mathrm{clean}}\) be the locus of multipart nodal fibers whose local
discriminant branches form the Li-clean arrangement required by B054.

At any \(p\in C_m^{\mathrm{clean}}\), Saito's Theorem 3 makes every rational
nodal relation type \((0,0)\) after \(\mathbf Q(n)\). B054 identifies the
entire rational degree-one local channel with that relation kernel. B010 then
gives the equivalence

\[
 p\in\Sigma_{\zeta,m}
 \quad\Longleftrightarrow\quad
 \exists\beta\in R(Y_p)_1^{(0,0)}:
 \langle\zeta,\Phi_{Y_p}(\beta)\rangle\ne0.
\]

Consequently G031 is exactly

\[
 \boxed{
 \exists m\gg0:\quad
 \Sigma_{\zeta,m}\cap C_m^{\mathrm{clean}}\ne\varnothing.
 }
\]

No additional cycle-construction, Hodge-type, or relative-lift choice remains
after the parameter \(p\) is found. Conversely, every G031 relation places
its parameter in this intersection.

## Consequence

The clean-nodal obligation is geometric incidence, recorded as G084. B127
then splits it into terminal support nonemptiness G008 and conditional cleanup
G085. B012 gives only \(\operatorname{codim}\Sigma_{\zeta,m}\ge2\); it
neither proves this support nonempty nor forces it to meet the clean nodal
locus.

## Scope guard

B125 is an exact reformulation under the clean-nodal hypotheses. It proves no
support point exists, constructs no algebraic cycle, and does not turn a
global Green-Griffiths invariant into a local one.
