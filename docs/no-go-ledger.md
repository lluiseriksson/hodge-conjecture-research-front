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
