---
brick_id: G123
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system ordered-node incidence of an arbitrary polarized smooth projective complex 2n-fold with a specified primitive rational middle Hodge class
smoothness: the ambient variety and tracked singularities are smooth/ODP; the final simultaneous-node germ must be reduced and smooth
projectivity: the reduced and doubled node schemes, line bundle, complete linear system, and detector family are projective
dimension: N nodes, value rank R<N, full conditional-gradient quotient V of dimension q<=2n, and a rank-one Hessian tensor in the N-dimensional value target
codimension: impose one-node determination at every node and force the intrinsic Hessian tensor's value factor into the no-coloop value image
coefficient_field: C for coherent jets and Hessian tensors; Q for the input Hodge class, vanishing-cycle detector, and specified pairing
cohomology_theory: coherent first-jet interpolation, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B191, G013, G090-G122, and NG106-NG154
claim: Construct from arbitrary (X,zeta) full-incidence ordered ODP data satisfying every one-node determination equality of B191 and having nonzero rank-one intrinsic Hessian tensor whose value factor lies in a rank-R no-coloop value image, while retaining positive adjoint defect, nonzero primitive image, a rational type-(0,0) detector, and nonzero specified Saito pairing.
falsifier: any strict one-node kernel, q>2n, tensor flattening rank zero or greater than one, value factor outside im(E), a value coloop, use of a restricted subfamily, or failure of any detector clause
---

# G123 — Construct class-directed one-node determination

B191 removes all auxiliary synchronization choices from G122. For the
actual reduced node scheme \(Z\) in the full complete linear system, put

\[
 V=H^0(X,I_Z\otimes L)/H^0(X,I_{2Z}\otimes L).
\]

The next construction must satisfy simultaneously:

1. \(R=\operatorname{rank}E<N\), and the value matroid has no coloop;
2. for every node \(i\),
   \[
   H^0(X,I_{\Psi_i}\otimes L)=H^0(X,I_{2Z}\otimes L),
   \]
   so a first jet at any one node determines the entire conditional-gradient
   class and \(q=\dim V\le2n\);
3. the intrinsic tensor
   \[
   \Gamma_Z=(d_i^*B_i)_i
   \in\mathcal T\otimes\operatorname{Sym}^2V^*
   \]
   is nonzero of tensor rank one;
4. its value factor lies in \(S=\operatorname{im}E\);
5. positive adjoint defect, nonzero primitive image, a rational type-
   \((0,0)\) detector, and nonzero specified Saito pairing with \(\zeta\)
   all survive.

Items 2--4 are exactly B190's full-system conformal synchronization, not a
dimension-count surrogate. They are tested by explicit section-space
equalities, matrix ranks, and membership in \(S\). Therefore G123 implies
G122, which via B190 kills the full quadratic Kuranishi tensor in G119.

The coherent identity

\[
 h^1(X,I_{2Z}\otimes L)=(2n+1)N-R-q
\]

shows the scale of the required superabundance when \(H^1(X,L)=0\), but
that number is not counted as existence. The node scheme, Hessian tensor,
and rational detector must be constructed jointly. B192/NG155 further
exclude proving these conditions only on invariant or single-character
sections of a nontrivial nodal symmetry: that is necessarily a strict
subfamily of a very ample complete system.
