# Research frontier

## Active gate: G031

For a specified nonzero primitive rational Hodge class \(\zeta\), construct
one Li-clean multipart nodal member and a rational type-\((0,0)\) relation
\(\beta\) whose Saito ambient class satisfies
\(\langle\zeta,\Phi(\beta)\rangle\ne0\). Equivalently, force the
class-specific local support to meet the controlled clean nodal locus.

B055 proves why an equisingular monodromy argument cannot supply this
specialization. Whenever the relation spaces and Saito ambient maps form a
morphism to the constant primitive homology of \(X\), their image subspace is
constant on each connected incidence stratum. NG037 records the failed
route. B056 then localizes every global detector to a two-parameter net, and
B057 identifies its distributed Picard-Lefschetz relation with the actual
extension chain. NG038 proves that replacing this loop by a complete
pencil's total equator kills the class in the first B022 quotient. G030 must
retain the genuine non-equator loop or construct a transverse defect class.
B058 also removes the ambient Hodge-type ambiguity: choose a rational
type-\((0,0)\) primitive homology target pairing with \(\zeta\), then lift
that exact target through B011's surjective tube map. G030 asked that a
collision recover this particular target exactly. B059 proves that exact
recovery is sufficient but strictly stronger than B010's required nonzero
pairing, and NG039 prevents treating it as the terminal minimum. G030 remains
a possible stronger mechanism; G031 records the actual clean-nodal pairing
obligation. Its decisive unknown is still class-controlled incidence, not
linear algebra.

## Duality correction at the active local target

B134 audits Saito equations (0.3)-(0.5) against the de
Cataldo-Migliorini local invariant. The cohomological stalk is

\[
 E(Y_p)=R(Y_p)^\vee,
\]

and the specified incidence coordinate is the functional
\(\beta\mapsto\langle\zeta,\gamma_\beta\rangle\). The local-arrangement
kernel calculations are polarized homological models of this dual channel.
NG107 forbids using \(R(Y_p)\ne0\) as proof that the functional is nonzero.
This correction sharpens G088 but does not reduce its terminal-equivalent
existence content.

B135 gives the exact normal-crossing residue coordinate. If
\(\operatorname{Res}_{D_i}\nabla\widetilde\nu_\zeta=a_i\delta_i\), then

\[
 s_m(\zeta)_p=[a]\in\operatorname{coker}\Delta^\ast
 \simeq(\ker\Delta)^\vee.
\]

At the smallest proportional pair \(\delta_2=c\delta_1\), survival is
exactly \(c a_1-a_2\ne0\). G089 is the falsifiable two-branch construction
gate. The attempted inference from nonzero individual residues fails:
\(q(1,c)\) is a nonzero coboundary, recorded as NG108.

B136 then closes G089 as a **high-power** mechanism. Relative Serre
vanishing over \(\operatorname{Hilb}^k(X)\) proves that, for every fixed
\(N\), all node schemes of length at most \(N\) impose independent
conditions on \(L^m\) once \(m\) is large. B027 forces their adjoint defect
and relation channel to vanish. NG109 records the general bounded-node
failure. The next scalable clean gate is therefore G013: its multipart node
count must grow with \(m\), satisfy the two-matroid/isolated-jet conditions,
and carry a nonzero B135 residue-cokernel class.

B137 makes the growth obligation quantitative. Fix a very ample \(H\), take
\(c\ge0\) with \(K_X\otimes H^c\) globally generated, and write
\(A_m=H^m\). S056 and generic projection force a degree-\(mn-c\) dependent
set with at most \(2(mn-c)+1\) points to contain \(mn-c+2\) collinear
points. Uniform conormal bounds for \(H\)-lines then force the whole line
into the singular locus. Hence any isolated-nodal G013 detector must have

\[
 |\Delta_m|\ge2(mn-c)+2.
\]

NG110 closes all slower growth. B138 also resolves the former equality
boundary. It extracts a minimal
\(\mathrm{CB}(mn-c)\) circuit and applies S057, which places every such
circuit of at most \(3(mn-c)-1\) points on a degree-at-most-two curve. The
line/conic first-jet audit forces that carrier into the singular locus.
Consequently

\[
 |\Delta_m|\ge3(mn-c).
\]

