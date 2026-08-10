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
\text{G008}\Longleftarrow\text{partitioned nodal realization G012}
\Longleftarrow\text{two-matroid incidence G013}
\Longleftarrow\text{unanchored detector spanning G014},
\qquad
\text{G008}\Longleftarrow\text{tube-to-local concentration G007}.
\]

The fixed-carrier branch now has an additional necessary local gate:

\[
\text{dimension-scaled multipart incidence}
\Longleftarrow
\text{multipart quasi-local channel G015}.
\]

G014 remains sufficient for HC but is not known equivalent to it. B034
shows that HC plus Thomas' fixed-carrier construction cannot recover G014's
two-block condition in middle dimensions \(n\ge3\): the required number of
independent blocks is asymptotically at least \(n!\).

The former fully independent-node chain G009-G011 is closed as NG-024 by
B027: its high-power relation spaces vanish for \(n\ge2\).

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
and B010. Restricting to fully independent-node members was the stronger
proposal G009, now disproved by B027.

## Current smallest attackable brick

**G013: class-paired two-matroid incidence.** Starting with a global tube or
quotient-level thimble detector for a specified nonzero primitive Hodge class,
construct a nodal member whose node set \(\Delta\) satisfies the exact
rank-function form of G012. Put \(A=L^m\),
\(F=K_X\otimes A^n\), and let \(r_A,r_F\) be the corresponding point-evaluation
ranks. B028 and Edmonds' theorem reduce partwise independence and positive
adjoint defect to

\[
 |S|\le 2r_A(S)\quad\text{for every }S\subseteq\Delta,
 \qquad r_F(\Delta)<|\Delta|.
\]

The nonzero defect supplies an extra-homology space, but a separate condition
must require the canonical map

\[
 \Phi_{Y_0}:E^\vee(Y_0)\longrightarrow
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}
\]

to have positive rank. The relation space must then carry a rational
type-\((0,0)\) element

\[
 \beta\in\ker\!\left(\bigoplus_y M_y\otimes\mathbf Q(n)
 \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n))\right)
\]

whose Saito class retains nonzero pairing with the specified Hodge class.
B025 proves that a higher isolated singularity cannot supply this relation
internally: its distinguished morsification cycles form an integral basis.
The relation must be a genuinely global failure of the local Milnor
lattices to inject into nearby-fiber homology. It must also survive the two
B022 quotients.

B026 identifies the relation dimension with extra homology, adjoint
node-evaluation defect, and local IC dimension, but not with the rank of
\(\Phi_{Y_0}\). B031 proves in arbitrarily high degree that this rank may be
zero even when all those dimensions are one, and NG-028 quarantines the
conflicting literal Green–Griffiths ambient-image equality. B027 proves why
only partwise independence is viable:
full independence propagates to the adjoint system and kills the defect at
high power in dimension at least four. B028
then proves that a minimal smoothing dependence is still insufficient: on
\(\mathbf P^2\times\mathbf P^2\), an \(A\)-evaluation circuit can remain
\(F\)-independent and have zero adjoint defect. Thus both matroid conditions
must be engineered simultaneously. B010 propagates a successful G013 pairing
through G012 and G008, then B007 to HC. A falsifier is a nonzero primitive
rational Hodge class orthogonal to every such two-matroid detector.

B029 tests the most direct positive-defect realization of that window. On
\(\mathbf P^2\times\mathbf P^2\), enough collinear points to make the adjoint
evaluation dependent force every section singular at those points to vanish
to second order along the carrier line. Hence the singular locus is not
isolated. The remaining incidence must produce adjoint dependence through
distributed support or a zero-dimensional Cayley-Bacharach mechanism while
retaining isolated first jets.

B030 shows that the two evaluation-rank and isolated-nodality requirements
are mutually compatible. A
plane-containing quintic threefold in \(\mathbf P^4\) has sixteen nodes that
split into two eight-point \((2,4)\) complete intersections, each independent
for quintics, while the full \((4,4)\) set has one-dimensional quintic—and
hence adjoint—defect. This is not a detector instance: the primitive middle
cohomology of \(\mathbf P^4\) is zero and the plane is an algebraic anchor
built into the equation. B031 extends the calculation to every degree
\(d\ge3\) and computes the canonical extra-to-primitive map as zero. The
remaining gate therefore has two independent vector-level parts after
geometric realization: positive ambient rank and class-directed nonzero
pairing.

B032 proves that those two parts are compatible with the finite geometric
conditions in a single example. A \((2,2)\) divisor in
\(\mathbf P^2\times\mathbf P^2\) containing the diagonal has seven nodes
independent for the defining system, adjoint defect one, a rank-one
extra-to-primitive map, and nonzero pairing with the primitive diagonal
component. The construction begins with that algebraic diagonal. NG-029
therefore leaves the vertical arrow unchanged: G013 must create the same
package from \(\zeta\) or a global detector without an algebraic anchor.

