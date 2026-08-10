# Initial landscape: cases, mechanisms, obstructions

Date: 2026-08-10. Result label: **EXPLORATORY** as a research map; each theorem
entry separately identifies its theorem status. This is a conservative seed,
not a claim of bibliographic completeness.

## Unconditional cases

| Scope | Status | Reason | Global propagation? |
|---|---|---|---|
| \(p=0\) and \(p=n\) | PROVED | components and closed points give the classes | no |
| \(p=1\) | PROVED | Lefschetz theorem on \((1,1)\)-classes | no |
| \(p=n-1\) | PROVED | hard Lefschetz plus divisor classes and powers of a hyperplane | no |
| \(\dim X\le3\) | PROVED | the preceding codimensions exhaust all cases | no |
| varieties with an algebraic cellular decomposition | PROVED | cycle classes of cells generate cohomology | no blanket reduction |
| selected abelian varieties, hypersurfaces, complete intersections, products, and fibrations | PROVED only case-by-case | special geometry or group constraints | never counted globally without an explicit reduction |
| injectively combined semiregular lci anchors in suitable families | PROVED, including all Artin-local obstructions | Ran/Buchweitz-Flenner; B003-B004 | no universal presentation or anchor theorem |

The general problem is already genuinely open for codimension-two classes on
smooth projective fourfolds. “Known below dimension four” is therefore a scope
boundary, not an induction mechanism.

## Mechanism audit