NG111 closes that smaller range. B139 then applies S058's \(h=4\) theorem
and audits all integral and reducible cubic carriers. Uniform first-jet
bounds on their normalizations force a positive-dimensional singular locus
whenever \(|\Delta_m|\le4(mn-c)-5\). Consequently

\[
 |\Delta_m|\ge4(mn-c)-4.
\]

NG112 closes that smaller range. B140 next uses S059 and a uniform
component-separation lemma for every reduced curve of degree at most four.
An occupied integral component of degree \(e\) carries
\(e(mn-c)-O(1)\) circuit points, so uniform first-jet bounds force it into
the singular locus. Thus

\[
 |\Delta_m|\ge5(mn-c)-10.
\]

NG113 closes that smaller range. B141 applies S060 for an arbitrary fixed
carrier degree \(E\). B140's uniform component lemma excludes the resulting
carrier, giving

\[
 \frac{|\Delta_m|}{mn-c}\longrightarrow\infty.
\]

NG114 therefore closes every fixed linear node budget. This is not counted as a new
sufficient reduction: isolated nodality at the new boundary, the two-matroid
inequalities, the ambient-map rank, and the specified B135 pairing all remain
unproved.

B142 supplies the first positive witness beyond that quantitative boundary.
For every \(n\ge2\), a general \((m,m)\) divisor in
\(\mathbf P^n\times\mathbf P^n\) containing a product fiber has \(m^n\)
isolated nodes. Its smoothing matroid is uniform and partitions into the
asymptotically optimal \(n!\) blocks; its adjoint defect and primitive
ambient rank are both one, and the fiber pairs nontrivially with the
primitive Hodge line. This proves that superlinear node growth and the
finite rank conditions are mutually compatible. It does not prove the
nonlinear Li-clean hypothesis, a canonical nonzero B135 residue, or any
unanchored construction from an arbitrary \((X,\zeta)\).

B143 closes the first two caveats in this special family. The moving-fiber
incidence is smooth of codimension \(R_m\) and lies in every labeled node
branch. Uniformity makes every \(R_m\)-fold intersection smooth of the same
codimension, hence equal to that incidence germ; all deeper intersections
coincide with it. The discriminant is therefore Li clean, B054 applies, and
B142's unique nonzero primitive pairing gives a nonzero B135 functional.
The sole surviving general obstruction is the algebraic anchor: no theorem
constructs this incidence from an arbitrary \((X,\zeta)\).

B144 isolates the exact geometric replacement for that anchor in the clean
calculation. If the node-branch conormals are uniform of rank \(R\), one
smooth codimension-\(R\) germ contained in every branch forces the whole
nonlinear discriminant arrangement to be Li clean. G090 asks for this
saturated germ together with the nonzero class pairing on an arbitrary
variety. NG115 closes the first unanchored shortcut: B132's filtered section
is constant and nonzero, hence has empty zero locus, while its ordinary
survival locus is precisely the unresolved G088 support and carries no
automatic nodal or smooth-stratum structure.

B145 computes the universal ordered-node tangent space. The nondegenerate
node Hessians eliminate node motion uniquely, so the projected tangent is
exactly the kernel of value evaluation. Consequently a smooth incidence
point of codimension \(2nN+R\) produces B144's saturated codimension-\(R\)
germ without mentioning a carrier. G091 is the resulting class-directed
excess-incidence gate. NG116 closes the generic attempt: first-jet
surjectivity gives \(R=N\), and B027-B028 then force zero adjoint defect and
zero local relation.

B146 computes the first obstruction beyond that tangent calculation. After
eliminating each moving critical point, the local smoothing functions have
Hessian

\[
d^2\tau_i(a,b)=-da_{p_i}(H_i^{-1}db_{p_i}).
\]

Every value relation must annihilate this Hessian on the tangent kernel. A
uniform \(U_{R,N}\) relation therefore forces conditional-gradient corank
at least \(n(R+1)\). G092 is the refined gate: construct this common
isotropic degeneracy, integrate it to a reduced smooth height-\(R\)
smoothing ideal, and retain the specified nonzero Saito pairing. NG117
closes value-rank drop without that second degeneracy.

