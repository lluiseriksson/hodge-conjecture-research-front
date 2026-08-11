---
brick_id: G182
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=8d+10=16n+10; N=10d+12=20n+12; h_Z(1)=5d+6=10n+6=N/2
codimension: construct the complete G144 package with delta_1=4d+5 and an isomorphic degree-one relation transport at B255's cubic-polarization boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B255, G013, G090-G148, G172, NG106-NG213, S081-S083
claim: For every arbitrary primitive target (X,zeta), choose A and construct the complete G144 package at m=2, slack s=8d+10, delta_1=4d+5, N=10d+12, and h_Z(1)=5d+6=N/2, retaining the full relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clauses.
falsifier: one primitive target for which no polarization realizes the boundary package; on even quadrics of dimension at least fourteen, B255 reduces the rank test at equality to A=O_Q(3)
---

# G182 — The sextic six-point boundary

B255 raises the common quadric floor to

\[
 m=2,\qquad s=8d+10,\qquad \delta_1=4d+5,\qquad
 N=10d+12,\qquad h_Z(1)=5d+6=N/2. \tag{1}
\]

On every even quadric of dimension at least fourteen, B253 excludes the
standard polarization at equality, B254 excludes the square polarization,
and B255 forces six full double blocks for every \(A=O_Q(k)\), \(k\ge4\).
Only the cubic polarization \(A=O_Q(3)\), with \(H=O_Q(6)\), survives the
rank audit.

G182 is the next falsifiable gate: classify whether a sextic tangent-
absorbing point span can have dimension exactly \(5d+6\), and if so whether
it can support every remaining G144 relation, ODP, Kuranishi, rational-type,
and nonzero specified-pairing clause. Rank survival alone would not construct
an algebraic cycle or prove or disprove HC.
