# Research frontier

## Active gate: G015

Extend B009's quasi-local identification of degree-one local intersection
cohomology with the full vanishing-cycle relation kernel from a bipartition
\(\Delta=J\sqcup K\) to a partition
\(\Delta=J_1\sqcup\cdots\sqcup J_q\), \(q\ge3\), with each block
independently smoothable. The calculation must include higher block
intersections and preserve the rational type-\((0,0)\) comparison.

B034 makes this extension necessary for the fixed-carrier route: in middle
dimension \(n\), the number of Thomas nodes divided by the capacity of one
independent block tends to \(n!\). Two blocks are eventually impossible for
\(n\ge3\). NG-032 shows why the bipartite theorem cannot simply be iterated:
the union of \(q-1\) independent blocks need not be independent.

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
The next falsifiable subgate is the same statement for every \(U_{2,r}\)
central line arrangement. Higher-rank multipart resolution remains a later,
separate obligation.

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

Immediate bricks:

1. Extend B035-B040 uniformly from \(U_{2,5}\) to \(U_{2,r}\), including
   residue, strict-support descent, and type \((0,0)\).
2. Extend the calculation to higher-rank multipart arrangements, including
   higher-dimensional exceptional strata and all additional differentials.
3. If G015 holds, replace the two-block constraint by Edmonds'
   \(|S|\le q r_A(S)\), with \(q\) allowed to scale at least as \(n!\) in
   fixed-carrier constructions.
4. Construct an algebraic incidence component satisfying the multipart
   inequalities and the independent condition \(r_F(\Delta)<|\Delta|\);
   then prove it actually occurs as the node set of a hypersurface member.
5. Compare its cross-part defect local system with the global coinvariant
   maps in B011, without coercing global tubes into local relations.
6. Use B009/G015's quasi-local partition model as the target for G007 and identify
   the exact class-preserving specialization datum still absent.
7. Audit boundary/intersection constructions that define a global incidence
   class without using an algebraic representative of \(\zeta\); NG-013
   excludes the HC-dependent Green-Griffiths construction.
8. Require every proposed incidence source to have a non-tautological
   primitive ambient class; B018/NG-015 exclude complete intersections of
   polarization divisors as detectors.
9. Test an algebraic collision bridge from distinct-fiber matching thimbles
   to one partitioned nodal Saito relation; B019/NG-016 show that the
   symplectic matching-path theorem does not provide this bridge.
10. Do not treat intersection-one pairs as relations; B020/NG-017 prove the
   opposite for Schnell's pair and leave the two-ODP relation computation
   open.
11. Compute any collision on the full vanishing-cycle complex. B021/NG-018
   rule out preserving a matching pair class by class through the cusp
   lattice; only basis change, extra cycles, or ambient-class preservation
   remain possible.
12. Track the class through the two exact quotients in B022. A kernel relation
   can die as an equator extension or in the pencil base-locus kernel;
   NG-019 forbids calling it an ambient detector earlier.
13. Require a non-invertible topology-changing comparison. B023/NG-020 show
    that Hurwitz moves inside a fixed fibration preserve the relation kernel
    and cannot close the matching/cusp gap.
14. Use B024 as a positive source-side checkpoint for complete intersections:
    global quotient-level thimble detectors exist, but NG-021 forbids
    counting them as local or algebraic.
15. Do not seek the required relation inside one isolated singularity's
    Milnor lattice. B025 proves its morsification cycles form a basis;
    NG-022 forces the relation into the global local-to-nearby-fiber kernel.
16. Use B026's equality of relation, extra-homology, coherent, and local
    defect dimensions only as a consistency test. B031/NG-027 forbid
    coercing a nonzero extra space into a nonzero primitive ambient image;
    NG-023 separately forbids promoting a nonzero image to a prescribed
    pairing.
17. Enforce B027/NG-024: full independence is fatal in dimension at least
    four at high power; only partwise independence may be imposed.
18. Enforce B028/NG-025: a circuit for \(A\)-evaluation may remain independent
    for adjoint \(F\)-evaluation, so smoothing dependence is not defect.
19. Enforce B029/NG-026: adjoint dependence obtained by overloading one
    low-degree line forces a nonisolated singular locus; first-jet nodal
    realizability is independent of both evaluation-rank conditions.
20. Use B030 only as a compatibility witness: its plane-containing quintic
    realizes isolated nodes and both matroid conditions, but has no primitive
    ambient class and begins with an algebraic anchor.
21. Carry \(\operatorname{rank}\Phi_Y>0\) as a third independent incidence
    condition. B031 proves it does not follow from the two evaluation ranks.
    NG-028 also forbids recovering it from the literal printed
    Green–Griffiths \(\rho(ii)\) equality without a documented resolution of
    that source conflict.
22. Use B032 as the positive compatibility test for all three ranks and the
    pairing, but enforce NG-029: its diagonal is an algebraic anchor and
    cannot be used in the class-selection step.
23. Keep the type-\((0,0)\), rational, and unipotent conditions explicit;
   nodal fibers satisfy them automatically, arbitrary singularities do not.
24. Keep the semiregularity gate G004 as an independent secondary route.

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
blocks. G015 is now the narrowest active local gate: compute the multipart
relation channel before changing the incidence target. B029/NG-026 test the
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
G008 remains the terminal-equivalent support
theorem; G007/NG-010 remain the concrete tube-concentration attempt and its
class-directed incidence mismatch.