G032 separates the extra cleanup content from terminal support nonemptiness:
starting with any detecting singular member, deform it to the Li-clean nodal
locus while preserving a nonzero pairing. The first attempt fails. By B025,
generic morsification yields a basis of the local Milnor lattice rather than
a relation, and B008 makes every separate Morse discriminant point locally
invisible in the required degree. NG040 records this NO-GO. A viable cleanup
must deliberately recollide the Morse data and compute the global
local-to-nearby kernel and ambient pairing.

## Adversarial audit: claimed general proof

S040 audits Bouali's arXiv:2401.03465v13 and its decisive dependencies.
The final degeneration argument invokes an arithmetic Hodge-locus theorem
whose proof runs through a claimed universal Tate theorem. On pp. 34-35 of
arXiv:2303.09932v16, that proof constructs a cycle only over a p-adic
completion \(\widehat{k}_{\sigma_p}\), then averages \(gZ\) under
\(\operatorname{Gal}(\bar k/k)\) without proving that \(Z\) is defined over
\(\bar k\) or a finite extension. B060 proves the field-of-definition guard
with a transcendental \(\mathbf Q_p\)-point of \(\mathbf P^1\), and NG041
quarantines the claimed proof. This audit changes no estimate of actual
general-Hodge progress.

## Closed local gate: G015

G015 extended B009's quasi-local identification of degree-one local
intersection cohomology with the full vanishing-cycle relation kernel from a
bipartition to \(q\) independently smoothable blocks under the explicit
Li-clean arrangement hypothesis. B034 made the extension necessary;
B035-B054 prove it, including the rational type-\((0,0)\) comparison.

B035 fixes the first new test case. Five distinct lines through the origin
of a two-dimensional smoothing slice have matroid \(U_{2,5}\), with a
\(2+2+1\) independent-block partition and no two-block partition. One
blow-up replaces the origin by \(E\simeq\mathbf P^1\) with five marked
crossings. Although \(N_E=\sum_iN_i\) and every local product \(N_EN_i\)
vanishes, NG-033 forbids replacing global hypercohomology on that marked
exceptional curve by the separate crossing stalks.
B036 quantifies the omitted gluing. Each of the five crossing cokernels is
one-dimensional, while their desired global relation subspace is

\[
 \ker\!\left(\mathbf Q^5\xrightarrow{e_i\mapsto\delta_i}
 \operatorname{span}\{\delta_i\}\right).
\]

Thus the missing exceptional differential must be the vanishing-cycle map,
up to target isomorphism. B037-B038 derive that map from the resolved
logarithmic intermediate-extension complex rather than merely postulate the
kernel demanded by G015.

B037 locates the map as the sole transgression

\[
 d_2:\mathbf Q^5\to H^2(\mathbf P^1,\ker N_E)\simeq\ker N_E
\]

in the exceptional hypercohomology spectral sequence. The resolved
contribution is the relation kernel precisely if this transgression is the
vanishing-cycle map followed by an injection of its span. NG-034 records a
separate type obstruction: S035's complex face algebra can compute the
perverse extension but cannot by itself prove rational type \((0,0)\).

B038 computes the transgression using the logarithmic residue sequence:

\[
 d_2(a_1,\ldots,a_5)=\sum_i a_i\delta_i.
\]

Therefore the resolved \(U_{2,5}\) exceptional contribution is the full
rational relation kernel. B039 proves that the shifted proper direct image
is perverse and splits by strict support into the downstairs IC and a
point-supported term. Undoing the surface shift places the point term in
ordinary degree two, so degree one is canonically the downstairs IC stalk.
The rational type-\((0,0)\) and Tate-twist comparison for this group is
closed by B040 using Saito's normal-crossing
mixed-Hodge calculation: the five crossing groups are \(\mathbf Q(0)\), and
the exceptional relation kernel is their type-\((0,0)\) sub-Hodge structure.
B041 proves the same statement for every \(U_{2,r}\) central line
arrangement. B042 then computes \(U_{3,r}\): the pair-point stalk is the
direct sum of its two incident line generators, the residue map is
\(e_i\mapsto\delta_i\), and non-semismall point summands occur only in
ordinary degrees \(2,3,4\). B043 extends the calculation to every simple
uniform \(U_{d,r}\): point-supported terms range from ordinary degree \(2\)
to \(2d-2\), never degree one.

