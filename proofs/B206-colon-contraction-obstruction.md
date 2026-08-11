---
brick_id: B206
status: PROVED
base_field: C
variety: the full degree-m projective tangent system of a smooth projective complex d-fold with G134's node scheme Z, profile spaces W_k, jet space U, and value spaces E_k
smoothness: X and Z are smooth and the central section has nondegenerate Hessian at every node; incidence smoothness is not inferred
projectivity: X, powers of H, all value spaces, profile spaces, and nodewise multiplication maps are projective coherent data
dimension: dim X=d; dim U=d; the obstruction in degree k lies in (T_k/A_(m,k)) tensor Sym^2 U^*
codimension: G135 is equivalent to vanishing of one explicit colon-quotient contraction map for every 0<=k<m
coefficient_field: C for values, profiles, contractions, and obstruction quotients; Q remains required separately for the detector
cohomology_theory: coherent quadratic profiles, finite point evaluation, graded multiplication, and cubic Kuranishi tensors
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B200-B205 and G130-G135
claim: For T_k=direct_sum_i H^k|_(p_i), define A_(m,k)=(S_m:E_(m-k)) as the vectors y such that ey lies in S_m for every e in E_(m-k). Then E_k is contained in A_(m,k), and under G134 the mixed cubic filter vanishes exactly when every contraction map delta_(m,k):W_k -> (T_k/A_(m,k)) tensor Sym^2 U^* is zero for 0<=k<m.
falsifier: a global value vector outside A_(m,k), a lower-product containment in G135 with nonzero delta_(m,k), vanishing of every delta_(m,k) with nonzero mixed cubic filter under G134, or failure of E_k subset A_(m,k)
---

# B206 — The mixed obstruction is a colon-quotient contraction

Put

\[
 \mathcal T_k=\bigoplus_i H^k|_{p_i},\qquad
 E_k=\operatorname{im}\!\left[H^0(H^k)\to\mathcal T_k\right],
\]

so \(S_m=E_m\). For \(0\le k<m\), define the value-colon subspace

\[
 A_{m,k}=(S_m:E_{m-k})
 =\left\{y\in\mathcal T_k:
 ey\in S_m\text{ for every }e\in E_{m-k}\right\}. \tag{1}
\]

All products in (1) are coordinatewise products of line-bundle fibers.
If \(y\in E_k\), choose a global section representing it. Multiplying it
by a representative of any \(e\in E_{m-k}\) gives a global degree-\(m\)
section. Therefore

\[
 E_k\subset A_{m,k}. \tag{2}
\]

## Exact obstruction maps

B205 supplies the contraction

\[
 C_{m,k}:W_k\longrightarrow
 \mathcal T_k\otimes\operatorname{Sym}^2U^*.
\]

Define

\[
 \delta_{m,k}:W_k\longrightarrow
 (\mathcal T_k/A_{m,k})\otimes\operatorname{Sym}^2U^* \tag{3}
\]

by composing \(C_{m,k}\) with the quotient. Choosing a basis of
\(\operatorname{Sym}^2U^*\) shows that

\[
 \delta_{m,k}(w)=0
 \quad\Longleftrightarrow\quad
 eC_{m,k}(w)\in
 S_m\otimes\operatorname{Sym}^2U^*
 \text{ for every }e\in E_{m-k}. \tag{4}
\]

Consequently, under G134's spanning equality, B205 gives

\[
 \Xi=0
 \quad\Longleftrightarrow\quad
 \delta_{m,k}=0\text{ for every }0\le k<m. \tag{5}
\]

The stronger inclusion

\[
 C_{m,k}(W_k)\subset
 E_k\otimes\operatorname{Sym}^2U^* \tag{6}
\]

would imply (5) by (2), but (6) is not necessary: the colon \(A_{m,k}\)
can be strictly larger than \(E_k\). B206 constructs neither the vanishing
in (5), the pure cubic filter, a later Kuranishi rung, a detector, nor a
cycle.
