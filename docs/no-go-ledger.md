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
