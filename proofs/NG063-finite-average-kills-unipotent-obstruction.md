---
brick_id: NG063
status: NO-GO
base_field: C with rational coefficients
variety: an A2 root-covered semistable collision family
smoothness: generic fibers smooth; semistable source regular
projectivity: proper/projective
dimension: ambient 2n, hyperplane fibers 2n-1, and collision parameter 1
codimension: middle codimension n; special fiber parameter codimension one
coefficient_field: Q
cohomology_theory: finite-group trace, unipotent nearby cycles, monodromy logarithm, and B022 kernels
hodge_type: rational type-(0,0) pairing downstream; averaging alone does not prove it for a special lift
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B076, B085-B087, G050
claim: Reynolds averaging over the finite S3 root-cover group also kills every unipotent collision-monodromy obstruction in the semistable nearby-cycle local system.
falsifier: a nontrivial nilpotent residue N commuting with the finite action and a nonzero class [Nt] in coker(N_J)
---

# NG063 — Finite averaging does not kill unipotent monodromy

**Status:** NO-GO

B086 makes a lift invariant under the finite deck group. After the finite
base change, semistable nearby cycles can still carry unipotent monodromy
$M=\exp N$. The finite Reynolds projector commutes with this action but does
not force $N$ to vanish.

For example, let the finite group act trivially on
$A=\mathbf Qe_0\oplus\mathbf Qe_1$, let $J=\mathbf Qe_1$, and set
$Ne_0=e_1$, $Ne_1=0$. Finite averaging changes nothing, while the quotient
class of $e_0$ has nonzero obstruction in
$\operatorname{coker}N_J=J$ and no invariant lift.

The re-entry condition is G051: compute the actual nilpotent residue on the
combined B022 kernel and the B057 lift.
