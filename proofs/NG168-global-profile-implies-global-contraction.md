---
brick_id: NG168
status: NO-GO
base_field: C
variety: a smooth projective complex variety with a finite smooth node scheme, a globally liftable lower quadratic profile, and final-degree inverse-Hessian transported tangent directions
smoothness: X and Z are smooth and the central Hessians are nondegenerate; no global vector-field lift of the transported directions is assumed
projectivity: X, H^k, H^m, profile spaces, and value spaces are projective; the contraction directions are only nodewise data
dimension: arbitrary dim X=d; the obstruction is already visible in a two-node one-coefficient linear model
codimension: global liftability of a quadratic profile does not formally put its contraction in E_k or in the colon A_(m,k)
coefficient_field: C for profiles and contractions; the exact countermodel is defined over Q
cohomology_theory: coherent second jets, finite point evaluation, and graded multiplication
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B204-B206 and G134-G136
claim: Infer delta_(m,k)=0 merely because w in W_k is the quadratic profile of a global section double on Z.
falsifier: contraction by the final nodewise transported directions is not a global section-valued differential operator and can yield a vector outside A_(m,k)
---

# NG168 — A global profile need not have a global contraction

- **Route:** take (w\in W_k), use its global double-section lift, and
  conclude that (C_{m,k}(w)\) belongs to
  (E_k\otimes\operatorname{Sym}^2U^*\), hence to the colon.
- **Valid input:** the full quadratic tensor (w\) is the second jet of a
  global section.
- **Invalid inference:** evaluating that tensor on the nodewise vectors
  (H_i^{-1}d_i b\) is the value of another global section of (H^k).

The transported vectors depend on the final degree-(m) central Hessians
and on the selected jet generators. They are not supplied by global vector
fields or by a global differential operator preserving (H^k). Thus the
contraction can escape both (E_k) and (A_{m,k}).

An exact two-node linear model isolates the missing implication. Take

\[
 \mathcal T_k=\mathcal T_m=\mathbf Q^2,\qquad
 E_{m-k}=E_k=S_m=\mathbf Q(1,1).
\]

Coordinatewise multiplication gives
(A_{m,k}=(S_m:E_{m-k})=\mathbf Q(1,1)\). The stated linear consequences
allow a profile contraction ((1,2)u^2\), whose class modulo (A_{m,k}) is
nonzero. This is not claimed as a projective counterexample; it proves that
global profile liftability alone does not formally supply the missing
symbol-lifting theorem.

- **Precise obstruction:** no global section-valued symbol realizes the
  inverse-Hessian nodewise contraction.
- **Re-entry condition:** construct such a compatible global operator, or
  prove the weaker colon containment in G136 by a different geometric
  mechanism.
