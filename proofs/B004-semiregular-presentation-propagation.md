---
brick_id: B004
status: PROVED
base_field: C
variety: smooth projective family f:X->T with a finite tuple of lci anchor cycles
smoothness: f smooth; T smooth irreducible; each anchor cycle lci (smooth submanifolds in Ran's cited formulation)
projectivity: f projective; relative Hilbert schemes projective over T
dimension: arbitrary relative dimension n
codimension: fixed q for every anchor cycle
coefficient_field: Q for cycles and Betti classes; C for deformation-obstruction groups
cohomology_theory: relative singular Betti cohomology plus coherent/de Rham semiregularity groups
hodge_type: prescribed flat class fiberwise of type (q,q)
cycle_class_map: CH^q(X_t)_Q -> H^{2q}(X_t,Q(q))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B002; Ran Theorem 0; Buchweitz-Flenner Theorems 5.2 and 7.8-7.10 (S017-S018)
claim: An anchored rational Hodge class with an injectively combined semiregular lci presentation is algebraic on every fiber of the connected base.
falsifier: a small-extension obstruction tuple in the kernel of the combined semiregularity map despite its injectivity, or a fiber missed by the resulting proper Hilbert component
---

# B004 - Semiregular-presentation propagation

## Statement

Let \(f:\mathcal X\to T\) be a smooth projective morphism with \(T\) smooth
and irreducible over \(\mathbf C\). Let
\(\alpha\) be a flat rational section of \(R^{2q}f_*\mathbf Q(q)\) that is of
type \((0,0)\), equivalently untwisted type \((q,q)\), at every point.

Fix \(t_0\in T\). Assume that there are codimension-\(q\) lci subschemes
\(Z_1,\ldots,Z_r\subset X_{t_0}\), integers \(a_i\), and an integer \(N>0\)
such that

\[
 N\alpha_{t_0}=\sum_{i=1}^r a_i[Z_i]
 \quad\text{in }H^{2q}(X_{t_0},\mathbf Q(q)).
\]

For each \(i\), write

\[
 \sigma_i:H^1(Z_i,N_{Z_i/X_{t_0}})
 \longrightarrow H^{q+1}(X_{t_0},\Omega_{X_{t_0}}^{q-1})
\]

for Bloch's semiregularity map. Assume the combined map

\[
 \Sigma_{\mathbf a}:\bigoplus_i H^1(Z_i,N_{Z_i/X_{t_0}})
 \longrightarrow H^{q+1}(X_{t_0},\Omega_{X_{t_0}}^{q-1}),
 \qquad (v_i)_i\longmapsto\sum_i a_i\sigma_i(v_i)
\]

is injective. Then for every \(t\in T\), the class \(\alpha_t\) lies in the
image of \(CH^q(X_t)_{\mathbf Q}\).

## Proof

Take the fiber product over \(T\) of the relative Hilbert schemes with the
Hilbert polynomials of the \(Z_i\), and let \(h=(Z_i)_i\) be the anchor point.
Its small-extension obstruction space at \(h\) is the direct sum of the
embedded obstruction spaces; for lci cycles these lie in
\(\bigoplus_i H^1(Z_i,N_{Z_i/X_{t_0}})\).

Ran's Theorem 0(ii) identifies the image of each relative obstruction under
\(\sigma_i\) with the Hodge obstruction to transporting \([Z_i]\). By
linearity, the image of an obstruction tuple under \(\Sigma_{\mathbf a}\) is
the Hodge obstruction to transporting \(\sum_i a_i[Z_i]\). This sum is the
flat class \(N\alpha\), which remains Hodge on \(T\); hence that image is zero.
Injectivity of \(\Sigma_{\mathbf a}\) makes the obstruction tuple zero for
every Artin-local small extension. The product Hilbert morphism is therefore
formally smooth at \(h\), and, being locally of finite presentation over
\(\mathbf C\), is smooth at \(h\). In particular its differential is
surjective and its source is smooth at \(h\).

B002 applies. The irreducible component through \(h\) is proper over \(T\),
contains an open image, and therefore surjects onto irreducible \(T\). On its
universal families the flat class of \(\sum_i a_i Z_i\) agrees at \(h\) with
\(N\alpha\), hence agrees everywhere on the component. Every fiber thus has a
rational cycle

\[
 \frac1N\sum_i a_i Z_{i,t}
\]

with Betti class \(\alpha_t\). QED.

## Adversarial scope audit

- Negative \(a_i\) are allowed because the conclusion concerns rational
  cycles, while the parameter space separately carries each effective
  subscheme \(Z_i\).
- Injectivity of every \(\sigma_i\) separately does **not** imply injectivity
  of \(\Sigma_{\mathbf a}\); cancellation between components is a real issue.
- The theorem begins with an algebraic anchor presentation and therefore does
  not discharge G001.
- No theorem here asserts that every algebraic class has an lci presentation
  satisfying the combined injectivity hypothesis. That is G004.
- The conclusion is fiberwise algebraicity on this one family/base. It becomes
  general-HC progress only if the separate universal anchor and presentation
  gates are proved.