The first nonuniform subgate G016 is closed by B044. On
\(\operatorname{Bl}_p\mathbf P^2\), the exceptional-flat residue coefficient
is forced to the partial triple sum, and the remaining equation is exactly
the full seven-cycle relation. Flat-supported direct-image summands begin in
ordinary degree two.

G017 is closed by B045: the two exceptional equations occupy independent
divisor classes and merely assign their two partial cycle sums, despite the
shared branch. The full relation equation remains unchanged.

B046 closes G018 for one nested pair. On
\(\operatorname{Bl}_{\widetilde\ell}\operatorname{Bl}_p\mathbf P^3\),
the exceptional coefficients are forced to the partial sums on the nested
flats, while the global equation remains the full vanishing-cycle relation.
The two flat supports and the origin begin in ordinary degree two.

B047 proves the first three-level chain. Its exact rank-five arrangement has
eleven branches, only four nontrivial connected flats of ranks
\(2<3<4<5\), and a three-block independent partition. The point-line-plane
wonderful fiber gives four triangular residue equations, while every lower
support begins in ordinary degree two.

B048 closes G020. Exact rank enumeration verifies the fork and its
three-block partition. The parent blow-up separates the two child planes, so
their blow-ups commute; both orders give the same global, parent, and child
residue equations. Every lower support begins in ordinary degree two.

B049 closes G021's order-independent geometric induction. Every wonderful
fiber has intrinsic Picard basis \(h,(e_F)\), every strict branch has class
\(h-\sum_{F\subset H_i}e_F\), and the geometric residue matrix is triangular.
NG035 records the failure of the stronger raw-exceptional-coordinate claim.
B050 closes G022: the origin residue anchors the arbitrary-SNC quotient,
giving the branch and flat coefficient sheaves with no higher sheaves and
with rational type \((0,0)\). B051 closes G023, and B052 closes G024 and
G019: the only total-degree-one
arrow is B049's divisor-class residue map, whose kernel is the full rational
type-\((0,0)\) relation space. NG036 disproves G025's analytic-linearization
claim using five quasi-local curved branches with a quadratic modulus. B053
proves G026 by the common-stratum blow-up. B054 then proves G027 and G015:
Li's clean-transform induction identifies every nonlinear central fiber with
its labelled tangent wonderful model, so the full multipart relation channel
survives. G028-G029 are the class-paired incidence and transport parents.
B055/NG037 exclude equisingular monodromy. B056-B057 put the actual detector
and its extension chain in one plane net, while NG038 excludes the total
pencil equator. B058 lets the ambient tube target itself be chosen rational
type \((0,0)\). B059/NG039 show that preserving that exact target is stronger
than necessary. B125 makes G031 exactly a clean support-incidence problem.
B127/NG102 split G084 into active terminal support gate G008 plus conditional
cleanup G085. B126/NG101 exclude performing that cleanup inside a suspended
$A_2$ local versal slice.

B128 computes G008's exact two-row edge sequence. Empty local support means
that the nonzero global incidence class lies entirely in
\(H^1(P_m,\mathcal H^{-d_m}K_m)\). G086 is the class-specific escape
exclusion. B129/NG103 strengthen B014: even on every projective space, a
full-support geometric polarizable weight-\(-1\) IC can have a nonzero
rational type-\((0,0)\) \(IH^1\) class and zero local target sheaf. Therefore
the next proof must use the exact universal-incidence origin of
\(s_m(\zeta)\), not only projectivity, purity, hard Lefschetz, or Hodge type.

B130 now audits the strongest immediate incidence-specific input. Nori
connectivity and Brogan Corollary 4.1 place the primitive \((r,r)\) component
in \(\mathcal H^{-d+1}\operatorname{gr}^{F}_{-r}\operatorname{DR}(M)\).
NG104 shows that this is not the local Betti sheaf: on \(P^{\rm sm}\), the
ordinary degree-\(-d+1\) de Rham cohomology vanishes while the Higgs-graded
cohomology can be nonzero. B131 proves the canonical rational first-Leray
transgression is nonzero. B132 uses projective strictness on full \(P_m\) to
realize the specified incidence class as a nonzero filtered section. NG105
closes the smooth-open and arbitrary-splitting comparisons. G088 is the
resulting filtered incidence boundary-survival gate. B133 computes its
minimal normal-crossing two-branch target: it is nonzero only when the two
vanishing cycles are proportional. NG106 closes the generic independent
double-node shortcut.

