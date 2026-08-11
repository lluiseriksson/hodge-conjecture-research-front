---
brick_id: B159
status: PROVED
base_field: C
variety: local analytic ordered-node critical-value germs of arbitrary rank R<N, projectively realizable on nonlinear analytic bases through B157
smoothness: every labeled discriminant branch is smooth and every intersection of at most R branches is transverse; the full simultaneous-node scheme in the escaping family is nonreduced
projectivity: B157 realizes the germs in projective hypersurface families, but generally only after nonlinear analytic pullback from the complete linear system
dimension: R+1 base coordinates x_1 through x_R and y; N branches; differential rank R
codimension: basis intersections have codimension R, while the escaping full ideal is (x_1,...,x_R,y^m) and has hidden-generator dimension one
coefficient_field: C for analytic germs and Q for the fixed local A1 Milnor lattices
cohomology_theory: Vandermonde representable matroids, analytic ideals, critical-value deformation theory, and local vanishing homology
hodge_type: no global rational type-(0,0) detector is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic representative of a specified Hodge class is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B141, B155-B158, and S065
claim: For every R<N and every m at least 2, there is an ordered critical-value germ with uniform conormal matroid U_(R,N), all intersections of at most R branches smooth of expected codimension, and the same (m-1)-jet as a saturated linear arrangement, but whose basis-node escape germ is y^m and whose full ideal is (x_1,...,x_R,y^m). Thus its hidden-generator space is one-dimensional.
falsifier: a vanishing Vandermonde basis minor, a singular branch or small intersection, containment of the basis germ in the perturbed branch, equality of the escaping ideal with the basis ideal, or failure of projective nonlinear-base realization under B157
---

# B159 — Uniform matroids permit arbitrarily high-order node escape

Fix \(1\le R<N\), distinct numbers \(a_1,\ldots,a_N\in\mathbf C\), and
coordinates \(x=(x_1,\ldots,x_R)\), \(y\). Put

\[
 \ell_i(x)=\sum_{j=0}^{R-1}a_i^j x_{j+1}.
\]

Every \(R\times R\) minor of the row matrix of the \(\ell_i\) is a
Vandermonde determinant, hence is nonzero. The conormal matroid of the
linear branches \(\ell_i=0\) is therefore \(U_{R,N}\).

Choose \(B=\{1,\ldots,R\}\) and, for \(m\ge2\), define

\[
 \tau_i^{(m)}=
 \begin{cases}
 \ell_i(x),&i<N,\\
 \ell_N(x)+y^m,&i=N.
 \end{cases} \tag{1}
\]

The differentials at the origin are still the \(\ell_i\), so the conormal
matroid remains \(U_{R,N}\). Every subset of at most \(R\) branches has
independent differentials and hence a smooth intersection of the expected
codimension.

The first \(R\) linear forms generate \((x_1,\ldots,x_R)\). On their common
germ \(F_B=\{x=0\}\), equation (1) restricts to

\[
 \epsilon_{B,N}=y^m.
\]

Consequently

\[
 I_{\tau^{(m)}}=(x_1,\ldots,x_R,y^m),\qquad
 \mu(I_{\tau^{(m)}})=R+1,
\]

while \(\operatorname{rank}d\tau^{(m)}_0=R\). B156 gives
\(\dim H_{\tau^{(m)}}=1\).

The saturated control family

\[
 \tau_i^{\mathrm{lin}}=\ell_i(x)
\]

has the same \((m-1)\)-jet as (1), and every extra node persists on \(F_B\).
Thus uniform tangent geometry and any prescribed finite jet order fail to
decide the persistence condition of B158. By B157, both germs occur as
ordered fixed-ODP critical values in projective hypersurface families after
nonlinear analytic pullback. This last realization does not assert that the
full complete-linear-system germ itself is arbitrary.
