---
brick_id: G030
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold, a generic plane net carrying a B056 Schnell detector loop, and a degeneration to one clean multipart nodal hyperplane
smoothness: X and fibers along the detector loop are smooth; the target has only ordinary double points and a Li-clean discriminant arrangement
projectivity: X, the hyperplane family, the plane net, and the degenerating family of nets are projective
dimension: dim_C X = 2n; the working parameter space is a projective plane and the collision target is one point of its discriminant curve
codimension: middle codimension n; the target is a higher discriminant stratum whose codimension equals the required multipart incidence
coefficient_field: Q
cohomology_theory: tube maps, extension chains, Lefschetz thimbles, nearby and vanishing cycles, B022 quotient homology, local intersection cohomology, and mixed Hodge modules
hodge_type: the specialized relation must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the specified class may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010-B013, B022-B025, B054, B056-B058, G029, NG023, NG037-NG038, and Saito S022
claim: Every B056 detector pair in a generic plane net admits an algebraic topology-changing collision to one clean q-block nodal member and a rational local relation beta such that Phi(beta) equals the original B057 tube class in primitive ambient homology and beta has type (0,0).
falsifier: a detector pair for which every clean nodal collision either has no specialization of the B057 extension chain, maps it to zero or a different ambient class, or produces no rational type-(0,0) relation
---

# G030 - Class-preserving collision inside a plane net

B056 reduces the global parameter space to a generic plane net without
changing the detecting tube. B057 identifies the detector with an explicit
boundary-zero thimble extension chain

\[
 c_g(\alpha)=
 \sum_i\varepsilon
 \langle\alpha_{i-1},\delta_i\rangle\Delta_i.
\]

The remaining theorem is now one specialization square. Construct an
algebraic degeneration of nets and meridian systems to a clean multipart
nodal point \(p\), together with

\[
 \operatorname{sp}_p(c_g(\alpha))
 =\beta\in R(Y_p)_1^{(0,0)},
\]

such that the diagram

\[
\begin{array}{ccc}
 \langle c_g(\alpha)\rangle
 &\xrightarrow{\operatorname{sp}_p}&
 R(Y_p)_1^{(0,0)}\\
 \downarrow && \downarrow\Phi_{Y_p}\\
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}
 &=&
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}
\end{array}
\]

commutes and

\[
 \Phi_{Y_p}(\beta)=[\tau_g(\alpha)].
\]

The right side already pairs nontrivially with the specified Hodge class.
Thus equality, not a dimension count or positive-rank statement, is the
required preservation condition.

## First failed specialization

Replacing \(g\) by the total equator of one complete pencil does not provide
the square. NG038 proves that its B057 vector is exactly
\(\tau_\infty(\alpha)\), hence zero in the first B022 quotient. The collision
must retain the actual non-equator net loop or acquire a transverse defect
class not in the equator-extension image.

No audited source constructs this specialization square. B054 computes the
local channel once the clean target exists; it does not identify a global
extension chain with a local Saito relation.

## Ambient Hodge-type audit

B058 removes a possible source-side mismatch. Choose first a rational
type-\((0,0)\) primitive homology class \(c\) pairing nontrivially with
\(\zeta\), then use B011's surjective tube map and B056 to realize exactly
\(c\) by a plane-net detector pair. The source of the specialization square
may therefore be fixed as

\[
 [\tau_g(\alpha)]=c\in
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}^{(0,0)}.
\]

B054 makes every relation in the clean target channel type \((0,0)\).
Accordingly, the only unresolved decisive statement in the square is the
geometric equality \(\Phi_{Y_p}(\beta)=c\); neither a new Hodge-type
conversion nor a dimension argument can replace it.
