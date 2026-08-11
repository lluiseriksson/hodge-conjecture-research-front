---
brick_id: NG141
status: NO-GO
base_field: C
variety: a smooth analytic critical-value parameter germ with a connected ideal-preserving symmetry action; projectively this models fields imported from polarized automorphisms
smoothness: the parameter germ is smooth and the displayed simultaneous ideal is smooth; the failure is a spanning failure, not a singularity
projectivity: not needed for the linear obstruction; projective use requires a separately verified polarized action on the full system
dimension: countermodel dimension d=3, N=2, R=1, symmetry-orbit rank r_A=1, and residual quotient dimension 1
codimension: the ideal I_tau=(u) already has H_tau=0, but the selected positive-dimensional symmetry orbit covers only half of ker(d tau_0)
coefficient_field: C; Q appears only in downstream Hodge detectors
cohomology_theory: analytic group actions and ideal-preserving logarithmic derivations
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative
dependencies: B156, B176-B177, G109-G110
claim: The existence of a positive-dimensional group orbit preserving the labelled node ideal automatically supplies the full logarithmic frame required by G109.
falsifier: tau=(u,(1+v)u) on C^3 has ker(d tau_0)=span(partial_v,partial_w), while w-translation is a one-dimensional ideal-preserving symmetry orbit
---

# NG141 — A positive symmetry orbit need not span the kernel

On \(M=\mathbf C^3\) with coordinates \((u,v,w)\), take

\[
 \tau=(u,(1+v)u),\qquad I_\tau=(u).
\]

Then \(R=1\), \(H_\tau=0\), and

\[
 \ker d\tau_0
 =\mathbf C\partial_v\oplus\mathbf C\partial_w. \tag{1}
\]

Let \(A=(\mathbf C,+)\) act by translation in \(w\). This action fixes
both critical-value functions, hence preserves the labelled ideal. Its
fundamental field is \(\partial_w\), so

\[
 T_0(A\cdot0)=\mathbf C\partial_w
 \subsetneq\ker d\tau_0. \tag{2}
\]

The missing direction \(\partial_v\) is itself logarithmic because it
preserves \((u)\), but it is not supplied by the chosen symmetry action.
Thus a positive-dimensional orbit and exact discriminant invariance do not
imply the spanning statement.

## Re-entry condition

Compute the actual orbit rank \(r_A\), form B177's quotient \(Q_A\), and
construct at least \(d-R-r_A\) independent all-order ideal-preserving
directions outside the group orbit. On an arbitrary variety the orbit may
contribute nothing. Every Hodge detector clause remains separate.
