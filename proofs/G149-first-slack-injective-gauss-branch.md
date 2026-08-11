---
brick_id: G149
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a specified nonzero rational middle Hodge class zeta primitive for a very ample A, and the squared polarization H=A^2
smoothness: X and the marked reduced scheme Z are smooth; the central degree-m divisor must have exactly the prescribed ODPs and every G144 incidence-smoothness clause
projectivity: X, the complete A^2 embedding, all H^k systems, the nodal family, and detector data are projective
dimension: dim X=2n; m>=5 and N=D_(2n)(m)+1; B222 excludes m=2,3,4
codimension: construct the full G144 package with the forced first-slack signature h_Z(2)=c_(2n)+1 and h_Z(m-2)=L_(2n)(m-2)
coefficient_field: C for polarization, sections, ranks, profiles, holonomy, Kuranishi tensors, and transports; Q for zeta and the detector
cohomology_theory: coherent restrictions through 3Z, principal parts through order two, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the detector must be rational type (0,0) and pair nontrivially with the specified rational type-(n,n) class zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B222, B226, G013, G090-G144, G148, NG106-NG183
claim: For every arbitrary primitive input (X,A,zeta), construct the complete G144 package for H=A^2 at some m>=5 with N=D_(2n)(m)+1; equivalently by B220 and B222, realize h_Z(2)=c_(2n)+1, h_Z(m-2)=L_(2n)(m-2), both complementary transport isomorphisms, and every central-profile, holonomy, finite-Kuranishi, rational-detector, and specified-pairing clause.
falsifier: one legitimate primitive input (X,A,zeta) for which H=A^2 and no degree m>=5 first-slack marked configuration realizes all displayed geometric, rank, rationality, Hodge-type, and pairing clauses
---

# G149 — The first-slack injective-Gauss branch

Start with a primitive input \((X,A,\zeta)\), where \(A\) is very ample.
The class remains primitive for \(H=A^2\), because its Lefschetz
operator is a nonzero scalar multiple of that for \(A\). B220 makes the
ordinary H-Gauss map injective. G149 asks for
the complete G144 package at the smallest strict node count

\[
 m\ge5,\qquad N=D_{2n}(m)+1. \tag{1}
\]

B222 excludes \(m=2,3,4\) at one-node slack under injective Gauss.
For \(m\ge5\), it forces, rather than merely requests,

\[
 h_Z(2)=c_{2n}+1,\qquad
 h_Z(m-2)=L_{2n}(m-2), \tag{2}
\]

and both complementary relation transports are isomorphisms. Thus the
equality obstruction is escaped by exactly one new degree-two point-span
direction; no special Gauss fiber is present.

The attempted proof supplies the polarization and all rank consequences,
but stops at existence: neither B220 nor B222 constructs a reduced
marked scheme with (2), the adjacent ODP profile, finite Kuranishi
closure, rational type-\((0,0)\) relation, or nonzero pairing with the
specified \(\zeta\). Those simultaneous construction obligations are
the falsifiable content of G149.

B226/NG186 now falsify the fixed-A universal quantifier: if \(A=B^2\),
then \(A^4\) separates every pair of triple neighborhoods, while every
candidate would require failure for every pair. G149 is therefore
**NO-GO** as stated. G152 tested an existential choice of exceptional
primitive polarization; B228 subsequently closed that repair as well.
