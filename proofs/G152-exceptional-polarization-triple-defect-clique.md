---
brick_id: G152
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A preserving that primitive target
smoothness: X and Z are smooth and reduced; the H^5 divisor for H=A^2 must have isolated ODPs and every retained incidence-smoothness clause
projectivity: X, the chosen A and H embeddings, the pairwise triple-defect locus, nodal system, and detector data are projective
dimension: dim X=2n; c=binom(2n+2,2); m=5; N=2c+2; Z is an N-vertex clique in the two-triple A^4 defect correspondence
codimension: choose an exceptional primitive polarization and realize the self-associated osculating configuration on one complete pairwise defect clique
coefficient_field: C for polarization, jets, self-association, profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to triple neighborhoods and Z, 2Z, 3Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-five relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B228, G013, G090-G148, NG106-NG186, S082
claim: For every arbitrary primitive target (X,zeta), choose a very ample A for which zeta is the retained primitive target and construct H=A^2 plus a reduced Z of 2binom(2n+2,2)+2 points forming a complete clique in the A^4 two-triple defect locus, whose H^2 columns are self-associated and whose second-osculator, degree-five ODP, Kuranishi, rational-type, and specified-pairing clauses are exactly those of G151.
falsifier: one primitive target for which no choice of very ample A admits a sufficiently large two-triple defect clique carrying all self-associated, osculator, ODP, rationality, Hodge-type, and pairing obligations
---

# G152 — Choose an exceptional polarization and a defect clique

B226 closes the formulation that fixes an arbitrary primitive
polarization \(A\): nontrivial powers have empty two-triple defect locus.
The corrected sufficient branch must choose \(A\) as part of the
construction.

For every primitive target \((X,\zeta)\), G152 asks for a very ample
\(A\), preserving the target primitive class, and

\[
Z\subset X,\qquad |Z|=2c_{2n}+2,
\]

such that every distinct pair belongs to
\(\mathfrak D_A^{(2,2)}\). On that same clique, the \(A^4=H^2\)
evaluation columns must be self-associated, every full second osculator
must be a hyperplane in their span, and all degree-five ODP, Kuranishi,
rational type-\((0,0)\), and specified-pairing clauses must hold.

This is not a high-positivity problem: B226 proves that raising a very
ample polarization power empties the required defect correspondence.

B228 tests every remaining polarization on the valid primitive input
\((Q^4,a-b)\). All powers \(O_Q(k)\), \(k\ge2\), have empty defect
locus. For \(O_Q(1)\), B227 forces every defect chord to be a line on
the quadric, so a complete clique lies in one isotropic \(\mathbf P^2\).
Its quartic point rank is at most 15, below the required 16. Thus G152
is **NO-GO** as universally quantified. G153 moves to second slack.
