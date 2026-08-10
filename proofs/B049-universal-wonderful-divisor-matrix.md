---
brick_id: B049
status: PROVED
base_field: C
variety: the projectivized exceptional fiber of the wonderful resolution of an arbitrary central representable hyperplane arrangement for any building set of flats
smoothness: all building centers and iterated blow-ups are smooth, and the final boundary is simple normal crossing
projectivity: the fiber begins as projective space and every blow-up is projective, so the wonderful fiber is smooth projective
dimension: arbitrary arrangement rank d at least 2, with wonderful fiber dimension d-1
codimension: blown projective flats have codimension at least 2 in the fiber; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational Betti H^2, Picard groups, and the divisor-class component of the logarithmic residue complex
hodge_type: h and all boundary divisor classes have type (1,1); no full coefficient Hodge theorem is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no downstream algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B044-B048, G019-G021, NG035, and Li S038
claim: For every representable central arrangement, every building set, and every Li-permissible blow-up order, the intrinsically labelled boundary classes together with h form a basis of H^2, every strict branch has class h minus the sum of boundary classes over contained building flats, and the geometric residue matrix is order-independent and triangular.
falsifier: failure of the blow-up H^2 decomposition for a smooth connected center of codimension at least two, a multiplicity other than one in an inclusion-order branch pullback, failure of Li's canonical model to preserve the map and labelled boundary, or a permissible-order counterexample to the intrinsic divisor formula
---

# B049 - Universal wonderful divisor matrix

This brick proves G021. It also records why NG035 forces intrinsic boundary
labels rather than raw exceptional coordinates.

## Setup and notation

Let \(H_1,\ldots,H_r\) be a central representable arrangement in
\(\mathbf C^d\). After blowing up the origin, work on
\(E_0=\mathbf P^{d-1}\). Let \(\mathcal B\) be any building set of
positive-dimensional flats of arrangement codimension at least two; the
hyperplanes themselves are already divisors and are not blow-up centers.
Write \(D_F\) for the final boundary divisor intrinsically indexed by
\(F\in\mathcal B\), as in Li Theorem 1.2, and put \(e_F=[D_F]\).

## Degree-two blow-up lemma

If \(q:\operatorname{Bl}_Z Y\to Y\) blows up a smooth connected center of
codimension \(c\ge2\), then

\[
 H^2(\operatorname{Bl}_Z Y,\mathbf Q)
 =q^*H^2(Y,\mathbf Q)\oplus\mathbf Q[E].
\]

Indeed, outside degree zero on \(Z\), the projective-bundle fiber contributes
nothing to total degree two. The only new Leray class is the fiber
hyperplane in \(H^0(Z,\mathbf Q)(-1)\), represented by \(-[E]\). Pullbacks
restrict trivially to a line in a fiber of \(E\to Z\), whereas \([E]\)
restricts as \(\mathcal O_{\mathbf P^{c-1}}(-1)\); hence the sum is direct.

Choose an inclusion-compatible wonderful order, blowing smaller geometric
flats before larger ones. Every center is an iterated blow-up of a projective
linear flat along its proper building subflats. Its dimension is unchanged,
so its codimension in the ambient fiber remains its original value, at least
two. It is connected. Repeated application of the lemma gives

\[
 H^2(E_{\mathcal B},\mathbf Q)
 =\mathbf Qh\oplus\bigoplus_{F\in\mathcal B}\mathbf Qe_F.
\]

In this order, a later center containing an earlier flat meets the earlier
exceptional divisor transversally rather than lying in it; incomparable
centers either separate after their building factors are blown up or retain
a clean non-containment intersection. This is Li Lemma 2.9 applied at each
minimal-center step. Consequently the raw exceptional divisor created at
the \(F\)-step is already the final \(D_F\).

## Multiplicity-one branch formula

Fix a branch hyperplane \(H_i\). At the step for \(F\), its current strict
transform contains the center exactly when \(F\subset H_i\). This can be
checked over the dense open subset of \(F\) obtained by deleting its proper
building subflats, where all earlier blow-ups are isomorphisms.

When a smooth Cartier divisor \(D=(x_1=0)\) contains a smooth center
\(Z=(x_1,\ldots,x_c)=0\), its pullback to \(\operatorname{Bl}_Z Y\) is

\[
 q^*D=\widetilde D+E.
\]

The coefficient is one because \(x_1\) has order one in the ideal of \(Z\).
If the center is not contained in \(D\), there is no exceptional component.
Starting from \([H_i]=h\) and iterating proves

\[
 [\widetilde H_i]
 =h-\sum_{\substack{F\in\mathcal B\\F\subset H_i}}e_F.
\]

## Arbitrary permissible orders

The preceding calculation used one order, but its objects are intrinsic.
Li Definition 1.1 defines \(E_{\mathcal B}\) as a closure with its morphism
to \(E_0\); Theorem 1.2 labels the boundary divisor \(D_F\) for every
building element; and Theorem 1.3 identifies every permissible iterated
blow-up order with that same wonderful compactification. Therefore the
pullback \(h\), the divisors \(D_F\), and every strict branch closure are
preserved by the canonical comparison. The basis and branch formula transfer
to every permissible order.

NG035 explains why this conclusion cannot be phrased using raw exceptional
classes at their creation steps. If a larger center is blown first, the
dominant transform of a contained smaller flat may lie in that exceptional
divisor. Later blowing it changes the earlier strict boundary class. The
change from raw coordinates to the intrinsic \((e_F)\) coordinates is
integral triangular; the formula above is in the latter basis.

## Geometric residue matrix

Suppose the degree-one logarithmic coefficient sheaf supplies a branch
coefficient \(a_i\delta_i\) and an exceptional coefficient
\(w_F\in W_F\) on \(D_F\). Weighting these coefficients by their divisor
classes and using the proved formula gives

\[
 h\otimes\sum_i a_i\delta_i
 +\sum_{F\in\mathcal B}e_F\otimes
 \left(w_F-\sum_{F\subset H_i}a_i\delta_i\right).
\]

Because \(h,(e_F)\) are independent, the geometric matrix is triangular and
order independent. Its equations are the global relation plus one assignment
of a partial sum to each exceptional coefficient.

## Scope guard

B049 proves the divisor geometry, not the antecedent “suppose” in the last
section. It does not prove that an arbitrary wonderful incidence has exactly
the coefficient rows \(W_F\), exclude higher local-complex cohomology, audit
all strict supports, or establish the full rational type-\((0,0)\) channel.
Those are G022 and G019. No algebraic cycle is constructed, and actual
progress toward the standard rational Hodge Conjecture remains zero.
