---
brick_id: B177
status: PROVED
base_field: C
variety: a smooth analytic parameter germ M with labelled critical-value ideal I_tau and a connected complex Lie-group action preserving that ideal; projectively, the action may come from polarized automorphisms of X
smoothness: M is smooth and the tracked spatial singularities are ODPs; no smoothness of V(I_tau) is assumed
projectivity: the local theorem is analytic; in the intended application a polarized automorphism group acts on the full projective linear system and lifts locally to the ordered ODP incidence
dimension: parameter dimension d; central critical-value rank R; symmetry-orbit rank r_A; residual logarithmic dimension d-R-r_A
codimension: the full logarithmic orbit must have dimension d-R, while group-generated fields contribute exactly r_A and no more
coefficient_field: C for Lie algebras and analytic vector fields; Q remains required for downstream Hodge detectors
cohomology_theory: ideal-preserving logarithmic derivations, holomorphic group actions, ODP critical-value deformation theory, and primitive rational cohomology only downstream
hodge_type: none asserted; rational type (0,0) and the specified nonzero pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156, B176, G100, G109
claim: Fundamental vector fields of any connected holomorphic action preserving I_tau lie in Theta(-log I_tau), and their values span exactly the tangent space to the group orbit. Hence they close B176 only when the orbit rank is d-R; otherwise every completion needs at least d-R-r_A independent non-group logarithmic directions.
falsifier: a fundamental field failing to preserve I_tau under an ideal-preserving action, an evaluation image larger than the group-orbit tangent, or a spanning completion using fewer than d-R-r_A additional directions
---

# B177 — Symmetry-orbit dimension ceiling

Let a connected complex Lie group \(A\) act holomorphically on a smooth
germ \((M,0)\), and suppose the action preserves the labelled ideal sheaf
\(I=I_\tau\) on a neighborhood of the local orbit. Differentiating the
action gives the fundamental-field map

\[
 \rho:\mathfrak a\longrightarrow\Theta_M,
 \qquad \xi\longmapsto\xi_M.
\]

Since every local group element preserves \(I\), differentiation gives

\[
 \xi_M(I)\subseteq I.
\]

Therefore

\[
 \rho(\mathfrak a)\subseteq\Theta(-\log I). \tag{1}
\]

Evaluation at the origin is the differential of the orbit map

\[
 o_0:A\longrightarrow M,\qquad a\longmapsto a\cdot0.
\]

Consequently

\[
 \operatorname{ev}_0\rho(\mathfrak a)
 =T_0(A\cdot0),
 \qquad
 r_A:=\dim T_0(A\cdot0)
 =\operatorname{rank}(do_0)_e. \tag{2}
\]

By B176,

\[
 T_0(A\cdot0)
 \subseteq
 \operatorname{ev}_0\Theta(-\log I)
 \subseteq
 \ker d\tau_0, \tag{3}
\]

and \(\dim\ker d\tau_0=d-R\). Thus symmetry fields alone can close the
logarithmic-orbit certificate only if

\[
 r_A=d-R. \tag{4}
\]

More generally, define the residual symmetry quotient

\[
 Q_A=\ker d\tau_0/T_0(A\cdot0),
 \qquad \dim Q_A=d-R-r_A. \tag{5}
\]

Any collection of additional logarithmic vector fields completing the
fundamental fields to a spanning B176 frame must have at least
\(d-R-r_A\) independent images in \(Q_A\). This is an exact linear
dimension bound, not a dimension-count existence claim.

## Full-linear-system application guard

For a polarized action on \((X,L)\), the connected group acts on
\(|L|\) and on the hypersurface incidence. Near an ordered collection of
disjoint ODPs, the lifted action transports each critical point
continuously, so it cannot permute the labels near the identity. If the
resulting local action preserves the tracked branch ideals, (1)--(5)
apply to the full affine linear-system germ.

This contributes only the actual orbit tangent. It does not show that the
orbit has dimension \(d-R\), does not construct the complementary fields,
and does not retain any Hodge detector automatically.
