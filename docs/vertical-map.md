# Vertical proof map

Date: 2026-08-10. Overall status: **EXPLORATORY**.

## Terminal-equivalent primary route

\[
\text{standard rational HC}
\Longleftrightarrow
\text{universal primitive middle singularity}
\Longleftrightarrow
\text{singular-hyperplane detection G005}.
\]

The first equivalence is BFNP Theorem 1.3 and Theorems 6.5-6.6, audited in
B007. The concrete terminal obligation is:

> For every smooth projective \(X/\mathbf C\) of dimension \(2n\), every very
> ample \(L\), and every nonzero primitive
> \(\zeta\in H^{2n}(X,\mathbf Q(n))\cap H^{0,0}\), find \(m>0\) and
> \(D\in|L^m|\) with \(\zeta|_D\ne0\).

Such a \(D\) is necessarily singular. For high powers BFNP Corollary 5.15
identifies the restriction with the local intersection-cohomology singularity
of the admissible normal function attached to \(\zeta\). No algebraic
representative of \(\zeta\) is assumed in this formulation.

## Current smallest attackable brick

**G005-NV: class-specific local nonvanishing.** Construct directly from
\((X,L,\zeta)\) a discriminant point \(p\in|L^m|\) such that

\[
0\ne\sigma_p(\operatorname{pr}_m^*\zeta)
\in IH^1_p\bigl(R^{2n-1}\pi_{m,*}\mathbf Q(n)\bigr).
\]

This is falsifiable by a triple \((X,L,\zeta)\) for which every such local
class vanishes for all \(m\). It propagates all the way upward by B007.

## Attempt audit

1. Pass to \(m\gg0\), where Lefschetz pencils have nontrivial vanishing
   cycles - valid by BFNP Proposition 5.11.
2. Use global monodromy to relate those cycles - valid ambient information.
3. Conclude that the specified \(\zeta\) has nonzero restriction at one
   singular fiber - **invalid**. Ambient vanishing cycles need not couple
   nontrivially to this class.

Step 3 is NG-008. Thomas's nodal variant does not repair it: his construction
of the detecting divisor begins with an algebraic representative, while his
deformation analysis shows that the nodal obstruction space retains the
embedded cycle obstruction.

## Secondary anchored route

\[
\text{HC}
\Longleftrightarrow
\text{universal middle HC (B001)}
\Longleftarrow
\text{anchor access G001 + presentation G004 + propagation B004}.
\]

B004 remains a proved sufficient theorem: an algebraic anchor with an
injectively combined semiregular lci presentation propagates across its
connected Hodge base. G001 and G004 remain open and independent. B005-B006
record structural limits on repairing or transporting the presentation.

This route is retained for cross-checking but is not the active gate because
it assumes access to an algebraic anchor. G005 reaches the terminal problem
without that assumption and is already known to be equivalent to HC.

## Promotion guard

Neither route counts as general progress until its universal open gate is
proved. A normal-function singularity criterion, a nonempty discriminant,
nontrivial ambient monodromy, or a nodal dimension count is not itself a cycle
construction.
