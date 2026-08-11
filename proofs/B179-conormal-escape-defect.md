---
brick_id: B179
status: PROVED
base_field: C
variety: a smooth basis-node persistence germ F_B with analytic escape ideal K_B arising from a labelled ODP critical-value family
smoothness: F_B is smooth; the escape subscheme V(K_B) and the full simultaneous-node germ need not be smooth or reduced
projectivity: not used in the conormal algebra; the intended application is the full projective complete-linear-system germ
dimension: basis-node dimension q=d-R; arbitrary number N-R of escape generators
codimension: vanishing of the conormal defect is equivalent to zero escape ideal and smooth codimension-R simultaneous-node persistence
coefficient_field: C for Kähler differentials and analytic local algebra; Q remains required only for downstream Hodge detectors
cohomology_theory: Kähler differentials, conormal modules, analytic differential ideals, and ODP critical-value deformation theory
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B158-B159, B176-B178, G100, G109-G111
claim: The canonical conormal differential beta_K:K_B/K_B^2 -> Omega^1_F_B tensor O_F_B/K_B vanishes if and only if K_B is stable under all tangent derivations, if and only if K_B=0, if and only if H_tau=0. It is the exact all-order obstruction that any connection comparison in G111 must kill.
falsifier: failure of beta_K to be well-defined, a vanishing beta_K for nonzero K_B contained in the maximal ideal, or H_tau=0 with nonzero beta_K
---

# B179 — The conormal escape defect

Let

\[
 O=\mathcal O_{F_B,0},\qquad K=K_B\subseteq\mathfrak m_O
\]

be B178's escape ideal. The universal derivation defines the canonical
conormal map

\[
 \beta_K:K/K^2\longrightarrow
 \Omega^1_{O/\mathbf C}\otimes_O O/K,
 \qquad
 [g]\longmapsto dg\pmod {K\Omega^1_O}. \tag{1}
\]

This is well-defined because

\[
 d(K^2)\subseteq K\Omega^1_O.
\]

It is \(O/K\)-linear: for \(a\in O\) and \(g\in K\),

\[
 d(ag)=a\,dg+g\,da\equiv a\,dg\pmod {K\Omega^1_O}. \tag{2}
\]

## Exact obstruction theorem

Choose analytic coordinates \(u_1,\ldots,u_q\) on \(F_B\). Then

\[
 dg=\sum_{j=1}^q\partial_{u_j}(g)\,du_j.
\]

Since \(\Omega^1_O\) is free on the \(du_j\), equation (1) gives

\[
 \beta_K=0
 \Longleftrightarrow
 \partial_{u_j}K\subseteq K\quad\text{for every }j. \tag{3}
\]

B178 turns (3) into

\[
 \boxed{
 \beta_{K_B}=0
 \Longleftrightarrow
 K_B=0
 \Longleftrightarrow
 H_\tau=0.
 } \tag{4}
\]

Thus \(\beta_{K_B}\) is not merely a first-order tangent map at the
origin. It is an \(O/K_B\)-linear morphism over the complete analytic
escape subscheme and records derivatives to every analytic order.

## Explicit high-order value

For \(O=\mathbf C\{y\}\) and \(K_m=(y^m)\),

\[
 \beta_{K_m}([y^m])
 =m y^{m-1}dy\pmod {y^m}. \tag{5}
\]

This is nonzero for every \(m\ge2\), but its coefficient vanishes to
order \(m-1\). Hence the obstruction can be invisible to an arbitrarily
long prescribed finite jet while remaining nonzero as a conormal
morphism.

## Gate interpretation

G111's proposed connection comparison must prove literal vanishing of
(1), not only vanishing on the central fiber or to a bounded order. Once
that is achieved, (4) closes the analytic persistence clause. Every
Hodge detector requirement remains separate.
