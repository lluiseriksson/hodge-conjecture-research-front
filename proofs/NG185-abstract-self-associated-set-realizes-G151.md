---
brick_id: NG185
status: NO-GO
base_field: C
variety: abstract self-associated reduced point configurations in projective space versus the required configurations on arbitrary polarized smooth projective 2n-folds
smoothness: the abstract points are reduced; no ambient X incidence, second-osculator absorption, or ODP divisor smoothness is supplied
projectivity: the abstract point configuration is projective; the missing embedding into the fixed H^2(X) remains projective
dimension: abstractly 2c+2 points in P^c; G151 has c=binom(2n+2,2) and dim X=2n
codimension: self-association controls a diagonal code duality only, not the codimension of the locus inside H^2(X) or the jet/ODP conditions
coefficient_field: C for Gale and bilinear-form classifications; Q detector and specified class data remain absent
cohomology_theory: finite Gorenstein Serre duality and evaluation codes only; no vanishing-cycle mixed Hodge structure is constructed
hodge_type: no rational type-(0,0) relation or specified nonzero pairing follows
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not reached
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B225, G151, S082
claim: Choose any abstract self-associated set of 2c+2 points in P^c, or any arithmetically Gorenstein example from S082, and count it as a construction of G151 on every arbitrary (X,A,zeta).
falsifier: S082 classifies configurations in a free projective space and requires an additional one-quadric defect for arithmetic Gorensteinness; it contains no embedding theorem into H^2(X), osculator-hyperplane theorem, ODP jet package, rational detector, or specified pairing
---

# NG185 — Abstract self-association does not embed the G151 core

- **Route:** select two orthogonal bases in \(\mathbf P^c\), obtaining a
  self-associated set by S082 Theorem 8.1, and declare G151 constructed.
- **Valid input:** this produces the exact abstract weighted self-dual
  evaluation matrix required by B225.
- **Invalid inference:** projective equivalence in a free
  \(\mathbf P^c\) places the columns on the fixed \(H^2(X)\)-image and
  realizes its marked second osculators.
- **Precise obstruction:** no map in S082 solves the incidence equations
  \[
  p_i\in X,\qquad
  \widehat O^{(2)}_{p_i}(H^2)\subset S_{2,Z}^{(0)}
  \]
  for arbitrary \(X\). Theorem 7.3 also shows that arithmetic
  Gorensteinness needs the additional condition of failing by exactly
  one to impose independent conditions on quadrics; self-association
  alone does not provide it.
- **Detector guard:** neither orthogonal bases nor a Gorenstein coordinate
  ring supplies a rational vanishing-cycle class, ODP Hessians, or the
  specified Hodge pairing.
- **Re-entry condition:** solve the fixed-\(X\) self-associated
  osculator incidence with all degree-five jet and detector clauses, as
  stated in G151.