| Mechanism | What it really supplies | Missing general bridge |
|---|---|---|
| weak/hard Lefschetz | cohomological restriction and isomorphisms | inverse maps need not be induced by known cycles |
| algebraic correspondences | functorial construction once a correspondence exists | constructing the decisive correspondence is often another Hodge problem |
| variation of Hodge structure and monodromy | controls how classes vary and identifies invariants | Hodge/invariant does not imply algebraic |
| Cattani-Deligne-Kaplan | Hodge loci are algebraic | no dominating relative Chow/Hilbert component follows |
| admissible normal functions | BFNP attach one to a primitive Hodge class via a Deligne/absolute-Hodge lift; a nonzero boundary singularity is terminal-equivalent to HC | no theorem forces a class-specific singularity; ambient vanishing cycles do not suffice |
| nodal defect and vanishing-cycle relations | B008 excludes smooth discriminant points; B009 computes the transverse nodal local channel as the relation space among vanishing cycles | positive defect does not force the specified Hodge class to pair nontrivially with a new middle cycle |
| Saito relation pairing | a type-\((0,0)\) unipotent local relation gives a primitive Hodge class \(\gamma_\beta\), and its pairing exactly detects restriction to the chosen singular fiber | does not construct a suitable singular fiber or relation for a specified class |
| Schnell tube mapping | global monodromy tubes generate all rational primitive middle cohomology when vanishing homology is nonzero | a global loop-fixed tube is not supported on one singular fiber and is not automatically a local Saito relation |
| global/local Green-Griffiths invariants | B012 proves global detection of every primitive class and high-power local detection of restriction; possible local support has codimension at least two | nonzero global hypercohomology does not force a nonzero local stalk; support nonemptiness is terminal-equivalent for Hodge classes |
| independent-node Severi geometry | B015 gives normal-crossing discriminant branches, expected-codimension partial smoothings, and the exact local IC channel once such a nodal member is fixed | does not construct the member from a specified Hodge class or force the class-specific restriction to be nonzero |
| detector-span formulation | B016 turns detection by any chosen singular-member collection into equality of its Saito detector span with primitive rational Hodge homology | B027 disproves the fully independent-node choice; G012 uses partitioned quasi-local nodal relations instead |
| finite detector certificate | B017 proves cumulative spans stabilize and full generation for a fixed variety is witnessed by finitely many detector classes | gives no effective power bound, no construction, and no monotonicity for the individual power-by-power spaces |
| tautological complete intersections | their classes and multiplicities are explicit and algebraic | B018 proves their primitive projections vanish, so they cannot detect primitive middle classes |
| symplectic matching paths | B019: two transported thimbles over distinct critical values glue to a Lagrangian sphere in the audited four-dimensional setting | no algebraic one-fiber collision, Hodge-type certificate, or Saito-class identification follows |
| intersection-one vanishing cycles | B020: Schnell constructs a pair with intersection number one and exhibits cusp/two-node dual-plane configurations | intersection one proves independence; a two-ODP member alone supplies no relation or nonzero detector |
| matching-to-cusp collision | B021 compares the two audited local lattices in the projective-surface setting | a class-by-class comparison is rank-incompatible; with B023, any viable bridge needs topology change, extra cycles, or later ambient-quotient preservation |
| thimble reconstruction | B022 gives a relative thimble basis, its vanishing-cycle boundary, and the exact quotients leading to ambient homology for generic hypersurface pencils | a relation may die as an equator extension or in the base-locus kernel before it becomes an ambient detector |
| Hurwitz equivalence | B023 shows distinguished bases in a fixed exact Morse fibration are related by invertible moves preserving boundary rank and relation-kernel dimension | cannot model a topology-changing collision or repair the matching/cusp rank mismatch |
| complete-intersection thimble detection | B024 lifts a nonzero detector for every primitive class through the surjection from the quotiented thimble group | special-family global topology only; no one-fiber Saito class, algebraic cycle, or general reduction follows |
| isolated-singularity morsification | B025: the \(\mu\) distinguished vanishing cycles form an integral basis of the local Milnor lattice | supplies no internal relation; a detector must arise from the global kernel of local Milnor lattices mapping to nearby-fiber homology |
| nodal defect-number equivalence | B026 equates relation, extra-homology, adjoint node-evaluation, desingularization, and local-IC dimensions | the canonical map from extra homology to primitive ambient homology has an independent rank |
| full node independence | B027 propagates defining-system interpolation to adjoint interpolation in dimension at least four at high power | the adjoint defect and relation space vanish; a viable locus must use partwise rather than full independence |
| two-matroid nodal window | B028 uses Edmonds' theorem to characterize two independently controlled blocks by \(|S|\le2r_A(S)\), while adjoint defect is \(r_F(\Delta)<|\Delta|\) | the two rank systems need not agree; G013 must realize both and select a defect direction pairing with the specified Hodge class |
| first-jet nodal realizability | B029 proves that too many prescribed singular points on one line force second-order vanishing along that line | abstract evaluation-rank conditions do not ensure an isolated nodal member; dependence must be supported without creating a singular carrier |
| plane-complete-intersection witness | B030 realizes isolated nodality, a two-part independent partition, and adjoint defect one on a plane-containing quintic threefold | P^4 has zero primitive middle cohomology and the plane is a preselected algebraic anchor; no class-specific or general propagation follows |
| extra-to-primitive map | B031 proves in every degree d at least 3 that the plane-containing relation and extra-homology spaces are one-dimensional while Saito's canonical map to primitive ambient homology is zero | positive defect does not imply a nonzero ambient detector; the literal Green-Griffiths rho(ii) equality is also quarantined |
| positive ambient-rank witness | B032 realizes defining-system-independent nodes, adjoint defect one, rank-one extra-to-primitive map, and nonzero primitive pairing on a diagonal-containing (2,2) divisor in P^2 x P^2 | the diagonal is a preselected algebraic anchor; compatibility does not supply non-circular class selection |
| high-power positive-rank witness | B033 proves that every diagonal-containing (m,m) family for m at least 3 has a uniform smoothing matroid, a two-block partition, adjoint defect one, and ambient rank one | full symmetric monodromy closes postulation, but the primitive direction remains the preselected algebraic diagonal |
| fixed-carrier block growth | B034 proves that Thomas' node count divided by one defining-system-independent block capacity tends to n! | two blocks cannot scale through a fixed carrier for n at least 3; a multipart local theorem or a lower-node unanchored incidence is required |
| multipart quasi-local channel | B054 closes G015 under the explicit Li clean-arrangement hypothesis: B009's relation-kernel identification survives q separately independent blocks | this is a local channel theorem and supplies no incidence or specified-class pairing |
| minimal multipart arrangement | B035 identifies U_(2,5), resolves it to an exceptional P^1 with five marked crossings, and proves all crossingwise degree-two Picard-Lefschetz products vanish | the unresolved datum is global exceptional-curve IC gluing and separation of the downstairs IC summand, not a local product at one crossing |
| exceptional gluing rank | B036 proves that the five crossing cokernels form Q^5 and that recovering the relation kernel requires the canonical quotient e_i -> delta_i of rank dim span(delta_i) | B037-B038 derive this differential; its required Hodge type remains open |
| exceptional transgression | B037 proves that the resolved degree-one group is the kernel of the sole d_2:Q^5 -> H^2(P^1,ker N_E) | B038 computes the residue class and B039 isolates the downstairs summand; rational type (0,0) remains open |
| exceptional residue map | B038 proves d_2(a_i)=sum a_i delta_i and hence identifies the resolved U_(2,5) degree-one contribution with the full rational relation kernel | B039 descends it to the IC stalk; Hodge type and the general multipart case remain open |
| downstairs IC descent | B039 proves that the only extra strict-support summands under the blow-up are point-supported in ordinary degree two, so the downstairs degree-one IC stalk is B038's relation kernel | B040 computes its Hodge type; propagation to general multipart arrangements remains open |
| exceptional Hodge type | B040 proves the downstairs U_(2,5) relation kernel is pure Tate type (0,0) after the explicit Q(n) normalization | only the minimal rank-two arrangement is covered; higher-rank exceptional strata remain open |
| uniform rank-two channel | B041 extends the residue, IC descent, and pure type-(0,0) result to every U_(2,r) central line arrangement | the next case U_(3,7) has an exceptional P^2 with line-incidence strata and extra differentials |
| uniform rank-three channel | B042 proves that the exceptional P^2 line-incidence row has no extra pair-point quotient, computes its residue map, and descends the pure type-(0,0) relation kernel for every U_(3,r) | arbitrary uniform rank and nonuniform incidence lattices remain open |
| uniform arbitrary-rank channel | B043 proves the full rational type-(0,0) relation channel for every simple uniform U_(d,r), with point-supported blow-up summands only in ordinary degrees 2 through 2d-2 | dependent-flat wonderful resolutions are not covered |
| first nonuniform gate | G016 fixes rank three with seven branches and exactly one dependent triple | the second exceptional divisor's incidence differential and composite proper-direct-image shifts are uncomputed |
| single dependent flat | B044 proves G016: on Bl_p(P^2), the exceptional-flat coefficient is forced to the partial triple sum and the residue kernel is the full relation space | compatibility for several or nested dependent flats remains open |
| two dependent flats | G017 fixes two dependent triples sharing one branch as the next test | their exceptional residue equations share a vanishing-cycle coefficient and have not been audited together |
| two-flat compatibility | B045 proves that two non-nested dependent-flat equations remain independent bookkeeping constraints even when the triples share a branch | arbitrarily many and nested flats remain open |
| nested-flat channel | B046 proves G018 for one explicit codimension-three flat nested in a codimension-two flat; the exceptional equations are triangular and lower supports begin in ordinary degree two | arbitrary nested sets and building-set order independence remain open |
| three-level nested chain | B047 proves the full relation channel for an exact rank-five three-block arrangement whose connected flats form a chain of ranks 2, 3, 4, and 5 | a chain does not test incomparable children or blow-up order independence |
| forked building set | B048 proves G020: the common-parent blow-up separates two incomparable child planes, both child orders give the same triangular residue kernel, and lower supports begin in degree two | one fork does not prove arbitrary order independence or coefficient-sheaf incidence |
| universal divisor matrix | B049 proves G021: intrinsic boundary classes give the Picard basis and every strict branch has class \(h-\sum_{F\subset H_i}e_F\) for every building set and permissible order | controls only geometry; NG035 shows raw exceptional coordinates are order dependent |
| universal coefficient sheaf | B050 proves G022: the origin residue anchors every SNC cokernel, giving exactly the branch lines and exceptional W_F terms, with no higher cohomology sheaves | global residue hypercohomology and lower strict supports remain open |
| universal strict-support bound | B051 proves G023: every non-full-support wonderful direct-image summand begins in ordinary degree at least two | does not compute global residue hypercohomology |
| universal residue channel | B052 proves G024 and G019: B049's divisor matrix is the sole degree-one differential and its kernel is the full rational type-(0,0) relation space | central representable arrangements only |
| analytic linearization NO-GO | NG036 disproves G025: five quasi-local smooth plane branches have a quadratic analytic modulus absent from their tangent lines | analytic equivalence is stronger than the needed IC comparison |
| exact quasi-local IC invariance | B053 proves G026 by blowing up the common stratum: the exceptional restriction is the uniform tangent arrangement and gives the same rational type-(0,0) relation channel | nonuniform cross-block dependencies require iterated centers |
| clean-arrangement tangent channel | B054 proves G027 and G015: nonlinear clean wonderful fibers equal their labelled tangent models and preserve the full rational type-(0,0) relation channel | assumes clean incidence and supplies no specified-class pairing |
| dimension-scaled incidence gate | G028 asks for a clean q-block nodal member with positive adjoint/ambient rank and a relation pairing with a specified primitive Hodge class | this is the genuinely geometric, non-circular obstruction after local closure |
| equisingular ambient-image rigidity | B055 proves the ambient image is constant on a connected stratum whenever the canonical relation maps form a morphism to fixed primitive homology | large node or relation monodromy cannot create new detector directions inside one component |
| equisingular monodromy NO-GO | NG037 excludes sweeping one positive Saito image through primitive homology by monodromy inside one incidence component | a topology-changing boundary or distinct component is required |
| topology-changing detector transport | G029 asks to specialize a chosen global tube/thimble detector to one clean nodal relation while preserving the B022 quotient class, rational type, and specified pairing | no audited specialization theorem supplies all three properties |
| plane-net localization | B056 proves every Schnell detector pair can be represented in a generic projective plane net with the same primitive ambient tube class | reduces the parameter dimension to two but does not produce a collision point |
| tube/thimble chain identity | B057 proves B013's distributed coefficients are the coefficients in the ordered thimble-extension expression and retain the Schnell ambient class | the chain is still distributed among separate meridians and has no local Hodge type |
| Hodge-targeted tube selection | B058 chooses a rational type-(0,0) primitive homology class pairing with the specified Hodge class and lifts it through the surjective tube map into the plane net | the resulting Hodge homology class is topological and not known algebraic or locally nodal |
| total-equator NO-GO | NG038 proves the total-equator vector of one complete pencil is in \(\operatorname{im}\tau_\infty\) and vanishes in \(\mathcal T(Y)\) | the actual detector must remain a non-equator loop in the plane net |
| pairing versus exact class | B059 proves that a detector outside \(\zeta^\perp\) suffices, while containing a preselected nonorthogonal class is strictly stronger; NG039 closes exact recovery as a necessary gate | the linear correction constructs no local relation or support point |
| clean-nodal support gate | G031 asks that the class-specific support meet the Li-clean multipart nodal locus, equivalently that one clean relation pair nontrivially with \(\zeta\) | support nonemptiness is terminal-hard and no theorem forces intersection with the controlled locus |
| pairing-preserving nodalization | G032 isolates the cleanup theorem from an arbitrary detecting singular member to the Li-clean nodal locus | NG040 shows generic morsification gives a local Milnor basis and separate zero-channel Morse values, not the required one-fiber global relation |
| iterated nearby-cycle comparison | B061 audits natural lax comparison and two conditional commutation theorems; B063 supplies the rational MHM lift on the without-slopes branch; G033 asks for detector compatibility | NG042: commutation is false in general; B062 retains the critical graph conormal; no audited source supplies the B022/Saito-pairing square |
| mixed-Hodge recollision comparison | B063 supplies permutation invariance inside MHM under without slopes; B064 gives the explicit A2 cusp transition chart; G034 asks for resolved descent | NG043: smooth total space does not verify without slopes in the raw cusp coordinates; strict multispecialisability and detector-pairing descent remain open |
| resolved A2 cusp | B065 gives the three-blowup SNC model with multiplicities (2,3,6); G035 asks for chartwise Hodge/V-filtration compatibility and detector pushdown | NG044: the quasi-ordinary theorem controls one coordinate for a one-dimensional cusp, not the required two-parameter family comparison |
| A2 total-space semistability | B066 computes the raw pullback and finds singular sections over E3 and E2; G036 asks for a proper semistable Hodge-module model and full-support detector descent | NG045: an SNC discriminant on the base does not make the total family semistable |
| A2 Weyl-cover branch | B067 explicitly gives the degree-six S3 cover, reflection arrangement, and three collision sections; B068 imports simultaneous resolution for surface A2; G037 asks for dimension-uniform descent | NG046: every middle-route hyperplane fiber has odd dimension 2n-1, so the surface RDP theorem never matches the required dimension |
| arbitrary-dimensional weak semistability | B069 imports a projective alteration/modification yielding toroidal equidimensional reduced fibers in every dimension; G038 asks for equivariant rational detector trace | NG047: weak semistability permits singular total space and supplies no S3 action, MHM strictness, support decomposition, or nonzero detector descent |
| equivariant semistable resolution | B070 gives equivariant absolute resolution; B071 imports the arbitrary-dimensional quasi-local semistable theorem and lifts finite-group strict automorphisms at the log-stack level | NG048 blocks the absolute shortcut; NG049 notes that scheme realization is noncanonical and that semistable geometry alone supplies no rational detector trace |
| stacky detector descent | B072 supplies rational stack MHM, six operations, nearby/vanishing cycles, proper pushforward, and quotient-stack equivariant comparison; G040 retains the class-specific square | the formalism does not identify the invariant full-support summand, multi-V strictness, B022 quotients, or nonzero pairing |
| A2 trace representation | B073 computes the local root lattice as the standard two-dimensional S3 representation with zero invariants; NG050 blocks normalized averaging of a local root detector | G041 must find an additional trivial constituent in global thimble-extension/full-support data and prove it survives both quotient kernels |
| full-support Galois descent | B074 proves that rational invariants of finite-Galois pushdown recover the original intermediate-extension object | NG051: object-level trivial summand does not imply the specified boundary class projects nontrivially to it; G042 requires the six-sheet class calculation |
| global tube transfer | B075 proves the invariant sheet-transfer has normalized trace equal to the original B058 tube and preserves its nonzero pairing before collision | NG052: transfer does not control nearby specialization, proper supports, or the two B022 kernels; G042 remains the boundary calculation |
| nearby-cycle trace retract | B076 proves finite-cover unit/trace remain a rational split retract after nearby cycles, including the B063 iterated setting | NG053: cover and averaging preserve but cannot create original boundary nonvanishing; residual G042 is the original G032 specialization/support/quotient problem |
| stacky strict-support decomposition | B077 proves the pure proper pushdown has semisimple perverse cohomology and each perverse cohomology object decomposes uniquely by strict support | NG054: object existence does not force class landing; splitting across perverse degrees is separately noncanonical |
| toric support parity | B078 proves that globally proper toric support terms occur in even ordinary generic degree and that simplicial-source toric fibers have pure Hodge-Tate even cohomology | NG055: local toroidal charts do not identify the global non-toric coefficient Hodge modules or the B058 detector degree; G044 is the coefficient-sensitive gluing gate |
| toroidal coefficient parity | B079 gives a smooth projective toroidal product whose positive-genus fiber coefficient creates an odd degree-three proper-support term | NG056 disproves coefficient-blind parity; G044 must compute the exact normal-degree plus coefficient-degree convolution for the B057 chain |
| detector support normalization | B080 converts the degree-one relation group to normalized direct-image degree $-1$ and shows divisor $b=0$ and point $b=-1$ are both toric-parity allowed | NG057 closes parity exclusion; G045 must compute the two multiplicity spaces and actual B058 class coordinates |
| canonical detector grade | B081 separates the full/divisor $E_\infty^{-1,0}$ grade from the point $E_\infty^{0,-1}$ grade using the canonical perverse filtration | NG058 closes a total projection from an arbitrary derived splitting; G046 is the canonical full-support landing gate |
| exact plane-net collision mechanism | G030 asks for a topology-changing specialization of B057's chain to one clean nodal relation with identical primitive ambient class and rational type (0,0) | sufficient but stronger than G031; no audited nearby-cycle theorem gives the square |
| arbitrary building-set channel | B049-B052 prove G019: every representable wonderful arrangement has the full residue kernel, strict-support bound, and rational type-(0,0) comparison | central linear geometry only; B054 is needed for nonlinear clean germs |
| classifying-space boundary pullback | Green-Griffiths II models selected singular loci as inverse images of boundary components and proposes a cohomological nonemptiness test | the class-directed nodal construction assumes HC; the global formula is programmatic and contains unresolved compactification/correction data |
| degenerations | limiting mixed Hodge structures, vanishing cycles, specialization | a special-fiber cycle may fail to lift; type and rationality can jump |
| spreading out | places data over a finitely generated field/base | spreading a class is not spreading a cycle that does not yet exist |
| reduction modulo primes | Frobenius and etale/Tate information | needs comparison, Tate-type algebraicity, and cycle lifting back to characteristic zero |
| claimed degeneration proof audit | S040/NG041 audit Bouali's 2023-2024 preprint chain; B060 proves its completion-valued cycle cannot be Galois-averaged without finite algebraic descent | the decisive Tate theorem constructs a cycle only over a p-adic completion and supplies no descent to kbar; the claimed general Hodge conclusion is not established |
| motives/absolute Hodge classes | packages realizations and correspondences | absolute Hodge is weaker than known algebraicity in general |
| abelian varieties/Mumford-Tate groups | representation-theoretic description of Hodge tensors | exceptional Hodge tensors need actual algebraic cycles |
| hypersurface Jacobian rings/Noether-Lefschetz theory | computes infinitesimal Hodge loci and primitive variation | tangent-space or locus information is not cycle existence |
| products and fibrations | Kunneth/Leray decompositions and conditional propagation | mixed Hodge tensors and differentials/extensions create extra classes |
| deformation rigidity | an existing relative cycle retains its class | it does not guarantee the relative cycle space dominates the Hodge locus |
| cycle-class rigidity | locally constant Betti class in a flat family of cycles | only applies after the cycle family exists |

