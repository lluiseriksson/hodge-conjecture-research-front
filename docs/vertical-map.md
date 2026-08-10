# Vertical proof map

Date: 2026-08-10. Overall status: **EXPLORATORY**.

## Terminal-equivalent primary route

\[
\text{standard rational HC}
\Longleftrightarrow
\text{universal primitive middle singularity}
\Longleftrightarrow
\text{singular-hyperplane detection G005}
\Longleftarrow
\text{class-specific nodal relation G006}.
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

## Local channel reduction

B008 excludes every smooth point of the discriminant: its rational local
intersection-cohomology group is zero. Thus a generic Lefschetz critical value
cannot detect ζ.

Under the explicit transverse nodal hypotheses of B009, the remaining local
channel is

\[
 \operatorname{Rel}(\delta_i)
 =\ker\!\left(\mathbf Q^r\to H_{2n-1}(X_s,\mathbf Q),
 (a_i)\mapsto\sum_i a_i\delta_i\right).
\]

This turns the abstract local singularity into a concrete relation space but
does not make the specified class's image nonzero.

## Current smallest attackable brick

**G006: class-specific vanishing-cycle relation.** Construct directly from
\((X,L,\zeta)\) a transverse nodal point \(p\in|L^m|\), a relation
\(0\ne a\in\operatorname{Rel}(\delta_i)\), and its new middle class
\(\beta_a\in H_{2n}(X_p,\mathbf Q)\) such that

\[
 \langle\zeta,i_*\beta_a\rangle\ne0.
\]

This is falsifiable by a triple \((X,L,\zeta)\) for which all such pairing
functionals vanish for every \(m\). It implies G005 and propagates all the way
upward by B007. Thomas's theorem gives the converse under HC, so the universal
statement remains terminal-equivalent.

## Attempt audit

1. Pass to \(m\gg0\), where Lefschetz pencils have nontrivial vanishing
   cycles - valid by BFNP Proposition 5.11.
2. Use global monodromy to relate those cycles - valid ambient information.
3. Move to a smooth discriminant point - **closed by B008** because its local
   rational intersection-cohomology channel is zero.
4. Choose a higher nodal stratum with a positive relation space - valid as a
   source of possible local directions under B009.
5. Conclude that the specified \(\zeta\) couples to one of those directions -
   **invalid**. A nonzero vector space does not make the class-specific linear
   functional nonzero.

Steps 3 and 5 are B008 and NG-009 respectively; the ambient inference already
failed as NG-008. Thomas's constructive nodal direction does not repair the
gap because it begins with an algebraic representative, while his deformation
analysis shows that the nodal obstruction space retains the embedded-cycle
obstruction.

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
nontrivial ambient monodromy, a nonzero nodal relation space, or a nodal
dimension count is not itself a cycle construction.
