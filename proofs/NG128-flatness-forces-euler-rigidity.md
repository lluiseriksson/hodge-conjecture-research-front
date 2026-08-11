---
brick_id: NG128
status: NO-GO
base_field: C
variety: flat projective hypersurface families in one fixed complete linear system, including B161's arbitrary-rank uniform escaping family
smoothness: the central fiber has only tracked ordinary double points and is smooth elsewhere; one tracked node smooths along the basis germ
projectivity: every fiber is projective with the same polarization and Hilbert polynomial
dimension: arbitrary hypersurface dimension r; B161 base dimension R+1 and value rank R<N
codimension: the basis-node germ has codimension R, but one extra branch fails to contain it
coefficient_field: C for algebraic families and Z for Hilbert polynomials and Euler characteristics
cohomology_theory: flat projective deformation theory, Hilbert polynomials, Milnor fibers, and topological Euler characteristic
hodge_type: no specified type-(0,0) detector is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is absent; no algebraicity conclusion is made
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B161 and G101-G102
claim: Projective flatness in a fixed linear system and constancy of the Hilbert polynomial force topological Euler constancy on a basis-node germ and therefore force every tracked node to persist.
falsifier: B161 is flat and Hilbert-polynomial constant, but exactly one node disappears and the Euler characteristic changes by one signed Milnor contribution
---

# NG128 — Flatness does not imply Euler rigidity

- **Route:** infer B160's constant topological Euler characteristic from
  projectivity, flatness, and a fixed Hilbert polynomial.
- **Valid input:** these hypotheses control algebraic numerical invariants
  such as the Hilbert polynomial and arithmetic genus.
- **Invalid inference:** they make the singular fibers topologically locally
  trivial or conserve the total Milnor number.
- **Precise obstruction:** B161 realizes B159 as a relative effective
  Cartier divisor in \(X\times T\). The family is flat, every fiber lies in
  the same \(|L^k|\), and the Hilbert polynomial is constant. Along
  \(F_B=\{x=0\}\), however, the last critical value is \(y^m\): the central
  fiber has \(N\) nodes and a nearby \(y\ne0\) fiber has \(N-1\). B160 gives

  \[
  \chi(Y_0)-\chi(Y_y)=-(-1)^r\ne0.
  \]

- **Re-entry condition:** prove actual topological local triviality, total
  Milnor-number constancy, or an equivalent global conservation theorem on
  G102's class-directed basis stratum, then retain the specified pairing.
