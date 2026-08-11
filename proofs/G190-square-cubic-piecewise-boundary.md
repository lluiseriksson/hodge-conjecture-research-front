---
brick_id: G190
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; K(d)=6d+6 for d=14,16,18,20 and K(d)=7d+5 for even d>=22; h_Z(1)=K(d); delta_1=K(d)-d-1; slack s_4(d)=2(K(d)-d-1); N=2K(d)
codimension: construct the complete G144 package with delta_1=K(d)-d-1 and an isomorphic degree-one relation transport at B263's square-cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B272, G013, G090-G148, G172, NG106-NG228, S081-S084
claim: The proposed universal G144 package at the piecewise rank K(d) cannot exist: B271-B272 exclude both cubic and quartic equality on the valid even-quadric test inputs for every even d>=22.
falsifier: a valid G190 package on an even quadric of dimension at least 22, or failure of the B271 cubic or B272 quartic exclusion
---

# G190 — The square/cubic piecewise boundary

B263 reduces the next balanced signature to

\[
 h_Z(1)=K(d),\quad
 \delta_1=K(d)-d-1,\quad
 s_4(d)=2(K(d)-d-1),\quad N=2K(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & K(d) & s_4(d) & \text{polarizations not yet excluded}\\ \hline
 14,16,18,20 & 6d+6 & 10d+10 & A=O_Q(2)\\
 22 & 159 & 272 & A=O_Q(4)\\
 d\ge24\text{ even} & 7d+5 & 12d+8 & A=O_Q(4).
\end{array} \tag{2}
\]

G190 is the next falsifiable gate: classify equality in the square
low-dimensional cases and the quartic high-dimensional cases, then retain every G144
relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing
clause. Rank survival alone would not construct an algebraic cycle or
prove or disprove HC.

NG222 shows that a single good variable edge cannot improve B261 in
the totally orthogonal locus. The narrowest re-entry is to prove that
the sum of at least two variable-edge images supplies the missing jet,
or to exclude that locus by a stronger geometric argument.

B264 proves the two-edge image-sum theorem outside one explicit
residual locus. Thus cubic/quartic equality can survive only when the
six independent-double supports lie in a projective plane through the
seventh point. Classifying or excluding that planar locus is now the
narrowest branch of G190.

B265 formerly claimed to exclude the planar locus, but B267 retracts
that argument. Restoring the removed variable factor cancels the
complementary-unit jet difference, and every planar edge image is the
same rank-\((d-1)\) space. B266 independently removes the standard tie
at \(d=22\), so the active high-dimensional branch is now exactly
cubic/quartic equality on the B264 planar locus. G190 remains
EXPLORATORY at the B267 checkpoint; no detector, pairing, cycle, proof,
or disproof of HC is produced there.

B268 shows that the remaining cubic rank is not merely an artifact of
the pair-line products. On an explicit split \(3+3\) planar
configuration, the six doubles are independent and the full sextic
system contributes exactly \(d-1\) further jets, giving rank
\(7d+5\). NG225 therefore closes further sextic interpolation as an
exclusion route. The smallest live obligation is to test or construct
the missing G144 relation transport, ODP, Kuranishi, rational-type, and
specified-pairing clauses on this exact rank witness.

B269 proves that this exact witness cannot be promoted directly. Every
eighth distinct double neighborhood contributes a new sextic
restriction coordinate, whereas a G190 equality candidate requires
\(N=2(7d+5)\) marked supports with all tangent osculators absorbed by
the same rank-\((7d+5)\) span. NG226 closes only that promotion route.
The next smallest gate is to classify all planar cubic equality
first-jet base schemes, or to audit the quartic equality branch; the
full detector package remains open.

B270-B271 now classify every cubic equality configuration. Rank-one
plane sextic jets collapse the anticanonical differential; the
six-point weak-del-Pezzo root and fundamental-cycle classification
forces complementary collinear triples through \(u\). Generalized B269
then separates every eighth double, contradicting the required
\(N=2(7d+5)\) marked supports. NG227 excludes \(A=O_Q(3)\) for every
even \(d\ge22\). Immediately before B272, the survivors were square
equality in dimensions \(14,16,18,20\) and quartic equality for every
even \(d\ge22\); no relation, ODP, Kuranishi, rational-type, or
specified-pairing clause had been constructed.

B272 excludes the remaining quartic equality by producing residual
rank at least \(d\), hence total rank at least \(7d+6\). Thus the
quadric test input falsifies G190 for every even \(d\ge22\), and G190
is NO-GO. This is a special-input obstruction to the proposed universal
boundary, not a proof or disproof of HC.
