---
brick_id: G145
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with a very ample H, a specified primitive rational middle Hodge class, and a class-directed reduced marked scheme Z
smoothness: X and Z are smooth; the central degree-m divisor must have isolated ODPs and every incidence smoothness clause remains exactly as in G143-G144
projectivity: X, powers H^k through m, marked osculating spaces, the nodal linear system, and detector family are projective
dimension: dim X=2n; N must equal the extremal floor D_(2n)(m)
codimension: construct the full G144 package on the equality face where all degree-two marked osculators coincide and both complementary transport maps are isomorphisms
coefficient_field: C for sections, jets, profiles, holonomy, and relation transports; Q for the specified Hodge class, detector, and nonzero pairing
cohomology_theory: coherent finite-jet restriction, principal parts through order two, graded value relations, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) and pair nontrivially with the arbitrary specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the specified class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B221, G013, G090-G144, NG106-NG182, S081
claim: For every arbitrary pair (X,zeta) in the standard rational Hodge problem, construct the complete G144 configuration with N=D_(2n)(m); equivalently, retain every G143 profile, holonomy, congruence, full-system, rational-detector, specified-pairing, pure-cubic-closure, and later-rung clause while realizing B216's common marked osculator and transport-isomorphism equalities.
falsifier: one smooth projective complex 2n-fold and primitive rational middle Hodge class for which no choice of very ample H, m, and Z realizes every displayed clause at N=D_(2n)(m)
---

# G145 — Extremal common-osculator branch

This is the equality branch of G144. For arbitrary \((X,\zeta)\), find
the complete class-directed G143 configuration with

\[
 N=D_{2n}(m). \tag{1}
\]

B216 then forces, for \(m\ge3\),

\[
 S^{(0)}_{2,Z}=\widehat O^{(2)}_{p_i}(H^2)
 \quad\text{for all }p_i\in Z, \tag{2}
\]

and makes the two complementary relation transports at degrees
\(2\) and \(m-2\) isomorphisms. For \(m=2\), replace (2) by the common
affine tangent-space equality and the degree-one transport isomorphism.

The falsifiable universal theorem is exactly the existence assertion
above with every G143-G144 clause retained. A proof would propagate to
G144 and then through the existing sufficient chain; a counterexample
would close only this equality branch, not the slack range \(N>D_{2n}(m)\)
and not the rational Hodge Conjecture.

No special-family osculating defect counts unless it supplies an explicit
proved reduction from arbitrary \((X,\zeta)\) and preserves the rational
detector with its specified nonzero pairing.

B221 supplies the falsifier anticipated above. For the legitimate input
\((Q^{2n},a-b)\), every very ample Gauss map is injective, whereas
B217 shows that any equality configuration would put
\(D_{2n}(m)>1\) marked points in one Gauss fiber. Thus the universal
G145 claim is **NO-GO**. Only G148's strict-slack range survives.
