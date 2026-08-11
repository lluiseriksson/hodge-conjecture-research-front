---
brick_id: NG153
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold, a fixed finite ordered point set, and sufficiently high powers of an ample line bundle
smoothness: the ambient variety is smooth and prescribed nondegenerate quadratic jets can produce ODPs; no excess-incidence smoothness follows
projectivity: the ambient variety, line bundle powers, and complete linear systems are projective
dimension: N fixed points, N value lines, and N gradient blocks of dimension 2n
codimension: full first-jet separation makes value evaluation surjective and supplies every node-supported gradient direction, so the augmented annihilator is zero
coefficient_field: C for coherent jets and Hessian linear algebra; Q detector data are not produced
cohomology_theory: Serre vanishing, coherent finite-jet evaluation, and ODP second-order deformation theory
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic representative or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: S065, B157, B188-B190, G119-G122
claim: Realize a synchronized augmented defect in a chosen small projective or analytic subfamily after making the line bundle sufficiently positive, and count that defect as a property of the full complete-linear-system incidence.
falsifier: surjectivity of full first-jet evaluation makes E surjective and the conditional-gradient image equal to the entire direct sum, while the chosen restricted subfamily can still have the desired synchronized image
---

# NG153 — High positivity destroys a restricted-family augmented defect

- **Route:** fix the prospective nodes, raise an ample line bundle to a
  sufficiently high power, prescribe conformally synchronized jets in a
  selected small family, and count B190's rank defect for the surrounding
  full complete linear system.
- **Valid input:** S065 makes prescribed finite jets available. B157 uses
  this correctly to realize arbitrary critical-value germs on a nonlinear
  pullback with fixed nondegenerate Hessians.
- **Invalid inference:** a rank defect of the chosen pullback or linear
  subfamily remains a rank defect after all global sections are restored.

Let \(Z=\{p_1,\ldots,p_N\}\) be fixed. For a sufficiently high power,
Serre vanishing makes the full first-jet evaluation

\[
 H^0(X,L^k)\longrightarrow
 \bigoplus_i\left(L^k|_{p_i}\oplus
 T_{p_i}^*X\otimes L^k|_{p_i}\right) \tag{1}
\]

surjective. Therefore the value map \(E\) is already surjective, so
\(R=N\), \(S=\mathcal T\), and

\[
 L_U=(S+H(U))^\perp=0. \tag{2}
\]

Moreover, restricting (1) to value-zero sections shows that the full
conditional-gradient image is

\[
 U=\bigoplus_iG_i. \tag{3}
\]

For every \(i\), sections exist whose only nonzero gradient is an arbitrary
element of \(G_i\). Hence B189's isolated-gradient image equals \(G_i\),
has dimension \(2n>n\), and its nondegenerate Hessian pairing spans the
value line \(\mathcal T_i\). Thus the full system fails both the value
defect and the nodewise axis-avoidance filter.

A selected subspace of sections may still have the synchronized graph of
B190, but its conditional-gradient image is not the image of the full
universal incidence. Adding the omitted sections changes \(U\), \(H(U)\),
and \(A_U\); the desired defect disappears.

- **Precise obstruction:** fixed-point high-power jet separation is
  antagonistic to G121/G122, not a construction mechanism for them.
- **Re-entry condition:** the support and its special geometry must vary
  with the line bundle so that first-jet superabundance is intrinsic to the
  full complete system. That full system must satisfy B189 at every node
  and B190's global synchronization, while retaining the rational detector
  and specified pairing.
