---
brick_id: B128
status: PROVED
base_field: C
variety: an arbitrary projective parameter space P^d carrying the full-support intersection complex of a rational local system; applied to the universal high-power hyperplane family of a smooth projective complex 2n-fold
smoothness: the ambient 2n-fold is smooth; the coefficient variation is smooth on the complement of the discriminant
projectivity: P^d and the ambient variety are projective
dimension: parameter dimension d at least 1; ambient dimension 2n; hyperplane fibers dimension 2n-1
codimension: middle codimension n on the ambient variety; the local target can be supported only in parameter codimension at least two
coefficient_field: Q
cohomology_theory: singular and intersection cohomology, ordinary cohomology sheaves, the hypercohomology spectral sequence, and polarizable Hodge modules in the application
hodge_type: arbitrary for the exact sequence; primitive rational type (0,0) after Q(n) for the incidence application
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B012, B014, G008, S024 equations (2.1)-(2.2), Definition 3.3, and formulas (2.7)-(2.13)
claim: For K=IC_P(V), IH^1(P,V) fits into the canonical edge sequence 0 -> H^1(P,H^(-d)K) -> IH^1(P,V) -> H^0(P,H^(-d+1)K) -> H^2(P,H^(-d)K); for the universal hyperplane incidence class, the edge section has stalk s(zeta)_p, so its local support is empty exactly when s(zeta) lies in the bottom-row image.
falsifier: an additional E_2 term or differential in total degree 1-d, or a mismatch between the edge-section stalk and the local Green-Griffiths component
---

# B128 — The two-row local-to-global edge sequence

**Status:** PROVED

Let \(P=\mathbf P^d\), let \(V\) be a rational local system on a dense
smooth open subset, and put \(K=IC_P(V)\) in perverse normalization. S024
equation (2.1) gives

\[
 \mathcal H^b(K)=0\qquad(b\notin[-d,-1]),
\]

while equation (2.2) gives

\[
 IH^1(P,V)=\mathbb H^{1-d}(P,K).
\]

Use the ordinary-sheaf hypercohomology spectral sequence

\[
 E_2^{a,b}=H^a(P,\mathcal H^bK)
 \Longrightarrow \mathbb H^{a+b}(P,K).
\]

In total degree \(1-d\), nonnegativity of \(a\) and the lower bound
\(b\ge-d\) leave exactly

\[
 E_2^{1,-d},\qquad E_2^{0,-d+1}.
\]

The first term has no possible incoming or outgoing differential. The second
has only the possible differential

\[
 d_2:E_2^{0,-d+1}\longrightarrow E_2^{2,-d}.
\]

The induced filtration therefore yields the canonical edge sequence

\[
 0\longrightarrow H^1(P,\mathcal H^{-d}K)
 \longrightarrow IH^1(P,V)
 \xrightarrow{e}
 H^0(P,\mathcal H^{-d+1}K)
 \xrightarrow{d_2}
 H^2(P,\mathcal H^{-d}K).
\]

## Incidence application

For the universal high-power hyperplane family, set

\[
 K_m=IC_{P_m}(R^{2n-1}\pi_{m,*}\mathbf Q(n)).
\]

S024 formulas (2.7)-(2.13) make restriction to a fiber compatible with the
canonical perverse graded component. Definition 3.3 then identifies the
stalk of the edge section with the local invariant:

\[
 e(s_m(\zeta))_p=s_m(\zeta)_p.
\]

Consequently

\[
 \operatorname{Sing}_m(\zeta)=\varnothing
 \Longleftrightarrow e(s_m(\zeta))=0
 \Longleftrightarrow
 s_m(\zeta)\in
 \operatorname{im}H^1(P_m,\mathcal H^{-d_m}K_m).
\]

This bottom-row image is the **escape space**. B128 converts G008 into one
exact edge-nonvanishing obligation but does not prove that obligation.

## Scope guard

The sequence is formal and canonical. It neither constructs a support point
nor proves that the incidence class avoids the escape space. Universal
avoidance for primitive rational Hodge classes remains terminal-equivalent
to the rational Hodge Conjecture.