## Known obstructions and anti-patterns

1. **Coefficient mismatch:** integral failures can disappear after tensoring
   with \(\mathbf Q\); torsion is invisible to the official target.
2. **Hodge-locus/cycle-locus gap:** both loci may be algebraic, but equality or
   dominance is precisely the missing algebraicity statement.
3. **Specialization asymmetry:** specialization of a generic cycle is easier
   than lifting a special-fiber cycle.
4. **Noether-Lefschetz dimension fallacy:** computing a tangent space or
   codimension does not exhibit a cycle.
5. **Absolute/algebraic fallacy:** Deligne proved Hodge classes on abelian
   varieties are absolute Hodge; this does not prove the Hodge Conjecture for
   all abelian varieties.
6. **Numerical-equivalence substitution:** positivity or numerical detection
   does not identify the image of the rational Betti cycle-class map.
7. **Product fallacy:** the conjecture for factors does not automatically
   cover new cross-factor Hodge tensors.
8. **Normal-function overreach:** cycle-induced normal functions presuppose
   cycles, while BFNP's class-induced normal function does not; in the latter
   route the missing statement is nonzero boundary singularity, which is
   equivalent to HC rather than an automatic consequence of admissibility.
9. **Generic-to-every-fiber fallacy:** a theorem on a very general fiber misses
   the special Hodge loci where new classes occur.
