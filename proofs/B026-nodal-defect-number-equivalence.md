---
brick_id: B026
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n with a sufficiently ample line bundle L and a nodal hypersurface member Y_0 in |L| with node scheme Delta
smoothness: X is smooth; Y_0 has only ordinary double points; a nearby fiber and the canonical desingularization of Y_0 are used
projectivity: X, Y_0, and the degeneration are projective
dimension: dim_C X = 2n and dim_C Y_0 = 2n-1
codimension: Y_0 has codimension 1 in X; the ambient Hodge application has middle codimension n
coefficient_field: Q for singular homology and local intersection cohomology; C for coherent cohomology and Hodge-number dimensions
cohomology_theory: singular homology and cohomology, vanishing cycles, limit mixed Hodge structures, local intersection cohomology, coherent sheaf cohomology of the adjoint node ideal, and desingularization cohomology
hodge_type: nodal rational relations have type (0,0) after Tate twist; the dimension comparison does not identify a prescribed Hodge direction
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraic cycle for the input Hodge class is assumed or constructed
cycle_equivalence: rational equivalence
scope: fiberwise
dependencies: Saito Proposition 1 and Theorem 1 (S022), Schoen Proposition 1.3 (S020), the non-rho(ii) components of Green-Griffiths Section 4.2.4 (S021), B009-B010, and the source-conflict audit B031
claim: Under the audited nodal hypotheses, the vanishing-cycle relation dimension equals the extra homology dimension and the stated adjoint, local-intersection-cohomology, and desingularization defect dimensions; the canonical map from extra homology to primitive ambient homology is a separate map whose rank is not included in this claim.
falsifier: nodal data satisfying the stated hypotheses for which the relation, extra, adjoint, local-IC, or stated desingularization dimensions differ
---

# B026 - Nodal defect dimensions and the separate ambient map

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L\) be
sufficiently ample in the sense used in Green-Griffiths Section 4.2.4, and
let \(Y_0\in|L|\) have only nodes with reduced node scheme \(\Delta\). For a
nearby smooth member \(Y_\infty\), define

\[
\begin{aligned}
 R(Y_0)&=\ker\!\left(
   \bigoplus_y H_{2n-1}(Z_{y,\infty},\mathbf Q(n))
   \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n))\right),\\
 E^\vee(Y_0)&=\operatorname{coker}\!\left(
   H_{2n}(Y_\infty,\mathbf Q(n))
   \longrightarrow H_{2n}(Y_0,\mathbf Q(n))\right).
\end{aligned}
\]

Saito's exact sequence gives a canonical isomorphism between the unipotent
type-\((0,0)\) part of \(R(Y_0)\) and the corresponding extra Hodge cycles in
\(E^\vee(Y_0)\). For nodes, every rational relation has this type. Under the
Green-Griffiths quasi-local nodal hypotheses, B009/B134 identify the
cohomological local intersection-cohomology channel with the dual relation
space, hence with the same dimension and Tate type.

Saito proves the first equality. Schoen Proposition 1.3 gives a canonical
isomorphism between the adjoint coherent defect and the desingularized excess
space under the displayed vanishing hypotheses. B009 supplies the quasi-local
intersection-cohomology identification. These results triangulate the
non-\(\rho(ii)\) components printed in the Green–Griffiths nodal defect
theorem and give the numerical equalities

\[
 \dim_{\mathbf Q}R(Y_0)
 =\dim_{\mathbf Q}E^\vee(Y_0)
 =h^1\!\left(X,I_\Delta\otimes K_X\otimes L^n\right)
 =\dim_{\mathbf Q}H^1(B^\bullet),
\]

together with the two stated desingularization/Hodge-number defect formulas.
For \(L\gg0\), the coherent group is the failure of the nodes to impose
independent conditions on \(H^0(X,K_X\otimes L^n)\).

## The ambient map is a separate rank

There is a canonical morphism

\[
 \Phi_{Y_0}:E^\vee(Y_0)
 \longrightarrow H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}.
\]

For a relation \(\beta\), Saito's class is
\(\gamma_\beta=\Phi_{Y_0}(\beta)\). Neither Saito's theorem nor the coherent
defect calculation says that \(\Phi_{Y_0}\) is injective. Consequently

\[
 \dim\operatorname{im}\Phi_{Y_0}
 \le \dim E^\vee(Y_0)
\]

can be strict. B031 gives a nodal plane-quintic example where the right side
is one and the left side is zero.

## Quarantined source conflict

Green–Griffiths page 18 explicitly defines its printed \(\rho(ii)\) as the
dimension of the image of
\(H_{2n}(Y_0)\to H_{2n}(X)_{\mathrm{prim}}\), and page 19 prints equality
with the other five invariants. B031 gives plane-containing nodal
hypersurfaces in \(\mathbf P^4\) of arbitrarily high degree for which the
relation and extra-homology dimensions are one and the primitive ambient
target is zero.

Thus the literal \(\rho(i)=\rho(ii)\) component conflicts with a direct
primary-source-backed family calculation; high ampleness does not remove
the conflict. The source itself is an extended research announcement and
says that complete details of some results were not yet written. NG-028
quarantines the ambient-image component. This brick uses only the
non-\(\rho(ii)\) comparisons that are independently triangulated above and
does not claim a resolution of the printed statement.

## What the equality does and does not give

A positive adjoint defect proves that a nonzero relation and a nonzero extra
homology class exist. It does **not** prove that any relation has nonzero
primitive ambient image, much less that

\[
 \langle\zeta,\gamma_\beta\rangle\ne0
\]

for a specified primitive Hodge class \(\zeta\). G013 must control both the
rank of \(\Phi_{Y_0}\) and the selected pairing; these conditions are not
encoded by the two evaluation matroids.

## Scope guard

No special-family defect is counted as progress toward arbitrary varieties.
The theorem starts with a selected nodal member and does not construct it
from \(\zeta\). It is a dimension comparison plus a type separation, not an
algebraic-cycle construction.
