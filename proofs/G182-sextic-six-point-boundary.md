---
brick_id: G182
status: NO-GO
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
dependencies: B007-B010, B134-B256, G013, G090-G148, G172, NG106-NG214, S081-S083
claim: No universal G144 package exists at m=2, slack s=8d+10, delta_1=4d+5, N=10d+12, and h_Z(1)=5d+6=N/2; B256 excludes the last cubic branch on every even quadric Q^d with d>=14.
falsifier: one complete G182 package on every valid primitive input, in particular a cubic candidate below six double blocks on one even quadric Q^d with d>=14
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

B256 closes the cubic branch. The points producing a three-element
line-through-point class lie on at most two triple lines, whose sextic
point rank together with \(P_5\) is at most fourteen. A marked point
outside this hard locus has a good-edge five-cycle. The product of its
five pair-line hyperplanes, multiplied by the complete \(O_Q(1)\)
system, supplies the full sixth double neighborhood. Hence every
nonstandard polarization has \(h_Z(1)\ge6d+6\), and every polarization
has

\[
 h_Z(1)\ge6d-7,\qquad s\ge10d-16. \tag{2}
\]

Thus G182 and every layer through \(s=10d-17\) are NO-GO. The next gate
is G183 at \(s=10d-16\), where only \(A=O_Q(1)\) survives the quadric
rank audit. No ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC is produced.
