---
brick_id: B166
status: PROVED
base_field: C
variety: the proper projective exhaustive tracked-ODP family g:Y_B->F_B of B163, with reduced escape divisor D in the smooth basis germ
smoothness: F_B is smooth; at a generic point of each irreducible component of D the component is smooth and the tracked Milnor balls are disjoint
projectivity: g is projective and proper base change identifies its direct-image stalks with fiber cohomology
dimension: hypersurface dimension r=2n-1 in the Hodge application; base dimension arbitrary
codimension: each nonpersistent scalar critical-value germ cuts a codimension-one reduced divisor component on F_B
coefficient_field: Q
cohomology_theory: proper direct images, perverse cohomology, ODP vanishing cycles, characteristic cycles, and normal Morse groups
hodge_type: the node-polar multiplicity has no asserted specified Hodge type or detector pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B158-B165, S030, S052, S067
claim: Let D be the reduced union in F_B of the zero divisors of the nonidentically-zero restricted extra critical values. At a generic smooth point of an irreducible component D_alpha, the off-zero coefficient of CC^+(K_B) along the conormal closure to D_alpha equals k_alpha, the number of tracked nodes whose reduced escape divisor contains D_alpha. In particular it is positive exactly when that component records node escape.
falsifier: a generic escape-divisor component with k_alpha tracked rank-one ODP specialization groups but total positive perverse microlocal multiplicity different from k_alpha
---

# B166 — Escape divisors have positive node-polar multiplicity

Write \(\bar\tau_i=\tau_i|_{F_B}\) for every extra tracked node. A node
persists exactly when \(\bar\tau_i\equiv0\). Let

\[
 D=\bigcup_{\bar\tau_i\not\equiv0}V(\bar\tau_i)_{\mathrm{red}}
   =\bigcup_\alpha D_\alpha.
\]

Choose a generic smooth point \(u\in D_\alpha\) away from all other
components and a small disk normal to \(D_\alpha\). Suppose precisely
\(k_\alpha\) tracked critical-value divisors contain \(D_\alpha\) there.
Milnor-ball excision splits the normal specialization group by the distinct
critical points. S030 and B162 give one rational middle rank for each of
those \(k_\alpha\) ODPs and no contribution from the locally trivial
complement. Therefore

\[
 \dim_{\mathbf Q}\mu_{(u,\xi)}(K_B)=k_\alpha, \tag{1}
\]

for a generic nonzero conormal covector \(\xi\) to \(D_\alpha\). Passing to
perverse cohomology and using the normalized t-exact microlocal Morse test,
(1) becomes

\[
 \sum_j m_{\alpha,j}=k_\alpha>0. \tag{2}
\]

The count is independent of the contact order of \(\bar\tau_i\): the
specialization cone compares the singular ODP fiber with a nearby smooth
fiber and has rank one. Nonreduced equations can affect monodromy but not
this generic reduced-support rank.

Consequently B165's positive certificate vanishes off the zero section if
and only if every \(\bar\tau_i\) is identically zero. In the tracked-Morse
regime it is an exact polar restatement of B158/B163, not a new source of
persistence.

## Scope guard

The formula uses exhaustive disjoint ODP control and a generic point of a
reduced escape component. It neither treats untracked singularities nor
proves the specified relation-channel pairing.
