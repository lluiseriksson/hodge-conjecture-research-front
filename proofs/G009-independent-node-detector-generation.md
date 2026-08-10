---
brick_id: G009
status: EXPLORATORY
base_field: C
variety: arbitrary polarized smooth projective X of dimension 2n and all nodal hyperplane members in sufficiently high powers whose nodes impose independent linear-system conditions
smoothness: X is smooth; detector members have only ordinary double points and their Severi strata are smooth under the independent-node hypothesis
projectivity: X is projective and L is ample, with members taken in very ample powers mL
dimension: dim X = 2n; detector fibers have dimension 2n-1
codimension: middle codimension n; an r-node independent Severi stratum has parameter-space codimension r
coefficient_field: Q
cohomology_theory: primitive singular Betti homology/cohomology, intersection cohomology, perverse sheaves, monodromy, and vanishing-cycle mixed Hodge structures
hodge_type: primitive type (0,0) after Tate twist; only type-(0,0) Saito relation classes enter the detector span
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010, B015-B025; boundary attempt audited in S026, matching paths in S027, thimble/Hurwitz models in S028-S029, and isolated Milnor bases in S030
claim: The rational span of Saito detector classes from all independent-node hyperplane members in all sufficiently high powers equals the primitive rational Hodge homology of X.
falsifier: a polarized smooth projective 2n-fold with a nonzero primitive rational Hodge cohomology class orthogonal to every Saito detector class arising from every independent-node member in every sufficiently high power
---

# G009 - Independent-node detector generation

For each sufficiently high \(m\), let \(\mathcal C_m^{\mathrm{ind}}\) consist
of the nodal members \(Y\in|mL|\) whose nodes impose independent conditions,
together with every
\(\beta\in R(Y)_1^{(0,0)}\). Define

\[
 D_{\mathrm{ind}}(X,L)=
 \operatorname{span}_{\mathbf Q}
 \{\gamma_\beta:(Y,\beta)\in\mathcal C_m^{\mathrm{ind}}
 \text{ for some }m\gg0\}.
\]

## Falsifiable sufficient theorem

Prove

\[
 D_{\mathrm{ind}}(X,L)
 =
 H_{2n}^{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)}.
\]

Here the right side is written in homological Hodge notation via Poincare
duality. B016 then gives a detector for every nonzero primitive rational
Hodge cohomology class. B010 turns that pairing into nonzero singular-fiber
restriction, and B007 propagates to the standard rational Hodge Conjecture.

This is stronger than G008 because the detector is required to come from the
independent-node locus. It is justified as an attackable gate by B015, which
completely controls the local discriminant and intersection-cohomology
channel on that locus.

## Attempt 1 - Generate from local normal-crossing geometry

B015 proves that the local channel is concentrated in the exact degree and
that the nodes can be independently smoothed. This determines the available
detector space at a chosen member, but it provides no lower bound on the
global span of the pushforward classes \(\gamma_\beta\). A positive local
defect can still map into a proper subspace, and can pair trivially with a
specified \(\zeta\).

## Attempt 2 - Compare with global tube generation

B011 spans all primitive homology by global tubes, while B013 writes a
loop-fixed tube cancellation as a distributed relation. To prove G009 from
this, one needs a transformation from global distributed relations to
independent-node local relations that preserves the resulting ambient
homology class. B015 supplies the target local geometry but no such
transformation. This is the exact content still missing from G007.

## Attempt 3 - Pull back a boundary class

Green and Griffiths II describe classifying-space boundary components whose
inverse images model singular loci and propose proving nonemptiness by a
nonzero pullback of the boundary class. Their construction of the decisive
nodal locus for a specified \(\zeta\), however, begins under the Hodge
Conjecture with an algebraic presentation \(k_0\zeta=[W-H]\). Their
class-dependent map is analyzed near the resulting already-existing
singularity, and the general boundary-intersection formula is presented as a
preliminary program with a correction term. It therefore cannot establish
G009 without a new, non-circular global construction. This route is NG-013.

## Attempt 4 - Transfer detectors between powers

B017 proves that the cumulative independent-node detector spans eventually
stabilize and that G009, if true for a fixed \(X\), has a finite detector
certificate. This is not an effective construction.

There is no automatic inclusion from the detector space in \(|mL|\) to the
one in \(|(m+k)L|\). Multiplying a defining section of \(Y\in|mL|\) by a
section of \(kL\) produces the reducible divisor
\(Y+\operatorname{div}(s)\), not an independent-node member, and supplies no
canonical preservation of Saito's relation or ambient detector class.
Therefore high-power amplification alone does not make the individual spans
monotone. This is NG-014.

## Attempt 5 - Force incidence through tautological complete intersections