10. **Kahler overreach:** projectivity is essential in the official target.
11. **Defect-only fallacy:** a nonzero nodal defect or local
    intersection-cohomology group supplies a possible target, not a nonzero
    image for the specified Hodge class.
12. **Global/local kernel fallacy:** Schnell's
    \(\ker(g-1)\) for a global monodromy loop is not Saito's relation kernel
    for simultaneous vanishing cycles at one singular fiber.
13. **Global/local support fallacy:** a nonzero global Green-Griffiths class
    need not have a nonzero local edge image by formal sheaf theory alone. A
    generic pencil avoids codimension-at-least-two support, and a net does not
    prove that the support is nonempty.
14. **Abstract-perversity fallacy:** B014 gives a smooth projective
    intersection-complex countermodel in which degree-one intersection
    hypercohomology is nonzero while every proposed local target group
    vanishes. G008 requires special hyperplane-family geometry.
15. **Incidence-after-selection fallacy:** B015 controls the deformation
    space around a chosen independent-node hyperplane. It does not select
    that hyperplane from \(\zeta\) or prove nonzero class-specific pairing.
16. **Boundary-pullback circularity:** a period-map boundary class can force
    an inverse image only after the global map, compactification, and nonzero
    pullback are independently constructed. Green-Griffiths II builds its
    class-specific nodal model from an HC-supplied algebraic representative.
