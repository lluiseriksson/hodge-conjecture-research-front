---
brick_id: B163
status: PROVED
base_field: C
variety: a proper projective hypersurface family g:Y_B->F_B over a smooth basis-node germ, with N exhaustive disjoint tracked ordinary-double-point charts
smoothness: the basis germ and ambient variety are smooth; every tracked Hessian is nondegenerate; no other singularities occur
projectivity: g is projective and obtained by proper base change from the complete-linear-system hypersurface family
dimension: hypersurface dimension r=2n-1 in the Hodge application; basis germ dimension arbitrary; cotangent bundle dimension twice that base dimension
codimension: the basis germ has codimension R in the parameter space; zero internal microsupport forces all N-R extra node branches to contain it
coefficient_field: Q
cohomology_theory: rational constructible derived categories, proper base change, microsupport, Milnor fibers, and analytic local triviality
hodge_type: none asserted by the microsupport criterion; the specified detector type remains a separate downstream condition
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or specified pairing is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B158-B162, S030, S052, S066, and parameterized Morse/Ehresmann triviality
claim: Let K_B=Rg_*Q_(Y_B). Under exhaustive tracked-Morse control, the following are equivalent: every tracked node persists on F_B; K_B has locally constant cohomology sheaves; and SS(K_B) is contained in the zero section of T^*F_B. If a node escapes, B162 detects nonlocal constancy on an arc, and the zero-section criterion then forces nonzero microsupport.
falsifier: a persistent tracked-Morse family with nonlocal proper direct image, a locally constant K_B with changing Euler characteristic, a zero-microsupport constructible complex that is not locally constant, or an escaping node invisible to microsupport
---

# B163 — Node persistence is zero internal microsupport

Let

\[
 g:\mathcal Y_B\longrightarrow F_B
\]

be the restriction of the proper hypersurface family to a smooth basis-node
germ, with B160's exhaustive disjoint Morse charts. Put

\[
 K_B=Rg_*\mathbf Q_{\mathcal Y_B}\in D_c^b(F_B,\mathbf Q).
\]

## Persistence implies local constancy

Suppose every tracked critical value vanishes on \(F_B\). The
parameterized holomorphic Morse lemma identifies each singular chart with
the product family \(q_i(z)=0\). On the complement of the Milnor balls,
proper submersion and Ehresmann give a locally trivial family. The common
boundary fibrations are locally trivial as well. Mayer--Vietoris gluing
therefore makes every cohomology sheaf of \(K_B\) locally constant.

Conversely, suppose \(K_B\) has locally constant cohomology sheaves. Proper
base change identifies its derived stalk at \(t\) with
\(R\Gamma(Y_t,\mathbf Q)\), so the topological Euler characteristic
\(\chi(Y_t)\) is locally constant. B160 then forces all \(N\) tracked nodes
to persist. Thus

\[
 \text{all nodes persist}
 \quad\Longleftrightarrow\quad
 K_B\text{ is locally constant}. \tag{1}
\]

Here “locally constant” for a derived constructible object means that all
its cohomology sheaves are local systems.

## Microsupport criterion

Kashiwara--Schapira Proposition 5.4.5, audited in S066, gives

\[
 K_B\text{ is locally constant}
 \quad\Longleftrightarrow\quad
 SS(K_B)\subseteq T^*_{F_B}F_B, \tag{2}
\]

where the right side is the zero section of \(T^*F_B\).

Equations (1)--(2) produce the exact microlocal certificate

\[
 H_\tau=0
 \quad\Longleftrightarrow\quad
 SS(K_B)\subseteq T^*_{F_B}F_B. \tag{3}
\]

For the reverse obstruction, if a node escapes, B162 chooses an analytic
arc with a nonzero rank-one local specialization group. Hence \(K_B\) is
not locally constant. The contrapositive of (2), rather than an unproved
identification of that arc with a particular covector, then gives a
nonzero covector in \(SS(K_B)\).

## Scope guard

This is the microsupport **inside** \(F_B\) after proper base change. It is
not the claim that the ambient direct image over the complete linear system
has zero microsupport; that object necessarily detects the discriminant.
Nor does (3) construct or preserve the specified Saito relation pairing.