B033 proves the same package throughout the high-power diagonal family.
For \(k=2m\ge6\), the zeros of a general section of
\(\Omega^1_{\mathbf P^2}(k)\) have full symmetric monodromy and uniform
degree-\(k\) evaluation rank
\((k^2+3k-14)/2\). They therefore partition into two independent blocks,
while the adjoint defect and ambient rank remain one. This closes the
postulation/high-power compatibility subproblem but strengthens NG-029: the
ambient direction is still computed from the forced algebraic diagonal.
The sufficient formulation G014 asks whether canonical images from **unanchored**
two-part nodal members span primitive rational Hodge homology.

B034 prevents treating that two-block formulation as dimension-neutral.
For a fixed smooth carrier \(W^n\subset X^{2n}\), Thomas' node count is
\(d m^n+O(m^{n-1})\), while one \(L^m\)-independent block has capacity at
most \(d m^n/n!+O(m^{n-1})\). Thus two blocks are eventually impossible for
\(n\ge3\). G014 remains sufficient but is not proved equivalent to HC.
The active smallest local gate is G015: extend B009's bipartite
quasi-local relation calculation to \(q\) separately independent blocks.
B035 reduces its first genuinely new case to \(U_{2,5}\): after blowing up,
the missing calculation is global intermediate-extension hypercohomology on
an exceptional \(\mathbf P^1\) with five marked points, not the sum of its
pairwise crossing complexes. B036 proves that those five local cokernels
form \(\mathbf Q^5\) and that the required global differential can only be
\(e_i\mapsto\delta_i\), up to target isomorphism. B037 locates it as the sole transgression
\(d_2:\mathbf Q^5\to H^2(\mathbf P^1,\ker N_E)\), and B038 proves that
\(d_2(e_i)=\delta_i\). The resolved contribution is therefore the full
relation kernel. B039 proves that additional strict-support summands under
the blow-up are point-supported in ordinary degree two, so this group is
the downstairs degree-one IC stalk. NG-034 prevents using a complex
face-quiver calculation alone for the rational Hodge-type step; B040 instead
uses Saito's mixed-Hodge-module calculation to prove pure type \((0,0)\)
after \(\mathbf Q(n)\). B041 extends all four steps uniformly to
\(U_{2,r}\). B042 computes the exceptional line-incidence row and
non-semismall shifts for every \(U_{3,r}\). B043 proves the dimension-uniform
\(U_{d,r}\) theorem. B044 proves the one-dependent-flat case; B045 proves
compatibility for two nonnested dependent flats sharing a branch; and B046
proves the first nested pair in rank four. B047 proves a three-level nested
chain in rank five, and B048 proves the first fork with order-independent
child blow-ups. B049 proves G021's universal intrinsic divisor matrix for
all building sets and permissible orders; NG035 excludes raw-coordinate
order invariance. B050 proves G022's universal coefficient-sheaf induction,
and B051 proves G023's strict-support descent. B052 proves G024 and G019 for
every central representable arrangement. NG036 disproves G025's analytic
linearization, while B053 proves G026 for the exact quasi-local uniform
normal arrangement. G027 is the smallest unresolved nonlinear nonuniform
comparison needed to promote G015 as stated. Only
after a general nonuniform calculation is
proved may the fixed-carrier branch replace the two-block inequality by
\(|S|\le q r_A(S)\).

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
close the terminal gate by using only polarization complete intersections as its ambient
detectors. Any successful degeneration must create genuinely
non-tautological primitive homology.

B019-B020 isolate the minimal two-critical-value attempt. A symplectic
matching path glues thimbles over two distinct critical values into a
Lagrangian sphere, but it is not a simultaneous-node relation and has no
automatic Hodge type. Schnell's intersection-one pair is rationally
independent, while the nearby statement that a dual-plane node represents a
two-ODP hyperplane supplies no relation theorem. Thus the smallest new
geometric datum remains an **algebraic collision comparison**: specialize
distinct-fiber thimble data to one partitioned nodal member, identify a
nonzero relation \(\beta\) of rational type \((0,0)\), and prove that
\(\gamma_\beta\) preserves the chosen global tube class or at least its
nonzero pairing with \(\zeta\).

B021 tests the simplest such bridge in the only dimension covered by the
audited matching-path source. It cannot preserve the two individual cycle
classes through the cusp: the matching pair spans rank at most one, whereas
the cusp pair has intersection one and spans rank two. A viable comparison
must therefore allow braid/basis change, extra cycles, or preservation only
of the final ambient tube class. This is a local mechanism obstruction on
surfaces, not global Hodge progress.

B022 computes what “preserve the ambient class” actually means in the
generic projective-hypersurface pencil model. The thimble boundary kernel is
followed by two quotients:

\[
 \ker\partial
 \twoheadrightarrow
 \mathcal T(Y)=\ker\partial/\operatorname{im}\tau_\infty
 \twoheadrightarrow
 H_n(X)/\iota_*H_n(X_b),
\]

and the last arrow has the explicit base-locus kernel \(K\). A collision
must preserve a nonzero class after both arrows. B023 proves that pure
Hurwitz moves cannot supply the missing non-invertible step: within a fixed
fibration they preserve boundary rank and relation-kernel dimension.

