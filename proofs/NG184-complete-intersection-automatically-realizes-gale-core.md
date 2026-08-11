---
brick_id: NG184
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, with the explicit valid test input P^n x P^n polarized by H=O(2,4)
smoothness: prospective complete-intersection divisors and their point intersection are transverse; no G149 ODP divisor is supplied
projectivity: X, all divisor intersections, restricted line bundles, and evaluation systems are projective
dimension: dim X=2n; the complete intersection has codimension 2n and dimension zero
codimension: residue duality targets the adjunction complement omega_X tensor product_i L_i tensor H^(-2), not automatically H^(m-2)
coefficient_field: C for residues and evaluation codes; Q Hodge detector data remain absent
cohomology_theory: Koszul adjunction, Gorenstein trace duality, coherent evaluation, and Cayley-Bacharach
hodge_type: no rational type-(0,0) relation or specified pairing follows from the canonical trace
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not reached
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B223-B224, G149-G150, S070
claim: On every arbitrary input, intersect divisors in powers of H and invoke complete-intersection Cayley-Bacharach duality to obtain E_(m-2)=E_2^(perp_lambda) and hence G150.
falsifier: B224 computes the complementary ambient twist and the polarized product P^n x P^n has omega_X tensor H^q nontrivial for every integer q, so no choice of H-power complete-intersection degrees gives the required canonical shift
---

# NG184 — Complete intersections dualize to the wrong twist in general

- **Route:** choose a reduced complete intersection of divisors in powers
  of \(H\), use its residue trace, and identify the complementary code
  to \(E_2\) with \(E_{m-2}\).
- **Valid input:** complete intersections are Gorenstein, their trace
  pairing is perfect, and S070 proves complementary-degree
  Cayley–Bacharach formulas in projective space.
- **Invalid inference:** the complementary degree or line bundle may be
  chosen independently of adjunction.
- **Precise obstruction:** B224 gives the actual complementary twist
  \(\omega_X\otimes H^{E-2}\). An ambient identification with
  \(H^{m-2}\) requires \(\omega_X\otimes H^{E-m}\simeq O_X\).
  For \(X=\mathbf P^n\times\mathbf P^n\) and \(H=O(2,4)\), no integer
  \(E-m\) satisfies this identity.
- **Detector guard:** even when the twist matches, residue duality alone
  does not impose G149's second-osculator absorption, doubled/tripled
  jets, ODP Hessians, rational Hodge type, or specified pairing.
- **Re-entry condition:** construct G150 by a non-complete-intersection
  point scheme or prove a non-circular twist-correction theorem retaining
  every detector clause.
