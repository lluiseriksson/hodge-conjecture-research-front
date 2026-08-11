---
brick_id: G118
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system incidence of an arbitrary smooth projective complex variety with a class-directed ordered ODP configuration and B185 algebraic basis carrier
smoothness: the projective variety, labelled critical incidences, and basis carrier are smooth at the marked configuration; all tracked singularities are ODPs
projectivity: every equation, localization, and numerator comes from the full projective universal family; no nonlinear special pullback may replace it
dimension: arbitrary projective and parameter dimensions; N nodes; value rank R; B185 presentation parameters M and E; certificate order D_car=E^(M+1)
codimension: prove the pulled-back escape conormal map vanishes through every coefficient of order at most D_car-1
coefficient_field: C for algebraic jets and conormal modules; Q for the specified rational Hodge class and detector
cohomology_theory: algebraic critical incidences, finite jets, Kahler differentials, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B185, G013, G088-G117, NG106-NG149, S015, S072
claim: For every proposed class-directed full-incidence ODP configuration, compute B185's finite presentation bound D_car and prove every coefficient of the conormal escape morphism through order D_car-1 vanishes, while retaining the uniform matroid, adjoint defect, primitive image, rational type, and specified nonzero pairing.
falsifier: a nonzero conormal coefficient within the audited order, an omitted presentation variable or localization, use of a nonlinear special base, failure of class direction, or loss of any detector clause
---

# G118 — Kill the finite full-incidence conormal jet

B185 constructs the labelled algebraic carrier and computes

\[
 D_{\mathrm{car}}=E^{M+1}
\]

from a finite presentation of the actual full incidence. B184 then proves
that the single finite obligation

\[
 j^{D_{\mathrm{car}}-1}\beta_{K_B}=0 \tag{1}
\]

implies \(\beta_{K_B}=0\), \(H_\tau=0\), and persistence of every tracked
node along the basis germ.

The only active case is \(\dim F_B=d-R\ge1\). B185 closes the
zero-dimensional case directly because all escape values vanish in the
local ring \(\mathbf C\).

G118 asks for a geometric proof of (1) for the class-directed
configuration, not a numerical evaluation on selected examples. The proof
must cover every coefficient in the audited finite jet, every nonbasis
escape numerator, and every arbitrary smooth projective complex variety.

The uniform-matroid, adjoint-defect, primitive-image, rational-type
\((0,0)\), and specified nonzero Saito-pairing clauses remain attached.
B185 supplies no vanishing mechanism for (1), and no such mechanism is
currently known.
