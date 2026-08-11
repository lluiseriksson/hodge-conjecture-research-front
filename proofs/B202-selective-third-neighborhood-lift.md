---
brick_id: B202
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with line bundle L=H^m, a nonempty reduced point scheme Z, a nowhere-zero value section t on Z, and a d-dimensional one-node-determined jet space U
smoothness: X and Z are smooth; a nondegenerate lifted quadratic profile gives ODP Hessians at Z, but no incidence smoothness follows
projectivity: X, L, the second and third infinitesimal neighborhoods of Z, and the coherent lifting sequence are projective
dimension: dim X=d; length Z=N; I_Z^2/I_Z^3 has fiber dimension d(d+1)/2 at each node; full first-jet separation would give dim V=dN
codimension: G130's quadratic congruence is equivalent to vanishing of one connecting-homomorphism class in H1(I_Z^3 L)
coefficient_field: C for sections, infinitesimal neighborhoods, cohomology, and quadratic jets; Q remains required separately for the detector
cohomology_theory: coherent ideal-power exact sequences, connecting homomorphisms, ODP quadratic jets, and finite-dimensional evaluation maps
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B201, G124-G131, and S065
claim: For t nonzero on Z and Q in Sym^2 U, divide the quadratic class mu_2(Q) by t|_Z to obtain q_(t,Q) in H0((I_Z^2/I_Z^3)L). There exists F in H0(I_Z^2 L) with tF-mu_2(Q) in H0(I_Z^3 L^2) exactly when the connecting class partial_Z(q_(t,Q)) in H1(I_Z^3 L) vanishes; the lifts form a torsor under H0(I_Z^3 L). If H1(I_Z^3 L)=0, the lift is automatic but the complete system separates all two-jets, forcing value rank N and dim V=dN, incompatible with the G130 branch for N>1.
falsifier: a lift with nonzero connecting class, a zero connecting class without a lift, two lifts whose difference is not triple on Z, or H1(I_Z^3 L)=0 without full two-jet and hence first-jet surjectivity
---

# B202 — G130 requires a selective third-neighborhood lift

Let \(I=I_Z\), let \(L=H^m\), and choose G130's

\[
 t\in H^0(X,L),\qquad t|_Z\ne0,\qquad
 Q\in\operatorname{Sym}^2U.
\]

The product \(\mu_2(Q)\) lies in \(H^0(I^2L^2)\). Its class on the
second conormal layer is

\[
 [\mu_2(Q)]\in
 H^0\bigl((I^2/I^3)\otimes L^2\bigr). \tag{1}
\]

Since \(t|_Z\) is a unit of the line \(L|_Z\), divide (1) by that value to
obtain a uniquely defined profile

\[
 q_{t,Q}\in
 H^0\bigl((I^2/I^3)\otimes L\bigr). \tag{2}
\]

## Exact lifting obstruction

The coherent exact sequence

\[
 0\longrightarrow I^3L
 \longrightarrow I^2L
 \longrightarrow (I^2/I^3)L
 \longrightarrow0 \tag{3}
\]

has connecting homomorphism

\[
 \partial_Z:
 H^0((I^2/I^3)L)\longrightarrow H^1(I^3L). \tag{4}
\]

Exactness gives

\[
 \partial_Z(q_{t,Q})=0
 \quad\Longleftrightarrow\quad
 \exists F\in H^0(I^2L)\text{ lifting }q_{t,Q}. \tag{5}
\]

For such a lift, multiplication by \(t\) and (2) show

\[
 tF-\mu_2(Q)\in H^0(I^3L^2). \tag{6}
\]

Conversely, (6) forces \(F\) to lift (2). The set of all lifts in (5) is
an affine torsor under the kernel \(H^0(I^3L)\).

If \(Q\) is nondegenerate and every derivative \(U\to G_i\) is an
isomorphism, then every fiber of \(q_{t,Q}\) is a nondegenerate quadratic
form. Any lift \(F\) therefore has an ODP Hessian at each marked point.
This is only a local Hessian conclusion; other singularities remain
uncontrolled.

## Why blanket vanishing is incompatible

It is tempting to force (5) by imposing

\[
 H^1(X,I^3L)=0. \tag{7}
\]

But the separate exact sequence

\[
 0\longrightarrow I^3L\longrightarrow L
 \longrightarrow L|_{\mathcal O_X/I^3}\longrightarrow0 \tag{8}
\]

then makes the complete two-jet evaluation surjective. Its projection to
values and first jets is also surjective. Hence

\[
 R=N,\qquad
 \dim H^0(I_ZL)/H^0(I_{2Z}L)=dN. \tag{9}
\]

For \(N>1\), equation (9) contradicts G130's value defect \(R<N\) and
one-node-determined dimension \(d\). Thus G130 needs the special condition

\[
 0\ne H^1(I^3L)\quad\text{with}\quad
 q_{t,Q}\in\ker\partial_Z, \tag{10}
\]

not automatic high-positivity interpolation. B202 does not construct this
selective kernel element, prove generator minimality, retain the detector,
or close any higher Kuranishi rung.
