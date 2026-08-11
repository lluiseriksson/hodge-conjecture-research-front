---
brick_id: B162
status: PROVED
base_field: C
variety: a proper projective hypersurface family restricted to a smooth basis-node germ, with N disjoint tracked ordinary-double-point charts and no other singularities
smoothness: the ambient variety and basis germ are smooth; each tracked spatial Hessian is nondegenerate; singularities are isolated and exhaustive
projectivity: the hypersurface family is projective; the local equivalence uses proper specialization and disjoint Milnor balls
dimension: hypersurface dimension r=2n-1 in the Hodge application; basis germ dimension arbitrary; N tracked nodes
codimension: the basis germ has codimension R in the full linear system; vanishing of every arcwise escape complex forces the N-R extra branches to contain it
coefficient_field: Q for vanishing-cycle groups; C for analytic arcs and critical values
cohomology_theory: rational nearby and vanishing cycles, proper base change, Milnor fibers, analytic curve selection, and critical-value deformation theory
hodge_type: no type assertion is made for the persistence certificate; the downstream detector must separately retain rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or specified pairing is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B025, B158-B160, S030, S052, and analytic curve selection
claim: For every analytic arc gamma in a basis-node germ, the local specialization cone is the direct sum of one rank-one middle-degree vanishing-cycle group for each tracked node whose critical value is not identically zero on gamma. Therefore all extra nodes persist on the basis germ if and only if every arcwise vanishing-cycle complex is zero; it suffices to test arcs because a nonzero analytic escape component is detected by an analytic curve.
falsifier: an escaping Morse node with zero arcwise vanishing-cycle group, a persistent Morse node contributing a nonzero relative group, cancellation between disjoint point-supported local groups, or a nonzero analytic escape germ invisible on every analytic arc
---

# B162 — Arcwise vanishing cycles exactly detect node escape

Retain B160's proper family and exhaustive disjoint Morse charts over a
smooth basis-node germ \(F_B\). Let

\[
 \gamma:(\Delta,0)\longrightarrow(F_B,0)
\]

be an analytic arc. For each tracked node define

\[
 E_\gamma=
 \{i:\tau_i\circ\gamma\text{ is not identically zero}\}.
\]

After possibly replacing \(\Delta\) by a punctured subdisk, precisely the
nodes indexed by \(E_\gamma\) are absent from the generic fiber of the
pulled-back family.

## Local specialization cone

The parameterized holomorphic Morse lemma gives the \(i\)-th chart as

\[
 q_i(z)+\tau_i(\gamma(t))=0
\]

with \(q_i\) nondegenerate. If \(\tau_i\circ\gamma\equiv0\), this is a
topologically constant singular chart and contributes no relative
vanishing cycle. If it is nonzero, the generic chart is the Milnor fiber of
one ordinary double point. S030 identifies its reduced middle cohomology
with \(\mathbf Q\) and all other reduced cohomology with zero.

Because the Milnor balls are disjoint, the local specialization cone is
point-supported and splits canonically as

\[
 \Phi_\gamma\simeq
 \bigoplus_{i\in E_\gamma}(V_i)_{p_i}[-r],
 \qquad \dim_{\mathbf Q}V_i=1. \tag{1}
\]

The decomposition by distinct supports is canonical; identifying an
individual \(V_i\) with a specified copy of \(\mathbf Q\) requires an
orientation choice. Up to the displayed ordinary-cohomology convention,

\[
 \dim_{\mathbf Q}\mathbb H^r(\Phi_\gamma)=|E_\gamma|,
 \qquad
 \chi(\Phi_\gamma)=(-1)^r|E_\gamma|. \tag{2}
\]

Formula (2) is B160's Euler jump. It also shows that no global relation
among vanishing cycles can cancel the persistence test: the complex is a
direct sum over distinct point supports before any map to ambient
cohomology.

## Arc criterion

If every node persists on \(F_B\), each \(\tau_i|_{F_B}\) is zero and
\(\Phi_\gamma=0\) for every arc.

Conversely, suppose an escape component
\(\epsilon_{B,i}=\tau_i|_{F_B}\) is nonzero. Analytic curve selection gives
an arc \(\gamma\) on which
\(\epsilon_{B,i}\circ\gamma\not\equiv0\). Then \(i\in E_\gamma\), so (1)
makes \(\Phi_\gamma\ne0\). Hence

\[
 \left(\forall\gamma,\ \Phi_\gamma=0\right)
 \quad\Longleftrightarrow\quad
 \epsilon_B\equiv0
 \quad\Longleftrightarrow\quad
 H_\tau=0. \tag{3}
\]

The last equivalence is B158. Thus G102 may be attacked by proving
arcwise vanishing-cycle triviality, a condition compatible with
sheaf-theoretic and Hodge-module tools.

## Scope guard

The direct sum (1) uses isolated tracked Morse charts and exclusion of all
other singularities. It is the local specialization cone, not an assertion
that the corresponding cycles inject independently into the cohomology of
a global smooth fiber. B162 proves persistence only and does not supply the
specified Saito pairing.
