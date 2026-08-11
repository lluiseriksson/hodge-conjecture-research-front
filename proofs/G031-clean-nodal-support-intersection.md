---
brick_id: G031
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a sufficiently high universal hyperplane family
smoothness: X is smooth; the sought hyperplane has only ordinary double points and its local discriminant branches form a Li-clean arrangement
projectivity: X and the universal hyperplane family are projective
dimension: dim_C X = 2n; the hyperplane fibers have dimension 2n-1 and the local parameter slice has dimension equal to the clean arrangement rank
codimension: middle codimension n; the sought parameter lies in the codimension-at-least-two support of the specified class
coefficient_field: Q
cohomology_theory: singular and intersection cohomology, mixed Hodge modules, vanishing cycles, local relations, and primitive homology with Tate twist
hodge_type: primitive rational type (0,0) input and a rational type-(0,0) local relation after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the input class may be assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007, B009-B010, B012, B054, B056-B059, B125, G008, G028-G030, G084, and NG037-NG039
claim: For every nonzero primitive rational Hodge class zeta, some sufficiently high hyperplane family contains a Li-clean multipart nodal member Y_p and a rational local relation beta whose Saito ambient class pairs nontrivially with zeta.
falsifier: a smooth projective complex 2n-fold and nonzero primitive rational Hodge class for which every clean multipart nodal local relation in every sufficiently high hyperplane family has ambient image orthogonal to zeta
---

# G031 - Clean-nodal intersection with class-specific support

**Status:** EXPLORATORY — active parent; exact incidence subgate G084

## Falsifiable theorem

For every polarized smooth projective \(X/\mathbf C\) of dimension \(2n\)
and every

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)},
\]

find a sufficiently high hyperplane family and a Li-clean multipart nodal
member \(Y_p\) carrying

\[
 \beta\in R(Y_p)_1^{(0,0)},\qquad
 \langle\zeta,\Phi_{Y_p}(\beta)\rangle\ne0.
\]

B010 then proves \(\zeta|_{Y_p}\ne0\), and B007 propagates universal
existence to the standard rational Hodge Conjecture. B054 verifies the full
rational type-\((0,0)\) local channel once the stated clean nodal geometry
exists.

B125 removes the remaining local-class bookkeeping: G031 is equivalent to
the single incidence

\[
 \Sigma_{\zeta,m}\cap C_m^{\mathrm{clean}}\ne\varnothing
\]

for some high power. G084 is this exact active subgate.

This theorem is a sufficient mechanism, not a known equivalent
reformulation: HC guarantees a detecting singular member by B007, but no
audited theorem upgrades that member to the Li-clean multipart nodal locus.

## Attempt 1 - Generic plane localization

B056 puts any selected global tube detector in a generic projective plane
net. This controls the fundamental group and preserves its ambient tube
class, but it does not place a point of the class-specific support
\(\operatorname{Sing}(\zeta)\) in that plane. By B012 the support has
codimension at least two. A plane can meet a nonempty component of the right
codimension, but no dimension argument proves that the support is nonempty;
components of larger codimension can also be missed by a generic plane.

## Attempt 2 - Collide the exact global target

G030 asks for the stronger identity
\(\Phi_{Y_p}(\beta)=c\) with the particular B058 tube target. B059 and
NG039 show that this identity is not logically necessary. Weakening it to
the displayed nonzero pairing removes the artificial direction constraint,
but does not construct the collision or support point.

## Precise remaining obstruction

The unresolved datum is a class-controlled incidence:

\[
 \operatorname{Sing}(\zeta)
 \cap
 \{\text{Li-clean multipart nodal hyperplanes}\}
 \ne\varnothing.
\]

B012 does not even prove the first set nonempty. B054 computes the local
channel on the second set but gives no information about its pairing with
\(\zeta\). B056-B058 give a global nonorthogonal tube but no specialization
to this intersection. Thus the gate remains terminal-hard; describing it
more accurately has not reduced its open mathematical content.

## Re-entry condition

Prove either a class-specific support theorem forcing the displayed
intersection, or a topology-changing specialization of the B057 detector
chain whose local Saito image merely retains nonzero pairing with \(\zeta\).
Every specialization step must be checked through both B022 quotients and
the rational Tate-normalized Hodge structure.
