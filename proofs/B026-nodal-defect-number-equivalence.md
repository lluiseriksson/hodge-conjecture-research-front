---
brick_id: B026
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n with a sufficiently ample line bundle L and a nodal hypersurface member Y_0 in |L| with node scheme Delta
smoothness: X is smooth; Y_0 has only ordinary double points; the canonical desingularization of Y_0 is used in two of the compared invariants
projectivity: X and Y_0 are projective
dimension: dim_C X = 2n and dim_C Y_0 = 2n-1
codimension: Y_0 has codimension 1 in X; the ambient Hodge application has middle codimension n
coefficient_field: Q for singular homology and local intersection cohomology; C for coherent cohomology and Hodge-number dimensions
cohomology_theory: singular homology and cohomology, vanishing cycles, local intersection cohomology, coherent sheaf cohomology of the adjoint node ideal, and the cohomology of a canonical desingularization
hodge_type: nodal rational relations have type (0,0) after Tate twist by B010; the theorem compared here is numerical and does not identify a prescribed Hodge direction
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraic cycle for the input Hodge class is assumed or constructed
cycle_equivalence: rational equivalence
scope: fiberwise
dependencies: Green-Griffiths Section 4.2.4 (S021) and B009-B010
claim: Under the audited high-ampleness nodal hypotheses, the dimension of the rational relation space among the nodal vanishing cycles equals the dimension of the primitive ambient homology image, the adjoint node-evaluation defect h^1(I_Delta tensor K_X tensor L^n), and the relevant local intersection-cohomology group; this numerical equality does not select a vector pairing nontrivially with a prescribed Hodge class.
falsifier: a nodal member satisfying the stated Green-Griffiths hypotheses for which any two of their six displayed defect invariants have different dimensions
---

# B026 - Nodal defect numbers agree

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L\) be
sufficiently ample in the sense of Green-Griffiths Section 4.2.4, and let
\(Y_0\in|L|\) have only nodes with reduced node scheme \(\Delta\). For a
nearby smooth member, write \(\delta_\lambda\) for the transported vanishing
cycles. Define

\[
\begin{aligned}
 \rho_{\mathrm{rel}}
   &=\dim_{\mathbf Q}\operatorname{Rel}(\delta_\lambda),\\
 \rho_{\mathrm{amb}}
   &=\dim_{\mathbf Q}\operatorname{im}\!\left(
        H_{2n}(Y_0,\mathbf Q)\to H_{2n}(X,\mathbf Q)_{\mathrm{prim}}
      \right),\\
 \rho_{\mathrm{adj}}
   &=h^1\!\left(X,I_\Delta\otimes K_X\otimes L^n\right),\\
 \rho_{\mathrm{IC}}
   &=\dim_{\mathbf Q}H^1(B^\bullet).
\end{aligned}
\]

The theorem on pp. 18-19 of Green-Griffiths identifies these four numbers,
together with two equivalent desingularization/Hodge-number defects:

\[
 \rho_{\mathrm{rel}}=\rho_{\mathrm{amb}}
 =\rho_{\mathrm{adj}}=\rho_{\mathrm{IC}}.
\]

For \(L\gg0\), the coherent group is the failure of the nodes to impose
independent conditions on
\(H^0(X,K_X\otimes L^n)\). Thus a topological relation count can be tested
by an algebraic evaluation defect in the chosen nodal member. B009 identifies
the local channel with the relation space, and B010 ensures that nodal
rational relations have type \((0,0)\) after the Tate twist.

## What the equality does and does not give

The theorem proves that a positive adjoint defect is equivalent to the
existence of at least one vanishing-cycle relation and at least one primitive
ambient homology direction coming from \(Y_0\). It therefore upgrades a bare
node count to an exact feasibility test.

It remains a comparison of **dimensions**. It does not, as stated, construct
a class-preserving map from a chosen global tube or thimble detector to an
adjoint defect class, nor does positivity imply

\[
 \langle\zeta,\gamma_\beta\rangle\ne0
\]

for a specified primitive Hodge class \(\zeta\). A nonzero detector subspace
may lie inside the annihilator of that one functional. The missing
vector-level, class-paired incidence statement survives only in G012's
partwise-independent formulation.

## Scope guard

No special-family defect is counted as progress toward arbitrary varieties.
The theorem starts with a selected nodal member and does not construct it
from \(\zeta\). The equality of dimensions is not an algebraic-cycle
construction and does not prove G012.
