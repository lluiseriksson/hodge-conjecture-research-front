---
brick_id: G172
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta, a to-be-chosen very ample A, H=A^2, and an excess j=j(X,zeta)
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=6d+6+2j; N=8d+8+2j; h_Z(1)=4d+4+j=N/2; the excess must be unbounded along the even-quadric inputs as d tends to infinity
codimension: construct the complete G144 package beyond B248's fixed-additive obstruction, with delta_1=3d+3+j and an isomorphic degree-one relation transport
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B249, G013, G090-G148, NG106-NG207, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and an integer j>=0, then construct H=A^2 and a reduced Z with the complete G144 package at slack s=6d+6+2j, rank h_Z(1)=4d+4+j=N/2, an isomorphic full-support relation transport, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing; on the quadric test family the chosen excess must satisfy B248's dichotomy and hence grow without bound with d.
falsifier: one primitive target for which no choice of A and excess j realizes the complete package, or a proposed bounded-excess construction contradicted by B248 on even quadrics
---

# G172 — Allow dimension-growing degree-two excess

B248 closes every balanced \(m=2\) branch whose additive excess is
bounded independently of dimension. The surviving degree-two signature
must therefore have

\[
 s=6d+6+2j,\qquad
 \delta_1=3d+3+j,\qquad
 N=8d+8+2j,\qquad
 h_Z(1)=4d+4+j=N/2, \tag{1}
\]

where \(j=j(X,\zeta)\) cannot remain bounded on the quadric inputs.

More precisely, a quadric candidate must satisfy

\[
 j\ge d-7
 \quad\text{or}\quad
 4d+4+j\le\binom{2j+10}{j+3}. \tag{2}
\]

B249 sharpens this window from unbounded to linear growth. On every
even quadric, the square polarization requires \(j\ge d-1\), every
\(k\ge3\) requires \(j\ge d+1\), and the standard polarization requires
\(j\ge d-7\). Thus the smallest surviving subgate is G173 at
\(j=d-7\), equivalently \(s=8d-8\), with only the standard quadric
polarization left.

G172 remains an exploratory parent. These necessary ranks supply no
point scheme, ODP package, Kuranishi closure, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
