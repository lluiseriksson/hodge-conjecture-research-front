---
brick_id: G186
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; F(d)=min(7d-12,6d+6); slack s_*(d)=2(F(d)-d-1)=min(12d-26,10d+10); N=2F(d); h_Z(1)=F(d)=N/2
codimension: construct the complete G144 package with delta_1=F(d)-d-1 and an isomorphic degree-one relation transport at B259's piecewise post-band boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B260, G013, G090-G148, G172, NG106-NG218, S081-S083
claim: No universal G144 package exists at B259's piecewise boundary F(d); B260 excludes the required equality on every even quadric Q^d with d>=22 and reduces all remaining dimension/polarization regimes.
falsifier: one complete G186 package on every valid primitive input, in particular an equality package in one of B260's excluded high-dimensional polarization regimes
---

# G186 — The piecewise post-standard-band boundary

B259 raises the standard quadric floor to \(7d-12\), while B254-B256
give the nonstandard floor \(6d+6\). Define

\[
 F(d)=\min\{7d-12,6d+6\}. \tag{1}
\]

The next balanced degree-two signature is

\[
 h_Z(1)=F(d),\qquad
 \delta_1=F(d)-d-1,\qquad
 s_*(d)=2(F(d)-d-1),\qquad
 N=2F(d). \tag{2}
\]

Equivalently,

\[
\begin{array}{c|c|c|c}
 d & h_Z(1) & s_*(d) & \text{polarizations not yet excluded}\\ \hline
 14,16 & 7d-12 & 12d-26 & A=O_Q(1)\\
 18 & 114 & 190 & A=O_Q(k),\ k\ge1\\
 d\ge20\text{ even} & 6d+6 & 10d+10 & A=O_Q(k),\ k\ge2
\end{array} \tag{3}
\]

B260 closes the unrestricted polarization table. Cubic and quartic
equality at \(6d+6\) fail by six- and eight-edge separators. Every
\(k\ge5\) supplies a seventh full double block. For the square
polarization in even dimension at least 22, the six supports span at
most a \(\mathbf P^5\), whose quartic point rank is only 126; the
forced span escape supplies a seventh full double block.

Thus G186 is NO-GO as a universal gate. The surviving regimes pass to
G187: standard \(d=14,16\); standard or square \(d=18\); square
\(d=20\); and cubic or quartic for even \(d\ge22\). No ODP package,
rational detector, specified pairing, algebraic cycle, proof, or
disproof of HC is produced.
