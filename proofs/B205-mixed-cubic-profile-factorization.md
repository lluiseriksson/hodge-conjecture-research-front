---
brick_id: B205
status: PROVED
base_field: C
variety: the full degree-m projective tangent system of a smooth projective complex d-fold with G130's ODP section F, node scheme Z, jet space U, and value image S
smoothness: X and Z are smooth and the Hessian of F is nondegenerate at every node; reduced incidence smoothness is not inferred
projectivity: X, powers of H, quadratic-profile spaces, the full projective tangent system, and all nodewise contractions are projective coherent data
dimension: dim X=d; dim U=d; the mixed cubic target is (T_m/S_m) tensor Sym^2 U^*
codimension: B201's mixed cubic filter factors through W_m and, under G134, is controlled exactly by contractions of lower profiles multiplied by lower value data
coefficient_field: C for sections, profiles, Hessian transports, and cubic tensors; Q remains required separately for the detector
cohomology_theory: coherent quadratic profiles, ODP inverse Hessians, graded multiplication, and cubic Kuranishi tensors
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B154, B191-B204, G124-G134
claim: B201's mixed map Xi factors through a linear contraction map Xihat_m:W_m->(T_m/S_m) tensor Sym^2 U^*, whose kernel contains the central profile line C q_F. If G134 gives W_m=C q_F+sum_(a=1)^m E_a W_(m-a), then Xi=0 exactly when for every e in E_a and w in W_(m-a), the nodewise product of e with the contraction of w by the two final inverse-Hessian transported U directions lies in S_m tensor Sym^2 U^*.
falsifier: dependence of the mixed tensor on a triple-vanishing representative, nonzero Xihat_m(q_F), vanishing on every lower product with nonzero Xi under the G134 spanning equality, or a lower-product contraction outside S_m with Xi zero
---

# B205 — The mixed cubic filter factors through graded profiles

Let \(L=H^m\), let

\[
 S_m=\operatorname{im}\!\left[
 H^0(X,L)\to\bigoplus_iL_{p_i}
 \right],
\]

and retain G130's \(d\)-dimensional jet space \(U\). For \(b\in U\), put

\[
 v_{b,i}=H_i^{-1}(d_ib)\in T_{p_i}X, \tag{1}
\]

where \(H_i=\operatorname{Hess}_{p_i}(F)\).

## Factorization through the quadratic profile

For a profile

\[
 w=(w_i)\in W_m\subset
 \bigoplus_i\operatorname{Sym}^2T_{p_i}^*X\otimes L_{p_i},
\]

define

\[
 \widehat\Xi_m(w)(b,c)=
 \left[
 \bigl(w_i(v_{b,i},v_{c,i})\bigr)_i
 \right]\in\mathcal T_m/S_m. \tag{2}
\]

If \(a\in H^0(I_Z^2L)\) represents \(w\), equation (2) is exactly B201's
mixed tensor \(\Xi([a])(b,c)\). Changing \(a\) by an element of
\(H^0(I_Z^3L)\) does not change its Hessian, so the factorization is
well-defined.

Let \(q_F=\rho(F)\). Then

\[
 \widehat\Xi_m(q_F)(b,c)=
 \left[
 \bigl(H_i(v_{b,i},v_{c,i})\bigr)_i
 \right]
 =
 \left[
 \bigl(B_i(d_ib,d_ic)\bigr)_i
 \right]. \tag{3}
\]

B200 identifies the last vector with
\(\lambda B_V(b,c)\), and \(\lambda\in S_m\). Hence

\[
 \mathbf Cq_F\subset\ker\widehat\Xi_m. \tag{4}
\]

## Lower-product contractions

For \(w\in W_k\), define its contraction by the **final degree-\(m\)**
transported directions:

\[
 C_{m,k}(w)(b,c)=
 \bigl(w_i(v_{b,i},v_{c,i})\bigr)_i
 \in\bigoplus_iH^k|_{p_i}. \tag{5}
\]

If \(e\in E_a\) and \(a+k=m\), the product profile satisfies

\[
 \widehat\Xi_m(ew)(b,c)=
 \left[e\,C_{m,k}(w)(b,c)\right]\in\mathcal T_m/S_m. \tag{6}
\]

Assume G134's spanning equality

\[
 W_m=\mathbf Cq_F+
 \sum_{a=1}^mE_aW_{m-a}. \tag{7}
\]

Combining (4), (6), and (7) gives the exact criterion

\[
 \Xi=0
 \quad\Longleftrightarrow\quad
 e\,C_{m,m-a}(w)\in
 S_m\otimes\operatorname{Sym}^2U^*
\quad
 \text{for every }a,e,w. \tag{8}
\]

B205 does not prove any containment in (8), the pure cubic filter, later
Kuranishi vanishing, a detector, or a cycle.
