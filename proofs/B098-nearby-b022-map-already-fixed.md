---
brick_id: B098
status: PROVED
base_field: C with rational homology
variety: a smooth projective complex 2n-fold with a B057 detector in an audited B022 Lefschetz-pencil model and fixed smooth reference hyperplane
smoothness: ambient, reference fiber, and all fibers along the detector loop smooth; pencil critical points Morse
projectivity: ambient variety, hyperplane family, pencil blowup, and plane net projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: relative thimble homology, B022 exact sequences, primitive ambient homology, and tube maps
hodge_type: the selected B058 ambient value is rational type (0,0) after Q(n); the quotient theorem itself is topological
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B022, B057-B058
claim: Once a nearby class t_psi is identified with the B057 extension chain in the B022 pencil model, the nearby ambient map is already well defined after the equator-extension and base-locus quotients and sends t_psi to B058's selected class c.
falsifier: a B057 chain in the audited B022 model whose equator or base-locus representative changes its ambient image, or whose composite ambient image differs from its tube class
---

# B098 — The nearby B022 map and detector value are already fixed

**Status:** PROVED

Let $t=\tau_g(\alpha)$ be B057's boundary-zero thimble extension. B022 gives
the canonical sequence of maps

\[
 \ker\partial
 \twoheadrightarrow
 \mathcal T(Y)=\ker\partial/\operatorname{im}\tau_\infty
 \twoheadrightarrow
 \mathcal T(Y)/K
 \longrightarrow
 H_{2n}(X,\mathbf Q)/\operatorname{im}H_{2n}(H_0,\mathbf Q).
\]

The first quotient kills the equator-extension image by definition. The
second kills the base-locus kernel $K$ by B022's exact sequence. Therefore
the composite nearby ambient map $q_P$ is independent of both choices.

B057 identifies the composite image of $t$ with its Schnell tube class, and
B058 selected the detector so that this class is $c$. Hence, once an actual
nearby-cycle class $t_\psi$ has been proved to realize $t$,

\[
 q_P(t_\psi)=c.
\]

## Boundary

B098 closes G061's two generic quotient checks and its value check only after
the B057 realization is supplied. It does not extend $q_P$ across the
topology-changing collision or construct the special map $q_S$. NG074/G062
isolate that remaining arrow.
