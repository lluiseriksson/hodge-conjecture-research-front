---
brick_id: B271
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22, primitive ruling difference zeta=a-b, cubic A=O_Q(3), H=O_Q(6), and a hypothetical G190 marked scheme
smoothness: Q^d and the reduced marked scheme are smooth; the auxiliary blow-up of the isotropic plane at six distinct points is a smooth weak del Pezzo surface of degree three; no central ODP package is constructed
projectivity: the complete cubic and sextic systems, plane blow-up, anticanonical morphism, double-neighborhood restrictions, and marked point span are projective
dimension: dim X=d=2n>=22; cubic equality would have h_Z(1)=7d+5 and N=2(7d+5); the planar anticanonical surface has dimension two and degree three
codimension: the primitive codimension-n ruling difference supplies a universal test input; the theorem excludes the cubic polarization from G190 but does not close the quartic or low-dimensional square branches
coefficient_field: Q for zeta and C for sections, jets, blow-ups, roots, and anticanonical maps
cohomology_theory: rational singular cohomology, coherent first-jet restriction, plane blow-up intersection theory, and rational-double-point resolution geometry
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B270, G190, NG222-NG226, S081, S084
claim: Every planar cubic equality configuration surviving B264 is forced to consist of three supports on each of two lines through the seventh point. B269 then shows that no eighth tangent osculator is absorbed, contradicting G190's N=2(7d+5)>7 marked supports. Hence A=O_Q(3) cannot realize G190 for any even d>=22.
falsifier: a planar cubic equality configuration whose six points do not split into complementary collinear triples through u, an effective irreducible (-2)-curve on the six-point blow-up outside the line/conic list, zero anticanonical differential away from an A2 intersection, an absorbed eighth double after the 3+3 classification, or a cubic G190 package on a valid even quadric
---

# B271 — Planar cubic equality is necessarily \(3+3\)

Assume that the cubic polarization survives G190 on a split even
quadric. B264 puts six independent double supports \(P_6\) and the
seventh point \(u\) in one isotropic plane \(\Pi\). B260 chooses \(u\)
outside the four-point hard line, so the good-edge graph on \(P_6\)
has a perfect matching. Its three pair lines give a cubic \(C_0\)
through \(P_6\) with \(C_0(u)\ne0\).

## Equality gives rank-one plane jets

The six double neighborhoods have total rank \(6d+6\). Their plane
part has rank at most 18 and their normal part at most \(6(d-2)\);
equality forces both maxima.

Degree-five plane values at \(P_6\) are independent: to isolate one of
six reduced points, multiply five lines, each through one of the other
points and avoiding the target. The cubic \(C_0\), times a quadratic
unit, separates \(u\) from \(P_6\). Hence the degree-five value map on
\(P_6\cup\{u\}\) has rank seven. The conormal quotient used in B268
therefore supplies all \(d-2\) normal residual directions at \(u\).

Cubic equality has total residual rank \(d-1\), so the residual plane
sextic image has rank exactly one. B270 now implies that the cubic
system through \(P_6\) has projective differential zero at \(u\).

## The degree-three weak del Pezzo surface

No four points of \(P_6\) are collinear. Indeed, four double points on
one line impose at most seven tangential value/derivative conditions
along the degree-six restriction and four normal-to-line derivatives,
for rank at most 11; the other two doubles contribute at most six, so
the plane rank would be at most 17 rather than 18.

Blow up the six distinct points:

\[
 \pi:S=\operatorname{Bl}_{P_6}\mathbf P^2\longrightarrow\mathbf P^2,
 \qquad -K_S=3H-\sum_{i=1}^6E_i,\qquad K_S^2=3. \tag{1}
\]

The no-four-collinear condition is precisely the remaining
almost-general-position condition for six distinct points, so \(S\)
is a weak del Pezzo surface and \(|-K_S|\) is the cubic system through
\(P_6\). By S084, its anticanonical morphism

\[
 \phi:S\longrightarrow S_{\mathrm{ac}}\subset\mathbf P^3 \tag{2}
\]

is the minimal resolution of a normal cubic surface, is an isomorphism
off the \((-2)\)-curves, and has the fundamental cycles as its
schematic nontrivial fibers.

## All effective roots are lines or one conic

Let an irreducible nonexceptional \((-2)\)-curve have class

\[
 eH-\sum_{i=1}^6m_iE_i,\qquad e,m_i\ge0. \tag{3}
\]

The root equations are

\[
 \sum m_i=3e,\qquad \sum m_i^2=e^2+2. \tag{4}
\]

Cauchy gives \(9e^2\le6(e^2+2)\), hence \(e\le2\).
For \(e=1\), equations (4) force three \(m_i=1\); the curve is a line
through three points. For \(e=2\), they force all six \(m_i=1\); the
curve is an irreducible conic through all six. Distinct ordinary
blow-ups create no effective exceptional difference \(E_i-E_j\).

An irreducible conic through all six cannot coexist with a three-point
line by Bézout. Two three-point lines meet on \(S\) exactly when their
triples are disjoint; then their intersection number is one. Thus every
connected fundamental cycle is of type \(A_1\) or \(A_2\).

## Zero differential forces complementary triples

Let \(\widetilde u\in S\) be the lift of \(u\). B270 says
\(d\phi_{\widetilde u}=0\). It cannot lie off the exceptional locus,
where \(\phi\) is an isomorphism.

For an \(A_1\) fiber, or at a smooth point of an \(A_2\) fiber, the
fundamental-cycle ideal has a local linear generator, so the
anticanonical differential has positive rank. At the transverse
intersection of the two reduced components of an \(A_2\) fiber, the
fiber ideal is locally \((st)\subset(s,t)^2\), and the differential is
zero. Therefore \(\widetilde u\) is the intersection of two
\((-2)\)-curves forming an \(A_2\) fiber.

Those curves are strict transforms of two lines through complementary
triples of \(P_6\). Their plane intersection is \(u\). Hence

\[
 P_6=\{p_1,p_2,p_3\}\sqcup\{q_1,q_2,q_3\}, \tag{5}
\]

with each triple collinear on one of two distinct lines through \(u\).

## Exclusion of cubic equality

B269 applies to every configuration (5): any eighth distinct double
neighborhood raises the rank above \(7d+5\). But B196's lower-profile
extinction in a G190 equality candidate absorbs the tangent osculator
of every marked support into the same rank-\((7d+5)\) span, while

\[
 N=2(7d+5)>7. \tag{6}
\]

This contradiction excludes \(A=O_Q(3)\) for every even \(d\ge22\).
The quartic branch and the low-dimensional square branch remain open.
No detector, specified pairing, algebraic cycle, proof, or disproof of
HC is produced.
