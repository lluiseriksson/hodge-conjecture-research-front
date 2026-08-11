---
brick_id: B154
status: PROVED
base_field: C
variety: the local analytic ordered-node deformation germ of a hypersurface in a smooth projective complex variety, with critical-value map tau of differential rank R<N
smoothness: the ambient variety and central nodes are smooth/ordinary double points; smoothness of the rank-deficient simultaneous-node germ is the conclusion tested by the obstruction
projectivity: the ambient hypersurface problem is projective; the proof uses only its local analytic critical-value germ
dimension: parameter tangent W; tangent kernel V=ker E; obstruction target C=coker E of dimension N-R; cubic tensor space C tensor Sym^3(V^*)
codimension: a smooth excess germ would have height R and requires the reduced Kuranishi germ to vanish identically; after quadratic vanishing its first possible term is cubic
coefficient_field: C
cohomology_theory: analytic implicit-function theory, local nodal deformation theory, and finite-dimensional symmetric multilinear algebra
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or specified Hodge detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B153, analytic implicit-function theorem, chain rule through third order, and polarization
claim: Any rank-R critical-value germ admits a reduced Kuranishi map kappa:ker E -> coker E whose zero germ is the simultaneous-node germ after solving the independent equations. Its quadratic tensor is B146's relation obstruction. If that tensor vanishes, the cubic tensor kappa_3 in coker(E) tensor Sym^3((ker E)^*) is canonical, with the displayed correction formula. Nonzero kappa_3 obstructs a reduced smooth height-R node germ.
falsifier: two implicit reductions with different cubic tensors after zero quadratic tensor, an incorrect third critical-value formula, or a nonzero cubic tensor on a reduced smooth germ having tangent ker E and height R
---

# B154 — The first post-Hessian obstruction is cubic Kuranishi data

Let

\[
 \tau:(W,0)\longrightarrow(\mathcal T,0),\qquad
 d\tau_0=E,\qquad \operatorname{rank}E=R<N.
\]

Put

\[
 V=\ker E,\qquad C=\operatorname{coker}E.
\]

Choose complements \(W=V\oplus M\) and
\(\mathcal T=\operatorname{im}E\oplus C\), with
\(E|_M:M\xrightarrow{\sim}\operatorname{im}E\). The implicit-function
theorem gives a unique analytic \(m:(V,0)\to(M,0)\), with
\(m(0)=dm_0=0\), such that the \(\operatorname{im}E\)-component of
\(\tau(v+m(v))\) is zero. Define the reduced Kuranishi germ

\[
 \kappa(v)=\pi_C\tau(v+m(v)):(V,0)\longrightarrow(C,0).
\]

Then

\[
 \tau^{-1}(0)\simeq\kappa^{-1}(0).
\]

The simultaneous-node germ is reduced and smooth of height \(R\), with
tangent \(V\), exactly when \(\kappa\) vanishes identically.

## Quadratic and cubic tensors

Write

\[
 B=d^2\tau_0,\qquad T=d^3\tau_0.
\]

The quadratic tensor is

\[
 \kappa_2(a,b)=\pi_C B(a,b),\qquad a,b\in V.
\]

This is precisely B146's relation-Hessian obstruction. Suppose
\(\kappa_2=0\). Let

\[
 m_2(a,b)=
 -(E|_M)^{-1}\pi_{\operatorname{im}E}B(a,b).
\]

The third-order chain rule gives

\[
 \begin{aligned}
 \kappa_3(a,b,c)=\pi_C\bigl(
 &T(a,b,c)
 +B(a,m_2(b,c))\\
 &+B(b,m_2(a,c))
 +B(c,m_2(a,b))
 \bigr).
 \end{aligned}
\]

Changing either complement changes the reduced Kuranishi germ by analytic
source and target coordinates whose linear parts are the canonical
identities on \(V\) and \(C\). When the quadratic tensor is zero, such
changes cannot alter the cubic homogeneous term. Hence

\[
 \kappa_3\in C\otimes\operatorname{Sym}^3V^*
\]

is canonical.

If \(\kappa_3\ne0\), then \(\kappa\not\equiv0\), so the ordered-node germ
cannot be the reduced smooth height-\(R\) germ required by G090-G097.

## Third derivative of one critical value

At node \(p_i\), write \(H_i=d_x^2s\), \(S_i=d_x^3s\), and for a parameter
direction \(a\), set

\[
 v_a=H_i^{-1}(da_{p_i}).
\]

Differentiating the critical-point equation through second order gives

\[
 \begin{aligned}
 d^3\tau_i(a,b,c)=&
 d_x^2a(v_b,v_c)
 +d_x^2b(v_a,v_c)\\
 &+d_x^2c(v_a,v_b)
 -S_i(v_a,v_b,v_c).
 \end{aligned}
\]

For \(a=b=c\),

\[
 d^3\tau_i(a,a,a)
 =3d_x^2a(v_a,v_a)-S_i(v_a,v_a,v_a).
\]

Thus \(\kappa_3\) is explicitly computable from spatial two-jets of
deformation sections, spatial three-jets of the central hypersurface,
Hessian inverses, and the second-order implicit correction \(m_2\).

B154 neither proves \(\kappa_3=0\) nor controls fourth and higher terms.