17. **Power-monotonicity fallacy:** multiplying a section in \(|mL|\) by one
    in \(|kL|\) produces a reducible divisor in \(|(m+k)L|\), not a
    class-preserving transfer between independent-node detector spaces.
18. **Tautological-detector fallacy:** a middle complete intersection of
    polarization divisors has class proportional to \(c_1(L)^n\), hence zero
    primitive projection. Making its degrees larger cannot produce a
    primitive detector.
19. **Matching-path type fallacy:** gluing two thimbles over distinct
    critical values gives a symplectic Lagrangian sphere, not automatically
    a rational type-\((0,0)\) relation at one algebraic singular member.
20. **Intersection-one relation fallacy:** vanishing cycles with pairing one
    are rationally independent. The occurrence of a two-node hyperplane in
    the same discriminant slice does not by itself supply another relation.
21. **Collision-continuity fallacy:** a matching pair spans rank at most one,
    while the cusp pair spans rank two. Individual vanishing-cycle classes
    cannot simply be carried unchanged through the cusp collision.
22. **Relative-to-ambient fallacy:** a nonzero zero-boundary thimble
    combination can vanish modulo equator extensions or in the pencil
    base-locus kernel; it is not automatically a primitive ambient class.
23. **Hurwitz-repair fallacy:** an invertible change of distinguished basis
    preserves boundary rank and relation-kernel dimension. It cannot replace
    the non-invertible topology change required by collision.
