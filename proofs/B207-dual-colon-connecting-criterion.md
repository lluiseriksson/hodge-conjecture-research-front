---
brick_id: B207
status: PROVED
base_field: C
variety: the full degree-m projective tangent system of a smooth projective complex d-fold with finite smooth node scheme Z, G134's profile spaces, and G136's value-colon spaces
smoothness: X and Z are smooth and the central Hessians are nondegenerate; no smoothness of the simultaneous-node incidence is inferred
projectivity: X, powers of H, ideal powers I_Z^2 and I_Z^3, point-evaluation spaces, and all connecting maps are projective coherent data
dimension: dim X=d; each degree k obstruction is dual to relation-weighted functionals on the finite quadratic-profile fiber space Q_k
codimension: every colon-contraction obstruction vanishes exactly when all relation-weighted Hessian functionals lie in the image of one dual connecting map
coefficient_field: C for profiles, relations, duality, and connecting maps; Q remains required separately for the detector
cohomology_theory: coherent sheaf cohomology, second conormal jets, finite-dimensional duality, and cubic Kuranishi tensors
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B200-B206 and G130-G136
claim: Let R_m=S_m^perp. Then A_(m,k)^perp is spanned by the contractions e star r with e in E_(m-k) and r in R_m. If ell_(r,e,b,c) evaluates a full quadratic profile on the final inverse-Hessian directions and pairs the resulting node vector with e star r, then delta_(m,k)=0 exactly when every ell_(r,e,b,c) belongs to the image of partial_k^*:H1(I_Z^3 H^k)^* -> H0((I_Z^2/I_Z^3)H^k)^*.
falsifier: a functional in A_(m,k)^perp not spanned by e star r, an ell annihilating W_k but outside im(partial_k^*), an ell in im(partial_k^*) nonzero on W_k, or vanishing of all displayed ell classes with nonzero delta_(m,k)
---

# B207 — Dual colon classes are connecting-map functionals

Retain

\[
 \mathcal T_j=\bigoplus_iH^j|_{p_i},\qquad
 R_m=S_m^\perp\subset\mathcal T_m^*.
\]

For \(e\in E_{m-k}\) and \(r\in R_m\), define intrinsically

\[
 e\star r\in\mathcal T_k^*,\qquad
 \langle e\star r,y\rangle=\langle r,ey\rangle. \tag{1}
\]

B206's colon is the kernel of

\[
 \mathcal T_k\longrightarrow
 \operatorname{Hom}(E_{m-k},\mathcal T_m/S_m),
 \qquad y\longmapsto(e\mapsto ey\bmod S_m).
\]

Dualizing this finite-dimensional map gives

\[
 A_{m,k}^\perp
 =\operatorname{span}\{e\star r:
 e\in E_{m-k},\ r\in R_m\}. \tag{2}
\]

## Coherent absorption

Set

\[
 \mathcal Q_k=H^0\!\left((I_Z^2/I_Z^3)H^k\right).
\]

The full nodewise contraction extends from \(W_k\) to a linear map

\[
 \widetilde C_{m,k}:\mathcal Q_k\longrightarrow
 \mathcal T_k\otimes\operatorname{Sym}^2U^*. \tag{3}
\]

For \(b,c\in U\), define

\[
 \ell_{r,e,b,c}(q)=
 \left\langle r,
 e\,\widetilde C_{m,k}(q)(b,c)\right\rangle
 \in\mathbf C. \tag{4}
\]

By (2), the colon obstruction \(\delta_{m,k}\) vanishes exactly when every
functional (4) annihilates \(W_k\).

The coherent exact sequence

\[
 0\to I_Z^3H^k\to I_Z^2H^k\to
 (I_Z^2/I_Z^3)H^k\to0
\]

has connecting map

\[
 \partial_k:\mathcal Q_k\longrightarrow H^1(I_Z^3H^k),
 \qquad W_k=\ker\partial_k. \tag{5}
\]

Finite-dimensional duality gives

\[
 W_k^\perp=\operatorname{im}\partial_k^*. \tag{6}
\]

Combining (4)--(6),

\[
 \delta_{m,k}=0
 \quad\Longleftrightarrow\quad
 \ell_{r,e,b,c}\in\operatorname{im}\partial_k^*
 \quad\text{for every }r,e,b,c. \tag{7}
\]

B207 is an exact dual/coherent certificate. It supplies no preimages in
(7), no pure cubic vanishing, no later Kuranishi closure, no detector, and
no cycle.
