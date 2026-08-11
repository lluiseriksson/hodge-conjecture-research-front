---
brick_id: B167
status: PROVED
base_field: C
variety: a smooth complete-linear-system parameter manifold P, a smooth closed basis germ i:F_B->P, and a rational constructible complex K on P
smoothness: P and F_B are smooth; no transversality or non-characteristic hypothesis is imposed on i
projectivity: in the Hodge application K=Rh_*Q for the projective universal hypersurface map; the inverse-image estimate itself is analytic
dimension: arbitrary dimensions dim P=d and dim F_B=b; microsupports are conic subsets of the corresponding cotangent bundles
codimension: F_B has codimension R; i-sharp records limiting characteristic directions modulo the normal geometry of this embedding
coefficient_field: Q
cohomology_theory: rational constructible derived categories, microsupport, microlocal inverse image, proper base change, and perverse characteristic cycles
hodge_type: none asserted; the specified rational type-(0,0) relation functional remains separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream
cycle_equivalence: rational equivalence
scope: relative
dependencies: B163-B166, S052, S066-S068
claim: For the closed embedding i:F_B->P, Kashiwara-Schapira's microlocal inverse-image estimate gives SS(i^(-1)K) contained in i-sharp SS(K). Therefore i-sharp SS(K) contained in the zero section of T^*F_B is sufficient for local constancy of the full base-changed direct image and hence, under B163's exhaustive tracked-Morse hypotheses, for persistence of every node.
falsifier: a closed embedding and constructible K with an internal microsupport covector outside i-sharp SS(K), or a zero i-sharp image whose inverse image is not locally constant
---

# B167 — The full normal-cone pullback is a persistence certificate

Let \(i:F_B\hookrightarrow P\) be a closed embedding of smooth analytic
germs and \(K\in D_c^b(P,\mathbf Q)\). Kashiwara--Schapira attach to a
closed conic subset \(C\subset T^*P\) its microlocal inverse image
\(i^\#C\subset T^*F_B\). Corollary 6.4.4 gives

\[
 SS(i^{-1}K)\subseteq i^\#SS(K). \tag{1}
\]

This statement requires neither ordinary transversality nor the
non-characteristic condition. The normal-cone operation is essential
precisely when \(i\) is characteristic.

For the universal hypersurface map \(h:\mathcal U\to P\), proper base
change identifies

\[
 i^{-1}Rh_*\mathbf Q_{\mathcal U}
 \simeq Rg_*\mathbf Q_{\mathcal U\times_PF_B}=K_B. \tag{2}
\]

Consequently

\[
 i^\#SS(Rh_*\mathbf Q_{\mathcal U})
 \subseteq T^*_{F_B}F_B
 \quad\Longrightarrow\quad
 SS(K_B)\subseteq T^*_{F_B}F_B. \tag{3}
\]

B163 then converts (3), under exhaustive tracked-Morse control, into
persistence of all nodes. B165 converts the same conclusion into vanishing
of every off-zero positive perverse characteristic multiplicity.

## Higher-discriminant envelope

The universal incidence \(\mathcal U\) and the base \(P\) are smooth and
\(h\) is projective. Migliorini--Shende Theorem C describes
\(h^\dagger(0_{\mathcal U})\) as the union of conormals to the
codimension-\(a\) components of the higher discriminants
\(\Delta^a(h)\), while their equation (2.2) gives

\[
 SS(Rh_*\mathbf Q_{\mathcal U})
 \subseteq h^\dagger(0_{\mathcal U}). \tag{4}
\]

Thus the stronger envelope condition
\(i^\#h^\dagger(0_{\mathcal U})\subseteq0_{F_B}\) is sufficient for (3).
It is not necessary: the envelope can contain conormals that do not occur
in the actual sheaf microsupport.

## Scope guard

B167 is a sufficient microlocal criterion. It neither proves its
class-directed realization nor preserves the specified Saito pairing by
itself.
