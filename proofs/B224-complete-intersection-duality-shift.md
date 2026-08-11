---
brick_id: B224
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X and a transverse reduced zero-dimensional complete intersection Z of divisors with line bundles L_1,...,L_d
smoothness: X and every divisor meet transversely, so Z is reduced and Gorenstein; no nodal hypersurface or G149 incidence is produced
projectivity: X, the divisors, Z, and all restricted line bundles are projective
dimension: dim X=d; Z has dimension zero; the Hodge branch has d=2n
codimension: Z is a codimension-d complete intersection; its residue-dual complement to H^2 has the adjunction twist omega_X tensor L_1 tensor ... tensor L_d tensor H^(-2)
coefficient_field: C for adjunction, trace, and evaluation pairings
cohomology_theory: dualizing sheaves, Koszul adjunction, Grothendieck trace for a reduced Gorenstein zero-scheme, and coherent restriction
hodge_type: none asserted; residue duality alone has no rational type-(0,0) conclusion
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B223, G149, S070
claim: If Z is a transverse complete intersection of D_i in |L_i|, then omega_Z=(omega_X tensor product_i L_i)|_Z and the canonical trace-dual fiber system to H^2|_Z is (omega_X tensor product_i L_i tensor H^(-2))|_Z. If every L_i=H^(e_i), this canonical system equals the restriction of H^(m-2) via an ambient line-bundle identity only if omega_X tensor H^(sum e_i-m) is trivial.
falsifier: a transverse complete intersection with a different adjunction dualizing sheaf or a canonical ambient identification with H^(m-2) while omega_X tensor H^(sum e_i-m) is nontrivial
---

# B224 — Complete-intersection duality has a fixed canonical shift

Let

\[
Z=D_1\cap\cdots\cap D_d,\qquad D_i\in|L_i|
\]

be transverse and zero-dimensional on the smooth \(d\)-fold \(X\).
Koszul adjunction gives

\[
\omega_Z\simeq
\left(\omega_X\otimes L_1\otimes\cdots\otimes L_d\right)|_Z. \tag{1}
\]

For every line bundle \(M\), the trace pairing on the reduced Gorenstein
scheme \(Z\) is perfect:

\[
H^0(Z,M|_Z)\times
H^0(Z,\omega_Z\otimes M^{-1}|_Z)
\longrightarrow\mathbf C. \tag{2}
\]

Taking \(M=H^2\), the canonical residue-dual fiber system is therefore

\[
\left(\omega_X\otimes L_1\otimes\cdots\otimes L_d
\otimes H^{-2}\right)|_Z. \tag{3}
\]

If \(L_i=H^{e_i}\) and \(E=\sum e_i\), then (3) is

\[
(\omega_X\otimes H^{E-2})|_Z. \tag{4}
\]

To identify (4) with \(H^{m-2}|_Z\) by an identity of ambient line
bundles—the input needed for a canonical theorem on global evaluation
codes—one needs

\[
\omega_X\otimes H^{E-m}\simeq O_X. \tag{5}
\]

S070 exhibits the same non-negotiable shift in projective space:
for a complete intersection of degrees \(d_i\), its complementary degree
is \(s-a\), where \(s=\sum d_i-d-1\).

Condition (5) is not universal. Take

\[
X=\mathbf P^n\times\mathbf P^n,\quad n\ge2,\qquad
A=O(1,2),\qquad H=A^2=O(2,4).
\]

Here \(\omega_X=O(-n-1,-n-1)\). If (5) held with \(q=E-m\), then

\[
-n-1+2q=0,\qquad -n-1+4q=0,
\]

which is impossible. This is a legitimate primitive Hodge setting:
the middle primitive space for \(A\) has dimension
\(b_{2n}-b_{2n-2}=1\), is rational, and all cohomology classes on the
product are algebraic.

B224 does not say that no specially engineered point scheme can satisfy
B223. It proves that the standard complete-intersection residue theorem
does not canonically target the required complementary H-power on every
input.