24. **Topological-generation fallacy:** surjectivity from a thimble quotient
    to primitive homology produces global topological classes, not algebraic
    cycles or rational type-\((0,0)\) relations at one singular fiber.
25. **Milnor-number relation fallacy:** a higher isolated hypersurface
    singularity has \(\mu\) morsification cycles, but they form a basis of its
    rank-\(\mu\) Milnor lattice. Any relation must be created by the global
    local-to-nearby-fiber map, not by the isolated germ alone.
26. **Positive-defect pairing fallacy:** B026 gives equal nonzero relation,
    extra-homology, and coherent-defect dimensions, but this does not control
    the rank of the map to primitive ambient homology or its pairing with the
    specified Hodge class.
27. **Full-independence detector fallacy:** in dimension at least four and at
    high power, B027 shows that full node independence forces zero adjoint
    defect and zero relation space.
28. **Smoothing-circuit fallacy:** minimal dependence for the defining-system
    evaluation matroid does not imply dependence for the adjoint evaluation
    matroid. B028 gives an explicit configuration on
    \(\mathbf P^2\times\mathbf P^2\) with the first property and zero adjoint
    defect.
29. **Collinear-defect fallacy:** enough points on a low-degree line to force
    adjoint dependence may also force the defining section and every first
    normal derivative to vanish along that line, producing nonisolated
    singularities rather than nodes.
