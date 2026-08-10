---
brick_id: B030
status: PROVED
base_field: C
variety: X = P^4 with A = O_X(5), a plane P in X, and a nodal quintic hypersurface Y containing P
smoothness: X and P are smooth; Y has exactly 16 isolated ordinary double points for a general construction with the prescribed transverse first normal data
projectivity: X, P, and Y are projective
dimension: dim_C X = 4, dim_C Y = 3, and dim_C P = 2
codimension: P has codimension 2 in X; the Hodge application would have middle codimension 2
coefficient_field: C for sections, evaluation ranks, and coherent defects; Q for the later Hodge application
cohomology_theory: coherent cohomology of point ideals and local analytic Hessians; no primitive Hodge detector is asserted
hodge_type: no nonzero primitive middle Hodge class exists on P^4; no class-specific Hodge pairing is asserted
cycle_class_map: CH^2(P^4)_Q -> H^4(P^4,Q(2)); its image is tautological and the primitive target is zero
cycle_equivalence: rational equivalence
scope: absolute
dependencies: Kloosterman plane-containing nodal family (S032), B028-B029, and the Koszul calculations below
claim: There is a nodal quintic threefold in P^4 whose 16 nodes partition into two 8-point subsets independently imposing conditions on O(5), while the full node set has one-dimensional O(5) = K_X tensor A^2 evaluation defect.
falsifier: failure of either subset evaluation map to be surjective, vanishing of the full defect, or a non-nodal singularity forced by the stated transverse plane construction
---

# B030 - A plane-quintic witness for the two-matroid window

This brick tests whether the abstract G013 rank conditions are compatible
with isolated nodality. It does not test the class-pairing condition.

Let \(P\simeq\mathbf P^2\subset\mathbf P^4=X\) be cut out by
\(x_0=x_1=0\). On \(P\), choose two smooth conics \(q_1,q_2\) and a smooth
quartic \(h\) such that all relevant intersections are transverse and \(h\)
avoids \(q_1\cap q_2\). Put \(g=q_1q_2\). Choose degree-four lifts \(G,H\)
to \(X\), with general higher normal terms, and set

\[
 s=x_0G+x_1H\in H^0(X,\mathcal O_X(5)).
\]

The quintic \(Y=V(s)\) contains \(P\).

## Isolated nodes

Along \(P\), the two first normal derivatives of \(s\) are \(g\) and \(h\).
Hence

\[
 \operatorname{Sing}(Y)\cap P
 =V_P(g,h)
 =J\sqcup K,
\]

where

\[
 J=V_P(q_1,h),\qquad K=V_P(q_2,h).
\]

Each set has \(2\cdot4=8\) reduced points, and their union is the reduced
complete intersection of two quartics, with \(16\) points. At each point,
\(dg\) and \(dh\) are independent tangent covectors. In local normal
coordinates \(u,v\), the quadratic term contains

\[
 u\,dg+v\,dh,
\]

whose normal-tangent cross block is nonsingular. The critical point is
therefore an ordinary double point. General higher normal terms avoid any
singularity away from \(P\) by Bertini applied off the base plane. This is
also the local form of Kloosterman's audited statement that a general
degree-\(d\) hypersurface containing a plane is nodal.

## The two evaluation conditions

Restriction from \(\mathbf P^4\) to \(P\) is surjective in degree five, so it
is enough to compute on \(P\). For either
\(J\) or \(K\), the Koszul resolution of a \((2,4)\) complete intersection,
twisted by five, is

\[
 0\longrightarrow\mathcal O_P(-1)
 \longrightarrow\mathcal O_P(3)\oplus\mathcal O_P(1)
 \longrightarrow I_J(5)\longrightarrow0.
\]

The cohomology of line bundles on \(\mathbf P^2\) gives
\(H^1(P,I_J(5))=0\), and likewise for \(K\). Thus both eight-point sets
independently impose conditions on \(A=\mathcal O_X(5)\).

For the full \((4,4)\) complete intersection \(\Delta=J\sqcup K\), the
twisted resolution is

\[
 0\longrightarrow\mathcal O_P(-3)
 \longrightarrow\mathcal O_P(1)^{\oplus2}
 \longrightarrow I_\Delta(5)\longrightarrow0.
\]

Therefore

\[
 H^1(P,I_\Delta(5))
 \simeq H^2(P,\mathcal O_P(-3))
 \simeq\mathbf C.
\]

Since \(K_X\otimes A^2=\mathcal O_X(-5+10)=\mathcal O_X(5)=A\), the
smoothing and adjoint evaluation matroids coincide here. The two parts are
independent, while the union has adjoint corank one. Thus isolated nodality
and both B028 rank conditions are simultaneously realizable.

## Scope guard

The witness is a special plane-containing quintic. Moreover,
\(H^4_{\mathrm{prim}}(\mathbf P^4,\mathbf Q(2))=0\), so there is no nonzero
primitive rational Hodge class \(\zeta\) whose pairing could be tested. The
plane is an algebraic anchor built into the equation. Consequently this brick
proves nonemptiness of the geometric rank window only; it supplies no general
Hodge progress and no non-circular class-selection mechanism for G013.
