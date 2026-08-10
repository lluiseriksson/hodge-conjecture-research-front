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
  mechanism. The active G031 gate requires the geometrically necessary
  condition \(\langle\zeta,\Phi_{Y_p}(\beta)\rangle\ne0\).

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
