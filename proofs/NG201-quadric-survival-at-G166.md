---
brick_id: NG201
status: NO-GO
base_field: C
variety: the smooth even quadric Q^8 with primitive ruling difference a-b at the G166 balanced rank, together with the dimension ranges used to exclude each polarization
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: complete quadric embeddings, mixed double-point spans, residual first-jet systems, and tangent contact loci are projective
dimension: G166 has s=4d+12, N=6d+14, and h_Z(1)=3d+7; on Q^8 every A=O_Q(k) is excluded
codimension: the ruling difference supplies a legitimate primitive codimension-four universal input
coefficient_field: Q for the Hodge input and C for sections, tangent jets, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed finite schemes
hodge_type: a-b is primitive rational type (4,4); no unknown class is assumed algebraic
cycle_class_map: CH^4(Q^8)_Q -> H^8(Q^8,Q(4)); the known ruling difference only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B243, G166
claim: Survive G166's necessary quadric test through some very ample polarization A=O_Q(k).
falsifier: B243 excludes k>=4 by four-double interpolation, k=3 by sextic four-double separation, k=2 by residual jet rank at least two, and k=1 by the standard d=8 quotient inequalities
---

# NG201 — No quadric polarization survives G166

- **Route:** use some \(O_Q(k)\) to realize the G166 rank on every valid
  quadric input.
- **Valid premise:** G166 leaves one more point-span dimension than G164.
- **Invalid inference:** one extra dimension absorbs the next full tangent
  osculator.
- **Powered obstruction:** four doubles are independent for \(k\ge4\);
  for \(k=3\), a point outside the three-line triangle supplies all
  residual first jets in dimensions at least six.
- **Square obstruction:** after B242's six-support span, the residual
  linear system has first-jet rank at least \(d-2\ge2\).
- **Standard obstruction:** in dimension at least eight, residual
  tangents exceed the \(d+5\) quotient or the five-dimensional
  post-third-tangent allowance.
- **Universal-quantifier guard:** \(Q^8\) is one valid input on which all
  polarizations fail. No claim about arbitrary varieties follows from
  special-family success; failure here only falsifies G166.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G166 and the layers \(4d+12,4d+13\) are closed. G148
  and HC remain open.
- **Re-entry condition:** move to G167 at
  \(s=4d+14,\delta_1=2d+7,N=6d+16,h_Z(1)=3d+8\).
