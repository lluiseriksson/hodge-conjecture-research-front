---
brick_id: NG081
status: NO-GO
base_field: C with rational homology and Hodge structures
variety: an arbitrary polarized smooth projective complex 2n-fold with a B058 detector and an isolated clean nodal hyperplane collision
smoothness: ambient and nearby fiber smooth; target has finitely many ordinary double points
projectivity: ambient variety and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; target singular support finite
coefficient_field: Q
cohomology_theory: relative singular homology, primitive ambient homology, Saito's relation map, and Hodge pairing
hodge_type: detector, relation, and primitive ambient classes rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B058, B104-B105, S022 Proposition 1 and Theorem 1
claim: Vanishing of B104's relative-bordism obstruction coset is necessary before a selected local relation can count as a detector for zeta.
falsifier: B105's scalar criterion and any nonzero bordism coset lying in the kernel of the compatible primitive ambient realization or of pairing with zeta
---

# NG081 — Zero relative-bordism obstruction is not necessary

**Status:** NO-GO

- **Route:** require
  $\overline\Omega(t,\beta)=0$ in the B104 quotient before counting the
  collision as progress toward the terminal Saito detector.
- **Valid implication:** coset vanishing supplies a relative bordism, forces
  equality with B058's full ambient class $c$, and is sufficient.
- **Invalid inference:** the relative bordism is necessary for the standard
  rational Hodge Conjecture reduction.
- **Precise obstruction:** S022 only requires
  $\langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0$. B105 rewrites this as the
  exact scalar condition
  $D_\zeta(c,\beta)\ne\langle\zeta,c\rangle$. A nonzero B104 coset can die
  under primitive ambient realization, or only after pairing with $\zeta$.
- **Finite countermodel:** with obstruction quotient $\mathbf Q^2$, ambient
  realization $(x,y)\mapsto x$, and coset $(0,1)$, the coset is nonzero but
  the ambient discrepancy is zero.
- **Re-entry condition:** G069 must construct the actual nodal relation and
  prove the scalar inequality. A collision pair or bordism may be used, but
  only its scalar ambient image must be controlled.
