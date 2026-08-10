---
brick_id: G006
status: EXPLORATORY
base_field: C
variety: arbitrary polarized smooth projective X of dimension 2n with a specified nonzero primitive rational middle Hodge class, together with a sought nodal hyperplane degeneration
smoothness: X smooth; nearby hyperplane fiber smooth; central hyperplane fiber has only ordinary double points
projectivity: X projective and L very ample
dimension: dim X = 2n and dim D = 2n-1
codimension: middle codimension n on X
coefficient_field: Q
cohomology_theory: singular Betti cohomology with Tate twist, Picard-Lefschetz homology, and local intersection cohomology
hodge_type: primitive (n,n), equivalently (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007, B008, B009, Thomas Theorem 1.1 (S019)
claim: For every nonzero primitive rational middle Hodge class, some high-degree transverse nodal hyperplane degeneration has a rational vanishing-cycle relation whose associated new middle cycle pairs nontrivially with that class.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class annihilating every new middle cycle arising from every such nodal relation in every power of the polarization
---

# G006 - Class-specific vanishing-cycle relation

## Falsifiable theorem sought

For every smooth projective \(X/\mathbf C\) of dimension \(2n\), very ample
\(L\), and nonzero primitive

\[
 \zeta\in H^{2n}(X,\mathbf Q(n))\cap H^{0,0},
\]

there should exist \(m>0\) and a nodal member \(D=X_{s_0}\in|L^m|\), in a
local deformation satisfying B009, with vanishing cycles \(\delta_i\) and a rational
relation

\[
 0\ne a=(a_i)\in\ker\!\left(\mathbf Q^r\to
 H_{2n-1}(X_s,\mathbf Q),\ (a_i)\mapsto\sum_i a_i\delta_i\right),
\]

such that a new class associated through the degeneration exact sequence,
\(\beta_a\in H_{2n}(D,\mathbf Q)\), satisfies

\[
 \langle \zeta|_D,\beta_a\rangle
 =\langle\zeta,i_*\beta_a\rangle\ne0.
\]

Here “associated” refers to a choice of lift through the standard degeneration
exact sequence; no canonical lift is asserted. The quotient measuring new
middle homology has the same relation-space description in the transverse
nodal setting. This formulation is finite-dimensional and directly
falsifiable once a nodal degeneration is specified.

## Why it propagates upward

The nonzero pairing forces \(\zeta|_D\ne0\). B007 then proves the rational Hodge
Conjecture. Conversely, if HC is assumed, Thomas Theorem 1.1 constructs a
high-degree nodal divisor carrying a middle homology class mapping to the
Poincare dual of \(\zeta\); its new component yields the required detecting
relation. Thus the universal form of G006 remains terminal-equivalent, not a
proved advance toward HC.

## Attempt and exact failure

High degree can supply nodal members, and dependent vanishing cycles can make
the local intersection-cohomology target nonzero. Neither statement controls
the linear functional

\[
 \operatorname{Rel}(\delta_i)\longrightarrow\mathbf Q,
 \qquad a\longmapsto\langle\zeta,i_*\beta_a\rangle .
\]

It may vanish identically for the specified \(\zeta\). A positive defect, a node
count, or a dimension estimate proves only that the domain is nonzero. The
class-specific nonzero pairing is precisely the missing theorem and is
recorded as NG-009.

## Next admissible attacks

1. Derive the pairing functional from limiting mixed Hodge structure data and
   search for a polarization/monodromy argument proving it is nonzero for a
   chosen \(\zeta\).
2. Seek a degeneration construction determined by the Hodge tensor itself,
   not by an already algebraic representative.
3. Test candidate statements first on families where the defect space and
   monodromy representation are explicitly computable; such tests remain
   EXPLORATORY or NUMERICAL until a universal theorem is proved.

Any construction beginning with a subvariety whose class is \(\zeta\) is circular for
this gate.
