---
brick_id: G127
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and one class-directed point scheme Z used in every embedding H^k through the degree-m birth
smoothness: the ambient variety and point supports are smooth; the degree-m divisor must have isolated ODPs and the final simultaneous-node germ must be reduced and smooth
projectivity: every lower embedding, point span, tangent space, degree-m complete system, doubled scheme, and detector family is projective
dimension: N points; for every k<m the value span is either full or has vector dimension at least 2n+1 and contains every embedded tangent space; V_m has dimension 2n
codimension: construct simultaneous tangent-span absorption in every lower embedding, followed by the primitive degree-m Hessian-holonomy birth
coefficient_field: C for embeddings, tangents, jets, and Hessians; Q for the Hodge class, vanishing-cycle detector, and specified pairing
cohomology_theory: projective secant/contact geometry, graded coherent first jets, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B196, G013, G090-G126, NG106-NG159, and S073
claim: Construct from arbitrary (X,zeta) one point scheme Z and degree m such that in every lower H^k embedding the span of Z is full or contains all tangent spaces at Z, while degree m has G125's primitive 2n-dimensional one-node-determined Hessian holonomy and the complete rational detector package.
falsifier: a lower embedding with a proper point span missing a marked tangent direction, a nonzero lower conditional jet, failure of primitive birth or Hessian holonomy at m, a positive-dimensional singular locus in the degree-m divisor, or failure of any detector clause
---

# G127 — Construct simultaneous lower tangent-span absorption

B196 translates every lower extinction equality in G125 into projective
geometry. Starting from arbitrary \((X,\zeta)\), construct one \(Z\) and
one birth degree \(m\) such that for every \(1\le k<m\), with

\[
 \phi_k:X\hookrightarrow\mathbf P(H^0(H^k)^*),
 \qquad L_{k,Z}=\langle\phi_k(Z)\rangle,
\]

one of the following holds:

1. **full span:** \(L_{k,Z}\) is the whole ambient projective space; or
2. **proper absorption:**
   \[
   T_{X,p_i}^{(k)}\subset L_{k,Z}\quad\text{for every }p_i\in Z. \tag{1}
   \]

In the second branch the vector value rank is at least \(2n+1\), and
\(L_{k,Z}\) is simultaneously tangent to \(X\) at all marked points.

At degree \(m\), the same \(Z\) must cease to have zero conditional jets
and instead satisfy all G125 obligations:

\[
 \dim V_m=2n,
\]

one-node determination, conformal Hessian holonomy, full-support multiplier
in the no-coloop value image, isolated ODPs, and the class-specific rational
detector.

G127 is a geometric sufficient form of G125's graded lower half; it does
not replace G125 or make the degree-m birth follow from the lower spans.
The same point scheme across the powers remains essential, but for
\(m\ge2\), B197 proves that the conditions need not be constructed
independently: absorption in degree \(m-1\) forces every earlier extinction.
B198/G128 then isolate the
new minimal generators required for the adjacent degree-\(m\) birth.
