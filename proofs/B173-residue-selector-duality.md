---
brick_id: B173
status: PROVED
base_field: C
variety: the reduced projective complete intersection obtained by homogenizing the gradient of a degree-m affine polynomial family on C^d, partitioned into tracked and auxiliary critical-point sections
smoothness: the parameter germ is smooth; every critical point is simple; the homogenized gradient complete intersection is reduced and has no point at infinity
projectivity: the critical scheme is projective in P^d; the polynomial family is affine and is not a general hypersurface family on an arbitrary projective variety
dimension: d spatial variables; complete-intersection length (m-1)^d; N tracked points; critical degree s=d(m-1)-d-1; selector degree e=s-m>=0
codimension: the moving degree-m evaluation map on the tracked points has central rank R<N; its relation space has dimension N-R
coefficient_field: C
cohomology_theory: Davis-Geramita-Orecchia residual duality, projective evaluation codes, Grothendieck residues, and analytic constant-rank linear algebra
hodge_type: none asserted; no rational type-(0,0) detector is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156, B170-B172, G100, G107, S069-S070
claim: At the maximal Jacobi selector degree e=s-m, Hessian-weighted selectors vanishing on every auxiliary critical point form exactly the dual kernel of degree-m evaluation on the tracked points. Consequently a local analytic frame of N-R exact selectors exists if and only if that moving evaluation map has constant rank R.
falsifier: a reduced gradient complete-intersection family satisfying the hypotheses in which the weighted selector space differs from the dual evaluation kernel, or has an analytic N-R frame while the tracked degree-m evaluation rank jumps
---

# B173 — Critical-degree residue selectors are dual to G107

Let \(f_t\) be a holomorphic family of affine polynomials of degree \(m\)
in \(d\) variables. Homogenize the \(d\) partial derivatives to forms of
degree \(m-1\) on \(\mathbf P^d\). Assume their common zero scheme
\(\Gamma_t\) is reduced, has no point at infinity, and splits analytically
as

\[
 \Gamma_t=A_t\sqcup T_t,
\]

where \(T_t=\{p_1(t),\ldots,p_N(t)\}\) is the tracked set and \(A_t\) is
the complete auxiliary set. Put

\[
 s=d(m-1)-d-1,\qquad e=s-m\ge0.
\]

Write \(R_a\) for homogeneous forms of degree \(a\), equivalently affine
polynomials of degree at most \(a\) on the chosen chart. Define the
unweighted exact-selector image

\[
 \operatorname{Sel}_e(T_t)
 =
 \operatorname{ev}_{T_t}\bigl((I_{A_t})_e\bigr)
 \subseteq\mathbf C^N. \tag{1}
\]

Forms in \((I_{\Gamma_t})_e\) are the kernel of this evaluation, so

\[
 \dim\operatorname{Sel}_e(T_t)
 =
 \dim (I_{A_t})_e/(I_{\Gamma_t})_e. \tag{2}
\]

Because \(A_t\) and \(T_t\) are residual in the reduced complete
intersection \(\Gamma_t\), the Davis--Geramita--Orecchia theorem gives

\[
 \dim (I_{A_t})_e/(I_{\Gamma_t})_e
 =
 h^1\!\left(I_{T_t}(s-e)\right)
 =
 N-\operatorname{rank}\operatorname{ev}_{T_t}^{\,m}. \tag{3}
\]

The last equality is the evaluation exact sequence and \(s-e=m\).

Let

\[
 J_i(t)=\det\operatorname{Hess}f_t(p_i(t)).
\]

Every \(J_i\) is a unit. For \(A\in(I_{A_t})_e\) and \(B\in R_m\), the
product \(AB\) has degree at most \(s\). Jacobi's formula therefore gives

\[
 \sum_{i=1}^N
 \frac{A(p_i(t))B(p_i(t))}{J_i(t)}=0, \tag{4}
\]

because \(A\) vanishes on every auxiliary point. Hence the
Hessian-weighted selector space

\[
 \operatorname{Sel}^{\mathrm{res}}_e(T_t)
 =
 \left\{
 \left(\frac{A(p_i(t))}{J_i(t)}\right)_i:
 A\in(I_{A_t})_e
 \right\}
\]

is contained in

\[
 \ker\!\left(\operatorname{ev}_{T_t}^{\,m}\right)^*.
\]

Both spaces have dimension
\(N-\operatorname{rank}\operatorname{ev}_{T_t}^{\,m}\) by (3), so

\[
 \boxed{\operatorname{Sel}^{\mathrm{res}}_e(T_t)
 =\ker\!\left(\operatorname{ev}_{T_t}^{\,m}\right)^*.} \tag{5}
\]

## Family consequence

Suppose the central degree-\(m\) evaluation rank is \(R\). If
\(N-R\) analytic exact selectors have independent central residue rows,
their rows remain independent nearby. Equation (5) forces the moving
evaluation rank to be at most \(R\). A nonzero central \(R\times R\)
minor keeps it at least \(R\), hence the rank is identically \(R\).

Conversely, if the moving evaluation rank is identically \(R\), (3) makes
the selector image a rank-\(N-R\) analytic vector bundle. The evaluation
maps on \(A_t\) and \(\Gamma_t\) then have constant rank, so analytic
constant-rank splittings lift a local frame to degree-\(e\) polynomials
vanishing on \(A_t\).

By B170, degree-\(m\) evaluation on the moving tracked critical
configuration is the critical-value Jacobian for the full polynomial
coefficient family. Thus the complete exact-selector implementation of
B172 is equivalent here to G107's constant-rank condition. It is not a
weaker route to G100.

## Scope guard

The equality uses a reduced projective complete intersection with no
critical point at infinity and selectors that vanish exactly on all
auxiliary points. It does not treat arbitrary smooth projective \(X\).
B174 shows that replacing exact vanishing by the bare condition
\([\rho_A]=0\) in \(\mathcal O/I_\tau\) is tautological, not a broader
residue mechanism. B173 supplies no rational Hodge type, primitive ambient
image, or specified pairing.
