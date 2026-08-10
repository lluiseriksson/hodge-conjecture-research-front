---
brick_id: G013
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective X of dimension 2n, a specified primitive rational Hodge class, a global detector, and a sought high-degree nodal member with node scheme Delta
smoothness: X and nearby fibers are smooth; the sought member has only ordinary double points; its node scheme satisfies the two-part smoothing-matroid inequalities
projectivity: X and the hypersurface family are projective
dimension: dim_C X = 2n and the nodal hypersurface has dimension 2n-1
codimension: middle codimension n on X; nodes have codimension 2n in X and define a higher-codimension incidence condition
coefficient_field: Q for Hodge, homology, and Saito relation data; C for smoothing and adjoint evaluation matroids
cohomology_theory: primitive Betti homology and cohomology, monodromy tubes, nodal vanishing cycles, local intersection cohomology, mixed Hodge structures, and coherent node-evaluation cohomology
hodge_type: the specified class and sought Saito relation have rational type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B009-B013, B016, and B022-B028
claim: Every specified primitive rational Hodge class with a nonzero global detector admits a high-degree nodal member whose node scheme satisfies the two-part smoothing-matroid inequalities, has positive adjoint evaluation defect, and contains a rational Saito relation whose ambient class retains nonzero pairing with the specified class.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class for which every nodal node scheme satisfying the two-part matroid inequalities either has zero adjoint defect or has detector image contained in the class annihilator
---

# G013 - Class-paired two-matroid incidence

## Falsifiable theorem sought

For

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0},
\]

construct a sufficiently high line bundle \(A\), a nodal member
\(Y_0\in|A|\) with node scheme \(\Delta\), and a relation \(\beta\) such
that:

1. \(|S|\le2r_A(S)\) for every \(S\subseteq\Delta\), so Edmonds' theorem
   partitions \(\Delta\) into two independently smoothable parts;
2. \(r_F(\Delta)<|\Delta|\) for
   \(F=K_X\otimes A^n\), so B026 supplies a nonzero nodal relation space;
3. \(\beta\) is rational and its Saito ambient class survives the B022
   quotients with \(\langle\zeta,\gamma_\beta\rangle\ne0\).

This is an exact rank-function version of G012. B028 removes the ambiguity
from “partitioned independence,” while B009 and B010 supply the local channel,
Hodge type, and pairing once the incidence is constructed. Universal G013
implies G012, G008, and hence the standard rational Hodge Conjecture through
B007.

## Attempt 1 - Choose a smoothing circuit

Every circuit of the smoothing evaluation matroid admits the required
two-part partition. B028 gives an explicit high-power configuration on
\(\mathbf P^2\times\mathbf P^2\) where such a circuit becomes independent in
the adjoint evaluation matroid. Thus a smoothing circuit does not force the
strict inequality \(r_F(\Delta)<|\Delta|\). This shortcut is NG-025.

## Re-entry condition

Construct an algebraic incidence component on which the Edmonds inequalities
hold fiberwise and the adjoint corank is positive; then build a rational
comparison from its adjoint cokernel to the Saito relation local system and
prove that the global detector gives a section not everywhere annihilated by
\(\zeta\). The incidence must be defined without an algebraic representative
of \(\zeta\).