For smooth projective complete intersections, B024 uses the exact sequence

\[
 0\to K\to\mathcal T(Y)\to PH_n(X)\to0
\]

to show that every nonzero primitive cohomology class has a nonzero global
quotient-level thimble detector. This verifies the source of the proposed
collision in that special setting. It does not localize the detector, give it
Saito type \((0,0)\), make it algebraic, or reduce arbitrary varieties to
complete intersections.

B025 further excludes Milnor-number amplification as a shortcut. The
\(\mu\) distinguished vanishing cycles of one isolated hypersurface
singularity are a basis of its rank-\(\mu\) Milnor lattice, so no local
relation appears merely by colliding Morse points. The next audit must study
global incidence or defect formulas controlling the kernel of the
local-to-global Milnor map, with the kernel vector prescribed by the global
detector rather than found only by dimension count.

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
mechanism proposed for closing G008; its specialization must now be forced
into the B028 two-matroid window required by G013.

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
   local IC channel when a controlled nodal member is already supplied, but
   it neither constructs that member from the tube nor preserves the
   class-specific pairing.
5. Replace the missing collision by a matching path - **type error**. B019
   produces a Lagrangian sphere from distinct critical fibers, not a local
   type-\((0,0)\) relation. Replace it by Schnell's intersection-one pair -
   **linear-algebra error**. B020 proves that pair is independent.
6. Collide the matching endpoints through the cusp while preserving the two
   fiber classes - **rank error**. B021 shows that rank one cannot specialize
   class by class to the intersection-one rank-two cusp lattice.
7. Preserve merely a zero-boundary thimble combination - **quotient error**.
   B022 shows that equator extensions and base-locus classes can kill it
   before it reaches ambient primitive homology.
8. Repair the mismatch by Hurwitz moves alone - **invariance error**. B023
   shows that invertible moves in a fixed fibration preserve the relation
   kernel.
9. Use complete-intersection thimble surjectivity as algebraicity -
   **category error**. B024 generates primitive homology topologically, not
   local Hodge detectors or algebraic cycles.
10. Use one higher isolated singularity as an internal relation - **basis
    error**. B025 proves that its morsification cycles form a Milnor basis.
11. Impose full node independence to obtain the cleanest local model -
    **defect-annihilation error**. B026-B027 prove that in dimension at least
    four at high power this forces the adjoint defect and relation space to
    vanish. Only partwise independence remains viable.
12. Replace full independence by a circuit of the smoothing evaluation
    matroid - **two-matroid error**. B028 gives an explicit
    \(\mathbf P^2\times\mathbf P^2\) configuration that is minimally dependent
    for \(A\) but independent for the adjoint system \(F\), hence has no
    defect. G013 must impose both rank systems.
13. Force the second rank condition by putting enough points on one line -
    **isolation error**. B029 shows that the first normal jet then vanishes
    along the line, producing a positive-dimensional singular locus rather
    than a nodal member.
14. Replace the line by a plane complete intersection - **geometrically
     valid but class-blind**. B030 realizes nodality, the two-part partition,
     and defect one, but its ambient primitive Hodge target is zero and the
     construction starts from a contained algebraic plane.
15. Infer a nonzero ambient detector from positive extra homology -
    **map-kernel error**. B031 gives a one-dimensional extra-homology source
    whose canonical map to primitive ambient homology is zero.
16. Restore injectivity by taking higher degree - **ampleness error**. B031's
    plane-containing family exists for arbitrarily large degree; NG-028
    quarantines the conflicting literal six-invariant source statement.
17. Use the diagonal positive-rank witness for an arbitrary class -
    **algebraic-anchor error**. B032's ambient detector is precisely the
    primitive projection of the diagonal forced into the divisor. NG-029
    requires a non-circular replacement.

Step 4 is NG-010. Step 5 is split into NG-016 and NG-017; step 6 is NG-018;
steps 7-8 are NG-019 and NG-020; step 9 is NG-021; step 10 is NG-022;
step 11 is NG-024; step 12 is NG-025; and step 13 is NG-026. Step 14 is a
special-family checkpoint, not a NO-GO or general advance.
Inferring a nonzero local class merely from global
nonvanishing or a generic slice is NG-011. The open construction must create
a higher discriminant stratum and verify the specialization through Saito's
exact sequence; merely factoring the global monodromy or increasing slice
dimension does not do so.

The now-exact geometric sub-obligation is:

\[
\text{tube detector for }\zeta
\longrightarrow
\text{two-matroid nodal }H\text{ with }\zeta|_{X_H}\ne0.
\]

B009 controls the quasi-local relation channel on the right-hand object. The arrow remains
terminal-equivalent because its nonzero restriction is precisely G005.

## Boundary-pullback audit

Green-Griffiths II proposes detecting singular loci as inverse images of
boundary components of partially compactified Hodge-theoretic classifying
spaces. This does not yet supply G013. Their class-directed nodal point is
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
