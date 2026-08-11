---
brick_id: B131
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex variety X of dimension 2r and its universal sufficiently high smooth hyperplane family
smoothness: X is smooth; the incidence family is restricted to the smooth parameter locus P_sm
projectivity: X and the hyperplane fibers are projective; P_sm is quasi-projective
dimension: dim_C X=2r; hyperplane dimension n=2r-1 at least 3; dim P_sm=d
codimension: middle codimension r on X
coefficient_field: Q, with the Tate twist Q(r) retained in the Hodge application
cohomology_theory: rational singular cohomology, Leray spectral sequences, weak Lefschetz, Nori connectivity, and variations of Hodge structure
hodge_type: arbitrary primitive degree 2r for the topological statement; rational type (r,r), or (0,0) after Q(r), in the Hodge application
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B012, B130, S024, S053, S054
claim: For every nonzero primitive class alpha in H^(2r)(X,Q), Nori's restriction isomorphism sends alpha to a class whose canonical first Leray symbol is nonzero in the vanishing-cohomology quotient H^1(P_sm,V_Q); equivalently the primitive kernel at Leray grade zero is canonically isomorphic to the new cokernel at grade one.
falsifier: a nonzero primitive alpha whose incidence pullback lies in Leray filtration L^2, or failure of the grade-p restriction isomorphism for some p at least two
---

# B131 — Canonical first-Leray transgression

**Status:** PROVED

Put \(n=2r-1\), so that \(X\) has dimension \(n+1=2r\), and let

\[
 \ell:\mathcal X^{\rm sm}\hookrightarrow P^{\rm sm}\times X
\]

be the smooth universal high-power incidence. Give both total cohomology
groups the decreasing Leray filtration for projection to \(P^{\rm sm}\).
For \(m\gg0\), Nori connectivity gives an isomorphism

\[
 \ell^*:H^{n+1}(P^{\rm sm}\times X,\mathbf Q)
 \xrightarrow{\sim}H^{n+1}(\mathcal X^{\rm sm},\mathbf Q),
\]

because \(n+1<2n\) for \(n\ge3\).

## Filtered linear-algebra lemma

Let \(f:(A,L)\to(B,L)\) be an isomorphism of finite decreasing filtered
vector spaces. If

\[
 \operatorname{gr}_L^p f
\]

is an isomorphism for every \(p\ge2\), then \(f(L^2A)=L^2B\). Passing to
the two-step quotients by \(L^2\) and applying the snake lemma gives a
canonical isomorphism

\[
 \ker(\operatorname{gr}_L^0f)
 \xrightarrow{\sim}
 \operatorname{coker}(\operatorname{gr}_L^1f).
\]

Concretely, if \(a\notin L^1A\), \(f(a)\in L^1B\), and the first symbol of
\(f(a)\) were zero, then \(f(a)\in L^2B=f(L^2A)\). Injectivity of \(f\)
would force \(a\in L^2A\), a contradiction.

## Application to the incidence

Deligne degeneration identifies the Leray associated grades in total degree
\(n+1\) with

\[
 E_2^{p,n+1-p}=H^p(P^{\rm sm},R^{n+1-p}\pi_*\mathbf Q).
\]

For \(p\ge2\), one has \(n+1-p<n\). Weak Lefschetz therefore makes

\[
 H^{n+1-p}(X,\mathbf Q)
 \longrightarrow R^{n+1-p}\pi_*\mathbf Q
\]

an isomorphism of local systems. Hence every
\(\operatorname{gr}_L^p\ell^*\), \(p\ge2\), is an isomorphism.

If \(0\ne\alpha\in H^{n+1}_{\rm prim}(X,\mathbf Q)\), then its restriction
to every smooth hyperplane is zero. Indeed, weak Lefschetz supplies every
class in \(H^{n-1}(X_p)\) from \(X\), and Poincare duality on \(X_p\) turns
the pairing with \(i_p^*\alpha\) into the pairing with
\(c_1(L)\smile\alpha=0\). Thus

\[
 \alpha\in\ker(\operatorname{gr}_L^0\ell^*).
\]

The filtered lemma now gives a nonzero canonical first symbol. In grade one,
the ambient summand is the image of

\[
 H^1(P^{\rm sm},H^n(X,\mathbf Q))
 \longrightarrow H^1(P^{\rm sm},R^n\pi_*\mathbf Q).
\]

Hard Lefschetz canonically splits the fiber local system into its ambient
part and vanishing cohomology \(V_{\mathbf Q}\). Therefore the cokernel is
\(H^1(P^{\rm sm},V_{\mathbf Q})\), and the construction yields an injection

\[
 \delta_m:H^{n+1}_{\rm prim}(X,\mathbf Q)
 \hookrightarrow H^1(P^{\rm sm},V_{\mathbf Q}).
\]

For a rational \((r,r)\) class, \(\delta_m(\alpha)(r)\) is the canonical
type-\((0,0)\) global normal-function/incidence class on the smooth locus.

## Boundary

B131 proves global rational nonvanishing without choosing a decomposition-
theorem splitting. It does not show that the class has a nonzero local
singularity. The latter is exactly the failure of the global class to remain
in the B128 escape row after minimal extension across the discriminant.