## Sufficient parent: G014

For each smooth projective complex variety in the middle-degree reduction,
prove that the canonical primitive images of unanchored high-power nodal
relations satisfying B028's two-part condition span primitive rational Hodge
homology. By B016, failure is witnessed by a nonzero primitive rational Hodge
class annihilating every such image; success gives the class-specific
detector required by G008. The word *unanchored* forbids first choosing an
algebraic cycle with the desired primitive class.

G013 remains the geometric parent. Its exact conditions are:

For an arbitrary polarized smooth projective \(2n\)-fold, a specified
primitive rational Hodge class, and a nonzero global tube or quotient-level
thimble detector, construct a nodal incidence component whose node set
\(\Delta\) lies in B028's exact two-matroid window. With
\(A=L^m\), \(F=K_X\otimes A^n\), and evaluation ranks \(r_A,r_F\), require

\[
 |S|\le 2r_A(S)\quad(S\subseteq\Delta),
 \qquad r_F(\Delta)<|\Delta|.
\]

The first condition is exactly the existence of a partition into two
independently controlled node blocks; the second is positive adjoint defect.
Independently require the canonical map from the resulting extra homology to
primitive ambient homology to have positive rank. Only then can a rational
type-\((0,0)\) relation retain nonzero pairing with the specified Hodge class
and survive the equator-extension and base-locus quotients. G012 is the
parent partitioned-nodal gate and G008 is the terminal-equivalent support
gate. B027 excludes full independence, B028/NG-025 exclude the tempting
replacement by a mere circuit of the smoothing matroid, and B031/NG-027
exclude inferring ambient rank from positive defect. B032 proves the complete
rank package in one low-degree anchored example. B033 proves it for every
diagonal-containing \((m,m)\) family with \(m\ge3\), using full symmetric
monodromy to obtain a uniform smoothing matroid and two-block partition.
NG-029 forbids using the preselected diagonal for the arbitrary-class step;
NG-030 forbids replacing B033's full monodromy by double transitivity alone.
G014 is sufficient for rational HC, but no reverse implication is proved.
B034 blocks the standard attempt to obtain that reverse arrow from an
algebraic carrier while retaining two blocks.

Attack ledger:

1. B049-B054 close the universal clean multipart local channel, including
   divisor geometry, coefficient sheaves, support descent, and Hodge type.
2. Replace the two-block constraint by Edmonds'
   \(|S|\le q r_A(S)\), with \(q\) allowed to scale at least as \(n!\) in
   fixed-carrier constructions.
3. Construct an algebraic incidence component satisfying the multipart
   inequalities and the independent condition \(r_F(\Delta)<|\Delta|\);
   then prove it actually occurs as the node set of a hypersurface member.
4. Use B056-B058 to keep a Hodge-targeted detector loop and its extension
   chain in a generic plane net; NG038 forbids replacing it by a total
   pencil equator.
5. Construct G031's topology-changing specialization into G015's proved
   clean multipart target, preserving nonzero pairing with \(\zeta\). Exact
   recovery of the B058 target is optional stronger mechanism G030.
6. Audit boundary/intersection constructions that define a global incidence
   class without using an algebraic representative of \(\zeta\); NG-013
   excludes the HC-dependent Green-Griffiths construction.
7. Require every proposed incidence source to have a non-tautological
   primitive ambient class; B018/NG-015 exclude complete intersections of
   polarization divisors as detectors.
8. Test an algebraic collision bridge from distinct-fiber matching thimbles
   to one partitioned nodal Saito relation; B019/NG-016 show that the
   symplectic matching-path theorem does not provide this bridge.
9. Do not treat intersection-one pairs as relations; B020/NG-017 prove the
   opposite for Schnell's pair and leave the two-ODP relation computation
   open.
10. Compute any collision on the full vanishing-cycle complex. B021/NG-018
   rule out preserving a matching pair class by class through the cusp
   lattice; only basis change, extra cycles, or ambient-class preservation
   remain possible.
11. Track the class through the two exact quotients in B022. A kernel relation
   can die as an equator extension or in the pencil base-locus kernel;
   NG-019 forbids calling it an ambient detector earlier.
12. Require a non-invertible topology-changing comparison. B023/NG-020 show
    that Hurwitz moves inside a fixed fibration preserve the relation kernel
    and cannot close the matching/cusp gap.
