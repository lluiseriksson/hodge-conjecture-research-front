---
brick_id: G150
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a rational middle Hodge class zeta primitive for a very ample A and H=A^2
smoothness: X and Z are smooth and reduced; the degree-m divisor must have the G149 isolated ODPs and every retained incidence-smoothness clause
projectivity: X, all H^k evaluation systems, the marked scheme, nodal family, and detector data are projective
dimension: dim X=2n; m>=5; N=D_(2n)(m)+1; the two Gale-dual code dimensions are c_(2n)+1 and L_(2n)(m-2)
codimension: construct the exact weighted Gale-dual reduced evaluation core together with the doubled/tripled jet profile and every detector clause
coefficient_field: C for sections, Gale weights, jets, profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z, 2Z, and 3Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support relation must admit rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B224, G013, G090-G149, NG106-NG184
claim: For every primitive input (X,A,zeta), construct H=A^2, m>=5, Z of size D_(2n)(m)+1, and a full-support rational relation lambda such that E_(m-2)=E_2^(perp_lambda), the degree-two code has rank c_(2n)+1 and contains every marked full second osculator, and every G149 ODP-profile, holonomy, Kuranishi, rational-type, and specified-pairing clause holds.
falsifier: one primitive input for which no reduced first-slack weighted Gale core can be coupled to all doubled/tripled-jet, ODP, rationality, Hodge-type, and specified-pairing requirements
---

# G150 — Construct the weighted-Gale first-slack core

B223 rewrites G149's two transport isomorphisms as the exact equation

\[
E_{m-2}=E_2^{\perp_\lambda} \tag{1}
\]

for a full-support relation \(\lambda\), with

\[
\dim E_2=c_{2n}+1,\qquad
\dim E_{m-2}=L_{2n}(m-2). \tag{2}
\]

G150 makes (1)–(2) the concrete reduced-scheme construction target.
They must occur on the same \(Z\) that realizes the full second-osculator
absorption, adjacent \(Z,2Z,3Z\) profile, central ODP generator,
holonomy, finite Kuranishi closure, rational type-\((0,0)\), and nonzero
specified pairing.

The first attempted mechanism is a reduced transverse complete
intersection with its residue pairing. B224/NG184 show why that attempt
does not propagate universally: adjunction fixes the complementary
line bundle, which need not be \(H^{m-2}\). G150 therefore requires a
new non-complete-intersection construction or a proved comparison that
corrects the canonical twist without assuming the desired detector.
