---
brick_id: G045
status: EXPLORATORY
base_field: C with all Hodge and descent data over Q
variety: the B058 plane-net hyperplane family, its B071 semistable stack, and proper pushdown to the original base
smoothness: smooth generic hyperplane fibers and regular semistable source stack
projectivity: family, alterations, modifications, and pushdown are projective
dimension: ambient 2n, fiber 2n-1, base 2, and total space 2n+1
codimension: divisor support at codimension 1 and point support at codimension 2; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, perverse cohomology, strict support, and proper base change
hodge_type: detector target is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B071-B081, G043-G044, G046, NG055-NG058
claim: For the actual B071 pushdown, compute the multiplicities of divisor b=0 and point b=-1 terms; place the B058 class canonically in the perverse filtration, then separate full from divisor support inside pH^0.
falsifier: an unlisted support meeting normalized degree -1, an uncomputed allowed multiplicity, failure of canonical grade landing, or zero full-support graded projection
---

# G045 — Multiplicity and projection in the two allowed support shifts

**Status:** EXPLORATORY  
**Parent gates:** G044 / G043

B080 reduces the support-degree search on the plane base to two cases:

\[
 IC_D\quad(b=0),
 \qquad
 IC_p[1]\quad(b=-1).
\]

Both are allowed by toric parity. The required calculation is now:

1. identify every discriminant divisor $D$ and collision point $p$ created
   or dominated by the B071 semistable construction;
2. compute the corresponding perverse multiplicity spaces in shifts $0$
   and $-1$, including finite-stabilizer descent;
3. place the nearby specialization of the B057 extension chain in the
   canonical perverse filtration;
4. treat the point term as the separate \(E_\infty^{0,-1}\) grade and
   separate divisor from full support canonically inside
   \(E_\infty^{-1,0}\), as required by G046.

If either multiplicity vanishes, that is a genuine simplification. If it is
nonzero, its associated-graded class—not a coordinate from a chosen derived
splitting—must be computed. Only G046's full-support graded class enters the
two B022 quotient tests.
