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
| detector-span formulation | B016 turns detection by any chosen singular-member collection into equality of its Saito detector span with primitive rational Hodge homology | the independent-node span equality G009 is precisely the new open generation content |
| finite detector certificate | B017 proves cumulative spans stabilize and full generation for a fixed variety is witnessed by finitely many detector classes | gives no effective power bound, no construction, and no monotonicity for the individual power-by-power spaces |
| tautological complete intersections | their classes and multiplicities are explicit and algebraic | B018 proves their primitive projections vanish, so they cannot detect primitive middle classes |
| classifying-space boundary pullback | Green-Griffiths II models selected singular loci as inverse images of boundary components and proposes a cohomological nonemptiness test | the class-directed nodal construction assumes HC; the global formula is programmatic and contains unresolved compactification/correction data |
| degenerations | limiting mixed Hodge structures, vanishing cycles, specialization | a special-fiber cycle may fail to lift; type and rationality can jump |
| spreading out | places data over a finitely generated field/base | spreading a class is not spreading a cycle that does not yet exist |
| reduction modulo primes | Frobenius and etale/Tate information | needs comparison, Tate-type algebraicity, and cycle lifting back to characteristic zero |
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
remaining content as detector-span generation. G009 asks for this generation
on the independent-node locus and is now the active sufficient gate. B017
gives a finite certificate if the gate is true for a fixed variety, but
NG-014 blocks the naïve comparison between powers. B018/NG-015 further
require any successful incidence construction to create non-tautological
primitive homology rather than recycle polarization complete intersections.
