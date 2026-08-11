---
brick_id: B044
status: PROVED
base_field: C
variety: a three-dimensional nodal smoothing slice with seven central discriminant hyperplanes whose matroid has exactly one dependent triple, and its two-stage wonderful resolution
smoothness: the parameter threefold and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber has seven ordinary double points and nearby fibers are smooth
projectivity: both blow-ups and all exceptional strata are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 3, exceptional fiber dimension 2, dependent flat dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the origin has codimension 3, the unique dependent flat has codimension 2, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure of type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B035-B043, B134, G016, Green-Griffiths S021, and Saito S022/S037
claim: For the rank-three seven-branch arrangement with exactly one dependent triple, the polarized homological model dual to the two-stage downstairs cohomological IC channel is the full rational relation kernel, and both are pure type (0,0) after Q(n).
falsifier: a second-exceptional residue equation independent of the dependent-triple span equation, a positive-flat or point strict-support summand in ordinary degree one, or a non-(0,0) kernel component after Q(n)
---

# B044 - Single-dependent-flat relation channel

This brick proves G016.

## Two-stage exceptional fiber

Let \(F=H_1\cap H_2\cap H_3\) be the unique dependent codimension-two flat.
First blow up the origin. The first exceptional plane \(E=\mathbf P^2\)
contains three concurrent lines \(L_1,L_2,L_3\) at the point
\(p=\mathbf P(F)\). Then blow up the strict transform of \(F\).

The fiber of the composite map over the origin is

\[
 Z=\operatorname{Bl}_p\mathbf P^2.
\]

Let \(C\subset Z\) be its exceptional curve and \(M_i\subset Z\) the strict
transform of \(L_i\). If \(h\) is the pullback hyperplane class and \(e=[C]\),
then

\[
 [M_i]=h-e\quad(i=1,2,3),
 \qquad
 [M_i]=h\quad(i=4,5,6,7).
\]

The new exceptional divisor meets \(Z\) in \(C\). The curves
\(C,M_1,\ldots,M_7\) form an SNC divisor: \(C\) meets \(M_1,M_2,M_3\) in
three distinct points, while the remaining intersections are the proper
transforms of the ordinary line-pair points.

## Exceptional degree-one sheaf

Write

\[
 N_F=N_1+N_2+N_3,
 \qquad W_F=\operatorname{Im}N_F
 =\operatorname{span}\{\delta_1,\delta_2,\delta_3\},
\]

and \(N_E=\sum_{i=1}^7N_i\), \(W=\operatorname{Im}N_E\),
\(K=\ker N_E\). Every product among \(N_E,N_F,N_i\) vanishes. The same lift
argument as in B042-B043 identifies the degree-one stalk at any incidence
stratum with the direct sum of the coefficient spaces of the incident
curves. Hence

\[
 \mathcal H^0(A|_Z)=K_Z,
 \qquad
 \mathcal H^1(A|_Z)=
 (W_F)_C\oplus\bigoplus_{i=1}^7\mathbf Q_{M_i},
 \qquad
 \mathcal H^{\ge2}(A|_Z)=0.
\]

The new curve has coefficient \(W_F\), not a spurious one-dimensional
generator: its monodromy image is exactly \(\operatorname{Im}N_F\).

## Two-component residue map

The residue connecting morphism is divisor-class weighted. In the basis
\(h,e\) of \(H^2(Z,\mathbf Q)\), it sends

\[
 (w,a_1,\ldots,a_7)\in W_F\oplus\mathbf Q^7
\]

to

\[
 h\otimes\sum_{i=1}^7a_i\delta_i
 +e\otimes\left(w-\sum_{i=1}^3a_i\delta_i\right)
 \in H^2(Z,K_Z).
\]

Indeed, \(C\) contributes \(e\otimes w\), the first three strict transforms
contribute \((h-e)\otimes a_i\delta_i\), and the other four contribute
\(h\otimes a_i\delta_i\).

The kernel conditions are therefore

\[
 \sum_{i=1}^7a_i\delta_i=0,
 \qquad
 w=\sum_{i=1}^3a_i\delta_i.
\]

Projection to the seven \(a_i\) is a canonical isomorphism from this kernel
onto the full vanishing-cycle relation space; its inverse assigns the
displayed, automatically available \(w\in W_F\). Thus the dependent-flat
exceptional curve adds a bookkeeping equation but neither kills a relation
nor creates one.

## Composite direct-image supports

The composite resolution is not an isomorphism over \(F\setminus\{0\}\):
there the second blow-up has a \(\mathbf P^1\) fiber. Locally it is the product
of \(F\) with the rank-two three-line model of B041. That map is semismall,
so nonzero perverse cohomology away from the origin occurs only in degree
zero and may have strict support \(F\).

At the origin, \(Z\) is a surface and the two-row complex above has ordinary
hypercohomology only through degree four. After the dimension-three shift,
the composite direct image has perverse amplitude \([-1,1]\). Therefore:

- perverse degrees \(\pm1\) have point support;
- perverse degree zero can have strict supports \(B\), \(F\), and the point;
- after undoing the shift by three, point-supported terms occur in ordinary
  degrees \(2,3,4\);
- a perverse IC summand on the smooth curve \(F\) is a local system shifted
  by one, and after undoing the ambient shift it occurs in ordinary degree
  two.

No non-full-support summand contributes in ordinary degree one. Proper base
change and strict-support decomposition identify the resolved kernel with

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right).
\]

## Hodge type

After \(\mathbf Q(n)\), the spaces \(W_F\) and every branch line are sums of
\(\mathbf Q(0)\). The resolved divisor is SNC, and the residue map is a
morphism of rational mixed Hodge structures. Its kernel, transferred through
the Hodge-module strict-support decomposition, is therefore pure type
\((0,0)\).

## Scope guard

B044 proves only the first nonuniform dependent-flat model. It does not
establish compatibility for several or nested dependent flats, construct a
class-paired nodal member, or prove any algebraicity statement. The standard
rational Hodge Conjecture and G015 remain open.
