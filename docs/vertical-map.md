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
\]

Two sufficient attacks feed G008:

\[
\text{G008}\Longleftarrow\text{independent-node detector generation G009},
\qquad
\text{G008}\Longleftarrow\text{tube-to-local concentration G007}.
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
it is nonempty, but cannot establish nonemptiness. B014 shows that the missing
implication is false for intersection complexes in general, so a proof must
use the special geometric origin of the universal hyperplane variation and
the class \(s(\zeta)\).

## Detector-span reformulation

For any collection \(\mathcal C\) of singular members, B016 defines

\[
 D_{\mathcal C}=
 \operatorname{span}_{\mathbf Q}\{\gamma_\beta:(Y,\beta)\in\mathcal C\}
 \subseteq H_{2n}^{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)}.
\]

The Hodge-Riemann pairing is nondegenerate on primitive rational Hodge
classes. Therefore \(\mathcal C\) detects every nonzero primitive Hodge class
if and only if \(D_{\mathcal C}\) is the entire primitive rational Hodge
homology. This replaces a class-by-class existence quantifier by one exact
finite-dimensional generation obligation.

For all singular members, the equality is terminal-equivalent through B007
and B010. Restricting to independent-node members gives the stronger
sufficient theorem G009.

## Current smallest attackable brick

**G009: independent-node detector generation.** Prove that the Saito classes
from every independent-node member across sufficiently high powers span

\[
 H_{2n}^{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)}.
\]

B015 makes every local summand auditable. B016 propagates span equality to
G008 and then B007 to HC. A falsifier is a nonzero primitive rational Hodge
class orthogonal to all such detector classes.

B017 proves that, for a fixed \(X\), the cumulative detector spans stabilize
and full generation is witnessed by finitely many detector classes. This is a
finite certificate form, not an effective construction: it neither bounds the
required powers nor rules out stabilization at a proper subspace. NG-014
prevents treating multiplication of defining sections as a comparison
between the individual detector spaces at different powers.

B018 imposes a further necessary design constraint. A codimension-\(n\)
complete intersection cut by powers of \(L\) has class proportional to
\(c_1(L)^n\), so its primitive projection is zero and it pairs trivially with
every primitive \(\zeta\). Thus a class-blind incidence construction cannot
close G009 by using only polarization complete intersections as its ambient
detectors. Any successful degeneration must create genuinely
non-tautological primitive homology.

B019-B020 isolate the minimal two-critical-value attempt. A symplectic
matching path glues thimbles over two distinct critical values into a
Lagrangian sphere, but it is not a simultaneous-node relation and has no
automatic Hodge type. Schnell's intersection-one pair is rationally
independent, while the nearby statement that a dual-plane node represents a
two-ODP hyperplane supplies no relation theorem. Thus the smallest new
geometric datum remains an **algebraic collision comparison**: specialize
distinct-fiber thimble data to one independent-node member, identify a
nonzero relation \(\beta\) of rational type \((0,0)\), and prove that
\(\gamma_\beta\) preserves the chosen global tube class or at least its
nonzero pairing with \(\zeta\).

The parent gate G008 remains: starting from the already nonzero global class
\(s(\zeta)\), construct a discriminant point \(p\) with

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
mechanism proposed for closing G008; if its specialization can be forced into
the B015 independent-node locus for a spanning set, it would close G009.

## Attempt audit

1. Pass to \(m\gg0\) and use B011 to choose a loop-fixed vanishing class whose
   tube detects \(\zeta\) - valid global topology.
2. Factor the loop into Picard-Lefschetz meridians. B013 proves the exact
   telescoping distributed relation among the transported vanishing cycles.
3. Fill the loop in the full projective parameter space. A generic real
   two-disk meets several separate smooth discriminant points and generically
   misses the real-codimension-four class-specific support of B012.
4. Declare the distributed cancellation to be a relation at one singular
   member - **invalid without more input**. B008 kills every smooth-point
   local channel. B015 proves the coalesced normal-crossing geometry and exact
   local IC channel when an independent-node member is already supplied, but
   it neither constructs that member from the tube nor preserves the
   class-specific pairing.
5. Replace the missing collision by a matching path - **type error**. B019
   produces a Lagrangian sphere from distinct critical fibers, not a local
   type-\((0,0)\) relation. Replace it by Schnell's intersection-one pair -
   **linear-algebra error**. B020 proves that pair is independent.

Step 4 is NG-010. Step 5 is split into NG-016 and NG-017. Inferring a nonzero local class merely from global
nonvanishing or a generic slice is NG-011. The open construction must create
a higher discriminant stratum and verify the specialization through Saito's
exact sequence; merely factoring the global monodromy or increasing slice
dimension does not do so.

The now-exact geometric sub-obligation is:

\[
\text{tube detector for }\zeta
\longrightarrow
\text{independent-node }H\text{ with }\zeta|_{X_H}\ne0.
\]

B015 controls everything local to the right-hand object. The arrow remains
terminal-equivalent because its nonzero restriction is precisely G005.

## Boundary-pullback audit

Green-Griffiths II proposes detecting singular loci as inverse images of
boundary components of partially compactified Hodge-theoretic classifying
spaces. This does not yet supply G009. Their class-directed nodal point is
constructed after assuming HC and writing
\(k_0\zeta=[W-H]\); the global boundary formula is left with an unspecified
correction term and incomplete compactification data. Treating the proposed
boundary pullback as unconditional nonemptiness is NG-013.

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
