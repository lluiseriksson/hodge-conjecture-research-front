---
brick_id: B222
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with a very ample H, a reduced marked scheme Z, a full-support degree-m relation, and the complete lower-extinction and simultaneous-rank hypotheses of G144
smoothness: X and Z are smooth; central ODP and incidence smoothness are assumed only when inherited from G144 and are not produced
projectivity: X, all complete H^k systems, point spans, marked osculating spaces, and relation transports are projective
dimension: dim X=d; write N=D_d(m)+s with integer slack s>=0; the Hodge branch has d=2n
codimension: the slack is partitioned exactly among lower point-span excesses and the two complementary transport cokernels
coefficient_field: C for sections, ranks, osculators, Gauss maps, and transports; Q remains separately required for the Hodge detector
cohomology_theory: coherent finite-scheme restrictions, principal parts through order two, graded value relations, and finite-dimensional duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate G144 clauses
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B213-B217, B220-B221, G144-G148
claim: For m>=3, if delta_2=h_Z(2)-c_d and delta_c=h_Z(m-2)-L_d(m-2), then delta_2,delta_c>=0, delta_2+delta_c<=s, and both complementary transport cokernels have dimension s-delta_2-delta_c. Injective Gauss forces delta_2>=1. At s=1 there is no candidate for m=2,3,4; for m>=5 one has (delta_2,delta_c)=(1,0) and both transports are isomorphisms.
falsifier: a G144 rank tuple violating the slack identities, unequal complementary cokernel dimensions, or an injective-Gauss candidate with zero degree-two excess and more than one marked point
---

# B222 — The strict-slack rank budget

Write

\[
 N=D_d(m)+s,\qquad s\ge0. \tag{1}
\]

## Birth degree at least three

For \(m\ge3\), set

\[
 c_d=\binom{d+2}{2},\qquad
 \delta_2=h_Z(2)-c_d,\qquad
 \delta_c=h_Z(m-2)-L_d(m-2). \tag{2}
\]

B215 gives \(\delta_2,\delta_c\ge0\), and B213 gives

\[
 h_Z(2)+h_Z(m-2)\le N.
\]

Using \(D_d(m)=c_d+L_d(m-2)\) yields the exact budget

\[
 \delta_2+\delta_c\le s. \tag{3}
\]

The two B213 injections are

\[
 M_{\lambda,2}:E_2\hookrightarrow\mathcal R_{m-2},
 \qquad
 M_{\lambda,m-2}:E_{m-2}\hookrightarrow\mathcal R_2.
\]

Since \(\dim E_k=h_Z(k)\) and
\(\dim\mathcal R_k=N-h_Z(k)\), both cokernels have the same
dimension

\[
 s-\delta_2-\delta_c. \tag{4}
\]

Every marked full second osculator has dimension \(c_d\) and lies in
the degree-two point span of dimension \(c_d+\delta_2\). In particular,
if \(\delta_2=0\), every marked osculator equals that span. B217 then
puts every marked point in one common tangent \(d\)-plane. Therefore an
injective H-Gauss map and \(N>1\) force

\[
 \delta_2\ge1. \tag{5}
\]

At the first strict layer \(s=1\), equations (3) and (5) give formally

\[
 (\delta_2,\delta_c)=(1,0), \tag{6}
\]

and (4) makes both transports isomorphisms. This conclusion represents
an actual rank signature only when the complementary degrees are
compatible:

- If \(m=3\), then \(m-2=1\) and \(\delta_c=0\) says
  \(h_Z(1)=d+1\). Tangent absorption makes all marked tangent spaces
  equal, contradicting injective Gauss.
- If \(m=4\), then \(m-2=2\), so \(\delta_c=\delta_2\). Equation (3)
  reads \(2\delta_2\le s\), which contradicts
  \(\delta_2\ge1\) at \(s=1\).
- Hence (6) is viable only for \(m\ge5\).

## Birth degree two

Put \(\delta_1=h_Z(1)-(d+1)\). Then B213-B215 give

\[
 2\delta_1\le s,\qquad
 \dim\operatorname{coker}M_{\lambda,1}=s-2\delta_1. \tag{7}
\]

If \(\delta_1=0\), tangent absorption makes every marked tangent space
equal to the degree-one point span, contradicting injective Gauss when
\(N>1\). Thus injective Gauss forces \(\delta_1\ge1\), and (7) rules out
\(s=1\) entirely when \(m=2\).

B222 is rank bookkeeping, not existence. It constructs no marked
scheme, nodal profile, rational detector, specified pairing, or cycle.
