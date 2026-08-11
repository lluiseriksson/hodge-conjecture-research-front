---
brick_id: G151
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a rational middle Hodge class zeta primitive for a very ample A and H=A^2
smoothness: X and the reduced marked scheme Z are smooth; the H^5 divisor must have the prescribed isolated ODPs and every retained incidence-smoothness clause
projectivity: X, its complete H^2 evaluation configuration, the H^5 nodal system, and all detector data are projective
dimension: dim X=2n; c=binom(2n+2,2); m=5; N=2c+2; E_2 is a self-dual code of dimension c+1
codimension: construct a self-associated H^2 point configuration whose span contains every marked full second osculator as a hyperplane, together with every G150 jet and detector clause
coefficient_field: C for self-association, osculators, jets, profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z, 2Z, and 3Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the degree-five full-support relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B226, G013, G090-G150, NG106-NG185, S082
claim: For every primitive input (X,A,zeta), construct H=A^2 and a reduced Z of 2binom(2n+2,2)+2 points whose H^2 evaluation columns are self-associated, whose rank-(c+1) span contains every marked full second osculator as a hyperplane, and which realizes every degree-five G150 ODP-profile, holonomy, finite-Kuranishi, rational-type, and specified-pairing clause.
falsifier: one primitive input for which no self-associated degree-two point configuration can be embedded in X with all osculator, doubled/tripled-jet, ODP, rationality, Hodge-type, and pairing obligations
---

# G151 — Construct the self-associated osculating core

B225 reduces the first possible one-slack construction to the fixed birth
degree

\[
m=5,\qquad
N=2c_{2n}+2,\qquad
\dim E_2=c_{2n}+1. \tag{1}
\]

The degree-two evaluation columns form a self-associated configuration
in \(\mathbf P^{c_{2n}}\). G151 asks to realize that configuration
*inside the fixed \(H^2\)-embedding of \(X\)* while simultaneously:

1. every marked full second osculator is a hyperplane in the same
   \((c_{2n}+1)\)-dimensional point span;
2. the adjacent \(Z,2Z,3Z\) restriction profile and nondegenerate
   degree-five ODP generator hold;
3. holonomy and the finite Kuranishi ladder close;
4. the full-support relation has rational type \((0,0)\) and nonzero
   specified pairing with \(\zeta\).

S082 classifies the abstract linear-algebra shape of self-associated
sets, but it supplies no theorem placing one on an arbitrary fixed
polarized variety with the osculator and detector data above.

B226/NG186 give a direct fixed-A counterexample: powered primitive
polarizations have empty two-triple defect locus, whereas every such
osculator configuration would be a complete clique in that locus.
Thus G151 is **NO-GO** with its displayed universal triple quantifier.
G152 permitted the exceptional polarization to be chosen; B228 later
closed that universal first-slack repair.