30. **Extra-to-primitive injectivity fallacy:** B031 gives a one-dimensional
    extra-homology space whose canonical map to primitive ambient homology is
    zero. A nonzero source cannot be coerced into a nonzero detector.
31. **Six-invariant import fallacy:** the literal Green–Griffiths
    \(\rho(i)=\rho(ii)\) ambient-image component conflicts with B031 in
    arbitrarily high degree. NG-028 requires a documented correction before
    that component may be used.
32. **Anchored-witness propagation fallacy:** B032 realizes all three ranks
    and a nonzero pairing only because the divisor is forced to contain the
    algebraic diagonal. NG-029 forbids exporting that witness to an arbitrary
    Hodge class without a proved class-selection mechanism.
33. **Double-transitivity uniformity fallacy:** a doubly transitive node
    monodromy group controls pairs but need not be transitive on larger
    subsets. NG-030 requires the simple-transposition upgrade used in B033.
34. **Fixed-carrier two-block scaling fallacy:** B034 proves that the
    asymptotic number of required independent blocks is at least \(n!\).
    B033's two-block behavior is special to middle dimension two.
35. **Bipartite-induction fallacy:** separate independence of
    \(J_1,\ldots,J_q\) does not make
    \(J_2\cup\cdots\cup J_q\) independent, so B009 cannot be iterated.

## Open universal core

By brick B001, it is enough and necessary to solve the following still-global
problem: for every smooth projective complex variety of even dimension
\(2m\), construct codimension-\(m\) rational cycles for all rational classes in
\(H^{2m}\cap H^{m,m}\). No known mechanism in the table supplies this for
arbitrary varieties. Brick B007 gives a second exact formulation: every
nonzero primitive middle class must restrict nontrivially to some
high-degree singular hyperplane section. This removes the algebraic-anchor
assumption but does not weaken the open content.

