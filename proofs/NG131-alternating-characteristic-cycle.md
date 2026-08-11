---
brick_id: NG131
status: NO-GO
base_field: C
variety: a projective map g':Y x E->T obtained from B164's smooth-total-space node-escape map g:Y->T by product with a smooth projective elliptic curve E
smoothness: Y, E, and Y x E are smooth; singular fibers of g retain the tracked ODP escape
projectivity: g and g' are projective and their rational direct images satisfy decomposition and relative hard Lefschetz
dimension: arbitrary B164 fiber dimension plus one elliptic factor
codimension: the original positive-codimension discriminant microsupport survives on T
coefficient_field: Q
cohomology_theory: rational proper direct images, Kunneth formula, characteristic cycles in the Grothendieck group, perverse cohomology, and microsupport
hodge_type: the elliptic factor is pure but supplies no specified detector type or pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not resolved
cycle_equivalence: rational equivalence
scope: relative
dependencies: B164-B166, S037, S067
claim: Vanishing of the ordinary alternating characteristic cycle CC(K), or of every Euler function obtained from its Grothendieck class, forces SS(K) to lie in the zero section for a projective direct image from a smooth total space satisfying decomposition and relative hard Lefschetz.
falsifier: for K'=Rg'_*Q, Kunneth gives K'=Rg_*Q tensor RGamma(E,Q); chi(E)=1-2+1=0 makes CC(K')=0, while K' is a direct sum of shifts of Rg_*Q and retains its nonzero discriminant microsupport
---

# NG131 — Alternating characteristic cycles can cancel completely

- **Route:** replace G105's positive perverse coefficients by the ordinary
  Grothendieck-group characteristic cycle \(CC(K_B)\), or by an alternating
  Euler-index calculation.
- **Valid input:** characteristic cycles are additive in distinguished
  triangles and change sign under a shift. Projective decomposition and
  relative hard Lefschetz still hold.
- **Counterexample:** start with B164's projective node-escape map
  \(g:\mathcal Y\to T\) with \(\mathcal Y\) smooth and nonzero discriminant
  microsupport. For a smooth projective elliptic curve \(E\), set

  \[
  g':\mathcal Y\times E\longrightarrow T.
  \]

  Künneth gives

  \[
  Rg'_*\mathbf Q\simeq Rg_*\mathbf Q\otimes R\Gamma(E,\mathbf Q).
  \]

  Since the elliptic Betti numbers are \(1,2,1\), its Grothendieck class is
  \(1-2+1=0\). Hence \(CC(Rg'_*\mathbf Q)=0\), and every fiber Euler
  characteristic is zero. Nevertheless \(Rg'_*\mathbf Q\) is a nonzero
  direct sum of shifts of \(Rg_*\mathbf Q\), so its microsupport is exactly
  the same nonzero union.
- **Precise obstruction:** an alternating cycle forgets the union of
  supports across perverse degrees. Decomposition and Lefschetz symmetry do
  not restore the lost positive multiplicities.
- **Scope guard:** the product family is not itself a hypersurface family;
  it refutes the proposed general implication from the listed sheaf-theoretic
  hypotheses, not a stronger hypersurface-specific theorem.
- **Re-entry condition:** prove the individual nonnegative coefficients of
  \(CC^+\) vanish as required by G105, or prove a hypersurface-specific
  theorem that forbids all cross-degree cancellation and then check every
  detector clause separately.
