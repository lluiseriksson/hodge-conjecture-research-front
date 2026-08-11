---
brick_id: B278
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadrics Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) for k=3,4, H=A^2, and hypothetical G197 marked schemes
smoothness: Q^d and the reduced marked schemes are smooth; the cubic auxiliary plane blow-up is a smooth weak del Pezzo surface; no central ODP package is constructed
projectivity: the complete sextic/octic embeddings, planar restrictions, tangent osculators, weak del Pezzo anticanonical map, and marked point spans are projective
dimension: dim X=d=2n>=14; cubic and quartic equality 7d+5 are impossible, so both floors are at least 7d+6; in particular rank 103 is impossible on Q^14
codimension: the primitive middle ruling difference supplies a valid universal test input; the theorem extends B271-B272 from their former survivor range d>=22 to every even d>=14
coefficient_field: Q for zeta and C for sections, jets, plane coordinates, blow-ups, and tangent ranks
cohomology_theory: rational singular cohomology, coherent restriction to double schemes, and weak-del-Pezzo intersection/resolution geometry
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B277, G197-G198, NG222-NG233, S081, S084
claim: On every split even Q^d with d>=14, neither A=O_Q(3) nor A=O_Q(4) can realize h_Z(1)=7d+5 under the G144 tangent-absorption hypotheses. Thus rank 103 is impossible on Q^14, G197 is NO-GO, and G198 is active at rank 104 in dimension 14.
falsifier: a dimension-dependent failure of B269's eighth-point separator, B271's plane/conormal or weak-del-Pezzo argument, B272's quartic residual-rank construction, a cubic/quartic rank-103 G197 package on Q^14, or a different next boundary
---

# B278 — Cubic and quartic equality already fail in dimension fourteen

B271 and B272 were stated for \(d\ge22\) because that was the
high-dimensional survivor range at G190. Their proofs have no such
geometric threshold. We audit every dimension-sensitive step.

## Common planar reduction

B260 supplies six independent double supports for \(k=3,4\) in every
even dimension \(d\ge14\). B264, already stated in that range, shows
that equality \(7d+5\) forces all six supports and the seventh point
into one isotropic plane. Such planes exist on every split \(Q^{2n}\)
with \(n\ge2\).

The plane part of six double neighborhoods has rank at most 18 and the
normal part at most \(6(d-2)\); their sum is \(6d+6\) for every \(d\).
Degree-five/seven value interpolation supplies all \(d-2\) conormal
directions exactly as in B271-B272. No inequality uses \(d\ge22\).

## Cubic equality

B270 reduces residual plane-sextic rank one to zero differential of the
plane cubic system. B271's weak-del-Pezzo calculation is purely
two-dimensional: the six-point blow-up has only line/conic roots, and
zero anticanonical differential forces complementary collinear triples
through the seventh point.

B269's separator for every eighth point uses either a squared
hyperplane containing the isotropic plane or six plane-line factors.
Both constructions lift on every split \(Q^d\) with \(d\ge14\).
Therefore no eighth tangent osculator is absorbed, whereas

\[
 N=2(7d+5)>7. \tag{1}
\]

So cubic equality is impossible for every even \(d\ge14\).

## Quartic equality

B272 partitions the six plane supports by lines through the seventh
point. A good perfect matching gives all \(d+1\) residual jets. In the
four-point class, its explicit transverse octic supplies two plane jets
and degree-seven interpolation supplies all \(d-2\) normal jets. Hence

\[
 \operatorname{rank}_{\mathrm{res}}\ge2+(d-2)=d,\qquad
 h_Z(1)\ge6d+6+d=7d+6. \tag{2}
\]

Again, only \(d\ge2\) is used after the common six-double construction.
Quartic equality \(7d+5\) is impossible for every even \(d\ge14\).

At \(d=14\), equation (1)'s equality rank is \(7d+5=103\). Thus neither
surviving G197 polarization exists on this valid input. B278 constructs
no ODP package, Kuranishi vanishing, rational detector, specified
pairing, algebraic cycle, proof, or disproof of HC.