13. Use B024 as a positive source-side checkpoint for complete intersections:
    global quotient-level thimble detectors exist, but NG-021 forbids
    counting them as local or algebraic.
14. Do not seek the required relation inside one isolated singularity's
    Milnor lattice. B025 proves its morsification cycles form a basis;
    NG-022 forces the relation into the global local-to-nearby-fiber kernel.
15. Use B026's equality of relation, extra-homology, coherent, and local
    defect dimensions only as a consistency test. B031/NG-027 forbid
    coercing a nonzero extra space into a nonzero primitive ambient image;
    NG-023 separately forbids promoting a nonzero image to a prescribed
    pairing.
16. Enforce B027/NG-024: full independence is fatal in dimension at least
    four at high power; only partwise independence may be imposed.
17. Enforce B028/NG-025: a circuit for \(A\)-evaluation may remain independent
    for adjoint \(F\)-evaluation, so smoothing dependence is not defect.
18. Enforce B029/NG-026: adjoint dependence obtained by overloading one
    low-degree line forces a nonisolated singular locus; first-jet nodal
    realizability is independent of both evaluation-rank conditions.
19. Use B030 only as a compatibility witness: its plane-containing quintic
    realizes isolated nodes and both matroid conditions, but has no primitive
    ambient class and begins with an algebraic anchor.
20. Carry \(\operatorname{rank}\Phi_Y>0\) as a third independent incidence
    condition. B031 proves it does not follow from the two evaluation ranks.
    NG-028 also forbids recovering it from the literal printed
    Green–Griffiths \(\rho(ii)\) equality without a documented resolution of
    that source conflict.
21. Use B032 as the positive compatibility test for all three ranks and the
    pairing, but enforce NG-029: its diagonal is an algebraic anchor and
    cannot be used in the class-selection step.
22. Keep the type-\((0,0)\), rational, and unipotent conditions explicit;
   nodal fibers satisfy them automatically, arbitrary singularities do not.
23. Keep the semiregularity gate G004 as an independent secondary route.

If support realization fails, record whether the obstruction is an empty
local edge support, nonexistence of the required higher discriminant
incidence, loss of the tube class under specialization, loss of Hodge type,
or annihilation by the class-specific pairing. Do not promote a favorable
family.

## Latest bricks