Bricks B008-B009 refine the latter formulation: detection cannot occur at a
smooth discriminant point, and under a transverse nodal model its possible
local values form the rational relation space among the vanishing cycles.
B010 gives the exact pairing with the primitive Hodge class
\(\gamma_\beta\). B011 independently proves that global monodromy tubes detect
all primitive cohomology. B012 proves that the corresponding global
Green-Griffiths invariant is always nonzero but separates this from the local
stalk problem. B013 extracts the distributed Picard-Lefschetz relation from a
fixed loop. G008 asks for a global-to-local support theorem, while G007 is its
geometric tube-concentration mechanism; both remain terminal-equivalent and
open after universal quantification. B014 excludes a purely formal
hypercohomology proof, and B015 proves the desired local collision geometry
only after the class-directed nodal member is supplied. B016 repackages the
remaining content as detector-span generation. G009 asked for this generation
on the fully independent-node locus, but B027 disproves that choice. B017
gives a finite certificate if a detector collection spans for a fixed variety, but
NG-014 blocks the naïve comparison between powers. B018/NG-015 further
require any successful incidence construction to create non-tautological
primitive homology rather than recycle polarization complete intersections.
B019/NG-016 separate matching spheres from one-fiber Hodge detectors, and
B020/NG-017 show that Schnell's intersection-one pair is not the missing
relation. B021/NG-018 rule out the direct class-by-class cusp comparison in
the audited surface case. The remaining two-critical-value route needs a new algebraic
collision theorem preserving the detector class and rational Hodge type.
B022 specifies that the preserved datum must be nonzero after the
equator-extension and base-locus quotients. B023 shows that pure Hurwitz
mutation cannot supply the required topology change.
B024 verifies global quotient-level detection for complete intersections,
but NG-021 prevents treating this special topological generation as HC.
B025/NG-022 exclude internal Milnor relations. B026 separates exact defect
dimensions from the canonical ambient map. B031/NG-027 prove that this map
can vanish before the further NG-023 class-pairing obstruction is reached.
B027/NG-024 close G009-G011 and
force G012's partitioned quasi-local nodal target. B028/NG-025 separate the
smoothing and adjoint evaluation matroids and exclude a smoothing circuit as
a sufficient replacement. G013 is the exact geometric parent, and G014 is a
sufficient unanchored two-block span theorem. B034 shows that the
fixed-carrier route cannot scale that bipartite target for \(n\ge3\);
G015 and its general arrangement subgates are closed by B049-B054. NG036
closes analytic linearization as a NO-GO, while B053-B054 prove the exact
quasi-local and nonlinear clean invariant-channel theorems. G028 is the
class-paired incidence parent. B055/NG037 show that monodromy on one
equisingular component cannot enlarge its fixed ambient image. B056-B057
reduce the chosen detector to an explicit extension chain in a generic plane
net, while NG038 excludes the total-pencil equator. G030 is the current
stronger exact-class collision proposal; B059/NG039 replace it as a necessary
gate by G031's clean-nodal nonzero-pairing incidence.
B035 makes the multipart local channel finite and explicit at its first new instance: compute
the intermediate extension for the Picard-Lefschetz local system on the
five-marked exceptional \(\mathbf P^1\) resolving \(U_{2,5}\). NG-033
prevents substituting the five pairwise crossing calculations for this
global exceptional-divisor computation.
B036 further identifies the missing map: the five crossing generators must
map to their five vanishing cycles. The remaining proof obligation is to
derive that differential from the intermediate-extension quiver and then
audit its rational type \((0,0)\).
B037 locates that differential as the unique hypercohomology transgression
from the five skyscraper groups to \(H^2(\mathbf P^1,\ker N_E)\). NG-034
separates the subsequent Hodge problem: the complex arrangement quiver does
not retain the rational mixed-Hodge data needed by B010.
B038 computes the transgression by the logarithmic residue sequence and
obtains \(d_2(e_i)=\delta_i\). This closes the resolved \(U_{2,5}\) relation
calculation. It does not yet prove that the resulting group is the downstairs
IC summand of the proper direct image.
B029/NG-026 further require isolated first-jet realizability and exclude the
first line-supported positive-defect construction. B030 proves the three
geometric conditions are compatible in a plane-containing quintic, while
B031 shows more generally that the extra-to-primitive map is zero throughout
the arbitrary-degree plane-containing family and exposes NG-028. B032 gives
the complementary rank-one map and nonzero pairing on a
diagonal-containing \((2,2)\) divisor, proving compatibility of the complete
finite-rank package. NG-029 isolates the remaining obstruction: the
diagonal is an already-algebraic anchor. The class-specific, non-circular
incidence problem remains untouched. B033 removes the low-degree caveat:
for every \(m\ge3\), the diagonal-containing \((m,m)\) family has a uniform
smoothing matroid, a two-part independent partition, adjoint defect one,
and ambient rank one. The proof requires full symmetric monodromy; NG-030
records why double transitivity alone is insufficient. This strengthens the
compatibility evidence but leaves G014 wholly open because the detector
direction is still the preselected diagonal. B034 also shows that this
two-block sufficient theorem is not recovered from HC by the standard
fixed-carrier construction when \(n\ge3\). B054 closes the corresponding
multipart relation channel; the remaining obstruction is geometric
realization and class-preserving topology-changing transport, now G028-G030.
