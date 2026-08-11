---
brick_id: G136
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G134's class-directed primitive profile package
smoothness: X and Z are smooth and the central section has isolated ODPs; reduced smoothness of the full node incidence remains downstream
projectivity: X, all powers through H^m, value-colon spaces, quadratic profiles, the full tangent system, and detector family are projective
dimension: dim X=2n; U has dimension 2n; one finite-dimensional quotient obstruction delta_(m,k) occurs for each 0<=k<m
codimension: kill every colon-quotient contraction delta_(m,k) while retaining the primitive birth and all detector clauses
coefficient_field: C for sections, profiles, colon spaces, and cubic tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent quadratic profiles, finite point evaluation, graded multiplication, cubic Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B206, G013, G090-G135, NG106-NG168, and S065-S073
claim: Construct G134 for arbitrary (X,zeta) and prove delta_(m,k)=0 in (T_k/A_(m,k)) tensor Sym^2 U^* for every 0<=k<m, while retaining the ODP lift, adjacent ranks, full tangent system, rational detector, and specified nonzero pairing.
falsifier: a nonzero colon-quotient contraction in any lower degree, failure of G134, restriction to a tangent slice, or loss of any detector clause
---

# G136 — Kill the finite colon-contraction obstructions

For every (0\le k<m), retain B206's exact map

\[
 \delta_{m,k}:W_k\longrightarrow
 (\mathcal T_k/A_{m,k})\otimes\operatorname{Sym}^2U^*,
 \qquad A_{m,k}=(S_m:E_{m-k}).
\]

G136 asks for a class-directed full-system construction satisfying

\[
 \delta_{m,k}=0\qquad(0\le k<m). \tag{1}
\]

Under G134, B206 makes (1) equivalent to G135 and hence to vanishing of
the mixed cubic filter \(\Xi\). One possible stronger attack is to lift every
contracted profile to the lower value space \(E_k\), but the exact target is
the generally larger colon \(A_{m,k}\).

G136 retains every G134 and detector clause. It does not address the pure
cubic tensor \(\Theta\), any later Kuranishi rung, or the terminal cycle.

B207 dualizes (1) and identifies it with coherent absorption of every
relation-weighted Hessian functional through \(\partial_k^*\). G137 is that
preimage gate. NG169 blocks differentiating a zero-order value relation,
and NG170 records why standard Gaussian-map theorems do not supply the
required finite-node comparison.
