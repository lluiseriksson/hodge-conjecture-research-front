---
brick_id: B223
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with a G149 first-slack marked scheme Z and a full-support degree-m value relation lambda
smoothness: X and Z are smooth and reduced; central ODP and incidence smoothness are inherited from G149 and not constructed
projectivity: X, the complete H^2 and H^(m-2) systems, their evaluation configurations, and the marked scheme are projective
dimension: dim X=d; N=D_d(m)+1, m>=3, dim E_2=c_d+1, and dim E_(m-2)=L_d(m-2)
codimension: the two complementary evaluation codes are exact weighted orthogonal complements, equivalently weighted Gale dual configurations
coefficient_field: C for fibers, evaluation codes, lambda, and Gale duality; Q detector structure remains separate
cohomology_theory: coherent restriction to the reduced point scheme and finite-dimensional duality
hodge_type: none asserted; complex weighted Gale duality does not supply rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B213, B222, G149
claim: In every G149 candidate, the full-support relation lambda induces a nondegenerate diagonal pairing on the N coordinate fibers for which E_(m-2)=E_2^(perp_lambda). After trivialization, evaluation matrices A_2 and A_c satisfy A_2 D_lambda A_c^T=0 and rank(A_2)+rank(A_c)=N, so their column configurations are weighted Gale dual.
falsifier: a G149 candidate whose complementary evaluation code is a proper subspace of the lambda-orthogonal complement, a zero lambda coordinate, or ranks not summing to N
---

# B223 — First slack is exact weighted Gale duality

Put

\[
\mathcal T_k=\bigoplus_{i=1}^N H^k|_{p_i},\qquad
E_k=\operatorname{im}\bigl(H^0(X,H^k)\to\mathcal T_k\bigr).
\]

Let \(\lambda\in\mathcal R_m\) be G149's full-support relation. At each
point it is a nonzero functional on the one-dimensional fiber \(H^m|_{p_i}\).
It therefore defines a perfect coordinatewise pairing

\[
B_\lambda:\mathcal T_2\times\mathcal T_{m-2}\longrightarrow\mathbf C,
\qquad
B_\lambda(x,y)=\lambda(xy). \tag{1}
\]

Multiplication of global sections lands in \(E_m\), which \(\lambda\)
annihilates. Hence

\[
E_{m-2}\subset E_2^{\perp_\lambda}. \tag{2}
\]

B222 gives

\[
\dim E_2=c_d+1,\qquad
\dim E_{m-2}=L_d(m-2),\qquad
N=c_d+1+L_d(m-2). \tag{3}
\]

The pairing (1) is nondegenerate because every coordinate of \(\lambda\)
is nonzero. Thus the right side of (2) has dimension
\(N-\dim E_2=\dim E_{m-2}\), and

\[
E_{m-2}=E_2^{\perp_\lambda}. \tag{4}
\]

After trivializing all fibers, choose row-basis evaluation matrices
\(A_2,A_c\) and put \(D_\lambda=\operatorname{diag}(\lambda_i)\).
Equations (3)–(4) become

\[
A_2D_\lambda A_c^{\mathsf T}=0,\qquad
\operatorname{rank}A_2+\operatorname{rank}A_c=N. \tag{5}
\]

This is weighted Gale duality of their column configurations. It is an
exact reformulation of the two transport isomorphisms, not a construction
of either code. It carries complex weights only and supplies no rational
Hodge detector or cycle.
