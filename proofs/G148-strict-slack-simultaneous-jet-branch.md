---
brick_id: G148
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a specified nonzero primitive rational middle Hodge class zeta and a very ample polarization H
smoothness: X and the marked reduced point scheme Z are smooth; the central divisor must have exactly the prescribed ODPs and every retained incidence-smoothness clause of G144
projectivity: X, the complete H^m systems, the marked nodal construction, and all spread or degeneration data are projective
dimension: dim X=2n; choose m and a finite marked scheme of cardinality N strictly greater than D_(2n)(m)
codimension: the terminal target is codimension n; the operational obligation is the full G144 nodal, rank, profile, holonomy, Kuranishi, rational-detector, and specified-pairing package without equality saturation
coefficient_field: C for section, jet, profile, incidence, and transport data; Q for zeta, vanishing-cycle relations, detector, and cycle-class target
cohomology_theory: coherent restrictions to Z, 2Z, and 3Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito local pairing
hodge_type: the detector must be rational type (0,0) and pair nontrivially with the specified rational type-(n,n) class zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B221, G013, G090-G144, NG106-NG182
claim: For every arbitrary (X,zeta), construct some m and N>D_(2n)(m) marked ODPs satisfying the complete G144 simultaneous mixed-jet ranks, central quadratic profile, holonomy, finite Kuranishi closure, rational type-(0,0) detector, and nonzero specified pairing.
falsifier: one legitimate pair (X,zeta) for which every strict-slack candidate fails a required rank, ODP, profile, transport, rationality, Hodge-type, or specified-pairing clause
---

# G148 — Return to the strict-slack simultaneous-jet branch

B221 falsifies the universal equality specialization
\(N=D_{2n}(m)\). It does not alter G144's necessary lower bound. The
narrowest surviving branch is therefore

\[
 N>D_{2n}(m). \tag{1}
\]

For every arbitrary input \((X,\zeta)\), G148 asks for one degree \(m\),
one reduced marked set \(Z\) of \(N\) points, and the complete G144
package:

1. all simultaneous restriction ranks \(L_{2n}(k)\) and relation
   transports required by B213-B215;
2. the adjacent first- and second-profile birth, central nondegenerate
   ODP generator, conformal holonomy, pure and mixed cubic closure, and
   the remaining finite Kuranishi ladder;
3. a rational type-\((0,0)\) full-support vanishing-cycle relation whose
   Saito pairing with the specified \(\zeta\) is nonzero.

No common tangent plane or special Gauss fiber is required in the
strict-slack range: those were consequences of saturating every
inequality at equality. A dimension count, a special-family example, or
a detector constructed after assuming \(\zeta\) algebraic does not close
G148.