A class-blind way to create special hypersurfaces is to require them to
contain a codimension-\(n\) complete intersection cut by powers of \(L\).
B018 proves that its class is proportional to \(\ell^n\), has zero primitive
projection, and pairs trivially with every primitive \(\zeta\). Thus a nodal
construction whose proposed detector is just that complete-intersection
class yields no primitive detector, regardless of degree.

The singular member could still acquire other non-tautological vanishing
classes, but their existence and ambient pushforward would require a new
argument; they do not follow from the imposed complete intersection. The
tautological-incidence shortcut is NG-015.

## Attempt 6 - Use a matching path or an intersection-one pair

Matching paths show that two thimbles over distinct critical values can glue
to a Lagrangian middle sphere. B019 keeps the output type
honest: the construction is symplectic, the endpoints are distinct singular
fibers, and no theorem identifies the sphere with a type-\((0,0)\) Saito
class at one simultaneous-node member. Colliding the two endpoints while
preserving the ambient class and Hodge type is exactly the missing algebraic
specialization theorem. Treating the matching sphere itself as a G009
detector is NG-016.

Schnell's Lemma 6 also does not supply the desired local relation. B020 shows
that its two vanishing cycles have intersection number one and are therefore
rationally independent. The dual-plane node in the same proof corresponds
to a two-ODP hyperplane, but no relation, type-\((0,0)\) statement, or
nonzero Saito pushforward is proved for it. Confusing either configuration
with a detector is NG-017.

## Attempt 7 - Collide the matching endpoints through a cusp

The cusp/Milnor-number-two point in Schnell's general dual-plane slice is
the simplest available collision of two vanishing directions. B021 gives a
rank obstruction to using it as a class-by-class preserving matching
collision: the matching cycles are equal up to sign after transport, whereas
the cusp cycles have intersection one and span rank two. Thus the individual
cycle classes cannot be carried unchanged through this collision.

This does not exclude a transformation involving braid monodromy, additional
vanishing cycles, or preservation only of the final ambient tube class. B023
now excludes pure invertible Hurwitz basis change within a fixed fibration,
but not a topology-changing braid/collision process. The direct
matching-pair-to-cusp-pair identification is NG-018, and the pure basis-change
repair is NG-020.

## Attempt 8 - Preserve only a thimble relation

B022 gives the exact ambient reconstruction in a generic hypersurface pencil.
A vector in the relation kernel \(\ker\partial\) can vanish modulo the
equator-extension image. Even a nonzero class in \(\mathcal T(Y)\) can lie in
the base-locus kernel \(K\) and project to zero in ambient primitive homology.
Thus preservation of a thimble relation through collision is weaker than
preservation of the Saito ambient detector class. Treating them as equivalent
is NG-019.

The surviving target is consequently a morphism of the **quotiented**
thimble complexes that carries a class nontrivially through
\(\mathcal T(Y)/K\), then identifies it with a rational type-\((0,0)\) local
Saito class. No audited collision theorem supplies this map.

## Attempt 9 - Use complete-intersection thimble surjectivity

B024 proves that the quotiented thimble group surjects onto primitive middle
homology for smooth projective complete intersections, and hence supplies a
global detector for every nonzero primitive class in that special setting.
This verifies the source side of the proposed quotient-level collision.

It does not show that any basis of the detector space comes from
independent-node Saito classes, and it supplies no reduction from arbitrary
smooth projective varieties to complete intersections. The step from global
topological thimble generation to local Hodge detector generation remains
G009 itself. Counting the surjection as algebraicity is NG-021.

## Attempt 10 - Create a relation inside one higher isolated singularity

One might collide several Morse points into an isolated singularity of
Milnor number \(\mu>1\), morsify it, and treat the \(\mu\) vanishing cycles as
the missing relation. B025 proves the opposite: a distinguished
morsification gives an integral basis of the rank-\(\mu\) Milnor lattice.
The internal relation kernel is zero.

The missing dependence must therefore be created by the global embedding of
one or more local Milnor lattices into the homology of a projective nearby
fiber. G010 isolates this prescribed local-to-global defect theorem. Counting
Milnor number alone as a relation is NG-022.

## Re-entry condition

Construct a boundary or incidence class on the universal hyperplane
parameter space independently of an algebraic representative of \(\zeta\),
prove its pullback is nonzero in a way that retains the class-specific
pairing, and identify the resulting point with an independent-node Saito
detector. Equivalently, construct a class-preserving map from Schnell tube
generators into \(D_{\mathrm{ind}}(X,L)\). The construction must create
non-tautological primitive ambient homology rather than importing it through
an already-algebraic non-tautological subvariety. A two-critical-value route
must additionally prove an algebraic collision theorem identifying the
matching sphere with a one-fiber relation class and preserving rational
type \((0,0)\). It must also preserve nonvanishing after the
equator-extension and base-locus quotients in B022.
