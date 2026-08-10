---
brick_id: B058
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold in a sufficiently high embedding and a generic projective plane net of its hyperplane parameter space
smoothness: X and all hyperplane fibers along the selected detector loop are smooth
projectivity: X, the high-power embedding, and the plane net are projective
dimension: dim_C X = 2n; the detector loop lies in a two-dimensional projective net
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: polarized rational Hodge structures, primitive singular Betti homology and cohomology, monodromy tubes, and Poincare duality
hodge_type: the selected ambient tube class is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); the Hodge tube class is not asserted algebraic
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B011 global tube surjectivity, B016 perfect Hodge pairing, and B056 plane-net localization
claim: For every nonzero primitive rational middle Hodge class zeta, one can choose a Schnell detector pair in a generic plane net whose primitive ambient tube class is itself rational type (0,0) and pairs nontrivially with zeta.
falsifier: a nonzero primitive rational Hodge class whose rational Hodge-homology dual contains a nonzero pairing vector outside the surjective tube image or whose tube representative cannot be localized by B056
---

# B058 - Choose the tube target inside Hodge homology

Let

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}.
\]

B016 identifies the rational type-\((0,0)\) primitive homology

\[
 H^{\vee}_{\mathrm{Hdg}}
 =
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}^{(0,0)}
\]

as the perfect Hodge-theoretic dual of the primitive Hodge cohomology.
Therefore there is

\[
 c\in H^{\vee}_{\mathrm{Hdg}}
 \quad\text{with}\quad
 \langle\zeta,c\rangle\ne0.
\]

After passing to a sufficiently high embedding, B011 makes the rational tube
map surjective onto primitive ambient homology. Choose

\[
 (g,\alpha),\qquad g\alpha=\alpha,
\]

whose tube class is exactly \(c\). B056 replaces this pair by a pair in a
generic projective plane net without changing its monodromy-fixed class or
ambient tube:

\[
 [\tau_g(\alpha)]=c.
\]

Thus the source class for G030 can be chosen rational and of type \((0,0)\)
before any collision. A tube trace is still a topological construction; the
fact that its ambient class is Hodge does not make it algebraic.

## Consequence for the collision gate

B054 proves that the full rational relation channel of a clean nodal target
is pure type \((0,0)\). Hence G030 no longer needs an unexplained conversion
of an arbitrary ambient class into Hodge type. It must construct a clean
nodal relation \(\beta\) satisfying the exact geometric equality

\[
 \Phi_{Y_p}(\beta)=c.
\]

Existence of that specialization and equality remain open.
