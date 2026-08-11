# NO-GO ledger

## NG-001 - Hodge-locus algebraicity does not provide cycles

- **Label:** NO-GO
- **Route:** Cattani-Deligne-Kaplan algebraicity of the Hodge locus -> relative
  cycle-space dominance -> algebraicity of the class.
- **Valid input:** the locus where a fixed flat integral/rational class remains
  of Hodge type is algebraic.
- **Invalid inference:** an algebraic Hodge locus containing one point with an
  algebraic representative must be dominated by a component of a relative
  Hilbert or Chow scheme carrying that class.
- **Precise obstruction:** the image of each relevant relative-cycle component
  is algebraic/constructible, but the presence of one point proves neither
  infinitesimal unobstructedness nor dominance. Countably many proper cycle
  loci may sit inside a Hodge locus. CDK controls type, not existence or
  deformation of cycles.
- **Re-entry condition:** exhibit a theorem forcing a cycle component through
  the anchor to have tangent/obstruction theory sufficient for dominance, with
  hypotheses verified for arbitrary smooth projective families.

## NG-002 - Hard Lefschetz alone is not a cycle inverse

- **Label:** NO-GO
- **Route:** use the cohomological inverse of cup product with a hyperplane to
  pull an algebraic high-degree class back to an algebraic low-degree class.
- **Precise obstruction:** hard Lefschetz produces a rational Hodge-theoretic
  inverse, not an algebraic correspondence. Treating it as a cycle action
  assumes a case of the Lefschetz standard conjecture/Hodge Conjecture on a
  product.
- **Re-entry condition:** construct the inverse correspondence independently,
  or use B001's product-with-projective-space reduction, which avoids this
  hidden assumption.

## NG-003 - Specialization from characteristic p is not automatic lifting

- **Label:** NO-GO
- **Route:** find a Frobenius/Tate cycle after reduction modulo a prime and
  declare its characteristic-zero generic-fiber class algebraic.
- **Precise obstruction:** a special-fiber cycle need not lift; comparison of
  Betti, de Rham, crystalline, and etale realizations plus control of the class
  under specialization is required. The Tate conjecture, even when available
  for the reduction, does not by itself supply a lifted characteristic-zero
  cycle.
- **Re-entry condition:** a verified lifting theorem for the actual cycle or a
  relative cycle-space component dominating the mixed-characteristic base.

## NG-004 - Semiregularity is not a universal free input

- **Label:** NO-GO
- **Route:** choose any anchor cycle and invoke semiregularity to conclude that
  it deforms along the entire Hodge locus.
- **Precise obstruction:** semiregularity theorems have geometric hypotheses
  on the embedded cycle and control specified obstruction maps. An arbitrary
  rational cycle may be reducible, singular, non-lci, or obstructed, and no
  theorem currently supplies a semiregular representative for every algebraic
  cohomology class. Before the anchor is found, invoking a representative is
  circular; after an anchor is found, semiregularity still is not automatic.
- **Re-entry condition:** a page/theorem-level audit proving the exact
  deformation implication for a class of representatives, followed by an
  independent theorem that every required anchor class has such a
  representative.

## NG-005 - Cycle generation does not control combined semiregularity

- **Label:** NO-GO
- **Route:** use a moving lemma, resolution/alteration, or rational
  Chern-character generation to write an algebraic anchor as a combination of
  nicer cycles, then declare the presentation semiregular.
- **Precise obstruction:** these tools concern generation of Chow or
  \(K\)-theory classes. G004 requires injectivity of a specific map from the
  direct sum of embedded obstruction groups into
  \(H^{q+1}(X,\Omega_X^{q-1})\). Smoothness or lci-ness of the components does
  not force injectivity, separate injectivity of the individual maps does not
  prevent cancellation in their weighted sum, and pushforward from an
  alteration does not identify the source normal bundle with the target's
  embedded deformation theory.
- **Re-entry condition:** prove a stabilization operation that preserves the
  Chow class while explicitly killing the kernel of the combined
  semiregularity map.

## NG-006 - Appending cycles cannot kill the old kernel

- **Label:** NO-GO
- **Route:** start from a non-semiregular presentation and append cancelling
  rationally trivial pairs or sufficiently positive complete intersections
  until the combined semiregularity map becomes injective.
- **Precise obstruction:** the enlarged obstruction space is a direct sum and
  the enlarged map restricts to the old combined map. Every vector in the old
  kernel survives as the same vector with zero new coordinates. See B005.
- **Re-entry condition:** replace the original presentation through a
  geometric operation that changes its obstruction space; mere augmentation
  is permanently closed.

## NG-007 - B001 products do not automatically preserve semiregularity

- **Label:** NO-GO
- **Route:** take a semiregular lci presentation on \(X\), form the product
  cycles used in B001, and reuse semiregularity without recomputing the
  obstruction map.
- **Precise obstruction:** in B001's low-degree case the geometric product is
  \(Z\times\{t\}\subset X\times\mathbf P^r\). B006 proves that its obstruction
  group is
  \(H^1(N_{Z/X})\oplus H^1(\mathcal O_Z)^{\oplus r}\). The original
  injectivity hypothesis controls only the first summand.
- **Re-entry condition:** compute the product semiregularity map on the extra
  summand and prove injectivity, impose and propagate
  \(H^1(\mathcal O_Z)=0\), or construct a genuinely different presentation of
  the product class.

## NG-008 - Ambient vanishing cycles do not detect a specified class

- **Label:** NO-GO
- **Route:** replace \(L\) by a high power, use the existence and monodromy
  orbit of nontrivial vanishing cycles in a Lefschetz pencil, and conclude
  that the admissible normal function of every nonzero primitive Hodge class
  has a singularity.
- **Valid input:** BFNP Proposition 5.11 proves that vanishing cycles are
  nontrivial for \(L^m\) with \(m\gg0\). Corollary 5.15 computes the local
  singularity of the normal function as
  \(\sigma_p=\zeta|_{X_{m,p}}\).
- **Invalid inference:** a nonzero ambient vanishing-cycle representation
  forces \(\zeta|_{X_{m,p}}\ne0\) for this specified \(\zeta\) at some
  discriminant point.
- **Precise obstruction:** monodromy controls the available local
  intersection-cohomology directions, not the projection of an arbitrary
  fixed Hodge tensor into them. Universal class-specific nonvanishing is
  equivalent to HC by B007, so it cannot be inserted as an automatic
  Lefschetz consequence. In Thomas's nodal construction the detecting
  hypersurface is built only after choosing an algebraic representative; his
  Section 5 further gives
  \(H^1(N_{Z/X})\hookrightarrow H^1(I_{\{p_i\}}(NH))\), showing that high
  degree does not remove the original embedded-cycle obstruction.
- **Re-entry condition:** prove a class-specific local nonvanishing theorem
  producing \(p\) with
  \(0\ne\sigma_p(\operatorname{pr}_m^*\zeta)\) directly from
  \((X,L,\zeta)\), without assuming an algebraic representative and without a
  numerical dimension argument.

## NG-009 - Positive nodal defect does not detect a specified class

- **Label:** NO-GO
- **Route:** construct a nodal hyperplane section with a nonzero rational
  relation among its vanishing cycles, identify a nonzero local
  intersection-cohomology group, and conclude that the normal function of a
  specified nonzero Hodge class has a nonzero singularity there.
- **Valid input:** under B009's transverse nodal hypotheses,
  \(H^1(B^\bullet)\) is the relation space of the vanishing cycles. A positive
  defect therefore gives a nonzero possible target for singularities.
- **Invalid inference:** a nonzero target forces the image of every nonzero
  primitive rational Hodge class to be nonzero.
- **Precise obstruction:** for fixed \(\zeta\), detection is the nonvanishing of
  the linear functional
  \(a\mapsto\langle\zeta,i_*\beta_a\rangle\) on the relation space. Positive
  dimension of the domain does not prevent this functional from being zero.
  No audited monodromy theorem supplies class-specific nonvanishing. At a
  smooth discriminant point the situation is stronger: B008 shows that the
  rational target itself is zero.
- **Re-entry condition:** construct a nodal relation \(a\) directly from
  \((X,L,\zeta)\) and prove
  \(\langle\zeta,i_*\beta_a\rangle\ne0\), without choosing an algebraic
  representative of \(\zeta\) and without a dimension-count substitution.

## NG-010 - Global tube detection is not local singularity detection

- **Label:** NO-GO
- **Route:** invoke Schnell's surjective tube map, represent a primitive Hodge
  class by a tube swept around a monodromy loop, and declare that tube to be
  the relation class of a singular hyperplane.
- **Valid input:** B011 proves that every primitive rational middle class is a
  global tube class associated with some
  \(\alpha\in\ker(g-1)\). B010 proves that a type-\((0,0)\) local relation
  \(\beta\) at one singular fiber produces a primitive Hodge class
  \(\gamma_\beta\) and gives the exact detection pairing.
- **Invalid inference:** the global stabilizer condition
  \(g\alpha=\alpha\) supplies a relation among the local vanishing cycles of
  one singular fiber, or a canonical map from the tube to such a relation.
- **Precise obstruction:** the tube loop lives entirely in the smooth
  parameter locus. A generic filling disk meets the discriminant at several
  separate smooth points; B008 says every such point has zero rational local
  intersection-cohomology channel. Saito's relation kernel is attached to the
  simultaneous vanishing data at one higher discriminant stratum, whereas
  Schnell's kernel is \(\ker(g-1)\) for a global product of monodromies. The
  audited sources provide no map between these kernels. Factoring \(g\) into
  meridians does not geometrically collide their discriminant points and does
  not preserve a type-\((0,0)\) local class.
- **Re-entry condition:** construct an algebraic two-parameter degeneration
  that realizes the tube on its boundary, concentrates the discriminant
  intersections at one singular member, and proves via the vanishing-cycle
  sequence that the resulting Saito class retains the nonzero pairing.

## NG-011 - Global invariant does not automatically produce local support

- **Label:** NO-GO
- **Route:** use the nonzero global Green-Griffiths invariant of every nonzero
  primitive class, restrict it to a pencil or net, and conclude that a local
  singularity occurs at some hyperplane.
- **Valid input:** B012 proves \(s(\zeta)\ne0\) whenever \(\zeta\ne0\), and
  identifies \(s(\zeta)_p\ne0\) with nonzero restriction to \(X_p\) after a
  sufficiently high embedding. It also proves that the possible local
  support has codimension at least two.
- **Invalid inference:** a nonzero global intersection-cohomology class must
  force one of the associated local invariants to be nonzero, or a generic
  one-parameter pencil must
  encounter the class-specific singular support.
- **Precise obstruction:** global hypercohomology and local perverse stalks
  are different functors. A generic complex curve avoids a fixed
  codimension-at-least-two locus. A generic projective plane can meet a
  nonempty codimension-two component, but it cannot prove that the component
  exists. Selecting a curve through a detecting point presupposes that point.
  For primitive Hodge classes, universal nonemptiness of this support is
  terminal-equivalent to the rational Hodge Conjecture by B007 and B012.
- **Re-entry condition:** prove that a nonzero global class of the specific
  geometric form \(s(\zeta)\) forces \(s(\zeta)_p\ne0\) somewhere, or
  construct a Hodge-adapted higher-dimensional slice together with a direct
  proof of local stalk nonvanishing, without assuming an algebraic
  representative of \(\zeta\).

## NG-012 - Abstract perversity cannot force the missing local invariant

- **Label:** NO-GO
- **Route:** argue solely from
  \(s(\zeta)\in IH^1(B,IC(V))\ne0\) that
  \(\mathcal H^{-\dim B+1}(IC(V))_p\ne0\) for some \(p\), then declare the
  associated local invariant nonzero.
- **Valid input:** B012 places the global and local Green-Griffiths invariants
  in groups with these degrees.
- **Invalid inference:** nonzero degree-one intersection hypercohomology
  formally forces nonzero ordinary cohomology sheaves in the local target
  degree.
- **Precise obstruction:** B014 takes a smooth projective elliptic curve
  \(E\) with \(IC_E(\mathbf Q)=\mathbf Q_E[1]\). Then
  \(IH^1(E,\mathbf Q)=H^1(E,\mathbf Q)\ne0\), while
  \(\mathcal H^0(\mathbf Q_E[1])_p=0\) for every \(p\). Hypercohomology can
  be global even when the proposed local-degree sheaf vanishes everywhere.
- **Re-entry condition:** use the special geometric origin of
  \(IC(R^{2n-1}\pi_*\mathbf Q)\) and of the class \(s(\zeta)\). B015 gives a
  usable local model after an independent-node hyperplane is supplied, but a
  class-directed incidence theorem must still produce that hyperplane and
  prove nonzero restriction.

## NG-013 - Boundary pullback cannot start from an HC-built singularity

- **Label:** NO-GO
- **Route:** use a rational period/normal-function map
  \(\rho_\zeta\) to a partially compactified classifying space, prove the
  pullback of a boundary fundamental class is nonzero, and infer a
  class-specific singular hyperplane.
- **Valid input:** Green-Griffiths II identifies selected singular-locus
  components locally with inverse images of Hodge-theoretic boundary
  components and proposes boundary-class pullback as an existence mechanism.
- **Invalid inference:** the paper supplies an unconditional global
  class-dependent map and nonzero pullback for an arbitrary primitive Hodge
  class.
- **Precise obstruction:** on pp. 6-7, the nodal point for \(\zeta\) is
  produced after assuming HC and writing
  \(k_0\zeta=[W-H]\), then choosing a general hypersurface containing \(W\).
  This is the desired algebraicity input. On p. 8 the boundary-pullback
  question is explicitly posed under HC and the results are described as
  preliminary. On p. 95 the anticipated pullback formula still contains a
  correction term, and the relevant universal Jacobian compactification and
  boundary components are listed as objects to define.
- **Re-entry condition:** construct the class-dependent global map and its
  boundary cycle without an algebraic representative of \(\zeta\), control
  compactification and excess-intersection corrections, and prove that the
  nonzero pullback lands on an independent-node component carrying a
  nonzero Saito pairing.

## NG-014 - Raising the polarization does not transport local detectors

- **Label:** NO-GO
- **Route:** take a Saito detector in \(|mL|\), multiply its defining section
  by a section of \(kL\), and regard the result as the same detector in
  \(|(m+k)L|\); conclude that the individual detector spaces are monotone.
- **Valid input:** multiplication of sections gives a map
  \(H^0(X,mL)\times H^0(X,kL)\to H^0(X,(m+k)L)\). B017 independently proves
  that the cumulative spans form an ascending chain.
- **Invalid inference:** the product section defines an independent-node
  member and canonically preserves the local vanishing relation and Saito
  ambient class.
- **Precise obstruction:** the zero divisor of the product is
  \(Y+\operatorname{div}(s)\), hence reducible with a fixed component and
  extra intersection singularities. It is not in the B015
  independent-node locus in general. Neither the local relation space nor
  \(\gamma_\beta\) has a canonical comparison across this degeneration.
- **Re-entry condition:** construct a smoothing or correspondence between
  powers that stays in controlled independent-node strata and prove through
  the vanishing-cycle exact sequence that it preserves the ambient detector
  class.

## NG-015 - Tautological incidence cannot detect a primitive class

- **Label:** NO-GO
- **Route:** impose a codimension-\(n\) complete intersection of divisors from
  powers of \(L\) as a base locus for a nodal hyperplane construction, then
  use that complete-intersection class as the ambient detector.
- **Valid input:** high powers provide many divisors and can force special
  singular members through a chosen complete intersection.
- **Invalid inference:** the resulting complete-intersection class has a
  nonzero primitive component or can pair nontrivially with a primitive
  middle Hodge class.
- **Precise obstruction:** B018 gives
  \([W]=c\,c_1(L)^n\). For primitive \(\zeta\),
  \(c_1(L)\cup\zeta=0\), so
  \(\langle\zeta,[W]\rangle=0\), and the primitive projection of \([W]\) is
  zero. Higher degrees only change \(c\). Other vanishing classes of the
  singular member are not supplied by this calculation.
- **Re-entry condition:** prove that the degeneration creates an additional
  non-tautological Saito detector class with controlled ambient pushforward,
  without choosing a non-tautological algebraic subvariety representing the
  desired Hodge direction.

## NG-016 - Matching spheres are not automatically local Hodge detectors

- **Label:** NO-GO
- **Route:** choose a matching path between two Lefschetz critical values,
  glue the thimbles to a Lagrangian sphere, and declare its homology class to
  be an independent-node Saito detector.
- **Valid input:** B019 and Auroux's Definition 8.1 give an embedded
  Lagrangian sphere from two isotopic vanishing cycles transported to a
  smooth midpoint fiber.
- **Invalid inference:** the two endpoints are simultaneous nodes on one
  algebraic hyperplane, or the matching sphere equals
  \(\gamma_\beta\) for a rational type-\((0,0)\) local relation.
- **Precise obstruction:** the matching path runs between distinct critical
  values of a symplectic pencil. Its output is a real Lagrangian sphere. The
  cited construction supplies neither an algebraic collision into one
  singular member nor a mixed-Hodge comparison proving that the resulting
  class lies in Saito's local relation channel. Even for the audited
  projective surfaces, Hodge type is not automatic and codimension one is a
  special already-known Hodge case.
- **Re-entry condition:** construct a holomorphic two-parameter deformation
  that collides the two critical values into an independent-node member,
  identify the specialized matching class with \(\gamma_\beta\), and prove
  \(\beta\in R(Y)_1^{(0,0)}\) while preserving the nonzero ambient pairing.

## NG-017 - Intersection-one vanishing cycles do not form a relation

- **Label:** NO-GO
- **Route:** use Schnell's two vanishing cycles from Section 3.4, or the
  occurrence of a node in a general plane section of the dual variety, as
  the two-node relation required by B009-B010.
- **Valid input:** Schnell proves that for even-dimensional \(X\) there are
  vanishing cycles \(\delta_1,\delta_2\) with
  \((\delta_1,\delta_2)=1\), and records that a dual-plane node represents a
  hyperplane with two ordinary double points.
- **Invalid inference:** \(\delta_1-\delta_2=0\), or every simultaneous
  two-node hyperplane has a nonzero rational type-\((0,0)\) relation.
- **Precise obstruction:** intersection number one makes the constructed
  pair rationally linearly independent. Schnell obtains that pair from the
  cusp/Milnor-number-two case. The neighboring statement about a two-ODP
  hyperplane asserts only the singularity configuration; it supplies no
  dependence, Hodge type, or nonzero Saito pushforward.
- **Re-entry condition:** independently compute the vanishing-cycle map for
  a controlled multi-node algebraic collision, exhibit a nonzero kernel
  element of rational type \((0,0)\), and prove its ambient detector class
  survives and pairs nontrivially with the specified Hodge class.

## NG-018 - A matching pair cannot enter the cusp pair unchanged

- **Label:** NO-GO
- **Route:** move the two critical values of a matching path together through
  the cusp/Milnor-number-two model and identify the two vanishing cycles
  before and after collision class by class.
- **Valid input:** the matching cycles are isotopic in a common smooth fiber;
  the cusp model has two vanishing cycles.
- **Invalid inference:** continuity alone identifies the two matching-cycle
  classes with Schnell's two cusp-cycle classes.
- **Precise obstruction:** the matching classes agree up to orientation, so
  their rational span has rank at most one. The cusp cycles have intersection
  number one and span rank two. A linear comparison preserving both
  individual classes cannot change this rank. B021 makes the contradiction
  explicit.
- **Re-entry condition:** use a degeneration with a computed braid/basis
  change or additional vanishing cycles, and prove directly on the full
  specialization complex that the ambient tube class maps to a nonzero
  rational type-\((0,0)\) relation. Preserving only the ambient class remains
  logically possible but unproved.

## NG-019 - A thimble relation is not yet an ambient detector

- **Label:** NO-GO
- **Route:** construct a nonzero coefficient vector in the kernel of the
  thimble boundary map and immediately regard it as a nonzero primitive
  ambient detector class.
- **Valid input:** B022 identifies zero-boundary thimble combinations with
  \(\ker\partial\) in a generic projective-hypersurface pencil.
- **Invalid inference:** every nonzero element of \(\ker\partial\) maps
  nontrivially to ambient middle homology.
