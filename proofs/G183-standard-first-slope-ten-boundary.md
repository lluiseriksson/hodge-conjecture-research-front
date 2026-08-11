---
brick_id: G183
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=10d-16=20n-16; N=12d-14=24n-14; h_Z(1)=6d-7=12n-7=N/2
codimension: construct the complete G144 package with delta_1=5d-8 and an isomorphic degree-one relation transport at B256's standard-polarization boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B257, G013, G090-G148, G172, NG106-NG215, S081-S083
claim: No universal G144 package exists at m=2, slack s=10d-16, delta_1=5d-8, N=12d-14, and h_Z(1)=6d-7=N/2; B257 excludes the last standard equality branch on every even quadric Q^d with d>=14.
falsifier: one complete G183 package on every valid primitive input, in particular a standard equality candidate on one even quadric Q^d with d>=14
---

# G183 — The first standard slope-ten boundary

B256 raises the common quadric floor to

\[
 m=2,\qquad s=10d-16,\qquad \delta_1=5d-8,\qquad
 N=12d-14,\qquad h_Z(1)=6d-7=N/2. \tag{1}
\]

On every even quadric of dimension at least fourteen, B254-B256 force
\(h_Z(1)\ge6d+6\) for every nonstandard polarization. Only the
standard polarization \(A=O_Q(1)\), with \(H=O_Q(2)\), survives the
rank audit.

B257 closes the equality. Every B253 branch remains strictly excluded
except its final \(d-4\)-budget case. There, exact contraction forces the
last point \(x\) into \(J\), and
\(\operatorname{Sym}^2(J\cap x^\perp)\) remains in the annihilator after
the span fills. Its contact locus is a projective five-space of quadratic
point rank at most twenty-one, contradicting \(h_Z(1)=6d-7\). Hence

\[
 h_Z(1)\ge6d-6,\qquad s\ge10d-14. \tag{2}
\]

Thus G183 and its adjacent odd layer are NO-GO. The next gate is G184 at
\(s=10d-14\), again with only \(A=O_Q(1)\) surviving the quadric rank
audit. No ODP package, rational detector, specified pairing, algebraic
cycle, proof, or disproof of HC is produced.
