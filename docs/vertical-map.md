# Vertical proof map

Date: 2026-08-10. Overall status: **EXPLORATORY**.

## Terminal-equivalent primary route

\[
\text{standard rational HC}
\Longleftrightarrow
\text{universal primitive middle singularity}
\Longleftrightarrow
\text{singular-hyperplane detection G005}
\Longleftrightarrow
\text{class-specific nodal relation G006}
\Longleftarrow
\text{codimension-two support realization G008}
\Longleftarrow
\text{tube-to-local concentration G007}.
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

This turns the abstract local singularity into a concrete relation space.
B010 strengthens the statement: every type-\((0,0)\) unipotent relation
\(\beta\) determines a primitive Hodge class \(\gamma_\beta\), and

\[
 \zeta|_{X_p}\ne0
 \quad\Longleftrightarrow\quad
 \langle\zeta,\gamma_\beta\rangle\ne0
 \text{ for some }\beta.
\]

For ordinary double points every rational relation has the required Hodge
type. The missing input is therefore the existence of a relation outside the
kernel of this exact pairing.

## Global detector now available

B011 proves that, after passing to a high enough embedding with nonzero
vanishing homology, the global tube map is surjective onto primitive rational
middle cohomology. Thus every nonzero primitive Hodge class has a global tube
detector \((g,\alpha)\) with \(g\alpha=\alpha\).

This does not yet give a local singularity. The global kernel
\(\ker(g-1)\) and Saito's relation kernel at one singular fiber are different
objects.

## Exact global/local separation

B012 proves that the Green-Griffiths global invariant

\[
 s(\zeta)\in IH^1(\mathbf P^d,IC(R^{2n-1}))
\]

is nonzero for every nonzero primitive class. For \(m\gg0\), the associated
local class \(s(\zeta)_p\) is nonzero exactly when the singular hyperplane \(X_p\)
detects \(\zeta\). The possible local support
\(\operatorname{Sing}(\zeta)\) has codimension at least two.

This identifies the precise missing implication between two invariants of the
same primitive class:

\[
 s(\zeta)\ne0
 \quad\not\Rightarrow\quad
 \exists p\;s(\zeta)_p\ne0
\]

without a new support theorem. A generic pencil avoids a fixed
codimension-at-least-two support. A generic net can meet such a component if
it is nonempty, but cannot establish nonemptiness.

## Current smallest attackable brick

**G008: codimension-two support realization.** Starting from the already
nonzero global class \(s(\zeta)\), construct a discriminant point \(p\) with

\[
 s(\zeta)_p\ne0.
\]

Equivalently, construct an algebraic two-parameter degeneration that
concentrates the global data at one higher-codimension point and produces
\(\beta\in R(X_p)_1^{(0,0)}\) such that

\[
 \langle\zeta,\gamma_\beta\rangle\ne0.
\]

This is falsifiable by a triple \((X,L,\zeta)\) whose global invariant is
nonzero but every high-power local stalk vanishes. It is terminal-equivalent
after universal quantification. G007 is retained as one concrete geometric
mechanism proposed for closing G008.

## Attempt audit

1. Pass to \(m\gg0\) and use B011 to choose a loop-fixed vanishing class whose
   tube detects \(\zeta\) - valid global topology.
2. Factor the loop into Picard-Lefschetz meridians. B013 proves the exact
   telescoping distributed relation among the transported vanishing cycles.
3. Fill the loop in the full projective parameter space. A generic real
   two-disk meets several separate smooth discriminant points and generically
   misses the real-codimension-four class-specific support of B012.
4. Declare the distributed cancellation to be a relation at one singular
   member - **invalid**. B008 kills every smooth-point local channel, and no
   theorem coalesces the intersections while preserving the tube and its
   Hodge type.

Step 4 is NG-010. Inferring a nonzero local class merely from global
nonvanishing or a generic slice is NG-011. The open construction must create
a higher discriminant stratum and verify the specialization through Saito's
exact sequence; merely factoring the global monodromy or increasing slice
dimension does not do so.

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
nontrivial ambient monodromy, global tube surjectivity, a nonzero nodal
relation space, or a nodal dimension count is not itself a cycle
construction.
