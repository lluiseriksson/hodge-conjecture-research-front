---
brick_id: G085
status: EXPLORATORY
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X, a primitive rational Hodge class zeta, and a high-power hyperplane system in which Sigma_(zeta,m) is assumed nonempty
smoothness: X smooth; sought target multipart nodal with Li-clean discriminant arrangement
projectivity: X and the hyperplane systems projective
dimension: dim_C X=2n; hyperplane fibers 2n-1; parameter dimension arbitrary
codimension: middle cycle codimension n; source support codimension at least two
coefficient_field: Q
cohomology_theory: local intersection cohomology, admissible normal-function singularities, algebraic deformation, nearby cycles, and Saito nodal relations
hodge_type: target relation rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative may be used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B012, B054, B125-B127, G032, G084, NG040, NG101
claim: Conditional on Sigma_(zeta,m) being nonempty for some high-power embedding, after possibly increasing the power there is a Li-clean multipart nodal parameter in the class-specific support.
falsifier: a class with nonempty local restriction support at some high power whose support avoids every Li-clean multipart nodal locus at all allowed higher powers
---

# G085 — Conditional clean-support cleanup

**Status:** EXPLORATORY — conditional cleanup, not the terminal gate

Assume the terminal support datum has already been supplied:

\[
 p\in\Sigma_{\zeta,m}.
\]

Without using an algebraic representative of \(\zeta\), construct an allowed
higher embedding and

\[
 q\in\Sigma_{\zeta,m'}\cap C_{m'}^{\mathrm{clean}}.
\]

B125 supplies the relation and pairing at \(q\). Therefore G008 plus G085
implies G084 and G031.

## Known failures

- Generic morsification does not create a one-fiber relation (NG040).
- The local suspended-$A_2$ versal slice contains no multinode fiber
  (B126/NG101).
- A dimension or generic-slice argument cannot force the support to enter a
  prescribed locus.

## Exact missing datum

The proof must construct a global topology-changing algebraic deformation
and a comparison of local restriction classes showing nonvanishing at the
target. Merely connecting the two parameter points in projective space does
not transport a stalk class. Rationality, the Tate twist, and the actual
nearby-cycle comparison must be retained.

G085 is deliberately conditional. It does not replace or weaken G008, whose
universal nonemptiness statement is already terminal-equivalent to HC.
