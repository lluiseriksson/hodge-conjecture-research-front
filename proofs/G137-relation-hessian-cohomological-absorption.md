---
brick_id: G137
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G134's full class-directed profile package
smoothness: X and Z are smooth and the central section has isolated ODPs; reduced smoothness of the full node incidence remains downstream
projectivity: X, powers through H^m, ideal powers, value relations, full profile spaces, tangent system, and detector family are projective
dimension: dim X=2n; U has dimension 2n; the functionals range over every lower k, value relation, multiplier, and symmetric pair of U-directions
codimension: lift every relation-weighted Hessian functional through the dual third-neighborhood connecting map
coefficient_field: C for coherent duality and cubic tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent sheaf cohomology, second conormal jets, cubic Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B207, G013, G090-G136, NG106-NG170, S065-S074
claim: Construct G134 for arbitrary (X,zeta) and, for every 0<=k<m, r in S_m^perp, e in E_(m-k), and b,c in U, construct eta_(r,e,b,c) in H1(I_Z^3 H^k)^* satisfying partial_k^*(eta)=ell_(r,e,b,c), while retaining the full tangent system, ODPs, adjacent ranks, rational detector, and nonzero specified pairing.
falsifier: one relation-weighted Hessian functional outside im(partial_k^*), use of only a restricted tangent slice or special variety, failure of G134, or loss of any detector clause
---

# G137 — Absorb every relation-weighted Hessian functional

B207 reduces G136 to explicit coherent preimages. For all

\[
 0\le k<m,\quad r\in R_m=S_m^\perp,\quad
 e\in E_{m-k},\quad b,c\in U,
\]

construct

\[
 \eta_{r,e,b,c}\in H^1(I_Z^3H^k)^*
\]

such that

\[
 \partial_k^*(\eta_{r,e,b,c})
 =\ell_{r,e,b,c}. \tag{1}
\]

Equation (1) is falsifiable by evaluating the right side on any element of
\(W_k=\ker\partial_k\). It must hold for the full projective tangent system,
not after selecting directions that kill the functional.

Success proves every \(\delta_{m,k}=0\), hence G136/G135 and the mixed cubic
filter. It does not prove G134, the pure cubic filter, higher rungs, or the
terminal cycle.

B208/G138 give a stronger alternative: make every lower profile space zero
and let the central line be the first quadratic-profile birth. NG171 records
that G125's first-jet extinction does not imply this second-layer vanishing.