- **Precise obstruction:** the exact reconstruction first forms
  \(\mathcal T(Y)=\ker\partial/\operatorname{im}\tau_\infty\); equator
  extensions die. The projection from \(\mathcal T(Y)\) to ambient homology
  modulo the reference-fiber image has a further explicit kernel
  \(K=\ker(H_{n-2}(X')\to H_{n-2}(X_b))\). A relation can die at either
  stage before Hodge type or the class-specific pairing is considered.
- **Re-entry condition:** compute the proposed collision on the quotient
  \(\mathcal T(Y)/K\), prove the specialized class is nonzero there, and
  then identify it with a rational type-\((0,0)\) Saito class retaining the
  nonzero \(\zeta\)-pairing.

## NG-020 - Hurwitz moves cannot repair a relation-rank mismatch

- **Label:** NO-GO
- **Route:** apply braid/Hurwitz moves to the two-cycle matching
  configuration until it becomes the intersection-one cusp configuration,
  without changing the fibration or adding vanishing cycles.
- **Valid input:** distinguished bases in a fixed exact Morse fibration are
  related by Hurwitz moves.
- **Invalid inference:** an invertible Hurwitz change can change the rank of
  the thimble boundary map or the dimension of its kernel.
- **Precise obstruction:** Seidel's moves are generated by
  symplectomorphisms and Dehn twists and include inverses. B023 expresses the
  resulting homology square and proves that the relation kernels are
  isomorphic. The matching pair has a nonzero relation kernel (at least one
  dimensional); the intersection-one cusp pair has none.
- **Re-entry condition:** exhibit a genuinely topology-changing collision
  map or add further vanishing directions, then compute the induced
  non-invertible map on the full quotiented thimble complex. Calling that
  operation a Hurwitz move is insufficient.

## NG-021 - Global thimble generation is not algebraicity

- **Label:** NO-GO
- **Route:** use the surjection
  \(\mathcal T(Y)\twoheadrightarrow PH_n(X)\) for a smooth projective
  complete intersection and conclude that primitive Hodge classes are
  algebraic or already have local normal-function singularities.
- **Valid input:** B024 proves that every nonzero primitive cohomology class
  pairs nontrivially with the ambient image of some global quotiented
  thimble class.
- **Invalid inference:** the thimble image is represented by an algebraic
  cycle, or the global thimble combination is a rational type-\((0,0)\)
  relation at one singular hyperplane.
- **Precise obstruction:** the surjection reconstructs singular homology
  topologically. It carries no algebraic-cycle-class assertion and combines
  thimbles over multiple critical values. B010 requires a one-fiber Saito
  relation with the correct Hodge type and pairing. The complete-intersection
  hypothesis is also a special family with no reduction from arbitrary
  smooth projective varieties.
- **Re-entry condition:** construct a class-preserving algebraic collision
  from the chosen quotient-level thimble detector to one independent-node
  Saito relation, then prove its type \((0,0)\), nonzero pairing, and a
  mechanism reducing arbitrary smooth projective varieties if global scope
  is claimed.

## NG-022 - A higher isolated singularity has no internal morsification relation

- **Label:** NO-GO
- **Route:** collide several Morse critical points into one higher isolated
  hypersurface singularity and use the resulting \(\mu\) morsification cycles
  as a nonzero local relation.
- **Valid input:** a morsification has \(\mu\) Morse points and therefore
  supplies \(\mu\) distinguished vanishing cycles.
- **Invalid inference:** having several vanishing cycles or Milnor number
  \(\mu>1\) produces a nonzero coefficient vector that kills their classes
  inside the local Milnor lattice.
- **Precise obstruction:** B025, using Brieskorn's appendix and Ebeling's
  Theorem 3 and Corollary 4, proves that the distinguished cycles form an
  integral basis of the rank
  \(\mu\) Milnor lattice. The internal rational relation kernel is zero.
  Any Saito relation must instead lie in the kernel of the map from the sum
  of local Milnor lattices to homology of the global nearby projective fiber.
- **Re-entry condition:** construct a global algebraic incidence or
  topology-changing degeneration for which that local-to-global map has a
  prescribed kernel vector, and prove rational type \((0,0)\), survival
  through the B022 quotients, and nonzero pairing with the specified Hodge
  class.

## NG-023 - A positive adjoint defect does not select the prescribed detector

- **Label:** NO-GO
- **Route:** find a nodal member with
  \(h^1(I_\Delta\otimes K_X\otimes L^n)>0\) and conclude that it detects the
  specified primitive Hodge class.
- **Valid input:** B026 proves that this dimension equals the nodal relation
  and extra-homology dimensions. After separately proving that the
  extra-to-primitive map has nonzero image, that detector subspace is
  available for pairing.
- **Invalid inference:** any nonzero detector subspace pairs nontrivially
  with the specified \(\zeta\), or a coherent defect vector is automatically
  the chosen global detector.
- **Precise obstruction:** B031 first shows that the primitive ambient image
  may be zero (NG-027). Even after excluding that kernel failure, a
  positive-dimensional ambient image may be contained in the annihilator
  \(\zeta^\perp\). Dimension does not supply the required class-paired
  vector-level incidence.
- **Re-entry condition:** construct a rational comparison over a nodal
  incidence locus and prove that the section induced by the chosen global
  detector has a fiber with nonzero \(\zeta\)-pairing.

## NG-024 - Full node independence kills high-power defect

- **Label:** NO-GO
- **Route:** restrict the detector search to high-power nodal members whose
  entire node scheme imposes independent conditions on the defining linear
  system, as in G009-G011.
- **Valid input:** full independence gives the clean B015 normal-crossing
  discriminant model.
- **Invalid inference:** this controlled locus can still carry a nonzero
  vanishing-cycle relation in complex dimension at least four.
- **Precise obstruction:** B027 multiplies interpolation sections by a
  section of \(K_X\otimes A^{n-1}\) nonvanishing at every node. For
  \(n\ge2\) and \(A\) sufficiently high, this forces adjoint interpolation,
  so \(H^1(I_\Delta\otimes K_X\otimes A^n)=0\). B026 then forces the
  relation space to vanish. The nonzero primitive class on
  \(\mathbf P^2\times\mathbf P^2\) explicitly falsifies G009's universal span
  claim.
- **Re-entry condition:** allow the full node set to be dependent while
  requiring independently controlled parts \(\Delta=J\sqcup K\). Compute
  the cross-part relation in B009's quasi-local model and retain the
  prescribed pairing; this is G012.

## NG-025 - A smoothing circuit need not be an adjoint defect

- **Label:** NO-GO
- **Route:** choose a minimal dependent set of node-smoothing evaluation
  functionals, partition its circuit into two independent parts, and infer a
  nonzero vanishing-cycle relation.
- **Valid input:** every circuit of the \(A\)-evaluation matroid partitions
  into two nonempty independent subsets, so it satisfies the combinatorial
  part of the Green-Griffiths quasi-local hypothesis.
- **Invalid inference:** dependence for the defining system \(A\) persists in
  the larger adjoint system \(F=K_X\otimes A^n\).
- **Precise obstruction:** B028 proves \(r_A(S)\le r_F(S)\) at high power and
  gives \(m+2\) points on a line in
  \(\mathbf P^2\times\mathbf P^2\) that form an \(A=\mathcal O(m,m)\) circuit
  but impose independent conditions on
  \(F=\mathcal O(2m-3,2m-3)\) for \(m\ge4\). Their adjoint defect is zero.
- **Re-entry condition:** impose both Edmonds' inequalities
  \(|S|\le2r_A(S)\) and the independent strict condition
  \(r_F(\Delta)<|\Delta|\), then construct the nodal member and the
  class-paired rational relation. This is G013.

## NG-026 - Overloading one line destroys isolated nodality

- **Label:** NO-GO
- **Route:** on \(\mathbf P^2\times\mathbf P^2\), put enough candidate nodes
  on one line to satisfy Edmonds' two-part inequalities and force positive
  adjoint evaluation defect.
- **Valid input:** for \(A=\mathcal O(m,m)\), the smallest collinear sets
  dependent for \(F=K_X\otimes A^2=\mathcal O(2m-3,2m-3)\) remain
  partitionable into two \(A\)-independent subsets.
- **Invalid inference:** every finite configuration satisfying the two rank
  systems can occur as the isolated node scheme of a member of \(|A|\).
- **Precise obstruction:** B029 proves that a section of \(A\) singular at
  more than \(m\) points of \(C=\mathbf P^1\times\{q\}\) vanishes to second
  order along \(C\). Positive collinear \(F\)-defect requires more than
  \(2m-2\) points, so \(C\) lies in the singular locus and the member is not
  nodal.
- **Re-entry condition:** seek distributed support or a genuinely
  zero-dimensional Cayley-Bacharach-type adjoint dependence, and verify the
  first-jet incidence has an isolated nodal member before invoking B026.

## NG-027 - Positive extra homology need not reach primitive ambient homology

- **Label:** NO-GO
- **Route:** realize isolated nodes, a two-part smoothing partition, and
  positive adjoint defect, then infer that some vanishing-cycle relation has
  nonzero primitive ambient image.
- **Valid input:** B026 identifies the adjoint defect dimension with the
  relation and extra-homology dimensions. B030 realizes all three geometric
  conditions on a plane-containing nodal quintic.
- **Invalid inference:** the canonical Saito map
  \(\Phi_Y:E^\vee(Y)\to H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\) is injective,
  or even nonzero, whenever its source is nonzero.
- **Precise obstruction:** B031 has
  \(\dim E^\vee(Y)=1\) for general plane-containing nodal hypersurfaces
  \(Y\subset\mathbf P^4\) in every degree \(d\ge3\), while
  \(H_4(\mathbf P^4,\mathbf Q(2))_{\mathrm{prim}}=0\). Thus
  \(\Phi_Y=0\) and every nonzero relation has zero Saito ambient class, even
  in arbitrarily high degree.
- **Re-entry condition:** impose and prove a third rank condition
  \(\operatorname{rank}\Phi_Y>0\) independently of the smoothing and adjoint
  evaluation matroids, then prove that
  \(\operatorname{im}\Phi_Y\not\subseteq\zeta^\perp\).

## NG-028 - Literal import of the six-invariant ambient-image equality

- **Label:** NO-GO
- **Route:** use Green–Griffiths Section 4.2.4's printed
  \(\rho(i)=\rho(ii)\) to infer that every nonzero nodal relation has a
  nonzero primitive ambient image, or that the canonical map is injective.
- **Valid input:** pages 18-19 explicitly define \(\rho(i)\) as relation
  dimension and \(\rho(ii)\) as primitive ambient-image dimension, then
  print equality of six invariants. Page 2 describes the document as an
  extended research announcement and says some complete details were still
  unwritten.
- **Invalid inference:** import that component without checking it against
  Saito's separately defined canonical map and standard defect examples.
- **Precise obstruction:** B031 gives, for every \(d\ge3\), a general nodal
  degree-\(d\) hypersurface containing a plane in \(\mathbf P^4\). Its
  relation and extra-homology spaces have dimension one, while
  \(H_4(\mathbf P^4,\mathbf Q(2))_{\mathrm{prim}}=0\), so the ambient image
  has dimension zero. Arbitrarily high degree rules out a mere insufficient
  ampleness explanation.
- **Re-entry condition:** locate a published correction or an alternative
  definition of \(\rho(ii)\), or supply a proof with hypotheses that excludes
  the plane family. A targeted search through 2026-08-10 found none. Until
  then, retain only independently triangulated non-\(\rho(ii)\) defect
  comparisons and carry \(\operatorname{rank}\Phi_Y\) independently.

## NG-029 - Anchored positive-rank witness as general Hodge progress

- **Label:** NO-GO
- **Route:** use B032's nodal \((2,2)\) divisor containing the diagonal in
  \(\mathbf P^2\times\mathbf P^2\) as evidence that G013 can be solved for an
  arbitrary input Hodge class.
- **Valid input:** B032 simultaneously realizes defining-system node
  independence, adjoint defect one, a rational relation, rank-one
  extra-to-primitive map, and nonzero pairing with the primitive class
  \(h_1^2-h_1h_2+h_2^2\).
- **Invalid inference:** the same incidence can be constructed without first
  choosing an algebraic cycle whose primitive class is the desired detector.
- **Precise obstruction:** the divisor is required to contain the diagonal.
  Its extra class is the diagonal's homology class and its nonzero ambient
  image is proved by computing the already-known algebraic diagonal class.
  This is Thomas' HC-to-nodal direction, not the missing reverse
  class-selection mechanism.
- **Re-entry condition:** replace the fixed diagonal by incidence data
  constructed functorially from a rational Hodge class or global tube
  detector, without assuming an algebraic representative, while preserving
  all three ranks and the nonzero pairing.

## NG-030 - Double transitivity as uniform position

- **Label:** NO-GO
- **Route:** combine Clemens' doubly transitive monodromy on nodes with the
  existence of one independent subset and infer that every subset of the
  same cardinality is independent.
- **Valid input:** double transitivity identifies all ordered pairs of
  distinct nodes.
- **Invalid inference:** it identifies all subsets of every cardinality.
- **Precise obstruction:** the Edmonds inequalities involve arbitrary
  subsets. A 2-transitive group need not be transitive on \(s\)-subsets for
  \(s\ge3\), so the rank-failure locus on an \(s\)-subset labeling cover need
  not be irreducible or proper over the section space.
- **Re-entry condition:** prove sufficiently high set-transitivity. B033
  does this by constructing a simple double zero: its local monodromy is a
  transposition, which together with 2-transitivity gives the full symmetric
  group. This repairs the postulation step but not the algebraic-anchor
  obstruction NG-029.

## NG-031 - Fixed-carrier two-block scaling

- **Label:** NO-GO
- **Route:** start from an algebraic middle-dimensional carrier
  \(W^n\subset X^{2n}\), apply Thomas' high-power construction, and expect
  the resulting nodes to split into the same two independent blocks used by
  B009 and B033 in every dimension.
- **Valid input:** the nodes are the regular zeros of
  \(N^*_{W/X}\otimes L^m|_W\), and B033 realizes the two-block package when
  \(n=2\).
- **Invalid inference:** the number of blocks is dimension-independent.
- **Precise obstruction:** B034 proves
  \[
  \#Z_m=d\,m^n+O(m^{n-1}),\qquad
  h^0(W,L^m|_W)=\frac d{n!}m^n+O(m^{n-1}).
  \]
  Each independent block has size at most the second quantity. Hence every
  fixed \(q<n!\), in particular \(q=2\) for \(n\ge3\), is eventually
  impossible.
- **Re-entry condition:** either construct unanchored two-block members with
  fewer nodes, as G014 demands, or prove a multipart local channel and use
  dimension-scaled Edmonds inequalities.

## NG-032 - Inducting the bipartite local theorem

- **Label:** NO-GO
- **Route:** for
  \(\Delta=J_1\sqcup\cdots\sqcup J_q\), repeatedly apply B009 to
  \(J_1\) and \(J_2\cup\cdots\cup J_q\).
- **Valid input:** each individual \(J_a\) is independently smoothable.
- **Invalid inference:** the complement of one block is independently
  smoothable.
- **Precise obstruction:** separate independence is not closed under union;
  in the B034 density regime, a large union must be dependent. Therefore
  B009's bipartite hypotheses fail before the induction begins.
- **Re-entry condition:** compute the genuine multipart monodromy and local
  intersection-cohomology complex, including higher block intersections.
  This is G015.

## NG-033 - Crossingwise resolution as the multipart IC computation

- **Label:** NO-GO
- **Route:** resolve the multipart discriminant and identify the desired
  local intersection-cohomology group with the direct sum of the Koszul
  groups at the resulting pairwise normal crossings.
- **Valid input:** B035 resolves the minimal \(U_{2,5}\) arrangement by one
  blow-up. At every crossing \(E\cap\widetilde H_i\), the Picard-Lefschetz
  logarithms satisfy \(N_EN_i=0\).
- **Invalid inference:** vanishing of every crossingwise degree-two term
  computes the stalk of the intermediate extension at the original origin.
- **Precise obstruction:** the exceptional fiber is a complete
  \(\mathbf P^1\) with five marked points. Proper base change produces its
  global hypercohomology, not a direct sum of crossing stalks. The desired
  downstairs intermediate-extension summand must also be separated from
  possible point-supported summands in the proper direct image.
- **Re-entry condition:** compute the full marked-\(\mathbf P^1\)
  intermediate-extension quiver for the Picard-Lefschetz representation,
  isolate the downstairs IC summand, and compare its rational degree-one
  group and Hodge type with the five-cycle relation kernel.

## NG-034 - Complex arrangement quiver as a Hodge-type proof

- **Label:** NO-GO
- **Route:** compute the \(U_{2,5}\) intermediate extension with S035's
  arrangement face algebra and infer the rational type-\((0,0)\) statement
  required by G015.
- **Valid input:** Bapat's Definition 4.3 and Corollary 5.8 identify the
  complex perverse IC extension as the image of induction in coinduction.
- **Invalid inference:** this complex-linear module calculation preserves a
  rational lattice, weight filtration, or Hodge filtration.
- **Precise obstruction:** S035 defines its face algebra over \(\mathbf C\)
  and proves an equivalence of complex perverse-sheaf categories. No
  mixed-Hodge-module enhancement or comparison with Saito's rational
  type-\((0,0)\) class is supplied. The missing information is invisible to
  the cited category.
- **Re-entry condition:** after computing B037's rational transgression,
  construct the corresponding rational mixed Hodge module or compare it
  directly with Saito's local class, including the Tate twist, weights, and
  Hodge filtration.

## NG-035 - Raw exceptional classes are order invariant

- **Label:** NO-GO
- **Route:** prove G021 stepwise in an arbitrary permissible order by claiming
  that no later dominant center is contained in an earlier exceptional
  divisor.
- **Valid input:** Li permits orders whose prefixes are building sets and
  defines the dominant transform of a contained subvariety as its full
  inverse image.
- **Invalid inference:** a later dominant center always avoids the earlier
  exceptional boundary.
- **Precise obstruction:** for a point \(F\) on a smooth codimension-two
  curve \(G\) in a threefold, blowing up \(G\) first turns \(F\) into
  \(\mathbf P(N_{G/Y}|_F)\subset E_G\). Blowing this center up gives
  \([D_G]=[E_G^{\rm pull}]-[E_F]\).
- **Re-entry condition:** calculate in an inclusion-compatible order and use
  Li's canonical wonderful model to transport the intrinsic labelled
  divisors. B049 implements this repair.

## NG-036 - Quasi-local implies analytically linear

- **Label:** NO-GO
- **Route:** reduce G015 to B052 by simultaneously straightening every
  Green-Griffiths quasi-local discriminant branch to its tangent hyperplane.
- **Valid input:** the branches are smooth; at their codimension-two common
  intersection every pair of local equations is a coordinate system; the
  disjoint-node monodromies commute and are unipotent.
- **Invalid inference:** these first-order and monodromy conditions remove
  all higher analytic moduli.
- **Precise obstruction:** for slopes (M=\{0,1,2,4,8\}), the branches
  (y-mx-m^4x^2=0) satisfy the quasi-local condition. Their tangent set has
  trivial projective stabilizer, while quadratic coordinate changes alter
  their curvature vector only by values of a cubic polynomial. The vector
  ((m^4)_{m\in M}) is not a cubic evaluation vector, so the branches cannot
  all be straightened. Pullback from a submersive projective five-node family
  preserves projectivity.
- **Re-entry condition:** prove invariance only of the rational degree-one IC
  channel and its mixed Hodge structure under deformation to the tangent
  arrangement. This is G026.

## NG-037 - Equisingular monodromy generates new ambient directions

- **Label:** NO-GO
- **Route:** find one clean multipart nodal incidence component with a
  nonzero canonical ambient image and use large monodromy on its nodes or
  relation vectors to span primitive rational Hodge homology.
- **Valid input:** the relation local system can have large monodromy, and
  B033 shows that full symmetric node monodromy can control postulation.
- **Invalid inference:** monodromy of the domain moves its canonical image
  through different subspaces of the fixed ambient homology of \(X\).
- **Precise obstruction:** B055 proves that a morphism
  \(\Phi:\mathcal E\to
  H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\otimes\mathbf Q_S\)
  satisfies \(\Phi_s\rho(g)=\Phi_s\). Its image is constant on every
  connected equisingular stratum. Monodromy may move relation vectors inside
  the kernel but cannot create another ambient direction.
- **Re-entry condition:** compare distinct incidence components or cross a
  topology-changing boundary. The required specialization must survive the
  B022 equator and base-locus quotients, acquire rational type \((0,0)\), and
  retain nonzero pairing with the specified Hodge class. This is G029.

## NG-038 - The total pencil equator is the detector relation

- **Label:** NO-GO
- **Route:** factor the total equator of a complete generic Lefschetz pencil
  into all its meridians, apply B013 to an invariant class, and promote the
  telescoping relation to a nonzero ambient detector.
- **Valid input:** B057 identifies the telescoping coefficients with the
  actual coefficients in the ordered thimble-extension chain.
- **Invalid inference:** the total-equator extension survives the first
  B022 quotient.
- **Precise obstruction:** S029 equations (42)-(43) identify the coefficient
  matrix with \(T_\infty\), while equation (12) defines
  \(\mathcal T(Y)=\ker\partial/\operatorname{im}T_\infty\). Hence every
  invariant total-equator vector is zero in \(\mathcal T(Y)\), even when its
  thimble coefficients are nonzero.
- **Re-entry condition:** retain the actual non-equator detector loop placed
  in a generic plane net by B056. Track its B057 extension chain through a
  topology-changing collision and prove equality with a local Saito ambient
  class. This is G030.

## NG-039 - Exact recovery of a selected tube target is necessary

- **Label:** NO-GO
- **Route:** choose a nonorthogonal Hodge homology target \(c\) by B058 and
  treat equality \(\Phi_{Y_p}(\beta)=c\) as the smallest
  terminal-equivalent collision obligation.
- **Valid input:** such a \(c\) exists, and exact recovery would imply the
  required nonzero pairing.
- **Invalid inference:** every local detector subspace that pairs
  nontrivially with \(\zeta\) contains the independently preselected \(c\).
- **Precise obstruction:** B059 gives the type-\((0,0)\) rational model
  \(\zeta(x,y)=x\), \(c=(1,0)\), and
  \(D=\mathbf Q(1,1)\). The subspace \(D\) detects \(\zeta\), but
  \(c\notin D\).
- **Re-entry condition:** retain exact equality only as the stronger G030
  mechanism. B125 reduces G031 to G084's clean-support incidence; B127/NG102
  then identify active terminal gate G008 inside it and separate cleanup G085.

## NG-040 - Generic morsification preserves local detection

- **Label:** NO-GO
- **Route:** morsify a detecting isolated singularity into ordinary double
  points and infer a clean nodal Saito detector from conservation of Milnor
  number.
- **Valid input:** morsification preserves total Milnor rank and produces a
  distinguished collection of Morse vanishing cycles.
- **Invalid inference:** this collection supplies a relation at one singular
  fiber and retains the primitive ambient pairing with \(\zeta\).
- **Precise obstruction:** B025 proves that the distinguished cycles form an
  integral basis of the local Milnor lattice, so there is no internal
  relation. Their separate Morse values are smooth points of the
  discriminant, where B008 gives zero rational degree-one local IC channel.
- **Re-entry condition:** deliberately recollide the Morse data and compute a
  topology-changing map on the full nearby-cycle complex, proving survival
  through the B022 quotients, rational type \((0,0)\), and nonzero specified
  pairing. This is G032.

## NG-041 - Bouali's preprint chain closes the general Hodge Conjecture

- **Label:** NO-GO
- **Route:** import arXiv:2401.03465v13 as a general proof via its claimed
  hypersurface theorem, nearby-cycle degeneration, and arithmetic
  Hodge-locus criterion.
- **Valid input:** the final paper explicitly states a universal Hodge
  theorem and identifies arXiv:2303.09932 Theorem 4 as its decisive
  algebraicity input.
- **Invalid inference:** a cycle constructed over the p-adic completion
  \(\widehat{k}_{\sigma_p}\) can be averaged under
  \(G_k=\operatorname{Gal}(\bar k/k)\) merely because its cohomology class is
  invariant.
- **Precise obstruction:** S040 locates the step on pp. 34-35 of
  arXiv:2303.09932v16. No descent of the constructed cycle to \(\bar k\) or
  a finite extension is proved, so its \(G_k\)-orbit and the displayed finite
  average are undefined. B060 gives the exact field-of-definition
  countermodel.
- **Propagation:** the gap invalidates the written proof of its Theorem 3;
  Corollary 2(ii), Theorem 4, and the pp. 14-15 conclusion of
  arXiv:2401.03465v13 depend on that theorem.
- **Re-entry condition:** construct a representative over a finite algebraic
  extension of \(k\), with the same p-adic class, before applying trace or
  averaging. The replacement must not assume the Tate or Hodge conjecture.

## NG-042 - Iterated nearby cycles commute automatically

- **Label:** NO-GO
- **Route:** identify the two orders of nearby cycles in a recollision as a
  formal identity, or infer commutation from clean intersection of the
  reduced boundary divisors alone.
- **Valid input:** natural lax comparison maps among multivariable and
  iterated nearby-cycle objects do exist.
- **Invalid inference:** those maps are equivalences for an arbitrary
  coefficient object at a critical two-parameter collision.
- **Precise obstruction:** Kochersperger S041 states that nearby-cycle
  functors do not commute in general and obtains commutation only under a
  without-slopes hypothesis. Nadler gives a separate non-characteristic plus
  Thom criterion. B062 proves that graph embedding into a submersive ambient
  projection retains the original map's critical conormal obstruction.
- **Re-entry condition:** for the exact recollision chart and coefficient
  object, verify a published sufficient package and then prove the additional
  rational mixed-Hodge, B022-quotient, and Saito-pairing compatibilities in
  G033.

## NG-043 - Apply without-slopes commutation directly to the raw A2 chart

- **Label:** NO-GO
- **Route:** use the smooth total space of the miniversal \(A_2\) collision as
  sufficient input for B063 in the raw base coordinates.
- **Valid input:** B063 gives an isomorphism in mixed Hodge modules once the
  underlying graph-pair is without slopes.
- **Invalid inference:** total-space smoothness or generic nodality verifies
  that hypothesis.
- **Precise obstruction:** B064 computes discriminant
  \(4s^3+27t^2=0\) and critical points with \(st\ne0\). Thus the raw map
  fails the geometric without-slopes condition recalled in S042. For the
  graph-pushed module, the separate Bernstein-Sato/\(V\)-multifiltration
  condition has not been checked.
- **Re-entry condition:** prove that exact graph-pair condition directly, or
  pass to G034's resolved boundary and prove strict multispecialisability,
  descent, and pairing survival.

## NG-044 - Quasi-ordinary cusp compatibility is the two-parameter bridge

- **Label:** NO-GO
- **Route:** apply S042 Proposition 10.2 to the cusp and infer the full
  \((s,t)\)-recollision comparison.
- **Valid input:** a plane cusp is quasi-ordinary, and the cited proposition
  proves strict multispecialisability for a specified direct-image Hodge
  module.
- **Invalid inference:** it simultaneously controls both ambient base
  coordinates and the actual family detector object.
- **Precise obstruction:** the source treats a \(p\)-dimensional
  quasi-ordinary hypersurface along its first \(p\) ambient coordinates. For
  a plane cusp, \(p=1\). G033 needs two recollision parameters plus B022 and
  Saito-map compatibility, none of which is supplied by Proposition 10.2.
- **Re-entry condition:** verify the two local \(V\)-filtrations on every
  B065 double-crossing chart, glue around \(E_3\), and prove detector descent
  as formulated in G035.

## NG-045 - SNC base discriminant makes the total family semistable

- **Label:** NO-GO
- **Route:** stop after B065's three base blowups and treat the pulled-back
  \(A_2\) family as a smooth total-space normal-crossing degeneration.
- **Valid input:** the reduced total transform of the cusp in the base is SNC.
- **Invalid inference:** the raw pulled-back hypersurface is therefore smooth
  or semistable.
- **Precise obstruction:** B066 computes its Jacobian. The total family is
  still singular along the sections over \(E_3\) and \(E_2\), although it is
  smooth over generic \(E_1\).
- **Re-entry condition:** construct the total-space modification or finite
  base change explicitly, track rational descent and all direct-image
  supports, and prove detector-pairing survival as required by G036.

## NG-046 - Surface simultaneous resolution handles every suspended A2 gate

- **Label:** NO-GO
- **Route:** import the Weyl simultaneous resolution of a surface \(A_2\)
  rational double point as G036's arbitrary-dimensional total-space model.
- **Valid input:** B068/S043 proves the surface theorem, and B067 identifies
  the same \(S_3\) root cover algebraically.
- **Invalid inference:** quadratic suspension automatically extends the
  simultaneous resolution, rational MHM descent, and detector compatibility
  to the Hodge route.
- **Precise obstruction:** after B001, the ambient variety has dimension
  \(2n\), so a singular hyperplane fiber has odd dimension \(2n-1\), never
  surface dimension two. S043 is formulated using a minimal surface
  resolution and exceptional \((-2)\)-curves; it contains no dimension-
  uniform suspension theorem.
- **Re-entry condition:** prove G037 for every odd fiber dimension, including
  an \(S_3\)-equivariant semistable model, support-by-support rational
  pushdown, and survival of the quotient-level detector pairing.

## NG-047 - Weak semistable reduction closes detector descent

- **Label:** NO-GO
- **Route:** cite Abramovich–Karu Theorem 0.3 and declare G037 complete.
- **Valid input:** after a projective base alteration and projective
  modification, a dimension-uniform weakly semistable model exists.
- **Invalid inference:** this is a smooth \(S_3\)-equivariant model whose
  rational detector traces nontrivially to the original family.
- **Precise obstruction:** S044's definition permits singular total space;
  the alteration is not identified with the root cover, equivariance is not
  asserted, and no theorem there identifies rational MHM strictness,
  full-support pushdown, B022 quotients, or the Saito pairing.
- **Re-entry condition:** prove the six-part equivariant refinement and trace
  theorem G038.

## NG-048 - Absolute equivariant resolution preserves weak semistability

- **Label:** NO-GO
- **Route:** apply Temkin's canonical resolution to the total space from
  B069 and treat the result as a smooth weakly semistable family.
- **Valid input:** B070 proves that the absolute resolution is projective,
  regular, and equivariant under a finite group action.
- **Invalid inference:** the resolved map remains toroidal, equidimensional,
  saturated, and reduced-fiber and carries the same nearby-cycle detector.
- **Precise obstruction:** S045 chooses centers from absolute singularities
  and contains no relative statement about the morphism. These properties
  can be changed by arbitrary source blowups.
- **Re-entry condition:** prove G039 through equivariant subdivisions of the
  toroidal cone/lattice map and then establish the rational MHM trace square.

## NG-049 - Stacky semistability closes detector descent

- **Label:** NO-GO
- **Route:** apply the canonical semistable reduction of B071 and treat its
  output as both a finite-group-equivariant smooth scheme model and the
  rational detector trace required by G038.
- **Valid input:** S046 proves projective semistable reduction in arbitrary
  dimension and quasi-local compatibility lifts strict finite-group
  automorphisms at the logarithmic stack level.
- **Invalid inference:** the scheme realization is automatically equivariant,
  and rational nearby-cycle MHM, strict support, both B022 quotients, the
  Saito map, and the nonzero pairing descend without a separate theorem.
- **Precise obstruction:** S046 Remark 4.6 explicitly says that Kawamata's
  scheme realization is noncanonical. S046 contains no mixed-Hodge-module or
  detector-trace result.
- **Re-entry condition:** prove G040 either on the finite Deligne-Mumford
  stack or after an explicit equivariant projective scheme realization.

## NG-050 - Average a local A2 detector

- **Label:** NO-GO
- **Route:** choose any nonzero class in the local (A_2) vanishing lattice
  on the ordered-root cover and descend it by the normalized (S_3)-trace.
- **Valid input:** B072 supplies rational equivariant MHM and proper
  pushforward on the quotient stack, so the averaging endomorphism exists.
- **Invalid inference:** averaging a nonzero local class is nonzero.
- **Precise obstruction:** B073 computes the local root lattice as the
  standard two-dimensional (S_3)-representation. Its invariant space and
  normalized average projector are both zero.
- **Re-entry condition:** prove G041 by locating a trivial constituent in the
  larger global full-support nearby-cycle object and tracking it through both
  B022 quotients and the prescribed pairing.

## NG-051 - A trivial full-support summand forces nonzero trace

- **Label:** NO-GO
- **Route:** use B074's canonical invariant intermediate-extension summand to
  infer that any nonzero lifted boundary detector projects nontrivially to it.
- **Valid input:** finite-Galois intermediate-extension pushdown does contain
  the original full-support object as its rational invariant direct summand.
- **Invalid inference:** a specified nonzero vector has a nonzero component
  in that summand.
- **Precise obstruction:** in (mathbf1\oplus V_{\rm std}), the trivial
  summand exists but all vectors in (V_{\rm std}) average to zero. B073
  identifies (V_{\rm std}) as the local A2 root constituent.
- **Re-entry condition:** compute the actual equivariant boundary image and
  its two quotient projections as G042 requires.

## NG-052 - Finite-cover transfer survives collision

- **Label:** NO-GO
- **Route:** apply B075's identity (p_*p^!=d) on the smooth detector tube
  and infer that nearby specialization is a nonzero full-support detector.
- **Valid input:** the invariant sheet-transfer is nonzero before collision,
  normalized trace returns the original B058 tube, and the prescribed pairing
  is nonzero.
- **Invalid inference:** the specialized boundary avoids every kernel and
  lower-support summand.
- **Precise obstruction:** transfer does not compute nearby specialization.
  B022's equator-extension and base-locus kernels can kill a thimble class,
  and proper pushdown can place it on proper support.
- **Re-entry condition:** construct the actual semistable nearby boundary and
  verify support, both quotient maps, and the pairing as required by G042.

## NG-053 - Descent creates boundary nonvanishing

- **Label:** NO-GO
- **Route:** use the root cover, semistable nearby cycles, and normalized
  averaging to manufacture the missing nonzero detector downstairs.
- **Valid input:** B071-B072 provide the semistable stack and its rational
  nearby-cycle formalism; B075 supplies a nonzero invariant global transfer.
- **Invalid inference:** the cover/descent step creates a nonzero original
  boundary specialization.
- **Precise obstruction:** B076 proves that finite-cover unit and normalized
  trace remain a split pair after nearby cycles. They preserve existing
  nonvanishing but cannot turn a zero original nearby class into a nonzero
  one.
- **Re-entry condition:** prove the original/canonical specialization of the
  B058 tube is nonzero on full support, survives both B022 kernels, and keeps
  the prescribed pairing. This is G042's residual content and returns to
  G032/G031.

## NG-054 - Decomposition forces full-support landing

- **Label:** NO-GO
- **Route:** invoke the pure decomposition theorem for the semistable stack
  pushdown and infer that the specified nonzero specialized class has a
  nonzero full-support component.
- **Valid input:** B077 proves the pushdown is pure, semisimple, and decomposes
  into a full-support summand plus proper-support summands.
- **Invalid inference:** every nonzero class projects nontrivially to the
  full-support summand.
- **Precise obstruction:** a nonzero vector can lie entirely in the direct
  sum of exceptional/proper-support constituents. Semistable modifications
  create exactly such supports.
- **Re-entry condition:** compute the strict-support projection of the actual
  B058 nearby specialization and prove it is nonzero, as required by G043.

## NG-055 - Toric parity forces full-support landing

- **Label:** NO-GO
- **Route:** combine the ordinary degree-one label of the relation detector
  with B078's even support parity and declare all proper-support components
  of the B058 specialization zero.
- **Valid input:** for a globally proper toric map, B078 proves that a support
  term indexed by (V,b) occurs generically in ordinary degree
  (dim X-dim V+b), which is even; simplicial-source toric fibers have pure
  Hodge-Tate cohomology and no odd cohomology.
- **Invalid inference:** the same parity applies without further work to the
  global B071 hyperplane degeneration and to the exact Hodge module and
  degree containing the specified tube.
- **Precise obstruction:** B071 supplies local monomial/toroidal charts, not
  a single globally toric family. Global non-toric fiber cohomology produces
  coefficient Hodge modules and shifts, and no current brick identifies
  their contribution or the detector's normalization through nearby cycles
  and pushdown.
- **Re-entry condition:** prove G044's coefficient-sensitive toroidal parity
  and étale/stack gluing theorem, or compute the first odd proper-support term
  explicitly and subtract it in G043.

## NG-056 - Coefficient-blind toroidal parity

- **Label:** NO-GO
- **Route:** extend B078 chartwise and assert that even toric normal degree
  forces even total proper-support degree for every projective toroidal
  family, regardless of the coefficient system along the stratum.
- **Valid input:** the toric normal exceptional term in B079 occurs in
  ordinary degree two.
- **Invalid inference:** tensoring with global fiber cohomology preserves that
  parity.
- **Precise obstruction:** for
  $\operatorname{Bl}_0(\mathbf A^2)\times C\to\mathbf A^2$, where $C$ has
  positive genus, Kunneth produces the nonzero proper-support term
  $H^1(C,\mathbf Q)(-1)_0[-3]$. The map is smooth-factor toroidal and
  projective, yet the total support degree is odd.
- **Re-entry condition:** in G044 compute the exact convolution of normal
  support degree with coefficient degree and compare it with the B057
  detector degree. A matching degree must be retained and subtracted in G043.

## NG-057 - Toric parity after detector normalization

- **Label:** NO-GO
- **Route:** translate the relation channel into the normalized constant-sheaf
  direct image and then use B078 parity to exclude every proper support.
- **Valid input:** B080 identifies the degree-one coefficient-IC group with
  normalized direct-image degree $-1$, or raw total degree $2n$.
- **Invalid inference:** proper supports meeting that degree have odd toric
  parity.
- **Precise obstruction:** a codimension-$c$ support meets normalized degree
  $-1$ at shift $b=1-c$. The parity expression is then identically $2n$.
  Thus a divisor at $b=0$ and a point at $b=-1$ are both allowed.
- **Re-entry condition:** compute the actual multiplicity Hodge modules and
  B058 class coordinates for exactly those two shifts, as required by G045.

## NG-058 - A canonical total full-support projection

- **Label:** NO-GO
- **Route:** choose a decomposition-theorem isomorphism for the pure B071
  pushdown, sum all full-support constituents across perverse degrees, and
  treat the resulting projection of the B058 class as canonical.
- **Valid input:** B077 proves that such splittings exist and that every
  perverse cohomology object is semisimple with a unique strict-support
  decomposition.
- **Invalid inference:** the splitting across perverse degrees, and hence the
  induced total-class projection, is unique.
- **Precise obstruction:** de Cataldo-Migliorini Remarks 1.4.2 and 1.6.2
  explicitly state that decomposition-theorem splittings are noncanonical.
  Only the perverse filtration is canonical. In detector degree -1, the
  full/divisor contribution is $E_\infty^{-1,0}$, while the point term is
  the distinct grade $E_\infty^{0,-1}$.
- **Re-entry condition:** after G047 constructs a collision boundary class,
  use G046: pass it to the canonical $E_\infty^{-1,0}$ grade, then project by strict support inside
  ${}^pH^0$.

## NG-059 - Ambient homology canonically specializes to a collision stalk

- **Label:** NO-GO
- **Route:** take the B058 ambient primitive homology target $c$ and write a
  canonical class $\operatorname{sp}(c)\in H^{-1}(i_p^*K)$ at a chosen
  collision point.
- **Valid input:** B057 gives a smooth-locus extension-chain representative
  mapping to $c$, and B081 gives a canonical filtration on a stalk class once
  such a class exists.
- **Invalid inference:** ambient homology supplies a canonical reverse lift
  through the local relation and thimble-quotient maps.
- **Precise obstruction:** B022's arrows run from local/thimble data through
  the equator and base-locus quotients to ambient homology. Their kernels make
  reverse lifts nonunique, and a fixed collision relation space need not
  contain any lift of $c$. No collision family carrying the B057 chain has
  yet been constructed.
- **Re-entry condition:** prove G047-G048 by constructing the
  topology-changing family and nearby extension-chain class, killing its
  vanishing-cycle obstruction, and testing a special lift $\beta$ in G046.

## NG-060 - Nearby cycles canonically map back to the special stalk

- **Label:** NO-GO
- **Route:** after choosing a collision family, regard every nearby B057
  detector class as having a canonical special-stalk value.
- **Valid input:** nearby and vanishing cycles are defined functorially, and
  B083 gives their distinguished triangle.
- **Invalid inference:** the triangle provides an unconditional reverse map
  $\Psi_fK\to i^*K$ selecting a lift.
- **Precise obstruction:** the natural arrow is $i^*K\to\Psi_fK$. Exactness
  says a nearby class $t_\psi$ lifts only if
  $\mathrm{can}(t_\psi)=0$ in $\Phi_fK[1]$; when it lifts, the preceding
  term can make the lift nonunique.
- **Re-entry condition:** prove G048 by constructing the specified nearby
  class, computing and killing its vanishing-cycle obstruction, and
  controlling the lift ambiguity under both B022 quotients and the pairing.

## NG-061 - Detector-loop invariance equals collision invariance

- **Label:** NO-GO
- **Route:** use $g\alpha=\alpha$ from B057 as the monodromy-invariance
  hypothesis in B084's local invariant-cycle theorem.
- **Valid input:** the B057 detector loop closes its ordered extension chain,
  and B084 lifts nearby IC classes fixed by local collision monodromy.
- **Invalid inference:** the detector loop $g$ in the hyperplane complement
  and the loop around the collision parameter induce the same action.
- **Precise obstruction:** they are different parameter directions. The
  collision loop acts on the moving net and its ordered thimble system by a
  braid/Hurwitz transformation; no two-parameter comparison has identified
  its action on the specified B057 vector.
- **Re-entry condition:** prove G049 by realizing the B057 vector in nearby
  intersection cohomology and computing
  $T_{\mathrm{coll}}t_\psi=t_\psi$ for that exact class.

## NG-062 - A fixed ambient class has a fixed thimble lift

- **Label:** NO-GO
- **Route:** use constancy of the B058 primitive ambient class to conclude
  that its chosen B057 thimble lift is fixed by collision monodromy.
- **Valid input:** the B022 quotient map is monodromy equivariant and the
  ambient primitive local system is constant.
- **Invalid inference:** a lift of a fixed quotient vector must itself be
  fixed.
- **Precise obstruction:** monodromy may shear the lift by an equator or
  base-locus kernel vector. B085 proves that the defect defines a class in
  $\operatorname{coker}(M_J-I)$; the fixed quotient supplies no formal
  reason for that class to vanish.
- **Re-entry condition:** compute the actual braid action, combined kernel
  $J$, and B057 vector in G050, then exhibit a kernel adjustment killing the
  defect.

## NG-063 - Finite averaging kills the unipotent residue

- **Label:** NO-GO
- **Route:** average a thimble lift over the finite $S_3$ root-cover group
  and conclude it is invariant under all remaining collision monodromy.
- **Valid input:** B086 proves that Reynolds averaging kills the finite
  rational deck-group obstruction.
- **Invalid inference:** the same finite projector kills the unipotent
  monodromy $M=\exp N$ of the semistable degeneration.
- **Precise obstruction:** a nilpotent kernel shear can commute with the
  finite action and survive its average. B087 identifies its exact class as
  $[Nt]\in\operatorname{coker}N_J$.
- **Re-entry condition:** compute the actual logarithmic residue on the B057
  class and combined B022 kernel in G051, and solve $Nt+N_Jk=0$.

## NG-064 - Hurwitz rank invariance fixes the marked detector

- **Label:** NO-GO
- **Route:** use B023's Hurwitz invariance of boundary rank and relation
  dimension to conclude the exact B057 chain is fixed around a collision.
- **Valid input:** a collision loop acts on a distinguished factorization by
  braid/Hurwitz transformations, and these preserve the composite product at
  the unmarked factorization level.
- **Invalid inference:** the loop returns the chosen reference-fiber
  trivialization, composite detector loop $g$, and class $\alpha$ exactly.
- **Precise obstruction:** the collision transport may conjugate $g$ or act
  nontrivially on $\alpha$ while leaving every rank unchanged. B088 needs
  exact marked return, not only Hurwitz equivalence.
- **Re-entry condition:** construct G052's marked topology-changing family
  and verify exact return of $(g,\alpha)$ plus both B022 quotient maps.

## NG-065 - Marked collision geometry localizes the global detector

- **Label:** NO-GO
- **Route:** combine B089's fixed-reference collision disk with B058's global
  detector and identify their loop-fixed classes without an additional map.
- **Valid input:** B089 supplies a locally braid-invariant boundary loop, and
  B058 supplies some global loop-fixed tube pairing nontrivially with the
  prescribed primitive Hodge class.
- **Invalid inference:** the B089 boundary loop carries a fixed rational class
  whose B022 ambient image equals, or merely pairs as, the B058 detector.
- **Precise obstruction:** the two loop-fixed pairs are unrelated; the local
  relation image may be zero after B022 or orthogonal to the prescribed class.
- **Re-entry condition:** B090/NG066 exclude the positive total boundary;
  G054 must retain the nonlocal word and check its specialization, both
  quotient maps, and nonzero prescribed pairing.

## NG-066 - The positive total local boundary carries the detector

- **Label:** NO-GO
- **Route:** choose a class fixed by the positive boundary of B089's local
  nodal disk and use its B057 extension as the local detector.
- **Valid input:** the boundary factors into commuting positive
  Picard-Lefschetz meridians and a fixed class gives a formal relation.
- **Invalid inference:** that relation can have nonzero coefficients.
- **Precise obstruction:** B090 pairs the fixedness relation with the input
  class and obtains $\sum_i c_i^2=0$, hence every rational coefficient and
  the full ordered thimble extension vanish.
- **Re-entry condition:** G054 must retain a nonlocal distributed detector
  word and prove its nonzero specialization to the local relation channel.

## NG-067 - Pure marked Hurwitz transport localizes the detector

- **Label:** NO-GO
- **Route:** preserve the B058 chain solely by marked Hurwitz moves and then
  identify it with the positive total boundary extension at the nodal target.
- **Valid input:** B088 proves exact chain preservation under the marked
  Hurwitz hypotheses.
- **Invalid inference:** the preserved nonzero chain can equal the target's
  positive total-boundary extension.
- **Precise obstruction:** B090 makes that target extension zero; B091 turns
  the two statements into a contradiction with B058's nonzero pairing.
- **Re-entry condition:** construct G055's rational comparison and prove a
  nonzero topology-changing correction with type, quotient, and pairing
  control.

## NG-068 - Invariant-cycle liftability forces a local relation

- **Label:** NO-GO
- **Route:** use B084 to lift an invariant nearby detector, note that the lift
  is rational type $(0,0)$, and declare its B009 local component nonzero.
- **Valid input:** B083-B084 give existence of a special lift after the exact
  obstruction vanishes.
- **Invalid inference:** exactness defines or makes nonzero the map from that
  lift to the independently computed local relation group.
- **Precise obstruction:** B092 keeps the exact sequence, lift, and Hodge type
  fixed while choosing the missing map to be zero or the identity.
- **Re-entry condition:** B093 supplies the canonical target; G057 must use
  the associated grade and strict-support projection, control lift ambiguity,
  and calculate the specified detector coordinate.

## NG-069 - A total-stalk projection canonically selects the relation

- **Label:** NO-GO
- **Route:** choose a decomposition-theorem splitting of the proper pushdown
  and project $H^{-1}(i_H^*K)$ directly to the full-support relation stalk.
- **Valid input:** B093 canonically identifies the relation target once the
  full-support perverse summand has been reached.
- **Invalid inference:** the derived splitting used to reach that summand is
  canonical, so the total-stalk coordinate is intrinsic.
- **Precise obstruction:** B081 proves the derived splitting is noncanonical;
  only the perverse filtration and strict-support decomposition within one
  perverse cohomology object are canonical.
- **Re-entry condition:** G057 must first take the canonical associated grade,
  then full strict support, and prove the specified class remains nonzero.

## NG-070 - Lift ambiguity must be killed

- **Label:** NO-GO
- **Route:** require every B083 ambiguity direction to vanish after canonical
  relation landing, both B022 quotients, and prescribed pairing.
- **Valid input:** this condition would make the detector value independent of
  the selected special lift.
- **Invalid inference:** such independence is necessary for existence of a
  detecting lift.
- **Precise obstruction:** B094 shows that if $F(A)\ne0$, an ambiguity
  adjustment itself supplies a lift with nonzero pairing, even when the base
  lift has value zero.
- **Re-entry condition:** G058 must compute $F(\beta_0)$ and $F(A)$ and prove
  that they do not vanish simultaneously.

## NG-071 - The detector functional automatically descends

- **Label:** NO-GO
- **Route:** regard the special-stalk detector functional as the pullback of a
  nearby-stalk functional without checking the lift ambiguity.
- **Valid input:** if $F$ annihilates $\ker u$, finite-dimensional duality does
  give $F=u^*\lambda$.
- **Invalid inference:** that annihilation is automatic.
- **Precise obstruction:** B095 identifies it with
  $[F]=0$ in $\operatorname{coker}u^*$. If the class is nonzero, descent fails
  but an ambiguity-adjusted detecting lift already exists.
- **Re-entry condition:** G059 must compute the cokernel class first and the
  descended evaluation only in its zero branch.

## NG-072 - Liftability kills the ambiguity-boundary functional

- **Label:** NO-GO
- **Route:** use $\mathrm{can}(t_\psi)=0$ to conclude that the detector
  functional vanishes on the preceding long-exact boundary image.
- **Valid input:** liftability puts $t_\psi$ in $\operatorname{im}u$.
- **Invalid inference:** it constrains the separate covector $F$ on
  $\ker u=\operatorname{im}d$.
- **Precise obstruction:** the type-$(0,0)$ countermodel in NG072 has a
  liftable $t_\psi$ and $F\circ d\ne0$.
- **Re-entry condition:** G060 must compute $F\circ d$ and invoke the pairing
  square only if that computation vanishes.

## NG-073 - Proper pushforward automatically descends through B022

- **Label:** NO-GO
- **Route:** invoke functoriality of proper pushforward and nearby cycles to
  declare the B097 square before constructing the detector coefficient map.
- **Valid input:** proper pushforward is natural for an already-defined
  morphism of coefficient objects.
- **Invalid inference:** the B057 relative class has been realized in that
  object and the morphism kills both the equator-extension image and the
  base-locus kernel.
- **Precise obstruction:** B022/B082 retain nontrivial kernels and only
  forward maps; functoriality cannot supply an undefined quotient morphism.
- **Re-entry condition:** B098 closes the nearby kernels and value after B057
  realization; G062 must prove commutativity with the special Saito map.

## NG-074 - The nearby ambient map automatically equals the special map

- **Label:** NO-GO
- **Route:** use B098's generic equality $q_P(t_\psi)=c$ as the special Saito
  ambient-map comparison.
- **Valid input:** B098 closes both nearby B022 quotients and computes the
  nearby detector value; B010 defines the special Saito map independently.
- **Invalid inference:** those two maps agree across the topology-changing
  collision.
- **Precise obstruction:** B083 supplies only a special-to-nearby stalk map;
  it contains no compatibility statement with the two ambient constructions
  or the canonical full-support grade.
- **Re-entry condition:** G062 must prove
  $\Phi_H(r_H(\beta))=q_P(u\beta)$ on the actual collision object.

## NG-075 - A special lift is Saito's same relative chain

- **Label:** NO-GO
- **Route:** identify an abstract B083 special-stalk lift with the relative
  cycle $\gamma'$ used in Saito §2.5.
- **Valid input:** both objects map to data associated with the same collision.
- **Invalid inference:** they are the same relative homology representative
  and have the same local boundary and B022 quotient classes.
- **Precise obstruction:** B083 lifts form a torsor, while relative lifts of a
  fixed boundary can differ by absolute, equator, or base-locus classes.
- **Re-entry condition:** B100 removes literal representative equality; G064
  must construct the relative comparison, identify its boundary, and retain
  primitive ambient pushforward.

## NG-076 - The relative representatives must be identical

- **Label:** NO-GO
- **Route:** require Saito's chosen $\gamma'$ to equal the B057 chain in the
  full relative group and in both B022 kernel coordinates.
- **Valid input:** equality would imply equality of primitive ambient classes.
- **Invalid inference:** it is necessary.
- **Precise obstruction:** B100 proves any two lifts of the same local
  boundary differ by nearby homology whose image in $X$ is nonprimitive.
- **Re-entry condition:** G064 must identify the local boundary and primitive
  pushforward; representative equality is not required.

## NG-077 - Global boundary zero identifies the local relation coordinate

- **Label:** NO-GO
- **Route:** use B057's equation $\sum_i c_i\delta_i=0$ in the smooth
  reference fiber as the canonical Saito relation in $H_{2n-1}(Z_c)$.
- **Valid input:** the distributed thimble coefficients give a genuine
  zero-boundary relative class before collision.
- **Invalid inference:** the zero global image determines its marked vector
  in the direct sum of local Milnor homology groups after collision.
- **Precise obstruction:** the local-to-global boundary map may have a
  multidimensional kernel; distinct marked local vectors then have the same
  zero image.
- **Re-entry condition:** G065 must construct a map of pairs and identify its
  restriction on every oriented boundary sphere. B101 then supplies
  naturality automatically.

## NG-078 - Local collapsing maps globalize the distributed detector

- **Label:** NO-GO
- **Route:** apply the isolated-singularity collapse independently at every
  node and compose it with local boundary specialization to obtain G065.
- **Valid input:** S049 gives each local Milnor-fiber collapse, and S050 gives
  a local boundary-homology specialization under its Whitney hypotheses.
- **Invalid inference:** these local maps accept B057's arbitrary distributed
  global detector and preserve its marked relation and ambient closure.
- **Precise obstruction:** both sources begin with cycles already in local
  Milnor spaces. They provide no localization map from the distributed
  thimble complex, no collar-compatible global gluing, and no B022 or
  primitive ambient comparison.
- **Re-entry condition:** G066 must construct the class-specific localization,
  glue the local collapses to the exterior trivialization, and compare the
  two closed ambient chains.

## NG-079 - A second local/exterior collapse gluing is required

- **Label:** NO-GO
- **Route:** after fixing Saito's isolated-singularity setup, separately glue
  the S049 local collapse maps to an exterior Ehresmann trivialization.
- **Valid input:** local collapses model the topology near each isolated
  singular point.
- **Invalid inference:** this gluing remains a missing prerequisite for the
  relative group and Saito ambient map.
- **Precise obstruction:** S022 §2.5 already chooses one global good
  retraction, isomorphic off the singular set, defines $Z_c$, and identifies
  the relative groups. Reconstructing it does not place B057's distributed
  chain into those groups.
- **Re-entry condition:** G067 must construct the preceding collision-induced
  single-fiber realization and prove its marked boundary and ambient value.

## NG-080 - A full map on the distributed thimble complex is required

- **Label:** NO-GO
- **Route:** construct a natural chain map from every distributed thimble to
  the Saito nearby-fiber relative complex before comparing the chosen class.
- **Valid input:** such a map would send the selected detector to a target
  relative cycle and would be sufficient.
- **Invalid inference:** it is necessary for the terminal class-specific
  comparison.
- **Precise obstruction:** B104 shows the selected detector only requires one
  target lift to be relatively bordant to it. The exact invariant is a
  difference coset modulo the absolute nearby-fiber lift ambiguity.
- **Re-entry condition:** G068 may construct the collision total-space pair
  and kill the coset as a sufficient route, but B105/NG081 reduce the exact
  terminal obligation further to G069's scalar inequality.

## NG-081 - The relative-bordism obstruction coset must vanish

- **Label:** NO-GO
- **Route:** require B104's class
  $\overline\Omega(t,\beta)$ to vanish before the collision can furnish a
  Saito detector for the specified Hodge class.
- **Valid input:** coset vanishing gives one relative bordism and forces full
  compatible primitive ambient equality with B058's class $c$.
- **Invalid inference:** full relative bordism is necessary for terminal
  detection.
- **Precise obstruction:** S022's criterion only asks that
  $\langle\zeta,\Phi_{Y_0}(\beta)\rangle$ be nonzero. B105 rewrites this as
  $D_\zeta(c,\beta)\ne\langle\zeta,c\rangle$. A nonzero relative coset can
  die under primitive ambient realization or under the final pairing.
- **Countermodel:** in $\mathbf Q^2$, the nonzero coset $(0,1)$ is killed by
  the ambient map $(x,y)\mapsto x$; the full ambient discrepancy is already
  zero without a relative bordism.
- **Re-entry condition:** B106/NG082 show G069 is only the terminal
  restatement. B107/NG083 then restrict the collision certificate to the
  relevant perverse-filtration step; compute G070 there.

## NG-082 - An auxiliary global detector makes the terminal scalar a collision gate

- **Label:** NO-GO
- **Route:** write B010's local pairing using B058's class $c$ through
  $D_\zeta(c,\beta)$ and infer that the resulting inequality records a
  topology-changing specialization of $c$.
- **Valid input:** $\langle\zeta,c\rangle\ne0$, and B105's discrepancy
  inequality is equivalent to detection by $\beta$.
- **Invalid inference:** the notation supplies a map or correlation between
  the global tube and the local relation.
- **Precise obstruction:** B106 gives the identity
  $D_\zeta(c,\beta)\ne\langle\zeta,c\rangle$ if and only if
  $\langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0$; $c$ cancels. S022 and S023
  prove the local and global endpoint mechanisms separately, not the missing
  comparison.
- **Re-entry condition:** on the actual collision coefficient object, prove
  G070's filtered liftability and compute
  $[F_0]\in\operatorname{coker}(u_0^*)$; if it is zero, compute the descended
  value $\lambda(t_\psi)$ instead.

## NG-083 - The associated grade defines a total-stalk detector functional

- **Label:** NO-GO
- **Route:** use the canonical perverse filtration and strict-support
  decomposition to write a canonical $F\in S^*$ on the whole special stalk.
- **Valid input:** the filtration, its associated grades, and strict-support
  summands inside a perverse cohomology object are canonical.
- **Invalid inference:** these data canonically split the filtered stalk or
  project every class to one associated grade.
- **Precise obstruction:** B107 shows the quotient map begins only on the
  relevant step $S_0$. A functional $F_0\in S_0^*$ admits many extensions to
  $S$, distinguished only by a noncanonical complement. Ordinary B083
  liftability may also hold while filtered liftability fails.
- **Re-entry condition:** G070 must prove
  $t_\psi\in\operatorname{im}(u|_{S_0})$ and apply the dual certificate to
  $u_0:S_0\to P_\psi$ and $F_0$.

## NG-084 - Hodge strictness forces perverse-filtered liftability

- **Label:** NO-GO
- **Route:** combine B084 ordinary local-invariant-cycle surjectivity with
  purity or strictness of Hodge morphisms and infer a lift in $S_0$.
- **Valid input:** $t_\psi$ has an ordinary rational special lift, and all
  relevant maps respect their Hodge structures.
- **Invalid inference:** the map is strict for the independent perverse
  filtration.
- **Precise obstruction:** B108's pure-Tate example has an ordinary lift and
  a Hodge morphism, while
  $\omega_{\mathrm{fil}}(t)=[t]\ne0$ in
  $\operatorname{im}u/u(S_0)$. B084 asserts no perverse-filtration equality.
- **Re-entry condition:** G071 must compute the actual quotient class and
  kill it by an explicit filtered lift or a theorem proving perverse
  strictness for the precise collision map.

## NG-085 - Associated-graded maps determine the filtered lift

- **Label:** NO-GO
- **Route:** compute all $E_\infty$ dimensions, support summands, and induced
  maps, then infer the filtered-lift obstruction vanishes.
- **Valid input:** these graded objects and maps are canonical.
- **Invalid inference:** they recover the extensions between filtration
  grades.
- **Precise obstruction:** B109 constructs $u_0$ and $u_1$ with identical
  maps on every associated grade. The fixed class $t$ has a lift in $S_0$
  for $u_0$, but for $u_1$ its ordinary lift represents a nonzero class in
  $S/(S_0+\ker u_1)$.
- **Re-entry condition:** G072 must compute the actual ordinary-lift class
  including its off-diagonal filtration extension, or rule out a dual
  functional separating $t_\psi$ from $u(S_0)$.

## NG-086 - An ambient detector supplies an ordinarily liftable nearby class

- **Label:** NO-GO
- **Route:** use B058's nonzero ambient detector, or a Hurwitz-fixed B057
  representative, as though it were already the nearby class $t_\psi$, then
  apply B084 and G072.
- **Valid input:** the distributed thimble word has a nonzero primitive
  ambient pairing; an actual marked return would make that geometric word
  invariant; B084 lifts an actual invariant nearby IC class.
- **Invalid inference:** these facts construct the collision-induced source
  map from the distributed complex to the nearby stalk.
- **Precise obstruction:** B110 gives two rational pure-Tate source
  realizations with identical nonzero ambient image, one in $\operatorname{im}u$
  and one outside it. B091 independently proves that a pure-Hurwitz positive
  local-boundary comparison sends the B058 detector to zero.
- **Re-entry condition:** G073 must construct the actual topology-changing
  source map, prove $\operatorname{can}(t_\psi)=0$, choose a rational
  ordinary lift, and retain a nonzero prescribed pairing through both B022
  quotients. Only then is G072's filtered class defined.

## NG-087 - A full source map is required

- **Label:** NO-GO
- **Route:** require a natural chain map on the full distributed thimble
  complex, or a morphism on all its homology, before treating the selected
  B058 detector.
- **Valid input:** such a map is a useful sufficient mechanism and would
  compare many detector classes simultaneously.
- **Invalid inference:** it is necessary for the class-specific terminal
  chain.
- **Precise obstruction:** B111 shows that B083 and B109 use only one
  nearby class and one ordinary lift; both B022 checks and the final pairing
  are evaluations on that same class. B104/NG080 independently reduce the
  downstream chain comparison to one detector-specific relative bordism.
- **Re-entry condition:** G073 must construct a collision-certified
  realization of the selected class, not a global map; it must still prove
  ordinary liftability, rational type, both quotient survivals, and nonzero
  prescribed pairing.

## NG-088 - The marked boundary determines the excess

- **Label:** NO-GO
- **Route:** construct the same marked local boundary for the actual selected
  collision chain and the pure-Hurwitz reference, then infer the desired
  nonzero topology-changing correction.
- **Valid input:** equal boundaries make the difference a cycle in the
  relative target complex.
- **Invalid inference:** the boundary determines the homology class of that
  cycle, its Hodge type, quotient image, or pairing.
- **Precise obstruction:** in B112's exact model, $a$ and $a+\lambda z$ have
  the same boundary for every rational $\lambda$, while the excess is the
  arbitrary class $\lambda[z]$.
- **Re-entry condition:** G074 must construct the actual selected collision
  chain and compute its excess against the Hurwitz reference, including
  ordinary liftability, rational type, both B022 quotients, and nonzero
  prescribed pairing.

## NG-089 - A purely local A2 excess descends nontrivially

- **Label:** NO-GO
- **Route:** compute a nonzero selected excess solely in the local $A_2$
  root lattice on the ordered-root cover and descend it by normalized
  $S_3$ trace.
- **Valid input:** the local excess can be nonzero upstairs, and rational
  finite-group averaging is defined.
- **Invalid inference:** its invariant projection is nonzero.
- **Precise obstruction:** B113 applies B073's exact matrices: the rational
  $A_2$ lattice is the standard $S_3$ representation and the Reynolds
  projector vanishes identically on it.
- **Re-entry condition:** G075 must compute the selected excess in the full
  global coefficient object and prove a nonzero invariant full-support
  projection in the canonical perverse grade. This is G042's existing
  class-landing obligation in selected-chain coordinates.

## NG-090 - The root cover creates full-support landing

- **Label:** NO-GO
- **Route:** pass to the semistable $S_3$ root cover and use its invariant
  full-support summand to obtain a nonzero selected coordinate without
  proving the original downstairs specialization coordinate is nonzero.
- **Valid input:** the cover supplies a canonical invariant full-support
  Hodge object and exact rational averaging.
- **Invalid inference:** those operations create class-level nonvanishing.
- **Precise obstruction:** B114 applies B074/B076 on the canonical perverse
  grade: covered invariants and the original full-support object are
  isomorphic, with unit and normalized trace inverse. Their selected
  coordinates vanish or do not vanish together.
- **Re-entry condition:** G076 must construct the original selected nearby
  class and ordinary lift and prove its canonical full-support projection
  nonzero. This is G043 with the class-specific collision provenance made
  explicit, not a new reduction.

## NG-091 - Ngô support applies to the hyperplane family

- **Label:** NO-GO
- **Route:** combine projectivity, generic smoothness and irreducibility with
  Ngô's support theorem to force G076's selected class into full support.
- **Valid input:** the universal high-power hyperplane family has those
  three geometric properties.
- **Invalid inference:** they imply the delta-regular weak abelian fibration
  hypotheses.
- **Precise obstruction:** S051 requires a same-dimensional smooth
  commutative group scheme action with affine stabilizers and polarizable
  Tate module. B115 proves this is impossible for sufficiently high powers:
  the action would make a generic fiber an abelian homogeneous quotient with
  trivial canonical bundle, while adjunction makes its canonical bundle
  ample.
- **Re-entry condition:** B117 supplies a different family-specific support
  theorem for the original incidence map. G079 must still construct the
  selected relevant-grade class; no Ngô theorem creates it.

## NG-092 - Smooth-point relation vanishing kills divisor support

- **Label:** NO-GO
- **Route:** apply B008 at a generic smooth point of every discriminant
  divisor and use the vanishing of $IH^1_p(\mathcal H)$ to set the selected
  divisor coordinate equal to zero.
- **Valid input:** the full-support intermediate-extension contribution to
  the degree-$-1$ stalk vanishes at such a point.
- **Invalid inference:** the divisor-strict-support contribution to the same
  ordinary stalk degree also vanishes.
- **Precise obstruction:** B116's pure semisimple Hodge-module model
  $\mathbf Q_B^H[2]\oplus i_*\mathbf Q_D^H[1]$ has zero degree-$-1$
  full-support stalk and a one-dimensional divisor-supported stalk. These
  are independent strict-support coordinates.
- **Re-entry condition:** B117 executes the transverse support calculation
  for the original pushdown using S052's next-degree constancy. G079 must
  construct the selected class and prove its relevant grade nonzero.

## NG-093 - The middle direct image alone excludes divisor support

- **Label:** NO-GO
- **Route:** use only S052 equation (2.2.5), saying that the middle higher
  direct image on a Lefschetz disk is a shifted intersection complex, to
  exclude a punctual summand in perverse degree zero.
- **Valid input:** $R^d g_*\mathbf Q$ has no extra punctual direct summand.
- **Invalid inference:** a punctual summand of
  ${}^pH^0(Rg_*\mathbf Q[d+1])$ would occur in that sheaf.
- **Precise obstruction:** the normalized punctual term is in ordinary
  degree zero, which is $R^{d+1}g_*\mathbf Q$; $R^d$ is ordinary degree
  minus one. This is exactly the B080 shift after taking a transverse disk.
- **Re-entry condition:** B117 uses the additional equation (2.2.3):
  $R^{d+1}g_*\mathbf Q$ is constant across a Lefschetz critical value.
  Decomposition then forces the punctual multiplicity to vanish.

## NG-094 - High-degree constancy directly kills the point grade

- **Label:** NO-GO
- **Route:** use concentration of isolated vanishing cohomology to make high
  direct images constant, then immediately infer that
  ${}^pH^{-1}(K)$ has no point support.
- **Valid input:** $R^{d+3}h_*\mathbf Q$ is unchanged across the isolated
  collision.
- **Invalid inference:** a point term in ${}^pH^{-1}$ contributes directly
  to that sheaf.
- **Precise obstruction:** its shift is $i_{p*}V[1]$, so it contributes to
  $\mathcal H^{-1}(K)=R^{d+1}h_*\mathbf Q$. This middle-adjacent sheaf can
  jump by S022's relation/extra-cohomology group.
- **Re-entry condition:** B118 applies relative hard Lefschetz supportwise,
  reflecting the term into ${}^pH^1$ and hence the genuinely constant
  $R^{d+3}$. The contradiction then becomes valid.

## NG-095 - The total ordinary lift must be type (0,0)

- **Label:** NO-GO
- **Route:** require the entire rational ordinary special-stalk lift to be a
  Hodge class before using its canonical relation-grade coordinate.
- **Valid input:** the eventual nodal relation coordinate used by B010 must
  be rational type $(0,0)$ after $\mathbf Q(n)$.
- **Invalid inference:** all irrelevant components of the total lift must
  have the same type.
- **Precise obstruction:** in the rational Hodge morphism
  $u:\mathbf Q(0)\oplus\mathbf Q(-1)\to\mathbf Q(0)$ that projects to the
  first factor, $e_0+e_1$ is not a total type-$(0,0)$ vector but maps to the
  nonzero type-$(0,0)$ vector $e_0$. B117-B118 force the geometric detector
  coordinate into the remaining full-support grade, and B093/S022 make that
  clean-nodal relation grade pure $\mathbf Q(0)$ after normalization. B119
  records the exact geometric conclusion.
- **Re-entry condition:** B123/NG099 prove that no nonzero nearby class has a
  lift in $S_0$. Reverse the arrow through G065's marked relative boundary.

## NG-096 - Full plane-local invariance is required

- **Label:** NO-GO
- **Route:** require the selected nearby vector to be fixed under every loop
  in the punctured smooth locus of a two-dimensional plane neighborhood.
- **Valid input:** local invariant cycles requires invariance for the base on
  which the proper map is being considered.
- **Invalid inference:** that base must be the whole plane germ.
- **Precise obstruction:** B120 restricts the original proper incidence map
  to one marked algebraic curve and its analytic disk. The disk-normalized
  special group $H^0(i^*K_\Delta)$ is exactly the required plane-normalized
  group $H^{-1}(i^*K_B)$. Cyclic invariance therefore gives the needed
  special class. The explicit $\mathbf Z^2$ model in NG096 and
  `verification/verify_B120_one_disk.py` also proves that cyclic invariance
  can hold while simultaneous invariance fails, so the latter is strictly
  stronger.
- **Re-entry condition:** B122 proves every target class in the required
  degree is already cyclically invariant and ordinarily liftable, while
  B123 proves its filtered obstruction cannot vanish when it is nonzero.
  Use G065's relative-boundary construction.

## NG-097 - A nonzero ordinary lift forces a relation grade

- **Label:** NO-GO
- **Route:** after B117 eliminates divisor support and B118 eliminates point
  support, infer that every nonzero ordinary lift has a nonzero
  $E_\infty^{-1,0}$ relation coordinate.
- **Valid input:** those theorems eliminate the stated proper-support terms.
- **Invalid inference:** they exhaust total normalized degree $-1$.
- **Precise obstruction:** B121 corrects B080-B081 by adding the generally
  nonzero constant ambient grade $E_\infty^{-2,1}$, coming from
  ${}^pH^1$ and $R^{d+1}$. The pure type-$(0,0)$ vector supported entirely
  in that grade is a nonzero ordinary lift with zero relation coordinate.
  This also restores B092's earlier warning that an ordinary lift does not
  select the relation component.
- **Re-entry condition:** B123/NG099 prove that filtered lift is impossible
  for a nonzero nearby class. Construct the relation instead through G065's
  marked relative boundary.

## NG-098 - The raw cyclic thimble cocycle must vanish

- **Label:** NO-GO
- **Route:** require the selected raw thimble representative to have zero
  B085 class in the combined B022 kernel before lifting its actual nearby
  cohomology image.
- **Valid input:** B085 exactly decides existence of a monodromy-invariant
  raw representative.
- **Invalid inference:** such a representative is necessary for an ordinary
  special lift of the quotient target class.
- **Precise obstruction:** B122 uses S022's isolated vanishing concentration
  to make $H^{d+1}(Y_p)\to H^{d+1}(Y_t)$ surjective. Thus the entire actual
  target is invariant and liftable. The model
  $M(e)=e+j$, $M(j)=j$ has a nonzero raw kernel cocycle but trivial quotient
  monodromy, proving the distinction exactly.
- **Re-entry condition:** none for ordinary liftability. B123 computes the
  filtered class as nonzero; use G065's relative-boundary direction.

## NG-099 - A nonzero nearby class lifts through the relation step

- **Label:** NO-GO
- **Route:** construct a nonzero nearby detector $t_\Delta$ and prove
  $t_\Delta\in u_\Delta(S_0)$ so that its special lift has a relation
  coordinate.
- **Valid input:** B122 makes the total special-to-nearby map surjective, and
  the relation grade can be nonzero.
- **Invalid inference:** the relation grade maps onto nearby cohomology.
- **Precise obstruction:** S022's exact sequence defines the extra
  cohomology as
  $E(Y_p)=\ker(H^{d+1}(Y_p)\to H^{d+1}(Y_t))$. B009/B026/B093 identify its
  relation dual with the $E_\infty^{-1,0}$ channel, and B118 removes the
  lower point grade. B123 therefore gives
  $S_0=E(Y_p)$ and $u_\Delta(S_0)=0$. For every nonzero nearby class,
  $\omega_{\mathrm{fil}}(t_\Delta)=t_\Delta\ne0$.
- **Re-entry condition:** reverse the arrow. G065 must construct a marked map
  of pairs sending the selected B057 relative class into
  $H_{2n}(Y_t,Z_t)$ with nonzero local boundary relation and compatible
  primitive ambient realization. B099-B101 then propagate the pairing, but
  B124/NG100 show this is an exact-target mechanism stronger than G031.

## NG-100 - Relative-lift ambiguity adjusts the primitive target

- **Label:** NO-GO
- **Route:** after fixing a local relation $\beta$, vary its Saito relative
  lift or the marked map presenting it until the primitive ambient value is
  the preselected B058 class $c$.
- **Valid input:** $\partial^{-1}(\beta)$ is an affine torsor under the image
  of absolute nearby-fiber homology.
- **Invalid inference:** this ambiguity survives primitive ambient
  projection.
- **Precise obstruction:** S022 §§2.4-2.5 and B100 show that the ambiguity
  maps to the nonprimitive part. B124 therefore proves that every lift has
  the single value $\Phi_{Y_0}(\beta)$. A lift with value $c$ exists exactly
  when $\Phi_{Y_0}(\beta)=c$, so G065 already contains G030's exact-target
  obligation.
- **Re-entry condition:** prove G030's equality using genuinely new collision
  geometry, or abandon the preselected target and attack G008's strictly
  weaker support-nonemptiness gate. Representative choice alone cannot
  reopen the route.

## NG-101 - Local A2 nodalization supplies a clean relation

- **Label:** NO-GO
- **Route:** move a detecting suspended $A_2$ support point inside its local
  miniversal two-parameter deformation to one fiber carrying several nodes
  and a nonzero relation.
- **Valid input:** the $A_2$ Milnor number is two, and a morsification has two
  distinguished Morse critical points across the family.
- **Invalid inference:** the critical points occur simultaneously in one
  fiber.
- **Precise obstruction:** B126 parametrizes the discriminant critical value
  by $x\mapsto(-3x^2,2x^3)$ and proves this map injective. Every noncentral
  discriminant fiber has one node; the central fiber has one $A_2$ point.
  The local base contains no multipart nodal target and hence no one-fiber
  nodal relation channel.
- **Re-entry condition:** construct a global topology-changing deformation
  that adds or recollides critical points outside the single versal germ and
  prove preservation of the class-specific restriction/pairing. This is the
  remaining conditional cleanup G085/G032 obligation after G008.

## NG-102 - Clean incidence is smaller than support nonemptiness

- **Label:** NO-GO
- **Route:** replace the universally quantified support-nonemptiness theorem
  G008 by G084 and count the clean-locus intersection as a smaller terminal
  gate.
- **Valid input:** B125 proves G084 is exactly the clean-nodal formulation of
  G031, and any G084 witness is a valid nonzero local restriction witness.
- **Invalid inference:** adding the condition that the support point lie in
  the Li-clean multipart nodal locus makes the terminal obligation smaller.
- **Precise obstruction:** B007/B127 give
  \(\mathrm{HC}_{\mathbf Q}\Longleftrightarrow G008\), while set-theoretically
  \(G084\Rightarrow G008\). The reverse implication needs the separate
  cleanup theorem G085. BFNP Theorem 1.3 proves the terminal equivalence but
  contains no clean-locus conclusion.
- **Re-entry condition:** prove G085 from a nonempty class-specific support,
  with all specialization, rationality, and pairing data explicit. Until
  then G084 is a stronger sufficient program, not a reduction below HC.

## NG-103 - The formal projective Hodge package forces local support

- **Label:** NO-GO
- **Route:** prove G008 from projective-space base, full strict support,
  geometric polarizable weight-\(-1\) coefficients, purity, hard Lefschetz,
  and the rational type-\((0,0)\) of the global \(IH^1\) class.
- **Valid input:** the universal-hyperplane coefficient object and
  \(s_m(\zeta)\) have all these properties.
- **Invalid inference:** the B128 edge image must therefore be nonzero.
- **Precise obstruction:** B129 starts from the sign local system of an
  elliptic double cover of \(\mathbf P^1\) branched at four points, tensors
  with \(H^1(C)(1)\), external-products to dimension \(d\), and applies a
  finite small map to \(\mathbf P^d\). A full-support IC summand has a
  nonzero rational type-\((0,0)\) \(IH^1\) class but
  \(\mathcal H^{-d+1}=0\) everywhere. The class lies entirely in
  \(H^1(\mathbf P^d,\mathcal H^{-d}K)\).
- **Re-entry condition:** exploit the exact universal-incidence origin
  \(s_m(\zeta)=[q_m^*\zeta]_{00}\) and prove G086. Formal Hodge-module data
  on projective space cannot distinguish the incidence class from B129's
  escape class.

## NG-104 - Nori-Brogan Higgs nonvanishing is local Betti support

- **Label:** NO-GO
- **Route:** apply Nori connectivity and Brogan Corollary 4.1 to obtain the
  primitive \((r,r)\) bundle in
  \(\mathcal H^{-d+1}\operatorname{gr}_F^{-r}\operatorname{DR}(M)\), then
  read it as a nonzero local Green-Griffiths invariant.
- **Valid input:** B130 checks the exact specialization
  \(n_B=2r-1\), \(k=2r\), \(b=r\) and the resulting Hodge component for
  every \(r\ge2\).
- **Invalid inference:** cohomology of the associated-graded filtered de
  Rham complex equals the associated graded of ordinary de Rham cohomology.
- **Precise obstruction:** on \(P^{\rm sm}\), the minimal extension restricts
  to a flat local system and
  \(\operatorname{DR}(M)\simeq V_{\mathbf C}[d]\). Hence
  \(\mathcal H^{-d+1}\operatorname{DR}(M)=0\) there although Brogan's
  Higgs-graded cohomology sheaf can equal the nonzero bundle
  \(H^{r,r}_{\rm prim}(X)\otimes\mathcal O\). The filtered differentials
  perform an actual cancellation. Brogan p. 14 also says the Leray-incidence
  map was not checked to coincide with the abstract Corollary 4.1 map.
- **Re-entry condition:** B132 now identifies the canonical projective
  filtered section. Prove G088 by showing its cancellation fails at some
  discriminant stalk, with rational realization and strict support checked.

## NG-105 - Smooth-open Higgs globalization identifies the incidence class

- **Label:** NO-GO
- **Route:** use the proof of Brogan Corollary 5.2 over the smooth parameter
  locus, or choose a decomposition-theorem splitting, to label the primitive
  Higgs section by the specified incidence class.
- **Valid input:** Corollary 4.1 computes the primitive Higgs cohomology
  bundle, and the later Leray construction is canonical on the smooth locus.
- **Invalid inference:** global sections of that bundle on the nonproper
  discriminant complement equal the finite primitive space and filtered
  hypercohomology is strict there in the projective sense.
- **Precise obstruction:** if the discriminant is F=0 and G is a same-degree
  homogeneous polynomial not proportional to F, then G/F is a nonconstant
  regular function on the complement. Thus global sections of the primitive
  bundle are generally larger than the primitive vector space. The cited
  displayed proof does not control the filtered cancellations on this open
  base. A chosen derived decomposition is independently noncanonical by
  S037/B081.
- **Re-entry condition:** B131 proves rational first-Leray nonvanishing, and
  B132 starts with the canonical incidence class on full projective P, where
  projective strictness gives its nonzero filtered realization. Only G088
  boundary survival remains.

## NG-106 - A generic transverse double node forces boundary survival

- **Label:** NO-GO
- **Route:** use the smallest allowed codimension-two stratum, a transverse
  intersection of two nodal discriminant branches, as an automatic nonzero
  target for the canonical B132 section.
- **Valid input:** the fiber has two independently smoothable nodes and the
  discriminant is locally normal crossing.
- **Invalid inference:** two branches imply nonzero degree-one local IC.
- **Precise obstruction:** B133-B134 identify the intrinsic cohomological
  target with the dual of the kernel of
  \(\mathbf Q^2\to H_{2n-1}(X_s,\mathbf Q(n))\) sending the standard basis
  to the two vanishing cycles. Independent cycles give zero kernel. B020's
  intersection-one pair is an explicit audited independent pair.
- **Re-entry condition:** in the two-branch case, construct proportional
  vanishing cycles and prove a nonzero class-specific relation coordinate;
  otherwise use a higher multipart relation point. Either route remains
  inside G088.

## NG-107 - A cohomological local class is a selected relation vector

- **Label:** NO-GO
- **Route:** read the degree-one cohomological IC stalk literally as the
  vanishing-cycle relation kernel and infer that a nonzero relation space
  gives a nonzero incidence class.
- **Valid input:** the polarized residue calculations determine the correct
  rank and pure Tate type, and may model the dual channel by a coefficient
  kernel.
- **Invalid inference:** the specified cohomological class canonically
  selects a homological relation vector.
- **Precise obstruction:** B134 audits Saito's exact typing

  \[
  E(Y_p)=\mathcal H^{-d+1}(IC(V))_p=R(Y_p)^\vee.
  \]

  The incidence class is the functional
  \(\beta\mapsto\langle\zeta,\gamma_\beta\rangle\). It can be zero when
  \(R(Y_p)\ne0\). Polarization does not remove this class-specific scalar.
- **Re-entry condition:** construct an actual relation \(\beta\) at an
  actual boundary point and prove the B134 evaluation is nonzero.

## NG-108 - Nonzero individual branch residues force survival

- **Label:** NO-GO
- **Route:** at a proportional two-node point, prove one or both logarithmic
  residues \(a_i\delta_i\) are nonzero and infer a nonzero local incidence
  class.
- **Valid input:** the residue vector is a concrete degree-one cochain in the
  Green-Griffiths monodromy complex.
- **Invalid inference:** a nonzero cochain has nonzero cohomology class.
- **Precise obstruction:** B135 gives

  \[
  s_m(\zeta)_p=[a]\in\operatorname{coker}\Delta^\ast.
  \]

  When \(\delta_2=c\delta_1\), every \(q(1,c)\) is a coboundary. It can have
  both entries nonzero while its relation evaluation \(c q-c q\) vanishes.
- **Re-entry condition:** construct the boundary point and prove the
  lift-invariant mismatch \(c a_1-a_2\ne0\), as in G089.

## NG-109 - Increase power while keeping a bounded node model

- **Label:** NO-GO
- **Route:** use higher embeddings to gain flexibility while keeping exactly
  two, or any uniformly bounded number of, nodal branches carrying the B135
  residue quotient.
- **Valid input:** high powers improve global generation and jet separation.
- **Invalid inference:** that improvement preserves a nonzero adjoint defect
  or vanishing-cycle relation.
- **Precise obstruction:** B136 applies relative Serre vanishing uniformly
  over every \(\operatorname{Hilb}^k(X)\), \(k\le N\). For \(m\gg0\), all
  such finite schemes impose independent conditions on \(L^m\); B027 then
  gives

  \[
  H^1(I_\Delta\otimes K_X\otimes(L^m)^n)=0,\qquad R(Y)=0.
  \]

  For \(N=2\), G089's proportional-pair target is absent.
- **Re-entry condition:** use G013's growing multipart incidence, retain
  isolated nodes and adjoint defect, and prove its B135 quotient class is
  nonzero for the specified Hodge class.

## NG-110 - Grow nodes below the double-linear floor

- **Label:** NO-GO
- **Route:** escape B136 with an unbounded node count but keep
  \(|\Delta_m|\le2(mn-c)+1\), where \(K_X\otimes H^c\) is globally
  generated.
- **Valid input:** an unbounded family is not covered by any one fixed
  Hilbert scheme of points.
- **Invalid inference:** unbounded cardinality alone permits an isolated
  adjoint defect.
- **Precise obstruction:** B137 converts the defect into failure of
  degree-\(t_m=mn-c\) postulation. In this cardinality range S056 forces
  \(t_m+2\) collinear nodes. Their line lies in \(X\) for high \(m\), while
  the hypersurface value and every conormal first derivative vanish at more
  points than their degrees. The entire line is singular.
- **Re-entry condition:** work at or above \(2(mn-c)+2\) nodes, preserve
  isolated nodality and the two-matroid inequalities, and compute a nonzero
  B135 quotient for the prescribed Hodge class.

## NG-111 - Stop below the triple-linear floor

- **Label:** NO-GO
- **Route:** cross B137's double-linear threshold but keep
  \(|\Delta_m|\le3(mn-c)-1\).
- **Valid input:** S056 leaves a conic alternative at its boundary.
- **Invalid inference:** that this alternative, or any larger set below the
  triple-linear threshold, can remain an isolated-nodal detector.
- **Precise obstruction:** B138 extracts a minimal
  \(\mathrm{CB}(mn-c)\) circuit. S057 places it on a degree-at-most-two
  curve. Componentwise CB bounds force at least \(mn-c+1\) points on a line
  or \(2(mn-c)+2\) on an irreducible conic. Uniform conormal-degree bounds
  then make the hypersurface singular along that carrier.
- **Re-entry condition:** B139 subsequently raises the necessary count to
  \(4(mn-c)-4\); at or above that floor prove isolated
  first jets, multipart smoothability, positive adjoint and ambient ranks,
  and the prescribed nonzero B135 pairing.

## NG-112 - Stop below the quartic-linear floor

- **Label:** NO-GO
- **Route:** cross B138's triple-linear threshold but keep
  \(|\Delta_m|\le4(mn-c)-5\).
- **Valid input:** S057 controls only carriers of degree at most two, so this
  larger range required a new primary theorem and a cubic-carrier audit.
- **Invalid inference:** a cubic Cayley-Bacharach carrier can support an
  isolated-nodal adjoint defect merely because it is not a line or conic.
- **Precise obstruction:** B139 applies S058 to the minimal
  \(\mathrm{CB}(mn-c)\) circuit and obtains a degree-at-most-three carrier.
  Cubic componentwise Cayley-Bacharach bounds give linearly many points on
  an integral or reducible component. Uniform normalization/conormal bounds
  then force that component into the hypersurface singular locus.
- **Re-entry condition:** B140 subsequently raises the necessary count to
  \(5(mn-c)-10\); at or above that floor prove isolated
  first jets, multipart smoothability, both G013 matroid/rank conditions,
  and the prescribed nonzero B135 residue-cokernel pairing.

## NG-113 - Stop below the quintic-linear floor

- **Label:** NO-GO
- **Route:** cross B139's quartic-linear threshold but keep
  \(|\Delta_m|\le5(mn-c)-11\).
- **Valid input:** S058 controls carriers only through degree three; singular
  and reducible quartics require componentwise rather than classification-only
  control.
- **Invalid inference:** a degree-four carrier can retain isolated nodality
  because its components or singularities defeat the cubic case analysis.
- **Precise obstruction:** B140 combines S059 with uniform Hilbert-family
  regularity. A bounded-degree multiplier isolates an integral component,
  and curve duality forces \(e(mn-c)-O(1)\) circuit points on it. Uniform
  conormal slopes then put that component in the singular locus.
- **Re-entry condition:** B141 subsequently requires genuinely superlinear
  growth; with that growth prove isolated
  first jets, multipart smoothability, both G013 rank systems, and a nonzero
  B135 residue-cokernel value for the specified rational Hodge class.

## NG-114 - Keep any fixed linear node budget

- **Label:** NO-GO
- **Route:** allow \(|\Delta_m|\le C(mn-c)+D\) for arbitrary but fixed
  constants \(C,D\).
- **Valid input:** every earlier explicit floor is linear and can be crossed
  by increasing \(C\).
- **Invalid inference:** no low-degree carrier theorem remains after the
  explicit \(h\le5\) Picoco cases.
- **Precise obstruction:** choose a fixed integer \(E>C\). S060 applies for
  \(t_m\gg E\) and puts the intrinsic minimal \(\mathrm{CB}(t_m)\) circuit
  on a degree-at-most-\(E\) curve. B140's arbitrary fixed-degree component
  lemma forces an integral component into the singular locus. Equivalently,
  B141 proves \(|\Delta_m|/t_m\to\infty\).
- **Re-entry condition:** use a genuinely superlinear multipart node scheme,
  prove isolated first jets and both G013 rank systems, and obtain a nonzero
  B135 residue-cokernel value for the specified rational Hodge class.

## NG-115 - Treat the filtered section as a nodal-stratum equation

- **Label:** NO-GO
- **Route:** use B132's canonical nonzero filtered section
  \(h_m(\zeta)\) as an equation, zero locus, or already-proved support locus
  defining G090's saturated simultaneous-node germ.
- **Valid input:** the section is canonical, projective, nonzero, and
  constructed from the universal incidence class without an algebraic
  representative of \(\zeta\).
- **Invalid inference:** it unconditionally defines a nonempty smooth
  codimension-\(R\) nodal stratum.
- **Precise obstruction:** B132 identifies its coherent target with
  \(H_{\mathrm{prim}}^{n,n}(X)\otimes\mathcal O_{P_m}\), so
  \(h_m(\zeta)\) is constant and nonzero and has empty zero locus. Its
  ordinary local survival locus is exactly the unresolved G088/G008
  support. B129/NG103 prove that the formal projective Hodge package cannot
  force such survival. Even a survivor would not supply uniform nodality,
  smoothness, or saturated codimension.
- **Re-entry condition:** construct an actual simultaneous-node germ from
  the special universal-hyperplane incidence geometry, verify its conormal
  matroid and codimension, and only then apply B144.

## NG-116 - Use the generic ordered-node incidence

- **Label:** NO-GO
- **Route:** use a generic first-jet-surjective ordered \(N\)-node incidence
  as the smooth saturated component required by G091.
- **Valid input:** the principal-parts evaluation is surjective for
  sufficiently jet-ample systems and general configurations, making the
  incidence smooth of expected codimension \((2n+1)N\).
- **Invalid inference:** this transverse incidence carries positive adjoint
  defect or a nonzero vanishing-cycle relation.
- **Precise obstruction:** jet surjectivity forces the node values to impose
  \(N\) independent conditions. B027-B028 then propagate independence to
  \(K_X\otimes L^n\) in the high-power range, so the adjoint defect,
  relation space, and detector channel are zero.
- **Re-entry condition:** construct a nodal point with value rank \(R<N\)
  where the ordered incidence remains smooth of the exact smaller
  codimension \(2nN+R\), and prove a nonzero class-specific Saito pairing.

## NG-117 - Infer smooth excess from value-rank drop

- **Label:** NO-GO
- **Route:** impose the determinantal condition
  \(\operatorname{rank}E_\Delta=R<N\) and identify B145's tangent
  codimension with the actual codimension of a reduced smooth component.
- **Valid input:** the ordered-node incidence tangent has codimension
  \(2nN+R\).
- **Invalid inference:** tangent rank proves that the excess equations are
  locally redundant.
- **Precise obstruction:** B146 associates to every value relation a
  Hessian quadratic form on conditional gradients. Smoothness forces the
  entire gradient image to be simultaneously isotropic. For uniform
  \(U_{R,N}\), its corank is at least \(n(R+1)\); if it is surjective, the
  quadratic obstruction is explicitly nonzero.
- **Re-entry condition:** construct the Hessian-isotropic gradient
  degeneracy, integrate it through all higher orders to a reduced smooth
  height-\(R\) smoothing ideal, and prove the nonzero class-specific pairing
  in G092.

## NG-118 - Universalize the carrier Lagrangian core

- **Label:** NO-GO
- **Route:** for every nonzero primitive rational Hodge class \(\zeta\),
  choose an algebraic middle-dimensional carrier \(W\) pairing nontrivially
  with \(\zeta\), then apply S019 and B147.
- **Valid input:** the carrier conormals are maximal inverse-Hessian
  isotropic subspaces and explain the anchored smooth-excess examples.
- **Invalid inference:** such an algebraic detecting carrier is available
  before rational HC is proved.
- **Precise obstruction:** Hodge-Riemann nondegeneracy plus B016's
  annihilator argument shows that algebraic classes detecting every nonzero
  Hodge class span the entire Hodge space. A nonalgebraic carrier has no
  algebraic ideal or cycle class for the required projective incidence.
- **Re-entry condition:** construct G093's split Lagrangian jet core and its
  nonzero specified Saito pairing without selecting an algebraic carrier.

## NG-119 - Choose Lagrangians after generic jet interpolation

- **Label:** NO-GO
- **Route:** start from a conditionally first-jet-surjective nodal point and
  choose one maximal inverse-Hessian-isotropic \(n\)-plane at each node.
- **Valid input:** such Lagrangian planes exist over \(\mathbf C\).
- **Invalid inference:** the choices lower the quotient-gradient rank to the
  B148/G093 bound \(n\).
- **Precise obstruction:** surjectivity survives every quotient. The stacked
  quotient has dimension and rank \(nN>n\) for \(N>1\).
- **Re-entry condition:** construct the node scheme, section space, and
  Lagrangian quotients jointly so that projected-gradient rank is at most
  \(n\), then integrate the germ and prove its specified pairing.

## NG-120 - Keep a bounded oriented half-double scheme in high power

- **Label:** NO-GO
- **Route:** keep \(N\) bounded and increase the polarization power while
  retaining G094's oriented half-double evaluation defect.
- **Valid input:** individual low-power directed schemes can be
  superabundant.
- **Invalid inference:** their defect persists in the stable high-power
  regime.
- **Precise obstruction:** all length-\((n+1)N\) schemes lie in a fixed
  projective Hilbert scheme. Uniform relative Serre vanishing makes their
  high-power evaluation maps surjective, contradicting B149/G094's rank
  bound \(R+n<(n+1)N\).
- **Re-entry condition:** grow \(N\) superlinearly as required by B141 and
  construct the Hessian-compatible oriented defect, smooth integration, and
  nonzero specified pairing together.

## NG-121 - Use general oriented half-doubles

- **Label:** NO-GO
- **Route:** choose general supports and general orientations in
  \(\mathbf P^{2n}\) and expect their number to force G094 superabundance.
- **Valid input:** each local scheme has the exact B149 length \(n+1\).
- **Invalid inference:** general partial derivative data fail maximal rank.
- **Precise obstruction:** S062/B150 proves maximal rank for \(d\ne2\);
  none of the five source exceptions matches ambient dimension \(2n\) and
  half-double length \(n+1\). In the injective range no nonzero containing
  form exists; in the surjective range the rank is
  \((n+1)N>R+n\).
- **Re-entry condition:** construct a special configuration in B151's local
  defect or synchronized branch and verify all G095 conditions.

## NG-122 - Treat synchronization as the full Hessian condition

- **Label:** NO-GO
- **Route:** after synchronizing all projected-gradient blocks through one
  \(n\)-dimensional quotient, infer B146 isotropy and smooth excess.
- **Valid input:** quotient gradients have the anchored rank pattern.
- **Invalid inference:** common-kernel conormal gradients are unrestricted.
- **Precise obstruction:** B152's mixed Hessian map is surjective of rank
  \(n(N-R)\). Its kernel has dimension \(nR\), whereas an unrestricted
  conormal target has dimension \(nN\). Synchronization can therefore coexist
  with a nonzero B146 mixed obstruction.
- **Re-entry condition:** realize G096's synchronized quotient and conormal
  mixed kernel jointly, then prove pure quadratic compatibility, nonlinear
  integration, and the specified pairing.

## NG-123 - Infer the pure Hessian condition from the mixed one

- **Label:** NO-GO
- **Route:** after B152's mixed conormal equations hold, infer the remaining
  quotient-quotient Hessian equations.
- **Valid input:** every core-core and core-quotient relation pairing is
  zero.
- **Invalid inference:** the pure synchronized quotient class vanishes.
- **Precise obstruction:** with zero core conormal map, the mixed condition
  is automatic. Arbitrary symmetric quotient blocks of the nondegenerate
  inverse-Hessian matrices realize an arbitrary class in
  \(\operatorname{coker}(E)\otimes\operatorname{Sym}^2Q^*\), whose dimension
  is \((N-R)n(n+1)/2>0\).
- **Re-entry condition:** construct G097 with the canonical class
  \(\Omega_Q=0\), then prove all-order integration and the specified pairing.

## NG-124 - Integrate from second-order flatness

- **Label:** NO-GO
- **Route:** once B152's mixed tensor and B153's pure tensor vanish, infer a
  reduced smooth excess germ of height \(R\).
- **Valid input:** the reduced Kuranishi map has no linear or quadratic term.
- **Invalid inference:** every higher Kuranishi tensor vanishes.
- **Precise obstruction:** the two-node critical-value map
  \(\tau(x,y)=(x,x+y^3)\) comes from local families with fixed nondegenerate
  spatial Hessians. It has rank \(R=1<N=2\), zero quadratic relation tensor,
  and cubic reduced map \(\kappa(y)=y^3\). Its simultaneous-node ideal
  \((x,y^3)\) is nonreduced.
- **Re-entry condition:** compute and kill B154's canonical cubic tensor,
  then prove all higher tensors vanish and retain the specified pairing.

## NG-125 - Stop at any fixed Kuranishi order

- **Label:** NO-GO
- **Route:** choose a fixed \(k\), verify
  \(\kappa_2=\cdots=\kappa_k=0\), and infer smooth reduced excess.
- **Valid input:** every first nonzero homogeneous Kuranishi term obstructs
  integration.
- **Invalid inference:** no obstruction can first appear above \(k\).
- **Precise obstruction:** for every \(m>k\),
  \(\tau_m(x,y)=(x,x+y^m)\) has the same \(k\)-jet as the smooth factorized
  germ \((x,x)\), but its simultaneous-node ideal is the nonreduced
  \((x,y^m)\).
- **Re-entry condition:** prove the structural all-order factorization
  \(\tau=A f\) of B155/G099, or an equivalent identity for the entire
  analytic Kuranishi germ, then verify the specified pairing.

## NG-126 - Infer analytic syzygies from nodewise Milnor data

- **Label:** NO-GO
- **Route:** use fixed ODP Hessians, local \(A_1\) Milnor lattices, or the
  individual Picard--Lefschetz reflections to lift every linear
  critical-value relation analytically.
- **Valid input:** those invariants determine the nodewise vanishing-cycle
  model and its local monodromy generator.
- **Invalid inference:** they constrain higher analytic relations among
  different critical-value branches on the base.
- **Precise obstruction:** B157 realizes every analytic \(\tau\) on a
  nonlinear analytic pullback of a projective linear system while fixing
  all those local data. Taking \(\tau_m=(x,x+y^m)\) leaves a one-dimensional
  hidden-generator space and no lift of \((1,-1)\).
- **Scope guard:** the construction is not the full universal
  complete-linear-system germ.
- **Re-entry condition:** prove G100 from global full-linear-system
  incidence geometry and retain the specified detector pairing.

## NG-127 - Infer persistence from uniform tangent geometry

- **Label:** NO-GO
- **Route:** use a uniform \(U_{R,N}\) conormal matroid, smooth expected
  intersections through rank \(R\), and any fixed finite jet agreement to
  infer that all extra nodes persist on a basis-node germ.
- **Valid input:** these data control the arrangement through rank \(R\) and
  to the chosen finite order.
- **Invalid inference:** they imply analytic branch containment to all
  orders.
- **Precise obstruction:** B159 perturbs one Vandermonde branch to
  \(\ell_N(x)+y^m\). All stated data persist through order \(m-1\), but the
  branch restricts to \(y^m\) on \(F_B=\{x=0\}\), giving the ideal
  \((x_1,\ldots,x_R,y^m)\).
- **Scope guard:** B157 realizes the germ projectively only after a
  generally nonlinear analytic pullback.
- **Re-entry condition:** prove G101 from an identity in the full universal
  incidence germ and retain the specified pairing.

## NG-128 - Infer Euler rigidity from flat projective geometry

- **Label:** NO-GO
- **Route:** use projectivity, flatness, one fixed linear system, and
  constant Hilbert polynomial to infer constant topological Euler
  characteristic on the basis-node germ.
- **Valid input:** those hypotheses fix algebraic Hilbert data and
  arithmetic genus.
- **Invalid inference:** they make singular fibers topologically locally
  trivial or conserve total Milnor number.
- **Precise obstruction:** B161 realizes B159 as a flat relative effective
  Cartier divisor with constant Hilbert polynomial. One tracked node
  disappears along \(F_B\), so B160 makes Euler characteristic change by
  \(-(-1)^r\).
- **Re-entry condition:** prove topological local triviality, total
  Milnor-number constancy, or an equivalent conservation law on G102's
  actual class-directed stratum and retain the specified pairing.

## NG-129 - Replace the total vanishing cone by one constant cohomological piece

- **Label:** NO-GO
- **Route:** preserve one ambient direct-image cohomology sheaf or one flat class and
  infer that every disappearing-node specialization cone vanishes.
- **Valid input:** that summand or class remains locally constant and may
  retain its Hodge type.
- **Invalid inference:** the complementary middle vanishing cycles are
  zero.
- **Precise obstruction:** realize B161 on projective space with connected
  fibers. The unit class and proper base change give
  \(\mathbf Q_T\simeq R^0g_*\mathbf Q\), but an escaping node contributes
  the nonzero rank-one middle cone computed by B162.
- **Scope guard:** B161 does not realize the specified nonzero Saito
  pairing; the counterexample addresses only the invalid piece-to-total
  implication.
- **Re-entry condition:** prove the complete arcwise cone vanishes in G103
  and separately retain the specified relation-channel pairing.

## NG-130 - Infer zero microsupport from decomposition

- **Label:** NO-GO
- **Route:** use smooth total space, projectivity, decomposition, and
  semisimplicity to infer zero internal microsupport on \(F_B\).
- **Valid input:** the direct image decomposes into shifted semisimple
  intersection complexes with pure Hodge-module refinements.
- **Invalid inference:** every strict support is the whole basis germ and
  every coefficient object is locally constant there.
- **Precise obstruction:** B164 makes the B161 total space smooth, so S037
  applies. One node still escapes on \(F_B\), and B163 forces nonzero
  internal microsupport. The smooth universal hypersurface family likewise
  retains nodal discriminant microsupport.
- **Re-entry condition:** prove directly that G104's complete base-changed
  direct image has no nonzero characteristic covector and separately retain
  the specified relation-channel pairing.

## NG-131 - Infer zero microsupport from an alternating cycle

- **Label:** NO-GO
- **Route:** prove the ordinary Grothendieck-group characteristic cycle or
  all fiber Euler characteristics vanish, then infer G105.
- **Valid input:** characteristic cycles are additive with signs under
  shifts; projective decomposition and relative hard Lefschetz hold.
- **Invalid inference:** a zero alternating sum has no microsupport in the
  union of its summands.
- **Precise obstruction:** for B164's smooth-total-space projective escape
  map \(g\), the product map \(g':\mathcal Y\times E\to T\) with an elliptic
  curve satisfies
  \(Rg'_*\mathbf Q\simeq Rg_*\mathbf Q\otimes R\Gamma(E,\mathbf Q)\).
  The Betti numbers \(1,2,1\) give alternating class zero, but the direct
  sum of shifts retains exactly the nonzero microsupport of \(Rg_*\mathbf
  Q\).
- **Scope guard:** this projective counterexample is not a hypersurface
  family; it blocks the general sheaf-theoretic implication only.
- **Re-entry condition:** prove every nonnegative coefficient of B165's
  \(CC^+\) vanishes separately in G105, and retain the detector pairing.

## NG-132 - Replace the microlocal normal cone by pointwise conormals

- **Label:** NO-GO
- **Route:** restrict ambient characteristic covector fibers to \(F_B\),
  quotient by \(N^*_{F_B}P\), and infer G106 when the quotient is zero.
- **Valid input:** B168's smooth branch \(\ell_N(x)+y^m=0\) has every
  ambient conormal over its intersection with \(F_B\) contained pointwise
  in \(N^*_{F_B}P\).
- **Invalid inference:** \(i^\#\) of that conormal has only its zero
  section.
- **Precise obstruction:** the pullback equation is \(y^m=0\). The
  rank-one ODP specialization across its reduced divisor gives
  \(T^*_{\{y=0\}}F_B\subset i^\#\overline{T^*_{D_N}P}\).
- **Jet guard:** \(m\) can exceed any fixed tested order.
- **Re-entry condition:** prove the full normal-cone inclusion of G106,
  not pointwise or finite-order conormal absorption, and separately retain
  the specified pairing.

## NG-133 - Treat ambient microlocal absorption as a syzygy shortcut

- **Label:** NO-GO
- **Route:** use ambient sheaf microsupport or the higher-discriminant
  envelope to prove G106 without establishing the all-order critical-value
  identities of G100/G101.
- **Valid input:** B167 makes zero \(i^\#\)-image sufficient, and the
  Migliorini--Shende envelope is geometric and computable from critical
  tangent images.
- **Invalid inference:** microlocal absorption is strictly weaker than
  persistence of every tracked node.
- **Precise obstruction:** B169 computes the exhaustive ODP envelope as
  the union of the nodal conormals and proves branchwise that
  \(i^\#T^*_{D_j}P\) is zero exactly when \(F_B\subseteq D_j\). Every such
  conormal also occurs in \(SS(Rh_*\mathbf Q)\) by the nonzero one-ODP Euler
  jump. Hence both ambient absorption conditions are equivalent to
  \(H_\tau=0\) and analytic syzygy lifting.
- **Scope guard:** the equivalence neither disproves the existence of the
  syzygies nor supplies the rational type, primitive image, or specified
  pairing.
- **Re-entry condition:** solve G100/G101 in the full linear system with
  all detector clauses retained; no separate microlocal shortcut remains
  under the tracked-ODP hypotheses.

## NG-134 - Infer critical-rank rigidity from linearity

- **Label:** NO-GO
- **Route:** use the fact that a projective linear-system family depends
  affinely on its parameters, combine it with central value rank \(R<N\),
  and infer G107's constant moving evaluation rank.
- **Valid input:** B170 proves that the critical-value Jacobian is
  evaluation at the moving critical points.
- **Invalid inference:** affine-linearity of the spatial equations makes
  that evaluation matrix constant in rank.
- **Precise obstruction:** the two disjoint affine-linear ODP charts

  \[
  q(z)+x,\qquad q(w)+x+2yw_1
  \]

  have critical values \((x,x-y^2)\). Their central row matroid is
  \(U_{1,2}\), but the Jacobian has determinant \(-2y\), the smoothing
  ideal is \((x,y^2)\), and \(\dim H_\tau=1\).
- **Projective guard:** S065 finite-jet interpolation and Bertini realize
  the nonzero quadratic obstruction on a projective linear slice. In that
  realization the full complete-system evaluation may have larger rank,
  so the example does not refute G107.
- **Re-entry condition:** prove that the **full** critical-configuration
  image lies in the global rank-\(R\) evaluation degeneracy locus, or
  solve the weaker G100 factorization directly, while retaining the
  specified pairing.

## NG-135 - Infer constant critical rank from smooth excess

- **Label:** NO-GO
- **Route:** prove \(H_\tau=0\), or only B146's Hessian equations on
  \(\ker E\times\ker E\), and infer G107.
- **Valid input:** smooth excess gives analytic critical-value syzygies
  and kills every pure conditional Kuranishi tensor.
- **Invalid inference:** it also kills the determinantal mixed tensor on
  \(W\times\ker E\).
- **Precise obstruction:** the affine-linear ODP model has

  \[
  \tau=(x,(1+y)x),\qquad I_\tau=(x),\qquad H_\tau=0,
  \]

  with lifted relation \((1+y)\tau_1-\tau_2=0\). Nevertheless
  \(\det(d\tau)=x\), and the central relation evaluates to \(-1\) on
  \(d^2\tau_0(\partial_x,\partial_y)\).
- **Projective guard:** S065 realizes the decisive finite jets on a
  projective linear slice, not a rank-deficient full complete system.
- **Re-entry condition:** verify B171's mixed equations and every higher
  determinantal condition directly if pursuing optional G107. Otherwise
  return to the exact G100 syzygy gate and its specified pairing.

## NG-136 - Global residues automatically isolate tracked nodes

- **Label:** NO-GO
- **Route:** apply the Jacobi global residue theorem to the gradient of a
  polynomial chart and read off all analytic syzygies among the tracked
  nodal critical values.
- **Valid input:** B172 proves that admissible numerators of the form
  \(f_tA\) give the required syzygies when their auxiliary residue vanishes
  modulo the tracked value ideal and their central rows span every relation.
- **Invalid inference:** the residue theorem itself constructs those
  numerators or removes auxiliary critical points and infinity terms.
- **Precise obstruction:** for \(f_t=(z^2-1)^2+t\), the tracked values at
  \(z=\pm1\) have the exact syzygy \(t-t=0\). Yet
  \(\deg f_t=4\), while the one-variable Jacobi bound for
  \(f_t'=4z(z^2-1)\) is one. The would-be critical-value residue equals
  \(-1/4\), the uncancelled infinity contribution.
- **Scope guard:** this is an affine mechanism counterexample, not a Hodge
  counterexample and not an exclusion of every possible residue method.
- **Re-entry condition:** prove a bounded-degree selector theorem for the
  complete critical configuration, kill the auxiliary class in
  \(\mathcal O/I_\tau\), control the projective boundary, and retain rational
  type, primitive ambient image, and the specified nonzero pairing.

## NG-137 - Exact critical-degree selectors bypass critical-rank rigidity

- **Label:** NO-GO
- **Route:** construct \(N-R\) analytic Jacobi numerators of maximal
  admissible degree that vanish at every auxiliary critical point, and use
  their residue rows as a direct route to G100.
- **Valid input:** B172 makes such a frame sufficient for analytic syzygy
  lifting.
- **Invalid inference:** this exact-selector frame is weaker than G107.
- **Precise obstruction:** B173 applies residual Cayley--Bacharach duality
  at complementary degrees \(e=s-m\) and \(m\), then uses Hessian-weighted
  Jacobi orthogonality to prove
  \[
  \operatorname{Sel}^{\mathrm{res}}_e(T_t)
  =\ker(\operatorname{ev}_{T_t}^{m})^*.
  \]
  A local analytic frame of \(N-R\) rows therefore exists exactly when the
  moving degree-\(m\) evaluation rank stays \(R\).
- **Scope guard:** this equality concerns reduced no-infinity gradient
  complete intersections and exact auxiliary vanishing. It does not treat
  arbitrary projective varieties or nonzero auxiliary residues in
  \(I_\tau\).
- **Re-entry condition:** prove a genuinely different compact residue
  duality or prove G107 with every detector clause. B174/NG138 show that
  G108's bare auxiliary ideal-membership version is terminal-equivalent to
  G100.

## NG-138 - Auxiliary residue ideal membership is progress

- **Label:** NO-GO
- **Route:** allow a nonzero auxiliary residue \(\rho_A\), prove or observe
  \(\rho_A\in I_\tau\), choose coefficients
  \(\rho_A=\sum b_i\tau_i\), and count the adjusted row as a new syzygy.
- **Valid input:** an adjusted row \(b+c_A\) is a syzygy whenever
  \(c_A\cdot\tau+\rho_A=0\).
- **Invalid inference:** auxiliary ideal membership or existence of some
  coefficient representation supplies that syzygy independently.
- **Precise obstruction:** the residue identity already gives
  \(\rho_A=-c_A\cdot\tau\). B174 proves that
  \(b\mapsto b+c_A\) is an affine bijection from all coefficient
  representations of \(\rho_A\) to \(\operatorname{Syz}(\tau)\). The
  canonical representation gives zero; every other choice is exactly a
  pre-existing syzygy.
- **Hidden-generator guard:** for \(\tau=(x,x+y^2)\), every syzygy is a
  multiple of \((x+y^2,-x)\) and vanishes at the origin, so no auxiliary
  identity lifts the central relation \((1,-1)\).
- **Re-entry condition:** construct the nonzero analytic syzygy by
  independent geometry and retain all detector clauses. This is G100
  itself, not a smaller residue criterion.

## NG-139 - Free discriminant forces critical-value syzygy lifting

- **Label:** NO-GO
- **Route:** prove the reduced total discriminant is a free divisor, choose
  a Saito basis of logarithmic vector fields, and infer \(H_\tau=0\).
- **Valid input:** S071 controls the principal reduced equation
  \(F=\prod_i\tau_i\) and the module
  \(\operatorname{Der}(-\log V(F))\).
- **Invalid inference:** this determines the labelled simultaneous ideal
  \((\tau_1,\ldots,\tau_N)\) or lifts its central linear relations.
- **Precise obstruction:** B175 takes
  \(\tau=(x,x+y^2)\). The reduced plane curve
  \(F=x(x+y^2)\) has a branch-preserving Saito basis with coefficient
  determinant \(-4F\), but
  \(I_\tau=(x,y^2)\), \(\dim H_\tau=1\), and every analytic syzygy
  vanishes at the origin.
- **Scope guard:** the example is an exact local ODP critical-value model
  and has projectively realizable finite jets; it is not a claim about a
  rank-deficient full complete-system germ and is not a Hodge
  counterexample.
- **Re-entry condition:** prove a genuinely labelled, scheme-theoretic
  logarithmic theorem making syzygy evaluation surjective in the full
  complete-linear-system geometry, then retain the uniform matroid,
  adjoint defect, primitive ambient image, rational type \((0,0)\), and
  specified nonzero pairing. This is G100, not a smaller free-divisor gate.

## NG-140 - Zariski tangent directions integrate logarithmically

- **Label:** NO-GO
- **Route:** identify \(\ker d\tau_0\) and integrate each of its vectors to
  a derivation preserving the labelled ideal \(I_\tau\).
- **Valid input:** every ideal-preserving derivation evaluates into
  \(\ker d\tau_0\).
- **Invalid inference:** this inclusion is automatically surjective.
- **Precise obstruction:** for \(I_\tau=(x,y^2)\), a derivation
  \(a\partial_x+b\partial_y\) preserves the ideal exactly when
  \(a\in(x,y^2)\) and \(b\in(x,y)\). Hence every such derivation vanishes
  at the origin, whereas \(\ker d\tau_0=\mathbf C\partial_y\).
- **Scope guard:** B176 proves that surjectivity would close \(H_\tau\),
  but it does not manufacture the vector fields. The countermodel is local
  ODP deformation geometry, not a Hodge counterexample.
- **Re-entry condition:** construct \(d-R\) ideal-preserving analytic
  fields to all orders from the full complete-linear-system incidence, as
  in G109, while retaining every detector clause.

## NG-141 - A positive symmetry orbit spans the logarithmic kernel

- **Label:** NO-GO
- **Route:** use a connected polarized-automorphism orbit preserving the
  nodal ideal and count its positive dimension as the full G109 frame.
- **Valid input:** B177 proves that every fundamental field is logarithmic
  and that its value lies in \(\ker d\tau_0\).
- **Invalid inference:** a positive orbit has the full dimension \(d-R\).
- **Precise obstruction:** for
  \(\tau=(u,(1+v)u)\) on \(\mathbf C^3\), one has
  \(I_\tau=(u)\) and
  \(\ker d\tau_0=\mathbf C\partial_v\oplus
  \mathbf C\partial_w\). Translation in \(w\) preserves both branches
  but supplies only \(\partial_w\).
- **Dimension guard:** symmetry fields contribute exactly
  \(r_A=\dim T_0(A\cdot0)\); any completion needs at least
  \(d-R-r_A\) independent residual values.
- **Scope guard:** this is a local spanning obstruction, not a Hodge
  counterexample. A special variety with a large automorphism orbit cannot
  stand in for arbitrary smooth projective varieties.
- **Re-entry condition:** compute the actual orbit tangent, then construct
  the quotient frame in G110 and retain every detector clause.

## NG-142 - Gauss-Manin flatness stabilizes the escape ideal

- **Label:** NO-GO
- **Route:** use constant nodewise Milnor lattices, Picard--Lefschetz
  operators, or Gauss--Manin flatness to assert that B178's scalar escape
  ideal is stable under tangent differentiation.
- **Valid input:** Gauss--Manin gives a flat connection on a cohomology
  bundle or local system.
- **Invalid inference:** that connection acts on the analytic ideal of
  critical-value functions.
- **Precise obstruction:** B157 realizes
  \(\tau=(x,x+y^2)\) with fixed ODP Hessians and constant local
  \(A_1\) data. On the basis germ \(F_B=\{x=0\}\), the escape ideal is
  \(K_B=(y^2)\), but \(\partial_y(y^2)=2y\notin K_B\).
- **Scope guard:** the realization is projective over a generally
  nonlinear analytic pullback. It refutes a theorem based only on local
  flat data, not every possible full-system comparison.
- **Re-entry condition:** G111 must construct a canonical
  connection-compatible map from the actual full-family cohomological
  object to \(K_B\), prove differential stability, and retain every
  detector clause.

## NG-143 - Finite conormal jets force all-order vanishing

- **Label:** NO-GO
- **Route:** verify B179's conormal escape defect through one fixed finite
  jet order and promote that calculation to \(\beta_{K_B}=0\).
- **Valid input:** the checked jets vanish.
- **Invalid inference:** an analytic obstruction cannot first appear at a
  higher order.
- **Precise obstruction:** for any \(q\), choose \(m\ge q+2\) and
  \(K_m=(y^m)\). Then
  \(\beta_{K_m}([y^m])=m y^{m-1}dy\pmod {y^m}\) is nonzero, while its
  coefficient has zero \(q\)-jet.
- **Uniform-matroid guard:** B159 embeds this escape in a germ retaining a
  uniform conormal matroid and smooth expected intersections for every
  subset of at most \(R\) branches.
- **Projective guard:** B157-B159 give projective finite-jet realization
  over a nonlinear analytic base; this does not exclude a new theorem for
  the full system.
- **Re-entry condition:** prove literal analytic vanishing in G112, or
  prove a new uniform order bound from full-system geometry, with every
  detector clause retained.

## NG-144 - Algebraicity gives a uniform jet bound

- **Label:** NO-GO
- **Route:** observe that critical-value branches are algebraic/Nash and
  choose one finite jet order independent of their defining complexity.
- **Valid input:** a fixed simple polynomial presentation of degree \(D\)
  gives B180's order bound \(D\).
- **Invalid inference:** algebraicity supplies one bound independent of
  \(D\), the polarization power, and elimination complexity.
- **Precise obstruction:** \(\epsilon_m=y^m\) is the simple branch of
  \(P_m(y,z)=z-y^m\), with \(\partial_zP_m=1\). Its degree and vanishing
  order are both \(m\), and its conormal defect first occurs in degree
  \(m-1\).
- **Projective guard:** B157 realizes each polynomial escape after
  sufficient twisting, but does not give a fixed full-system presentation
  of bounded degree across all powers.
- **Re-entry condition:** G113 must compute and audit an explicit common
  degree bound after every full-incidence restriction, étale coordinate,
  and elimination step; then the required jets and detector clauses must
  still be proved.

## NG-145 - The value resultant gives simple labelled branches

- **Label:** NO-GO
- **Route:** eliminate the critical-point coordinates to the single
  resultant \(\operatorname{Res}(f',w-f)\) and apply B180 to each node.
- **Valid input:** the resultant vanishes exactly at the unordered set of
  critical values, with multiplicity.
- **Invalid inference:** it is simple in \(w\) at a value shared by
  several distinct critical points or remembers their labels.
- **Precise obstruction:** for \(f=(z^2-1)^2\), the distinct Morse points
  \(-1,0,1\) have values \(0,1,0\), and the resultant is
  \(256w^2(w-1)\). Its \(w\)-derivative vanishes at zero.
- **Squarefree guard:** replacing the specialized resultant by
  \(w(w-1)\) collapses the two zero-value labels and does not construct
  their nearby analytic branches.
- **Re-entry condition:** G114 must choose a critical-point separator,
  split the finite étale algebra into labelled factors, and track all
  degrees and denominators before invoking B180. Detector clauses remain
  separate.

## NG-146 - Central separation bounds idempotent complexity

- **Label:** NO-GO
- **Route:** use only the finite étale rank and the nonzero central gaps of
  a separator to assign a uniform complexity bound to the labelled
  idempotents.
- **Valid input:** B182 proves the idempotents exist analytically because
  the separator differences are units.
- **Invalid inference:** their inverse units or algebraic coefficients have
  bounded degree or become visible at a bounded jet order.
- **Precise obstruction:**
  \(A_m=\mathbf C\{y\}[z]/((z-y^m)(z-1))\) has rank two and central
  separator values \(0,1\) for every \(m\), but its idempotents contain
  \((1-y^m)^{-1}\) and first vary in order \(m\).
- **Morse guard:** this is the critical algebra of a cubic family with
  derivative \((z-y^m)(z-1)\); both Hessians are units near the origin.
- **Re-entry condition:** G115 must start from the complete equations and
  track the characteristic polynomial, discriminant inverse, Hensel roots,
  and idempotents quantitatively. Conormal jets and detector clauses remain
  separate.

## NG-147 - Unit-denominator complexity delays conormal detection

- **Label:** NO-GO
- **Route:** use arbitrarily late Taylor variation of a separator unit or
  its inverse as an obstruction to a finite conormal-escape certificate.
- **Valid input:** NG146 proves that fixed étale rank and fixed nonzero
  central separator gaps do not bound the complete Taylor complexity of
  labelled idempotents.
- **Invalid inference:** the first nonzero conormal coefficient of an
  escape ideal must occur as late as the first nonconstant coefficient of
  a unit denominator.
- **Precise obstruction:**
  \(\epsilon_m=y/(1-y^m)\) has a unit denominator first varying in order
  \(m\), but \((\epsilon_m)=(y)\) and its conormal defect is the nonzero
  class \(dy\bmod y\), visible in order zero for every \(m\).
- **Correction to NG146:** NG146 remains a valid obstruction to bounding
  complete idempotent complexity from rank and central separation alone.
  B183 shows it is not a conormal-order obstruction after unit clearing.
- **Re-entry condition:** G116 must certify the denominators are units,
  clear them, and bound the resulting numerator functions through the
  full labelled incidence. The required conormal jets and every detector
  clause remain separate.

## NG-148 - Algebraicity gives a simple polynomial over the base

- **Label:** NO-GO
- **Route:** eliminate every labelled étale coordinate and apply B180 to a
  polynomial in the original basis coordinates and one value variable.
- **Valid input:** each labelled value is an algebraic analytic branch, and
  effective elimination supplies polynomial relations of bounded degree.
- **Invalid inference:** one of those relations must have nonzero derivative
  in the value variable at the collided central value.
- **Precise obstruction:** on the étale cover
  \(\lambda^2=1+u\), the numerator
  \(\epsilon=u\lambda=u\sqrt{1+u}\) has order one, but its irreducible
  polynomial is \(z^2-u^2(1+u)\). Both conjugate values specialize to zero,
  so this polynomial and every multiple have zero \(z\)-derivative at the
  origin.
- **Scope guard:** this is collision of the value conjugates, not
  ramification of the separator cover; \(2\lambda\ne0\) at both central
  points.
- **Re-entry condition:** retain a pointed étale algebraic carrier, express
  the numerator regularly on it, and apply B184's carrier-degree bound as
  required by G117. B185 now closes the carrier construction; the jets and
  detectors remain open in G118.

## NG-149 - Effective carrier bounds force jet vanishing

- **Label:** NO-GO
- **Route:** after constructing B185's smooth étale carrier and finite
  certificate order, treat finiteness or low algebraic degree as evidence
  that the required conormal coefficients vanish.
- **Valid input:** the carrier and cleared numerators come from the actual
  labelled algebraic incidence, and B184-B185 give a rigorous finite order
  beyond which no first nonzero defect can hide.
- **Invalid inference:** bounded detectability implies vanishing.
- **Precise obstruction:** the affine-linear ODP charts
  \(f_1=z^2+x\) and \(f_2=w^2+yw+x\) have critical values
  \(x\) and \(x-y^2/4\). Their basis carrier \(x=0\) has degree one, but
  its escape ideal is \((y^2)\) and
  \(\beta([y^2])=2y\,dy\bmod y^2\ne0\).
- **Full-system guard:** the family is affine-linear in the parameters and
  has constant nondegenerate Hessians. What it lacks is the arbitrary-class
  Hodge detector, so it refutes only the carrier-data shortcut.
- **Re-entry condition:** G118 must prove the actual finitely many conormal
  coefficients vanish using new class-directed full-incidence geometry.
  Effective elimination, smoothness, and finite checkability are not that
  proof.

## NG-150 - Quadratic Kuranishi vanishing promotes to every order

- **Label:** NO-GO
- **Route:** prove B146's full quadratic relation-Hessian tensor vanishes
  and infer the cubic and all remaining rungs of B186's finite ladder.
- **Valid input:** after the quadratic tensor vanishes, B154 makes the
  corrected cubic tensor canonical.
- **Invalid inference:** canonical means zero, or quadratic flatness
  supplies a formal recurrence killing the higher tensors.
- **Precise obstruction:** for fixed \(a\ne b\), the affine-linear ODP
  charts
  \[
  f_a=x+yw+w^2/2+a w^3,\qquad
  f_b=x+yw+w^2/2+b w^3
  \]
  have critical values
  \(x-y^2/2-a y^3+O(y^4)\) and
  \(x-y^2/2-b y^3+O(y^4)\). On the first basis branch, the escape is
  \((a-b)y^3+O(y^4)\).
- **Jet conclusion:** \(K_B\subset\mathfrak m^3\) but
  \(K_B\not\subset\mathfrak m^4\); equivalently
  \(j^1\beta_{K_B}=0\) and \(j^2\beta_{K_B}\ne0\).
- **Re-entry condition:** after G119 kills the quadratic tensor, construct
  a separate cubic-vanishing mechanism and then continue through every
  finite rung required by G118. Hodge detector clauses remain attached.

## NG-151 - A global Lagrangian splits nodewise

- **Label:** NO-GO
- **Route:** saturate B187's \(nN\) ceiling for one full-support relation
  and infer the split nodewise conormal Lagrangians of B147-G093.
- **Valid input:** a maximal isotropic subspace for the nondegenerate
  full-support relation form is a global Lagrangian.
- **Invalid inference:** the global Lagrangian respects the direct-sum
  decomposition into nodal Hessian blocks.
- **Precise obstruction:** for \(N=2,R=1\), take identical
  \(2n\)-dimensional nondegenerate spaces \((H,B)\) and relation
  \(c=(1,-1)\). The diagonal
  \[
  U=\{(v,v):v\in H\}\subset(H\oplus H,B\oplus(-B))
  \]
  is isotropic of dimension \(2n=nN\), hence maximal, but both projections
  \(U\to H\) are isomorphisms.
- **Splitting guard:** \(U\) is not contained in
  \(\Lambda_1\oplus\Lambda_2\) for any proper nodewise maximal isotropics.
  One relation also does not impose the quadrics for every other relation.
- **Re-entry condition:** G120 uses only the global condition proved
  necessary by B187. Any nodewise split core or full G119 vanishing needs a
  separate geometric construction with every detector clause.

## NG-152 - Half-dimensional gradient rank creates isotropy

- **Label:** NO-GO
- **Route:** satisfy B187's numerical bound
  \(\dim U\le nN\) and infer that some nonzero value relation makes \(U\)
  isotropic.
- **Valid input:** any \(U\) isotropic for a full-support nondegenerate
  relation form has dimension at most \(nN\).
- **Invalid inference:** reverse the Witt-index implication using dimension
  alone.
- **Precise obstruction:** for \(N=2,R=1\), let
  \(S=\mathbf C(1,1)\) and take
  \(U=G_1\oplus0\), with \(\dim G_1=2n\). Then
  \(\dim U=2n=nN\), but nondegeneracy of the first Hessian gives
  \(H(U)=\mathbf C(1,0)\).
- **Augmented calculation:**
  \[
  S+H(U)=\mathbf C^2,\qquad
  (S+H(U))^\perp=0.
  \]
  The unique value relation \((1,-1)\) restricts to the nonzero first
  Hessian form.
- **Re-entry condition:** G121 must construct a rank-deficient augmented
  Hessian-value map and a no-zero-coordinate annihilator. Gradient rank,
  first-jet defect, and dimension counts alone do not supply them.

## NG-153 - Restrict a high-power family to manufacture the augmented defect

- **Label:** NO-GO
- **Route:** fix prospective nodes, use high-power jet interpolation to
  prescribe B190's synchronized pattern in a chosen small family, and count
  that family's augmented defect for the full complete-linear-system germ.
- **Valid input:** S065 permits arbitrary fixed finite jets in sufficiently
  high powers, and the selected subfamily can have the desired synchronized
  gradient image and fixed nondegenerate Hessians.
- **Invalid inference:** restoring all global sections preserves the value
  and conditional-gradient ranks of the restricted family.
- **Precise obstruction:** full first-jet surjectivity gives
  \(S=\mathcal T\) and \(U=\bigoplus_iG_i\). Hence \(L_U=0\). More locally,
  B189's isolated-gradient image is all of \(G_i\) at every node; its
  nondegenerate Hessian span contains the value line \(\mathcal T_i\), so
  a full-support augmented annihilator is impossible.
- **Re-entry condition:** construct special supports varying with the line
  bundle for which the defect belongs to the full universal incidence,
  passes B189 at every node, satisfies B190 globally, and retains the
  rational detector and specified nonzero pairing.

## NG-154 - Use the product-fiber detector as conformal synchronization

- **Label:** NO-GO
- **Route:** promote the B142-B143 moving-fiber incidence, which already has
  clean nodal geometry and a nonzero rational detector, to G122/G123.
- **Valid input:** the full value matroid is uniform, the deep incidence is
  smooth, and the unique relation pairs nontrivially with the primitive
  Hodge line.
- **Invalid inference:** the \(n\)-dimensional carrier-motion quotient is
  the entire conditional-gradient image.
- **Precise obstruction:** B152 proves that the full system also has an
  \(nR\)-dimensional conormal-gradient image. Thus
  \[
  \dim U=nR+n=n(R+1)>2n
  \]
  for the B142 range \(R>1\). B191 requires every projection
  \(U\to G_i\) to be injective into a \(2n\)-dimensional block, which is
  impossible.
- **Circularity guard:** the family additionally starts from a known
  algebraic fiber, but the finite coherent gate already fails before that
  logical issue is reached.
- **Re-entry condition:** construct unanchored full-system data with
  \(q\le2n\), all one-node kernel equalities, tensor rank one, value factor
  in \(S\), and the specified rational detector.

## NG-155 - Synchronize a nodal orbit in one semi-invariant component

- **Label:** NO-GO
- **Route:** make a finite group act transitively on the nodes and impose
  invariant, alternating, or one-character semi-invariant deformations so
  their jets are transported diagonally around the orbit.
- **Valid input:** equivariance genuinely relates values, gradients, and
  Hessians inside the selected character component.
- **Invalid inference:** that component equals the complete section space,
  or every omitted component contributes zero to the conditional-gradient
  quotient.
- **Precise obstruction:** B192 proves that for a very ample linearized
  bundle and a node orbit of size greater than one, every character space is
  strict. If all sections transformed by one character, the induced action
  on the very ample projective embedding would be trivial and the group
  could not move the nodes.
- **Full-system guard:** omitted isotypic components can enlarge
  \(H^0(I_ZL)/H^0(I_{2Z}L)\) and the Hessian flattening. There is no
  automatic inclusion of their value-zero sections in \(H^0(I_{2Z}L)\).
- **Re-entry condition:** compute all isotypic components and prove B191's
  equalities and tensor rank for their total, or construct G123 by a
  nonsymmetry mechanism, while retaining the rational detector.

## NG-156 - Promote reduced Cayley-Bacharach to doubled-jet holonomy

- **Label:** NO-GO
- **Route:** take the minimal reduced adjoint evaluation circuit of
  B138-B141, apply S056-S060, and count the resulting carrier as B193/G124
  one-node determination.
- **Valid input:** the reduced circuit has a unique full-support scalar
  relation and the audited theorems can force small circuits onto
  bounded-degree curves.
- **Invalid inference:** reduced values for
  \(F=K_X\otimes L^n\) determine first derivatives for \(L\) on \(2Z\),
  or determine inverse-Hessian similitudes.
- **Precise obstruction:** S056-S060 contain no map from reduced adjoint
  postulation to
  \(H^0(I_ZL)/H^0(I_{2Z}L)\), the one-node schemes \(\Psi_i\), or the
  Hessian tensor. They yield carrier containment only. B029 further shows
  that overloading the simplest line carrier puts the whole line in the
  singular locus rather than producing isolated ODPs.
- **Re-entry condition:** prove a new theorem for the actual doubled
  \(L\)-jet scheme giving B191's kernel equalities, B193's conformal
  cocycle, isolated nodes, and the rational detector.

## NG-157 - Multiply a lower-degree jet defect into the target power

- **Label:** NO-GO
- **Route:** construct nonzero conditional node gradients in \(H^k\), then
  multiply by sections of \(H^{m-k}\) to obtain G123/G124 in degree \(m\).
- **Valid input:** products remain value-zero on \(Z\), and their node
  gradients equal the multiplier values times the lower gradients.
- **Invalid inference:** multiplication preserves determination by any one
  node.
- **Precise obstruction:** if a lower section has nonzero gradient at
  \(p_i\), choose a multiplier vanishing at another node \(p_j\) but not at
  \(p_i\). The product has gradient zero at \(p_j\) and nonzero at \(p_i\),
  directly violating B191. B194 proves equivalently that target one-node
  determination forces every lower quotient to be zero.
- **Re-entry condition:** G125 must realize a primitive first-jet birth at
  degree \(m\), with no lower conditional gradients, and separately supply
  Hessian holonomy and the rational detector.

## NG-158 - Raise the power while preserving fixed-node holonomy

- **Label:** NO-GO
- **Route:** after constructing G125 at \(H^m\), pass to \(H^{m+a}\) with
  the same node scheme and use positivity to stabilize one-node
  determination, holonomy, and the detector.
- **Valid input:** multiplication embeds the old value-zero sections in the
  higher complete system.
- **Invalid inference:** added multiplier values preserve the
  \(2n\)-dimensional graph.
- **Precise obstruction:** B195 gives an injection
  \[
  E_a\otimes V_m\hookrightarrow V_{m+a}.
  \]
  Since \(H^a\) separates two points, \(r_a\ge2\), so
  \(q_{m+a}\ge4n>2n\). For \(a\gg0\), evaluation on fixed \(Z\) is
  surjective and \(V_{m+a}\) equals the full \(2nN\)-dimensional gradient
  target.
- **Scope guard:** choosing a new node scheme is not excluded, but requires
  a new primitive-birth and detector proof.
- **Re-entry condition:** close B186's finite Kuranishi ladder at the
  original birth degree as in G126, without polarization transport.

## NG-159 - Use generic Terracini theory to construct the absorbing spans

- **Label:** NO-GO
- **Route:** invoke Terracini's lemma or generic tangential-contact loci as
  existence of G127's special lower point schemes.
- **Valid input:** S073 Theorem 3.1 identifies, for general points, the
  tangent space to their secant variety with the span of their embedded
  tangent spaces.
- **Invalid inference:** the span of the points themselves contains those
  tangent spaces, or points with that property exist simultaneously in all
  lower embeddings.
- **Precise obstruction:** the containment direction is reversed and the
  scopes disagree. S073 uses general points in one embedding; G127 requires
  a highly special, class-directed \(Z\) fixed across every \(H^k\), with
  \(T_{X,p_i}^{(k)}\subset\langle\phi_k(Z)\rangle\).
- **Detector guard:** secant/contact theory supplies no isolated ODP member,
  doubled-scheme birth, Hessian holonomy, rational type, or specified Hodge
  pairing.
- **Re-entry condition:** analyze the actual special point-span incidence,
  then construct the degree-m primitive birth and detector separately.

## NG-160 - Move fixed points into high regularity to create primitive birth

- **Label:** NO-GO
- **Route:** fix \(Z\), raise \(m\) beyond its regularity threshold, and
  expect positivity to create G125's first \(2n\)-dimensional jet space.
- **Valid input:** S065 gives eventual generation of the ideal section
  module and eventual full first-jet interpolation for fixed \(Z\).
- **Invalid inference:** asymptotic generation produces new degree-\(m\)
  ideal generators or retains one-node determination.
- **Precise obstruction:** if lower jets vanish, B198 puts every product of
  lower ideal sections inside \(H^0(I_{2Z}H^m)\). Beyond the generator
  ceiling there are only such products, so \(V_m=0\). Beyond the jet-
  separation threshold one instead has \(\dim V_m=2nN>2n\) for \(N>1\).
- **Detector guard:** neither regime constructs ODP holonomy, a Kuranishi
  certificate, rational type, or a nonzero specified pairing.
- **Re-entry condition:** vary \(Z\) with \(m\), stay in its finite new-
  generator window, and close G128's adjacent birth and detector clauses.

## NG-161 - Use only the transverse jet generators as the nodal package

- **Label:** NO-GO
- **Route:** take exactly \(2n\) new degree-\(m\) generators with independent
  gradients at \(Z\), and choose their linear combination as the central
  divisor singular at every node.
- **Valid input:** their gradient classes can realize a
  \(2n\)-dimensional one-node-determined \(V_m\).
- **Invalid inference:** the same generator space contains a nonzero class
  in \(K_m=H^0(I_{2Z}H^m)\).
- **Precise obstruction:** when lower ideal sections vanish and the
  \(2n\) generators exhaust \(J_m\), B199's exact sequence has equal
  source and quotient dimensions, forcing \(K_m=0\).
- **Detector guard:** transverse point cutting alone supplies no central
  ODP member, Hessian holonomy, Kuranishi integration, rational type, or
  specified pairing.
- **Re-entry condition:** add G129's new double-generator line or construct
  the inherited-double branch with simultaneously nondegenerate lower
  Hessian combinations, then re-audit every detector clause.

## NG-162 - Recycle a point-ideal generator as the conformal multiplier

- **Label:** NO-GO
- **Route:** use \(F\) or one of G129's transverse degree-\(m\) generators
  as \(t\) in B200's quadratic congruence.
- **Valid input:** the proposed sections have the correct degree \(m\).
- **Invalid inference:** degree agreement gives the required value vector.
- **Precise obstruction:** every element of \(J_m=H^0(I_ZH^m)\) restricts
  to zero on \(Z\), while maximal holonomy forces every multiplier
  coordinate to be nonzero.
- **Detector guard:** a zero multiplier cannot encode B191's rank-one
  inverse-Hessian tensor and supplies no detector or pairing.
- **Re-entry condition:** construct an ambient
  \(t\in H^0(H^m)\setminus J_m\) with nowhere-zero values and prove
  \(tF-\mu_2(Q)\in H^0(I_Z^3H^{2m})\), retaining every higher obligation.

## NG-163 - Promote a formal Morse normal form to full cubic closure

- **Label:** NO-GO
- **Route:** formally normalize the central section \(F\) to its common
  quadratic form on the selected \(U\)-slice and infer \(\kappa_3=0\).
- **Valid input:** nodewise formal coordinates remove higher spatial terms
  of the fixed central ODP germ.
- **Invalid inference:** those coordinate changes synchronize every
  parameter direction in the full projective tangent system.
- **Precise obstruction:** B201's mixed block evaluates the independent
  Hessians of all
  \(\overline K=H^0(I_{2Z}H^m)/\mathbf CF\) directions. Central
  normalization imposes no vanishing of this map.
- **Detector guard:** a selected formal slice neither proves reduced
  full-incidence integration nor retains the rational detector and pairing.
- **Re-entry condition:** prove both \(\Theta=0\) and \(\Xi=0\) in G131
  without deleting \(\overline K\), then proceed separately to the quartic
  and every later finite rung.

## NG-164 - Kill the whole third-neighborhood obstruction group

- **Label:** NO-GO
- **Route:** impose \(H^1(I_Z^3H^m)=0\) so every prescribed quadratic
  profile lifts to a degree-\(m\) section.
- **Valid input:** B202's connecting homomorphism then vanishes and the
  quadratic lift exists.
- **Invalid inference:** the complete system still has the value and
  conditional-gradient defects required by G130.
- **Precise obstruction:** the same vanishing makes evaluation on
  \(\mathcal O_X/I_Z^3\) surjective. Hence \(R=N\) and
  \(\dim V_m=2nN>2n\) for \(N>1\).
- **Detector guard:** full jet interpolation supplies no value relation,
  class-specific rational detector, or specified nonzero pairing.
- **Re-entry condition:** construct G132's one nondegenerate kernel element
  for a nonzero connecting map, with a new minimal ODP lift and every
  detector clause.

## NG-165 - Count every coherent lift as a new minimal generator

- **Label:** NO-GO
- **Route:** prove \(\partial_Z(q)=0\), choose a lift \(F\), and count it as
  G129's new double-generator line.
- **Valid input:** \(F\) has the prescribed quadratic profile.
- **Invalid inference:** \(F\notin P_m=(R_+J)_m\).
- **Precise obstruction:** if \(q\in\rho(P_m)\), a decomposable lift
  \(p\in P_m\) already has that profile. Every other lift is \(p+g\) with
  \(g\in T_m\). When \(T_m\subset P_m\), every lift remains decomposable.
- **Detector guard:** a zero class in \(K_m/P_m\) cannot supply G129's
  central minimal generator, regardless of its local Hessian.
- **Re-entry condition:** prove G133's one-dimensional quotient conditions
  or construct the alternative triple-hidden branch, with ODPs and every
  detector clause.

## NG-166 - Multiply a lower quadratic profile into the birth degree

- **Label:** NO-GO
- **Route:** choose \(w\in W_{m-a}\), multiply by \(e\in E_a\), and count
  \(ew\) as G134's primitive quadratic profile.
- **Valid input:** a nowhere-zero value multiplier injects the lower
  profile and may preserve nondegeneracy.
- **Invalid inference:** the transported profile is indecomposable in
  degree \(m\).
- **Precise obstruction:** B204 places \(ew\) in
  \(E_aW_{m-a}\), one of the summands quotiented out in G134.
- **Detector guard:** a zero indecomposable class cannot supply G129's new
  double generator or any class-specific detector.
- **Re-entry condition:** construct a genuinely primitive nondegenerate
  profile line in G134 and retain the triple-hidden, ODP, rank, and detector
  conditions.

## NG-167 - Infer mixed cubic closure from a primitive profile line

- **Label:** NO-GO
- **Route:** prove G134's one-dimensional primitive quotient and infer
  \(\Xi=0\).
- **Valid input:** B205 shows that the central profile line lies in
  \(\ker\widehat\Xi_m\).
- **Invalid inference:** the decomposable profile denominator also lies in
  that kernel.
- **Precise obstruction:** a product \(ew\) from a lower profile has mixed
  contraction \(eC_{m,k}(w)\), which need not lie in the degree-\(m\) value
  image \(S_m\).
- **Detector guard:** a nonzero mixed cubic class obstructs reduced
  full-incidence integration before any detector can propagate.
- **Re-entry condition:** prove every containment in G135, then kill the
  pure cubic tensor and all later rungs separately.

## NG-168 - Treat a global profile contraction as a global value

- **Label:** NO-GO
- **Route:** lift \(w\in W_k\) to a global section double on \(Z\), contract
  its Hessian by the final inverse-Hessian transported directions, and
  count the result as an element of \(E_k\).
- **Valid input:** the uncontracted quadratic profile is a global second
  jet.
- **Invalid inference:** its contraction is the value of a global
  \(H^k\)-section or automatically lies in \(A_{m,k}\).
- **Precise obstruction:** the transported directions are nodewise data;
  no global section-valued differential operator with that symbol is
  provided. The exact two-node model in NG168 has a contraction outside the
  colon.
- **Detector guard:** a surviving colon class gives a nonzero mixed cubic
  obstruction before detector propagation.
- **Re-entry condition:** construct a compatible global symbol or prove
  G136's weaker colon containment by another geometric mechanism.

## NG-169 - Differentiate a value relation into a Hessian relation

- **Label:** NO-GO
- **Route:** differentiate \(r\in S_m^\perp\) and infer that every
  \(\ell_{r,e,b,c}\) annihilates \(W_k\).
- **Valid input:** \(r\) annihilates the values of all global degree-
  \(m\) sections.
- **Invalid inference:** it annihilates second jets at distinct marked
  points.
- **Precise obstruction:** for a lower double section \(s\), the global
  product \(es\) already has zero value on \(Z\); applying \(r\) gives only
  \(0=0\) and no Hessian identity.
- **Detector guard:** a nonzero functional on \(W_k\) is precisely a
  surviving mixed cubic class after the B207 dualization.
- **Re-entry condition:** construct the coherent preimage demanded by G137
  or a genuine global differential comparison.

## NG-170 - Import standard Gaussian-map surjectivity into G137

- **Label:** NO-GO
- **Route:** identify the Hessian symbol with a standard higher Gaussian
  map and count a surjectivity theorem as G137.
- **Valid input:** S074 defines diagonal-ideal Gaussian maps and records
  special deformation/second-fundamental-form applications.
- **Invalid inference:** those maps land in B207's dual connecting-map
  image.
- **Precise obstruction:** their source and target omit the finite value
  relation, marked scheme, central inverse Hessians, and the sequence for
  \(I_Z^3\). The audited positive results also have abelian-variety or
  canonical-curve hypotheses.
- **Detector guard:** S074 supplies no arbitrary-class rational detector or
  specified pairing.
- **Re-entry condition:** construct and prove an explicit comparison
  commuting with every G137 structure, for arbitrary \((X,\zeta)\).

## NG-171 - Infer profile extinction from first-jet extinction

- **Label:** NO-GO
- **Route:** use the lower equalities
  \(H^0(I_ZH^k)=H^0(I_Z^2H^k)\) from G125 and conclude \(W_k=0\).
- **Valid input:** the quotient measuring conditional first derivatives is
  zero.
- **Invalid inference:** the quotient measuring quadratic profiles is also
  zero.
- **Precise obstruction:** for the filtration
  \(T_k\subset K_k\subset J_k\), the equality \(J_k=K_k\) does not imply
  \(K_k=T_k\). The exact one-dimensional model has \(J_k=K_k=\mathbf Q\)
  and \(T_k=0\).
- **Detector guard:** a nonzero lower profile re-enters B204's decomposable
  denominator and can carry a nonzero B205 mixed cubic class.
- **Re-entry condition:** prove the second-layer vanishing in G138 by a
  global interpolation or Hilbert-function theorem while retaining the
  special degree-\(m\) birth and detector.

## NG-172 - Upgrade tangent absorption to second-osculating absorption

- **Label:** NO-GO
- **Route:** use B196/G127 or S073/Terracini to infer G139's order-two
  absorption.
- **Valid input:** the point span contains every marked tangent space, so
  \(S_Z^{(0)}=S_Z^{(1)}\).
- **Invalid inference:** it contains every marked second osculating space,
  so \(S_Z^{(2)}=S_Z^{(1)}\).
- **Precise obstruction:** the exact flag
  \(S_Z^{(0)}=S_Z^{(1)}=\mathbf Qe_0\subsetneq
  S_Z^{(2)}=\mathbf Qe_0\oplus\mathbf Qe_1\) has zero first-jet defect and
  nonzero profile defect. S073 controls tangent spans at general points,
  not second osculators at this special configuration.
- **Detector guard:** the extra order-two direction can contribute a
  decomposable mixed cubic obstruction before detector propagation.
- **Re-entry condition:** prove a second-order contact theorem for G139's
  special adjacent configuration while retaining its degree-\(m\) birth
  and detector.

## NG-173 - Use general higher Terracini theory to construct G140

- **Label:** NO-GO
- **Route:** apply S075 at general points or use maximal-rank fat-point
  interpolation and count the result as G140.
- **Valid input:** S075 computes osculating spaces of joins/secants from
  spans of osculating spaces at general points.
- **Invalid inference:** the point span absorbs all second osculators and
  realizes the adjacent increments \((0,0)\to(d,1)\).
- **Precise obstruction:** B211 requires conditional rank defects
  \(d(N-1)\) and \(\binom{d+1}{2}N-1\), whereas maximal rank gives
  increments \(dN\) and \(\binom{d+1}{2}N\). S075 also has no adjacent
  polarization comparison.
- **Detector guard:** the cited theorems supply no arbitrary-class rational
  detector or specified pairing.
- **Re-entry condition:** prove a special-point higher-contact theorem with
  B211's exact signature and every G140 detector clause.

## NG-174 - Raise the polarization with too few nodes

- **Label:** NO-GO
- **Route:** increase \(m\) while keeping \(Z_m\) fixed, bounded, or in
  the range \(N_m\le m+1\), and count positivity as G140.
- **Valid input:** \(H^m\) separates every zero-dimensional scheme of
  length at most \(m+1\).
- **Invalid inference:** the increasingly independent evaluation creates
  G140's nonzero no-coloop value relation.
- **Precise obstruction:** B212 makes evaluation on \(Z_m\) surjective
  when \(N_m\le m+1\), while lower extinction already forces
  \(m\le N_m\).
- **Detector guard:** separation supplies no rational type-\((0,0)\)
  relation, specified pairing, profile, or algebraic cycle.
- **Re-entry condition:** grow \(N_m\ge m+2\), meet B212's rank and
  support window, and retain every G141 detector clause.

## NG-175 - Ignore transport of the full-support relation

- **Label:** NO-GO
- **Route:** satisfy B212's separate degree-\(m-1\) and degree-\(m\)
  bounds and count any \(N\ge m+2\) as numerically feasible for G141.
- **Valid input:** B212 gives necessary individual Hilbert ranks.
- **Invalid inference:** the degree-\(m\) relation is independent of
  multiplication from complementary lower degrees.
- **Precise obstruction:** B213 injects \(E_a\) into
  \(E_{m-a}^{\perp}\), forcing
  \(h_Z(a)+h_Z(m-a)\le N\) and
  \(N\ge2n+1+\max\{m,2n+1\}\).
- **Detector guard:** the stronger ranks still construct no rational
  detector, profile, holonomy, or cycle.
- **Re-entry condition:** realize the actual transport maps and every
  G142 detector clause.

## NG-176 - Count lower point spans as only tangent-sized

- **Label:** NO-GO
- **Route:** search for G142 below B214's piecewise node floor by using
  only the \(2n+1\) tangent-rank lower bound.
- **Valid input:** tangent absorption is necessary in every lower degree.
- **Invalid inference:** powers \(H^k\), \(k\ge2\), do not universally
  generate the remaining quadratic jet directions.
- **Precise obstruction:** B214 generates \(1,x_i,x_ix_j\) by products of
  sections of \(H\), so lower second-osculating absorption has rank at
  least \(\binom{2n+2}{2}\). B213 then forces \(N\ge C_{2n}(m)\).
- **Detector guard:** the stronger floor supplies no central profile,
  holonomy, rational detector, specified pairing, or cycle.
- **Re-entry condition:** work inside G143's node window and retain every
  relation, profile, and detector clause.

## NG-177 - Count second osculators one point at a time

- **Label:** NO-GO
- **Route:** treat B214's pointwise floor \(C_{2n}(m)\) as the final
  universal constraint and search below \(D_{2n}(m)\).
- **Valid input:** one lower full second osculator contributes
  \(\binom{2n+2}{2}\) dimensions.
- **Invalid inference:** no universally independent family of several
  marked second osculators can be forced.
- **Precise obstruction:** B215 interpolates \(q\) triple,
  \(u\) double, and \(t\) reduced neighborhoods in degree
  \(3q+2u+t-1\), giving ranks \(L_{2n}(k)\); B213 then forces
  \(N\ge D_{2n}(m)\).
- **Detector guard:** simultaneous interpolation supplies no central
  profile, holonomy, rational detector, pairing, or cycle.
- **Re-entry condition:** work inside G144's node window with every
  relation, profile, and detector clause.

## NG-178 - Import a Togliatti system as the equality construction

- **Label:** NO-GO
- **Route:** identify B216's common-full-osculator equality with a
  Laplace equation and use a classical or monomial Togliatti example.
- **Valid input:** S077 equates specified WLP failures with a deficient
  general-point osculator on an apolar projected Veronese variety.
- **Invalid inference:** deficient dimension at one general point gives
  equality of all full second osculators at the marked nodes of arbitrary
  \((X,\zeta)\).
- **Precise obstruction:** the audited theorems concern special artinian
  ideals, projected Veronese or toric varieties, and no Hodge detector.
- **Detector guard:** no central ODP profile, rational type-\((0,0)\)
  relation, specified nonzero pairing, cycle, or general reduction occurs.
- **Re-entry condition:** prove a comparison valid for arbitrary
  \((X,\zeta)\) that yields G145 and preserves every G143-G144 clause.

## NG-179 - Use generic Gauss rigidity to kill the special fiber

- **Label:** NO-GO
- **Route:** infer from B218 that every fiber of the finite birational
  ordinary Gauss map is a singleton.
- **Valid input:** Zak tangency excludes positive-dimensional fibers;
  separable general-contact linearity makes the general fiber one point.
- **Invalid inference:** a finite birational normalization morphism is
  injective over all singular or nonnormal points of its image.
- **Precise obstruction:** S078 gives no cardinality or length bound for
  one special zero-dimensional Gauss fiber.
- **Detector guard:** generic Gauss geometry supplies no central nodal
  profile, relation, rational type, specified pairing, or cycle.
- **Re-entry condition:** prove the missing special-fiber bound under all
  G146 hypotheses, or construct the special fiber and test every clause.

## NG-180 - Promote a special hypersurface fiber to arbitrary G146

- **Label:** NO-GO
- **Route:** count B219's arbitrarily large Gauss fibers as the required
  construction for arbitrary \((X,\zeta)\).
- **Valid input:** the fiber-cardinality clause is feasible on smooth
  specially constructed hypersurfaces in every dimension at least two.
- **Invalid inference:** one may replace the fixed input \(X\) by that
  hypersurface or obtain a detector for the specified class \(\zeta\).
- **Precise obstruction:** arbitrary-input/special-family quantifier
  mismatch and absence of every class-directed detector clause.
- **Detector guard:** nodal hyperplane sections and common tangency alone
  give no rational type, full-support relation, pairing, or cycle.
- **Re-entry condition:** construct the required special fiber on every
  fixed \(X\) and retain all G146 profile and detector data.

## NG-181 - Create the equality fiber by raising polarization powers

- **Label:** NO-GO
- **Route:** replace a very ample A by large powers \(A^k\) and search
  asymptotically for G146's common-tangent fiber.
- **Valid input:** higher powers improve section and jet separation.
- **Invalid inference:** this produces coincident tangent spaces.
- **Precise obstruction:** B220 gives an \(A^k\)-section with zero first
  jet at \(p\) and nonzero value at \(q\) for every \(p\ne q\), so the
  Gauss map is injective for all \(k\ge2\).
- **Detector guard:** only G145-G147's equality branch is excluded;
  G144's slack range and the terminal Hodge problem remain open.
- **Re-entry condition:** B221/NG182 subsequently close the G147 escape;
  leave equality and return to G148's strict-slack branch.

## NG-182 - Universalize the extremal equality fiber

- **Label:** NO-GO
- **Route:** realize the complete G145-G147 equality package for every
  arbitrary \((X,\zeta)\) by finding an exceptional very ample
  polarization with a \(D_{2n}(m)\)-point Gauss fiber.
- **Valid input:** equality would force the common tangent plane and
  Gauss fiber by B216-B217.
- **Invalid inference:** every legitimate input admits any nontrivial
  Gauss fiber after a suitable choice of polarization.
- **Precise obstruction:** B221 takes the smooth even quadric and the
  nonzero primitive ruling difference \(a-b\). Its Picard group is
  generated by \(O(1)\); polarity makes the \(O(1)\)-Gauss map injective,
  and B220 makes every \(O(k)\)-Gauss map injective for \(k\ge2\).
- **Detector guard:** the class is algebraic only to certify a valid
  input to the failed universal mechanism. No conclusion about an
  unknown Hodge class or the Hodge Conjecture follows.
- **Re-entry condition:** use G148 and construct the full G144 package in
  the strict-slack range \(N>D_{2n}(m)\).

## NG-183 - Treat injective Gauss plus one slack node as construction

- **Label:** NO-GO
- **Route:** choose \(H=A^2\), use B220's injective Gauss map, set
  \(N=D_{2n}(m)+1\), and declare G149 realized.
- **Valid input:** B222 forces degree-two excess one, complementary
  excess zero, and two transport isomorphisms for any existing candidate.
- **Invalid inference:** those necessary ranks produce the point scheme,
  central ODP system, or detector.
- **Precise obstruction:** the simultaneous \(Z,2Z,3Z\) restriction
  signature, nondegenerate quadratic profile, holonomy, finite Kuranishi
  closure, rational full-support relation, and nonzero specified pairing
  all remain unconstructed.
- **Detector guard:** a one-dimensional complex rank excess is not a
  rational type-\((0,0)\) vanishing-cycle class or an algebraic cycle.
- **Re-entry condition:** prove the complete existence statement G149.

## NG-184 - Import complete-intersection residue duality as G150

- **Label:** NO-GO
- **Route:** cut \(Z\) transversely by divisors in powers of \(H\) and
  use Cayley–Bacharach/residue duality to assert
  \(E_{m-2}=E_2^{\perp_\lambda}\).
- **Valid input:** S070 gives a fixed complementary-degree theorem for
  projective complete intersections, and their Gorenstein trace is perfect.
- **Invalid inference:** the complementary twist can be prescribed as
  \(H^{m-2}\) independently of the canonical bundle and cutting divisors.
- **Precise obstruction:** B224 computes the actual twist as
  \(\omega_X\otimes H^{\sum e_i-2}\). Matching requires
  \(\omega_X\otimes H^{\sum e_i-m}\simeq O_X\), which fails for
  \(X=\mathbf P^n\times\mathbf P^n\), \(H=O(2,4)\).
- **Detector guard:** twist matching alone would still supply neither
  second-osculator absorption nor doubled/tripled jets, ODP Hessians,
  rational Hodge type, or the specified pairing.
- **Re-entry condition:** construct G150 by a non-complete-intersection
  scheme or a proved twist correction preserving every detector clause.

## NG-185 - Import an abstract self-associated set as G151

- **Label:** NO-GO
- **Route:** use S082's two-orthogonal-bases construction in a free
  \(\mathbf P^{c_{2n}}\) and count its \(2c_{2n}+2\) points as G151.
- **Valid input:** the resulting evaluation matrix has exactly B225's
  diagonal self-duality.
- **Invalid inference:** an abstract projective configuration lies on
  the fixed \(H^2(X)\)-image and satisfies its marked osculator incidence.
- **Precise obstruction:** S082 contains no solution of
  \(p_i\in X\) and
  \(\widehat O^{(2)}_{p_i}(H^2)\subset S_{2,Z}^{(0)}\) for arbitrary X.
  Its Theorem 7.3 additionally requires a one-condition quadratic defect
  to promote self-association to arithmetic Gorensteinness.
- **Detector guard:** orthogonal bases and Gorenstein coordinate rings
  provide no ODP Hessians, rational type-\((0,0)\) vanishing-cycle
  relation, specified pairing, or algebraic cycle.
- **Re-entry condition:** construct the full fixed-X degree-five
  self-associated osculator package stated in G151.

## NG-186 - Raise the primitive polarization to reach first slack

- **Label:** NO-GO
- **Route:** replace a primitive very ample bundle by powers and search
  for the G149-G151 first-slack configuration.
- **Valid input:** powers preserve primitivity up to a nonzero scalar
  Lefschetz operator and improve jet separation.
- **Invalid inference:** improved separation creates the necessary
  osculator collision.
- **Precise obstruction:** B226 requires every pair to fail
  \(A^4\)-interpolation on \(3p\sqcup3q\). If \(A=B^\ell\),
  \(\ell\ge2\), B215 gives surjectivity for every pair.
- **Universal witness:** on
  \(\mathbf P^n\times\mathbf P^n\), \(B=O(1,1)\) has a nonzero rational
  algebraic primitive middle class, and \(A=B^2\) is a valid fixed
  primitive polarization with empty defect locus.
- **Detector guard:** this closes only the fixed-A subbranches
  G149-G151, not G148, G152, or HC.
- **Re-entry condition:** B228/NG187 close first slack, B230 closes
  every layer through nine, and B231 later forces dimension-scaled slack;
  move to G155.

## NG-187 - Use an exceptional polarization to rescue first slack

- **Label:** NO-GO
- **Route:** after powers erase the two-triple defect locus, choose a
  low exceptional polarization separately on every primitive target.
- **Valid correction:** B226 proves that any first-slack candidate must
  use such an exceptional embedding.
- **Invalid inference:** every primitive target possesses one whose
  defect clique has the required point rank.
- **Precise obstruction:** B228 exhausts the valid input
  \((Q^4,a-b)\). Every \(O_Q(k)\), \(k\ge2\), has empty defect locus.
  For \(O_Q(1)\), B227 makes every defect chord a line on \(Q\), so a
  clique lies in an isotropic \(\mathbf P^2\); its quartic rank is at
  most 15 rather than 16.
- **Detector guard:** the known algebraic class \(a-b\) only certifies
  the universal test input. The argument proves neither algebraicity
  nor nonalgebraicity of any unknown Hodge class.
- **Conclusion:** G149-G152's first-slack specialization is closed,
  while G148 and HC remain open.
- **Re-entry condition:** B230 closes every layer through nine and B231
  later closes every fixed bound; move to G155's dimension-scaled threshold.

## NG-188 - Realize the universal gate with slack at most nine

- **Label:** NO-GO
- **Route:** keep the excess \(s=N-D_{2n}(m)\) uniformly small while
  varying the degree and polarization.
- **Valid premise:** positive slack avoids the exact equality
  Gauss-fiber obstruction.
- **Invalid inference:** one of the first nine layers must work on
  every primitive target.
- **Precise obstruction:** B230 exhausts every degree on
  \((Q^4,a-b)\). For \(m=2,s\le9\), two double jets cannot fit
  independently in the point span; for \(m\ge3,s\le14\), the analogous
  statement holds for two triple jets. Quadric defect chords force an
  isotropic plane, contradicting full tangent absorption or quartic rank.
- **Detector guard:** the argument constructs no ODP profile, rational
  relation, specified pairing, algebraic cycle, proof, or disproof of HC.
- **Conclusion:** every degree is excluded through slack nine. The
  stronger \(m\ge3\) exclusion persists through slack fourteen.
- **Re-entry condition:** G154 was the first signature not excluded by
  \(Q^4\), but B231 later falsifies its dimension-independent slack.
  Move to G155 with \(s=2d+2\).

## NG-189 - Realize the universal gate with a dimension-independent slack

- **Label:** NO-GO
- **Route:** fix a finite \(S\) and seek a G148 construction with
  \(s=N-D_{2n}(m)\le S\) in every even dimension.
- **Valid premise:** strict slack avoids equality saturation and may be
  chosen separately from the degree and polarization.
- **Invalid inference:** the excess can remain bounded while the dimension
  and local jet lengths grow.
- **Precise obstruction:** B231 proves on the valid input \(Q^d\) that
  \(m=2\) requires \(s\ge2d+2\), while \(m\ge3\) requires
  \(s\ge\binom{d+2}{2}\). Choosing even \(d\) with \(S<2d+2\) excludes
  every degree and every \(O_Q(k)\).
- **Geometric mechanism:** below the thresholds every marked pair is
  double- or triple-jet defective. Powered polarizations separate those
  jets. Under \(O_Q(1)\), the chords confine the marked points to a totally
  isotropic \(W\), but the required tangent or second osculator contains a
  tensor outside \(\operatorname{Sym}^2W\) or \(\operatorname{Sym}^4W\).
- **Detector guard:** the known algebraic ruling difference only certifies
  the test input. No unknown Hodge class, rational detector, specified
  pairing, cycle, proof, or disproof of HC is obtained.
- **Conclusion:** G154 and every fixed finite slack specialization are
  closed. G148 and HC remain open.
- **Re-entry condition:** dimension-scaled slack is necessary, but B232
  later excludes the first two such layers. Move to G156.

## NG-190 - Treat the first dimension-scaled floor as realizable

- **Label:** NO-GO
- **Route:** set \(m=2,s=2d+2,\delta_1=d+1\), so two tangent jet
  spaces have exactly the dimension of the point span.
- **Valid premise:** the B231 pairwise direct-sum inequality is no longer
  violated at equality.
- **Invalid inference:** equality leaves enough room for the remaining
  \(N-2\) marked points.
- **Precise obstruction:** B232 proves that powered polarizations separate
  two doubles and a third point. Under \(O_Q(1)\), an all-defective set is
  isotropically impossible; a nonorthogonal pair has disjoint tangent
  osculators that fill the entire span, whose symmetric-square
  decomposition contains only the two original quadric points.
- **Odd-layer guard:** at \(s=2d+3\), the integral budget still has
  \(\delta_1\le d+1\), so the same obstruction applies.
- **Detector guard:** no ODP profile, rational relation, specified pairing,
  algebraic cycle, proof, or disproof of HC is produced.
- **Conclusion:** G155 and both slack layers \(2d+2,2d+3\) are closed.
  G148 and HC remain open.
- **Re-entry condition:** G156 begins at the next balanced signature, but
  B233 later excludes it and its adjacent odd layer. Move to G157.

## NG-191 - Realize the gate with one extra tangent-span dimension

- **Label:** NO-GO
- **Route:** set \(m=2,s=2d+4,\delta_1=d+2\), giving a point span one
  dimension larger than two independent tangent osculators.
- **Valid premise:** the exact boundary obstruction of B232 no longer
  applies verbatim.
- **Invalid inference:** the single quotient dimension can absorb all
  remaining tangent spaces or quartic points.
- **Standard-polarization obstruction:** after choosing a nonorthogonal
  pair, a third tangent osculator maps to a subspace of dimension at least
  \(d-1\) modulo the first two, contradicting the one-dimensional quotient.
- **Square-polarization obstruction:** two doubles plus a point fill the
  proposed \(O_Q(4)\) span. Products of four ambient hyperplanes separate
  every fourth point unless all four are collinear. Hence all marked points
  would lie on a quadric line and have rank at most five.
- **Higher-power obstruction:** B215 separates two doubles plus two points
  for every \(O_Q(k)\), \(k\ge3\), exceeding the proposed span.
- **Odd-layer guard:** \(s=2d+5\) has the same integral rank budget and is
  excluded identically.
- **Detector guard:** no ODP package, rational relation, specified pairing,
  algebraic cycle, proof, or disproof of HC is produced.
- **Conclusion:** G156 and both layers \(2d+4,2d+5\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B234 later excludes G157 and its odd neighbor;
  move to G158.

## NG-192 - Realize the gate with two extra tangent-span dimensions

- **Label:** NO-GO
- **Route:** set \(m=2,s=2d+6,\delta_1=d+3\), leaving a
  two-dimensional quotient beyond two tangent osculators.
- **Valid premise:** this escapes B233's one-dimensional quotient bound.
- **Invalid inference:** two quotient dimensions suffice for the third
  tangent osculator or for the square-polarization point set.
- **Standard-polarization obstruction:** the third tangent quotient has
  rank at least \(d-1\ge3\).
- **Square-polarization obstruction:** four noncollinear base points fill
  the span. Every fifth dependent point must lie on a line containing
  three base points; all remaining points lie on the unique such line.
  The resulting line-plus-one-point set has quartic rank at most six.
- **Higher-power obstruction:** B233's mixed interpolation excludes these
  polarizations throughout the displayed rank band.
- **Odd-layer guard:** the integral budget is unchanged at \(s=2d+7\).
- **Detector guard:** no ODP package, rational detector, specified pairing,
  algebraic cycle, proof, or disproof of HC is produced.
- **Conclusion:** G157 and both layers \(2d+6,2d+7\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B235 later replaces the additive ladder by the
  slope-four floor; move to G159.

## NG-193 - Realize the gate below the slope-four degree-two floor

- **Label:** NO-GO
- **Route:** continue adding a dimension-independent number of span
  dimensions beyond two tangent osculators while keeping \(s<4d\).
- **Valid premise:** each two slack layers add one dimension to the
  degree-one point span.
- **Invalid inference:** a fixed additive excess can absorb the third
  tangent osculator uniformly as \(d\) grows.
- **Standard-polarization obstruction:** B235 gives two independent
  tangent osculators of total dimension \(2d+2\), plus a third quotient
  contribution of at least \(d-1\). Thus \(h_Z(1)\ge3d+1\) and
  \(s\ge4d\).
- **Other-polarization obstruction:** coordinate quartics separate three
  noncollinear double points for \(O_Q(2)\); B215 separates three doubles
  for every \(O_Q(k)\), \(k\ge3\). These cases require \(s\ge4d+4\).
- **G158 guard:** \(2d+8<4d\) for every even \(d\ge6\), providing a valid
  universal-quantifier falsifier.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is obtained.
- **Conclusion:** G158 and every sub-\(4d\) degree-two specialization are
  closed. G148 and HC remain open.
- **Re-entry condition:** B236 later excludes the exact boundary and its
  odd neighbor; move to G160.

## NG-194 - Realize the exact slope-four boundary

- **Label:** NO-GO
- **Route:** set \(m=2,s=4d,\delta_1=2d\), saturating B235.
- **Valid premise:** the available quotient has exactly the minimum
  \(d-1\) dimensions contributed by a third tangent osculator.
- **Invalid inference:** equality can absorb a fourth marked tangent.
- **Precise obstruction:** B236 forces the third point to be orthogonal to
  the initial nonorthogonal pair, making the three tangent osculators fill
  the entire span. A second hyperbolic decomposition confines every fourth
  point candidate to one of two isotropic lines, but an explicit tangent
  vector has the nonzero complementary component \(rr'-vw\).
- **Odd-layer guard:** \(s=4d+1\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  algebraic cycle, proof, or disproof of HC is obtained.
- **Conclusion:** G159 and both layers \(4d,4d+1\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B237 later excludes G160 and its odd neighbor;
  move to G161.

## NG-195 - Realize the post-slope-four rank

- **Label:** NO-GO
- **Route:** set \(m=2,s=4d+2,\delta_1=2d+1\), adding one dimension
  after B236.
- **Valid premise:** a third point meeting the initial hyperbolic plane now
  fills exactly the available quotient.
- **Invalid inference:** the associated contact locus has enough point rank.
- **Nonorthogonal-third obstruction:** self-adjoint annihilator duality
  identifies the complete tangential contact locus with one plane conic,
  whose \(O(2)\) point rank is at most five.
- **Orthogonal-residual obstruction:** if every other point lies in the
  orthogonal complement, its \(d\)-dimensional quotient cannot contain two
  nonorthogonal \((d-1)\)-dimensional tangents. Pairwise orthogonality then
  contradicts full tangent absorption.
- **Odd-layer guard:** \(s=4d+3\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G160 and both layers \(4d+2,4d+3\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B238 later excludes the exact three-double
  boundary; move to G162.

## NG-196 - Realize the exact three-double boundary

- **Label:** NO-GO
- **Route:** set \(m=2,s=4d+4,\delta_1=2d+2\), so three independent
  tangent osculators exactly fill the point span.
- **Valid premise:** standard, square, and higher quadric polarizations all
  satisfy the preceding necessary floors.
- **Invalid inference:** the filled span can contain a fourth marked point
  or tangent.
- **Higher-power obstruction:** B215 separates three doubles plus one
  reduced point at exponent six.
- **Square-polarization obstruction:** products of four hyperplanes
  separate a fourth point from three noncollinear doubles; the collinear
  alternative has point rank at most five.
- **Standard-polarization obstruction:** outside the plane contact conic,
  a fourth tangent contributes at least \(d-2\ge2\) quotient dimensions,
  while only one is available.
- **Odd-layer guard:** \(s=4d+5\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G161 and both layers \(4d+4,4d+5\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B239 later excludes G162 and its odd neighbor;
  move to G163.

## NG-197 - Realize one dimension beyond three doubles

- **Label:** NO-GO
- **Route:** set \(m=2,s=4d+6,\delta_1=2d+3\), adding one point-span
  dimension after the exact three-double boundary.
- **Valid premise:** at exponent six, three doubles plus one point fill
  the available span.
- **Invalid inference:** a fifth marked tangent can remain absorbed.
- **Higher-power obstruction:** six hyperplane factors separate the fifth
  point from three doubles and one reduced point.
- **Square-polarization obstruction:** the only residual quartic base locus
  is a pair line containing the fourth point; an explicit quartic has a
  nonzero transverse first jet at every further point of that line.
- **Standard-polarization obstruction:** quotient ranks exclude dimensions
  at least six. The exceptional \(Q^4\) self-adjoint annihilator has common
  isotropic eigenvectors only on the initial plane conic and at one extra
  point, of point rank at most six.
- **Odd-layer guard:** \(s=4d+7\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G162 and both layers \(4d+6,4d+7\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** B240 later excludes G163 and its odd neighbor;
  move to G164.

## NG-198 - Realize two dimensions beyond three doubles

- **Label:** NO-GO
- **Route:** set \(m=2,s=4d+8,\delta_1=2d+4\), allowing two point-span
  dimensions beyond three tangent osculators.
- **Valid premise:** at exponent six, three doubles plus two points fill
  the available span.
- **Invalid inference:** a sixth marked tangent can remain absorbed.
- **Higher-power obstruction:** two triangle-edge factors and four
  single-support factors give a sextic sixth-point separator.
- **Square-polarization obstruction:** after choosing the fourth point off
  the triangle, every sixth point admits either a quartic value separator
  or a quartic with one nonzero transverse first jet.
- **Standard-polarization obstruction:** quotient ranks exclude dimensions
  at least six. On \(Q^4\), every surviving annihilator is
  \(\operatorname{Sym}^2K\), and the contact locus lies in a quadric
  \(\mathbf P^3\)-section of point rank at most nine.
- **Odd-layer guard:** \(s=4d+9\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G163 and both layers \(4d+8,4d+9\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** G164 begins at
  \(s=4d+10,\delta_1=2d+5\).

## NG-199 - Use a higher or standard polarization at G164

- **Label:** NO-GO
- **Route:** retain \(O_Q(k\ge3)\), or use \(O_Q(1)\) uniformly in
  dimensions at least six.
- **Valid premise:** G164 has three point-span dimensions beyond the
  three tangent osculators.
- **Invalid inference:** those dimensions absorb every later marked
  tangent for one of these polarizations.
- **Higher-power obstruction:** a six-factor construction gives a value
  or transverse first-jet separator at the seventh point.
- **Standard obstruction:** quotient ranks close every \(d\ge8\). In
  \(d=6\), residual equality contains no third point, and the other branch
  has contact locus only one plane conic plus one point.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G164's necessary quadric test survives only through
  \(O_Q(2)\) for \(d\ge6\), and through \(O_Q(1)\) or \(O_Q(2)\) for
  \(d=4\). The floor remains \(s=4d+10\); G164 and HC remain open.
- **Re-entry condition:** B242 later excludes the square branch; use the
  valid \(Q^6\) input to close G164 and move to G166.

## NG-200 - Use the square polarization to survive G164

- **Label:** NO-GO
- **Route:** use \(A=O_Q(2)\) after B241 removes every other
  higher-dimensional quadric polarization.
- **Valid premise:** three doubles plus three values fit the G164 span.
- **Invalid inference:** every later marked tangent remains absorbed.
- **Base-locus obstruction:** after choosing one point off the triangle,
  the residual quartic value base locus lies on at most two lines, whose
  point rank is too small.
- **First-jet obstruction:** a sixth point outside that locus fills the
  span; four hyperplanes give a value or transverse first-jet separator
  at every seventh point.
- **Universal-quantifier guard:** on \(Q^6\), B241 leaves no other
  polarization. The unresolved standard \(Q^4\) special case cannot
  rescue a claim required for every input.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G164, G165, and both layers \(4d+10,4d+11\) are closed.
  G148 and HC remain open.
- **Re-entry condition:** G166 begins at
  \(s=4d+12,\delta_1=2d+6,N=6d+14,h_Z(1)=3d+7\).

## NG-201 - Survive G166 through a quadric polarization

- **Label:** NO-GO
- **Route:** choose some very ample \(A=O_Q(k)\) at the G166 rank.
- **Valid premise:** G166 leaves one dimension beyond B242's
  six-support square span.
- **Invalid inference:** that one dimension absorbs the next full tangent
  osculator for some polarization.
- **Powered obstruction:** B215 excludes \(k\ge4\) using four doubles.
  For \(k=3\), a point off the three-line triangle supplies all residual
  first jets in dimensions at least six.
- **Square obstruction:** the residual quartic system restricts to every
  next double neighborhood with rank at least \(d-2\ge2\).
- **Standard obstruction:** for \(d\ge8\), residual tangent pairs exceed
  the \(d+5\) quotient, while a tangent outside the three-point plane
  contributes at least \(d-2>5\).
- **Universal-quantifier guard:** \(Q^8\) is a valid input and every
  \(k\ge1\) fails there. No special-family success is promoted to a
  general theorem.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G166 and both layers \(4d+12,4d+13\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G167 begins at
  \(s=4d+14,\delta_1=2d+7,N=6d+16,h_Z(1)=3d+8\).

## NG-202 - Survive below the slope-six quadric floor

- **Label:** NO-GO
- **Route:** continue through G167 or any fixed additive extension of the
  slope-four degree-two branch.
- **Valid premise:** each two slack units add one balanced point-span
  dimension.
- **Invalid inference:** finitely many such dimensions absorb a fourth
  tangent block as the quadric dimension grows.
- **Nonstandard obstruction:** every \(O_Q(k\ge2)\) candidate has point
  rank at least \(4d+4\), hence slack at least \(6d+6\).
- **Standard obstruction:** point rank is at least \(4d\); at equality,
  the residual quotient contains only two points or the contact locus is
  one plane conic plus one point.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), forces
  \(s\ge6d\). Success in another special family would not reduce the
  general problem.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G167 and every layer \(s\le6d-1\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** G168 begins at
  \(s=6d,\delta_1=3d,N=8d+2,h_Z(1)=4d+1\).

## NG-203 - Survive the standard slope-six boundary

- **Label:** NO-GO
- **Route:** use the only remaining \(A=O_Q(1)\) polarization at
  \(h_Z(1)=4d+1\).
- **Valid premise:** one point-span dimension remains beyond B244's
  standard equality obstruction.
- **Invalid inference:** it absorbs a third residual tangent or a point
  outside the conic-plus-point contact locus.
- **Residual obstruction:** on the smaller quadric \(Q(U)\), a third
  residual tangent contributes at least \(d-3>1\).
- **Contact obstruction:** every other possible rank-one continuation
  leaves annihilator \(\operatorname{Sym}^2K\), whose common contact
  locus lies in a projective three-space of point rank at most ten.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. Special-family success elsewhere cannot rescue G168.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G168 and both layers \(6d,6d+1\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** G169 begins at
  \(s=6d+2,\delta_1=3d+1,N=8d+4,h_Z(1)=4d+2\).

## NG-204 - Continue the fixed-additive standard slope-six branch

- **Label:** NO-GO
- **Route:** retain \(A=O_Q(1)\) through G169 and later fixed additive
  slope-six layers.
- **Valid premise:** each balanced layer supplies another point-span
  dimension.
- **Invalid inference:** finitely many such dimensions absorb the third
  residual tangent or the next escape from \(K^\perp\).
- **Residual obstruction:** three residual tangent blocks force total
  point rank at least \(5d-3\).
- **Contact obstruction:** each required escape from the
  projective-three-space contact locus costs at least \(d-3\).
- **Common-floor guard:** B244 separately gives
  \(h_Z(1)\ge4d+4\) for every nonstandard polarization, so all
  polarizations require \(s\ge6d+6\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G169 and every layer \(6d+2,\ldots,6d+5\) are closed.
  G148 and HC remain open.
- **Re-entry condition:** G170 begins at
  \(s=6d+6,\delta_1=3d+3,N=8d+8,h_Z(1)=4d+4\), with only nonstandard
  quadric polarizations surviving the rank test.

## NG-205 - Survive the exact nonstandard six-plus-six boundary

- **Label:** NO-GO
- **Route:** attain B244's exact nonstandard floor
  \(h_Z(1)=4d+4\) and absorb every marked tangent osculator.
- **Valid premise:** for \(k=2,3\), four double neighborhoods can fill
  exactly the allowed span.
- **Invalid inference:** that full span can absorb any fifth marked
  point.
- **Quartic/sextic obstruction:** the good pair-line graph relative to
  the fifth point contains a four-cycle. Its four hyperplanes give a
  quartic vanishing twice at the first four points and nonzero at the
  fifth; two unit factors give the sextic separator.
- **Higher-power obstruction:** B215 separates four doubles and one
  reduced point in exponent eight, forcing rank \(4d+5\) for \(k\ge4\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G170 and both layers \(6d+6,6d+7\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G171 begins at
  \(s=6d+8,\delta_1=3d+4,N=8d+10,h_Z(1)=4d+5\).

## NG-206 - Continue with any fixed additive degree-two excess

- **Label:** NO-GO
- **Route:** use \(h_Z(1)=4d+4+j\) with one fixed \(j\) while the
  quadric dimension grows.
- **Valid premise:** every two additional slack units allow one more
  balanced code dimension.
- **Invalid inference:** a fixed number of extra dimensions absorbs
  arbitrarily many marked evaluations uniformly in \(d\).
- **High-power obstruction:** \(2k\ge8+j\) lets B215 separate four
  doubles and \(j+1\) simple points, one condition beyond the budget.
- **Bounded-power obstruction:** \(2k\le j+7\) bounds the point rank of
  every intermediate support span by
  \(\binom{2j+10}{j+3}\). In sufficiently large even dimension a new
  marked point escapes that span, and the square of a containing
  hyperplane separates it.
- **Standard obstruction:** B246 requires \(j\ge d-7\).
- **Universal-quantifier guard:** for every fixed \(j\), an explicitly
  bounded sufficiently large even quadric is a valid falsifying input.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G171 and every fixed-additive \(m=2\) continuation
  are closed. G148 and HC remain open.
- **Re-entry condition:** G172 permits \(j=j(X,\zeta)\) to grow with
  dimension and retains every ODP, Kuranishi, rationality, and pairing
  clause.

## NG-207 - Survive below the slope-eight degree-two floor

- **Label:** NO-GO
- **Route:** let G172's excess grow, but keep the balanced slack below
  \(8d-8\).
- **Valid premise:** B248 forced only unbounded excess and did not
  quantify its optimal growth.
- **Invalid inference:** sublinear growth can absorb the next marked
  tangent osculator.
- **Square obstruction:** varying one hyperplane of B247's good
  four-cycle gives at least \(d-1\) residual jets at the fifth point,
  forcing \(h_Z(1)\ge5d+3\).
- **Higher-power obstruction:** the fixed four-cycle quartic is a unit
  at the fifth point, so multiplication by \(O_Q(2k-4)\) supplies all
  \(d+1\) jets and forces \(h_Z(1)\ge5d+5\).
- **Standard obstruction:** B246 forces \(h_Z(1)\ge5d-3\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** every \(m=2\) layer below \(s=8d-8\) is closed. G148
  and HC remain open.
- **Re-entry condition:** G173 begins at
  \(s=8d-8,\delta_1=4d-4,N=10d-6,h_Z(1)=5d-3\), with only the
  standard quadric polarization surviving the rank test.

## NG-208 - Survive the standard slope-eight equality

- **Label:** NO-GO
- **Route:** attain B249's equality \(h_Z(1)=5d-3\) with the standard
  quadratic embedding.
- **Valid premise:** B246's tangent-rank lower bound allows equality.
- **Invalid inference:** either minimal branch can absorb all remaining
  marked tangents.
- **Residual obstruction:** when all residual points lie in
  \(U=\langle v,w\rangle^\perp\), the quotient has the impossible B236
  boundary rank \(3(d-2)+1\) on \(Q(U)\).
- **Mixed obstruction:** all cases except \(t,u\in W\) with
  \(u\in K\setminus K^\perp\) already force rank at least \(5d-2\).
- **Contact obstruction:** in the last case,
  \(J=K\cap u^\perp\) has dimension \(d-3\), and every rank-one
  \(E_z\), \(z\in J\), remains in the annihilator. Common contact lies
  in \(\mathbf P(J^\perp)\simeq\mathbf P^4\), whose quadratic point
  rank is at most fifteen.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G173 and both layers \(8d-8,8d-7\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G174 begins at
  \(s=8d-6,\delta_1=4d-3,N=10d-4,h_Z(1)=5d-2\).

## NG-209 - Survive one rank beyond standard slope-eight equality

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d-2\) with the standard quadratic
  embedding.
- **Valid premise:** one extra dimension reopens several minimal
  branches from B250.
- **Invalid inference:** a reopened branch absorbs every later marked
  tangent.
- **Residual obstruction:** the orthogonal residual quotient has the
  impossible B237 rank \(3(d-2)+2\) on \(Q^{d-2}\).
- **Filled-branch obstruction:** every branch that fills the budget
  retains rank-one annihilators indexed by a \((d-3)\)-space \(J\);
  contact remains inside \(\mathbf P(J^\perp)\simeq\mathbf P^4\).
- **Last-dimension obstruction:** if one dimension remains, a marked
  point outside \(J^\perp\) contributes at least \(d-4>1\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G174 and both layers \(8d-6,8d-5\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G175 begins at
  \(s=8d-4,\delta_1=4d-2,N=10d-2,h_Z(1)=5d-1\).

## NG-210 - Survive two ranks beyond standard slope-eight equality

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d-1\) with the standard quadratic
  embedding.
- **Valid premise:** two extra dimensions reopen B251's minimal mixed
  branches and put the residual quotient at \(3(d-2)+3\).
- **Invalid inference:** those reopened branches absorb every later
  marked tangent.
- **Residual obstruction:** for even \(d\ge10\), the residual rank is
  below B246's standard floor \(5(d-2)-3\) on \(Q^{d-2}\).
- **Filled-branch obstruction:** every filled branch retains rank-one
  annihilators indexed by a \((d-3)\)-space \(J\), so contact remains
  in \(\mathbf P(J^\perp)\simeq\mathbf P^4\).
- **Residual-budget obstruction:** if one or two dimensions remain, a
  point outside \(J^\perp\) contributes at least \(d-4>2\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge10\), is a
  valid input, and one such input falsifies G175's universal claim. No
  special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G175 and both layers \(8d-4,8d-3\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G176 begins at
  \(s=8d-2,\delta_1=4d-1,N=10d,h_Z(1)=5d\).

## NG-211 - Survive the standard parametric band

- **Label:** NO-GO
- **Route:** continue the standard polarization through
  \(h_Z(1)=5d-1+q\), \(0\le q\le d-7\).
- **Valid premise:** the last mixed quotient grows with \(q\).
- **Invalid inference:** it reaches the next tangent before the square
  polarization re-enters.
- **Residual obstruction:** the residual budget is at most
  \(4d-10<5d-13\), below B246 on \(Q^{d-2}\).
- **Mixed obstruction:** the worst remaining budget is
  \(q+2\le d-5<d-4\), while \(\operatorname{Sym}^2J\) forces at least
  \(d-4\) dimensions from the next tangent.
- **Common-floor consequence:** B249 and B253 give
  \(h_Z(1)\ge5d+3\) and \(s\ge8d+4\) for every polarization.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge10\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G176-G178 and every layer through \(s=8d+3\) are
  closed. G148 and HC remain open.
- **Re-entry condition:** G179 begins at
  \(s=8d+4,\delta_1=4d+2,N=10d+6,h_Z(1)=5d+3\); only
  \(A=O_Q(2)\) survives on even quadrics \(d\ge12\).

## NG-212 - Survive the square five-double boundary

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d+3\) with \(A=O_Q(2)\).
- **Valid premise:** B249 exhibited only \(d-1\) residual jets after
  four independent doubles.
- **Invalid inference:** the full quartic system cannot supply the two
  missing jets or another complete double block.
- **First span escape:** quartic point rank on \(\mathbf P^3\) is at
  most \(35<5d+3\), forcing a fifth point outside.
- **Second span escape:** quartic point rank on \(\mathbf P^4\) is at
  most \(70<5d+3\) for \(d\ge14\), forcing a sixth point outside.
- **Separator:** at each escape, a hyperplane square times
  \(H^0(O_Q(2))\) vanishes on all preceding doubles and supplies all
  \(d+1\) jets at the new point.
- **Square-floor consequence:** \(h_Z(1)\ge6d+6\).
- **Common-floor consequence:** B249, B253, and B254 give
  \(h_Z(1)\ge5d+5\) and \(s\ge8d+8\) for every polarization.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G179-G180 and every layer through \(s=8d+7\) are
  closed. G148 and HC remain open.
- **Re-entry condition:** G181 begins at
  \(s=8d+8,\delta_1=4d+4,N=10d+10,h_Z(1)=5d+5\), with only
  \(A=O_Q(k)\), \(k\ge3\), surviving.

## NG-213 - Survive the higher-power five-double equality

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d+5\) with \(A=O_Q(k)\), \(k\ge3\).
- **Valid premise:** B249 proves five independent double neighborhoods,
  exactly filling the proposed equality budget.
- **Invalid inference:** every later marked point can remain in that span.
- **Combinatorial obstruction:** relative to a sixth point, the five
  supports form line-through-point classes of size at most three. Six
  good pair edges cover every support at least twice.
- **Separator:** the product of the six pair-line hyperplanes vanishes on
  all five doubles and is a unit at the sixth point.
- **Cubic consequence:** equality fails for \(k=3\), so
  \(h_Z(1)\ge5d+6\).
- **Higher-power consequence:** for \(k\ge4\), the residual complete
  system supplies the whole sixth double block, so
  \(h_Z(1)\ge6d+6\).
- **Common-floor consequence:** B253-B255 give
  \(h_Z(1)\ge5d+6\) and \(s\ge8d+10\) for every polarization.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G181 and the layers \(s=8d+8,8d+9\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G182 begins at
  \(s=8d+10,\delta_1=4d+5,N=10d+12,h_Z(1)=5d+6\), with only
  \(A=O_Q(3)\) surviving at equality.

## NG-214 - Survive the cubic branch below six double blocks

- **Label:** NO-GO
- **Route:** retain \(A=O_Q(3)\) below \(h_Z(1)=6d+6\).
- **Valid premise:** B255's sextic separator supplied only one reduced
  sixth-point value at the first cubic equality.
- **Invalid inference:** every later marked point can force a
  three-element line-through-point class.
- **Hard-locus obstruction:** every such point lies on a line containing
  \(p_5\) and two of the first four supports. Those pair edges form a
  matching, hence determine at most two lines.
- **Point-rank obstruction:** the hard locus together with \(P_5\) has
  sextic point rank at most fourteen, below \(5d+5\).
- **Separator:** outside the hard locus, the good graph has a spanning
  five-cycle. Its quintic hyperplane product times \(H^0(O_Q(1))\)
  supplies the complete sixth double neighborhood.
- **Cubic-floor consequence:** \(h_Z(1)\ge6d+6\).
- **Common-floor consequence:** B253-B256 give
  \(h_Z(1)\ge6d-7\) and \(s\ge10d-16\) for every polarization.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G182 and every layer through \(s=10d-17\) are closed.
  G148 and HC remain open.
- **Re-entry condition:** G183 begins at
  \(s=10d-16,\delta_1=5d-8,N=12d-14,h_Z(1)=6d-7\), with only
  \(A=O_Q(1)\) surviving at equality.
