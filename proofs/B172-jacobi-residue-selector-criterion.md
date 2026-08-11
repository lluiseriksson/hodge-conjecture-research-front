---
brick_id: B172
status: PROVED
base_field: C
variety: a holomorphic family of affine polynomial functions on C^d, used only as a candidate local-chart mechanism for the projective hypersurface route
smoothness: the parameter germ and every ordered critical-point section are smooth; all critical points are simple and the gradient system has no zero at infinity
projectivity: not assumed for the affine residue theorem; a projective application must separately compactify the rational chart, control poles and infinity, and cover the full complete linear system
dimension: d spatial variables; N tracked critical points; M auxiliary critical points; central tracked value rank R<N
codimension: the desired simultaneous tracked-node germ has codimension R; the selector certificate requires N-R independent analytic syzygies
coefficient_field: C
cohomology_theory: Grothendieck residues, the Jacobi global residue formula, and analytic local algebra of the tracked critical-value ideal
hodge_type: none asserted; no rational type-(0,0) class is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156, G100, S069
claim: In a Jacobi-proper polynomial Morse family, admissible residue numerators f_t A give analytic syzygies among tracked critical values when the complete auxiliary critical-point residue vanishes. If N-R such exact-selector rows span the central relation space, then H_tau=0. Mere membership of the auxiliary residue in the tracked ideal is automatic and supplies no syzygy.
falsifier: an admissible selector family satisfying the stated auxiliary vanishing and spanning hypotheses but whose residue rows fail to be analytic syzygies or fail to kill H_tau
---

# B172 — Jacobi residues reduce G100 to a selector obligation

Let \(f_t(z)\) be a holomorphic family of polynomials on
\(\mathbf C^d\). Put

\[
 P_t=(\partial_1f_t,\ldots,\partial_df_t),\qquad
 D=\sum_{j=1}^d\deg(P_{t,j})-d-1.
\]

Assume the highest homogeneous parts of the \(P_{t,j}\) have no common
nonzero zero, uniformly near \(t=0\), and every critical point is simple.
Order all critical points analytically as tracked points \(p_i(t)\) and
auxiliary points \(a_j(t)\). Write

\[
 \tau_i(t)=f_t(p_i(t)),\qquad
 \nu_j(t)=f_t(a_j(t)),\qquad
 J_x(t)=\det\operatorname{Hess}_z f_t(x(t)).
\]

The tracked values satisfy \(\tau_i(0)=0\), and
\(R=\operatorname{rank}d\tau_0<N\).

For every polynomial \(A(t,z)\), analytic in \(t\), such that

\[
 \deg_z(f_tA)\le D, \tag{1}
\]

Jacobi's residue formula applied pointwise to \(Q_t=f_tA_t\) gives

\[
 \sum_{i=1}^N
 \frac{A(t,p_i(t))}{J_{p_i}(t)}\tau_i(t)
 +
 \rho_A(t)=0,\qquad
 \rho_A(t)=\sum_{j=1}^M
 \frac{A(t,a_j(t))}{J_{a_j}(t)}\nu_j(t). \tag{2}
\]

All coefficients are analytic because the Hessian determinants are units.
Equation (2) is a homogeneous syzygy of the tracked value tuple when the
auxiliary term vanishes.

There is an important correction to the more general interpretation.
Equation (2) itself already writes

\[
 \rho_A=-\sum_i
 \frac{A(t,p_i(t))}{J_{p_i}(t)}\tau_i,
\]

so \([\rho_A]=0\) in
\(\mathcal O_{T,0}/I_\tau\) is automatic for every admissible \(A\).
The canonical coefficient representation cancels the tracked row and gives
the zero syzygy. B174 proves that every other coefficient representation
differs from this one by a pre-existing analytic syzygy. Ideal membership
is therefore neither an obstruction nor a construction certificate.

The non-circular clean sufficient form is exact auxiliary vanishing.
Suppose \(A_1,\ldots,A_{N-R}\) satisfy
(1), vanish at every auxiliary critical point, and the rows

\[
 s_{\ell i}(0)=
 \frac{A_\ell(0,p_i(0))}{J_{p_i}(0)}
\]

span \(\ker(d\tau_0)^*\). Equations (2) are then \(N-R\) analytic
syzygies lifting all central linear value relations. B156 implies
\(H_\tau=0\), hence the rank-\(R\) factorization required by G100.

## What remains open

The residue theorem does not construct the exact selectors \(A_\ell\). Its degree
bound and the demand that they annihilate every auxiliary critical point
are separate global interpolation constraints. For a projective section,
one must additionally choose a meromorphic trivialization, account for its
poles and critical points at the boundary, and prove that the resulting
rows retain the full complete-system matroid, rational type, primitive
ambient image, and specified nonzero Saito pairing. None of those clauses
follows from B172.