B016 proves the detector-span equivalence, and B017 reduces full generation
for a fixed variety to a finite detector certificate without constructing
one. G009 was the independent-node generation gate, but B027 now closes it
as NG-024.
Green-Griffiths II supplies a
boundary-class program but its class-directed nodal construction assumes HC,
recorded as NG-013. NG-014 blocks naïve detector transfer between powers.
B018/NG-015 show that class-blind tautological complete intersections cannot
provide primitive detectors. B019/NG-016 distinguish symplectic matching
spheres from one-fiber Hodge detectors; B020/NG-017 show that Schnell's
intersection-one pair is independent rather than relational. B021/NG-018
add a rank obstruction to the direct matching-pair-to-cusp specialization.
B022/NG-019 identify the two quotient kernels between a thimble relation and
ambient homology. B023/NG-020 exclude pure Hurwitz basis change as a repair.
B024/NG-021 show that complete-intersection primitive homology is globally
detected by the quotiented thimble group without providing local Hodge
detectors or algebraicity. B025/NG-022 prove that a higher isolated
singularity contributes a local Milnor basis, not an internal relation.
B026 equates the nodal relation, extra-homology, coherent, desingularization,
and local-IC defect dimensions while keeping the ambient map separate.
B031/NG-027 prove that the map may be zero; NG-023 then records that even a
nonzero image need not select the prescribed pairing. B027/NG-024
close G009-G011: full independence forces zero high-power defect for
\(n\ge2\). G012 replaces them with B009's partitioned quasi-local model.
B028 applies Edmonds' matroid-partition theorem to make that model exact:
partwise smoothing independence is equivalent to all inequalities
\(|S|\le2r_A(S)\), but adjoint dependence is a second rank condition. Its
explicit \(\mathbf P^2\times\mathbf P^2\) configuration shows that a smoothing
circuit need not have adjoint defect (NG-025). G013 is the geometric parent,
and G014 is a sufficient unanchored two-block span theorem. B034 shows that
the standard fixed-carrier route needs asymptotically at least \(n!\)
blocks. B049-B054 now close G015's multipart relation channel under the
explicit clean-arrangement hypothesis. B055/NG037 then show that
equisingular monodromy cannot enlarge one fixed ambient image. B056-B057
localize and identify the detector chain, NG038 kills the total-equator
shortcut, and B058 chooses its ambient target in rational Hodge homology;
G031 is the clean-nodal pairing parent, and B125 isolates G084 as its exact
support-incidence subprogram. B127/NG102 restore G008 as the active
terminal-equivalent gate and isolate G085 as conditional cleanup.
B059/NG039 show that G030's
exact class recovery is an optional stronger mechanism. B124/NG100 further
prove that Saito relative-lift ambiguity cannot tune a fixed relation to that
preselected target, so G065 remains inside the stronger G030 branch.
B029/NG-026 test the
first collinear positive-defect configuration and show that it is singular
along its carrier line. The next construction must obtain adjoint dependence
from distributed or genuinely zero-dimensional incidence while preserving
isolated first jets. B030 proves that the full geometric rank package is
nonempty for a plane-containing quintic, but the ambient primitive middle
space is zero and its plane is a built-in algebraic anchor. B031 extends the
calculation to plane-containing hypersurfaces of every degree \(d\ge3\):
their extra spaces have dimension one and their canonical ambient maps are
zero. This proves that ambient rank is genuinely independent and quarantines
the conflicting literal Green–Griffiths \(\rho(ii)\) equality as NG-028.
B032 supplies the complementary positive case: its diagonal-containing
\((2,2)\) divisor has seven defining-system-independent nodes, adjoint defect
one, rank-one ambient image, and nonzero primitive pairing. Thus the complete
finite-rank package is geometrically compatible. NG-029 records why this is
not general progress: the desired detector is the primitive component of the
preselected algebraic diagonal. B033 removes the low-degree exception by
proving the full package for every \(m\ge3\), including the two-block
partition via full symmetric monodromy. The unresolved content is now sharply
class-specific and non-circular: produce such incidence from a global
detector without presupposing an algebraic representative.
G008 remains the terminal-equivalent support theorem. B128/G086 give its
exact edge-escape form, while B129/NG103 close the formal projective-Hodge
shortcut. B130/NG104 close the direct Nori/Higgs shortcut; B131-B132/NG105
discharge canonical map identification and leave G088's discriminant-stalk
survival. B133/NG106 require a genuine vanishing-cycle relation even in the
minimal codimension-two model. G007/NG-010 remain the concrete
tube-concentration attempt and its class-directed incidence mismatch.

The current local construction chain has reached an exact all-order form.
B155--B158 identify smooth rank-\(R\) excess with \(H_\tau=0\), analytic
syzygy lifting, and persistence of every node on a basis germ. B167--B168
move this to the full microlocal normal cone and exclude pointwise or
finite-jet substitutes. B169 then computes the exhaustive tracked-ODP
case: both actual ambient microsupport absorption and absorption of the
Migliorini--Shende envelope are equivalent to that same persistence and
syzygy condition. NG133 therefore closes the ambient-microlocal-shortcut
idea. The narrow unresolved geometric gate is again carrier-free
full-linear-system construction of \(H_\tau=0\), with the rational
type-\((0,0)\) specified Saito pairing retained independently.

B170 turns one sufficient branch into a global determinantal question:
\(d\tau\) is evaluation at the moving critical configuration. G107 asks
that the full configuration image remain in the rank-\(R\) evaluation
degeneracy locus. NG134 tests and rejects the first automatic mechanism:
an affine-linear projective slice already realizes the quadratic escape
\((x,x-y^2)\). What remains must use the full complete-system evaluation
geometry, not merely linear dependence of the family on its parameters.

B171/NG135 prevent this sufficient target from silently becoming the new
gate. Determinantal containment requires mixed Hessian vanishing on
\(W\times\ker E\), whereas smooth excess controls only the conditional
directions. The factorized affine-linear model
\(\tau=(x,(1+y)x)\) has \(H_\tau=0\) but jumping Jacobian rank. G107 is
therefore an optional strong mechanism; the exact frontier remains G100's
direct analytic syzygy lifting with the class-specific Saito pairing.
