---
brick_id: G135
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G134's class-directed primitive profile package
smoothness: X and Z are smooth and F has isolated ODPs; reduced smoothness of the full node incidence remains downstream
projectivity: X, all powers through H^m, graded quadratic profiles, full value space, and detector family are projective
dimension: dim X=2n; U has dimension 2n; every lower profile contraction is a symmetric U-form valued at N nodes
codimension: require every lower-profile contraction multiplied into degree m to land in the degree-m value image S_m
coefficient_field: C for profiles, values, contractions, and cubic tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: graded coherent quadratic jets, ODP inverse-Hessian transport, cubic Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B205, G013, G090-G134, NG106-NG167, and S065-S073
claim: Construct G134 for arbitrary (X,zeta) and prove e C_(m,m-a)(w) lies in S_m tensor Sym^2 U^* for every a>=1, e in E_a, and lower profile w in W_(m-a), while retaining the primitive profile, ODP lift, adjacent ranks, and complete rational detector.
falsifier: one lower profile and value multiplier whose contracted degree-m node vector escapes S_m, failure of G134's primitive line or ODP package, use of a restricted tangent slice, or failure of any detector clause
---

# G135 — Close all lower-profile contractions

Assume G134, so

\[
 W_m=\mathbf Cq_F+\sum_{a=1}^mE_aW_{m-a}.
\]

B205 proves that G131's mixed cubic filter vanishes exactly when

\[
 e\,C_{m,m-a}(w)\in
 S_m\otimes\operatorname{Sym}^2U^* \tag{1}
\]

for every \(1\le a\le m\), \(e\in E_a\), and
\(w\in W_{m-a}\). G135 asks for a class-directed geometric mechanism
proving all containments (1) in the full complete linear system.

The primitive line \(\mathbf Cq_F\) contributes no mixed obstruction by
B200. Nevertheless, the entire decomposable profile submodule must satisfy
(1). Success kills \(\Xi\) only; G131's pure tensor \(\Theta\), all later
Kuranishi rungs, and the terminal cycle remain open.
