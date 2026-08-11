---
brick_id: NG154
status: NO-GO
base_field: C
variety: the B142-B143 product X=P^n x P^n, its moving algebraic fiber, and the full O(m,m) complete-linear-system germ at the nodal divisor
smoothness: the product and fiber are smooth, the divisor has m^n ODPs, and the labeled discriminant arrangement is clean
projectivity: the product, fibers, divisors, complete linear system, and moving-fiber incidence are projective
dimension: n>=2, value rank R=binomial(m+n,n)-n>1, and full conditional-gradient rank nR+n>2n
codimension: B152's conormal gradient block has rank nR and the carrier-motion quotient has rank n, preventing injection into any one 2n-dimensional node block
coefficient_field: C for jets, Hessians, and ranks; Q for the special anchored detector already supplied by the fiber class
cohomology_theory: coherent first-jet interpolation, ODP Hessian deformation theory, and the B142-B143 rational vanishing-cycle detector
hodge_type: the special detector has rational type (0,0), but it is anchored by the known algebraic fiber
cycle_class_map: CH^n(P^n x P^n)_Q -> H^(2n)(P^n x P^n,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B142-B143, B152-B153, B190-B191, G122-G123
claim: Use the scalable moving-fiber witness B142-B143 as a full-system realization of B190/G123 conformal synchronization.
falsifier: B152 computes full conditional-gradient rank nR+n, which exceeds 2n for R>1, whereas B191 one-node determination requires rank at most 2n and injectivity into each node block
---

# NG154 — The product-fiber witness is not conformally synchronized

- **Route:** reuse B142-B143, the only audited scalable nodal detector with
  clean full-system incidence in every middle dimension, as the geometric
  realization of G122/G123.
- **Valid input:** the family has \(N=m^n\) nodes, uniform value rank
  \[
  R=\binom{m+n}{n}-n,
  \]
  clean nonlinear incidence, a rational type-\((0,0)\) relation, and a
  nonzero primitive pairing.
- **Invalid inference:** motion of the algebraic fiber describes the entire
  conditional-gradient image of the surrounding complete linear system.

B152 computes the full gradient image in this carrier family. Its
synchronized carrier-motion quotient has dimension \(n\), but the
common-kernel conormal-gradient image has rank \(nR\) and saturates B152's
bound. Therefore

\[
 \dim U=n+nR=n(R+1). \tag{1}
\]

For the B142 range \(n\ge2\) and sufficiently large \(m\), one has
\(R>1\), hence

\[
 \dim U=n(R+1)>2n=\dim G_i. \tag{2}
\]

B191 shows that G123 one-node determination requires every projection
\(U\to G_i\) to be injective, and therefore \(\dim U\le2n\). Equation (2)
makes this impossible. Equivalently, at every node the one-node kernel in
B191 is strictly larger than \(H^0(I_{2Z}\otimes L)\).

- **Precise obstruction:** the moving fiber synchronizes only one
  \(n\)-dimensional quotient. The full system also contains \(nR\)
  independent conormal directions; they cannot be discarded.
- **Circularity guard:** B142-B143 already start from the algebraic fiber,
  so they would not prove the general Hodge Conjecture even if the rank
  obstruction vanished. NG154 is stronger: the family fails the finite
  G123 gate before that circularity issue is reached.
- **Re-entry condition:** construct an unanchored full-system node scheme
  with \(q\le2n\), every one-node determination equality, rank-one
  intrinsic Hessian tensor with value factor in \(S\), and the specified
  rational detector.
