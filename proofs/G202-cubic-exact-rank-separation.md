---
brick_id: G202
status: EXPLORATORY
base_field: C
variety: the smooth split even-dimensional quadric Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic A=O_Q(3), H=O_Q(6), six independent double supports P6, and a seventh support u with exact residual rank d at the G200 boundary
smoothness: Q^d and the seven reduced supports are smooth and distinct; no central ODP package is assumed or constructed
projectivity: the complete sextic embedding, double-support span, tangent osculators, B260 selected-edge graph, endpoint-plane maps, and absorbed-support locus are projective
dimension: dim X=d=2n>=14; the seven-support double rank is 7d+6; residual rank at u is exactly d; N=2(7d+6)>7
codimension: after B281 removes the quartic branch, classify the cubic exact-rank-d configurations and prove their seven-support tangent span absorbs no eighth distinct tangent osculator
coefficient_field: Q for zeta and C for sextics, first jets, tangent osculators, endpoint-plane graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is assumed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B281, G200-G201, NG237-NG238, S081, S084-S085
claim: Every cubic seven-support configuration on Q^d with six independent doubles and total rank exactly 7d+6 admits, for each x outside the seven supports, a sextic F_x in H0(Q,I_(2P7)(6)) whose restriction to 2x is nonzero.
falsifier: one exact-rank cubic configuration with an eighth distinct Q-tangent osculator contained in the seven-support span
---

# G202 — Cubic exact-rank separation gate

B281 proves G201's quartic clause without any planar assumption. The
remaining statement is cubic:

\[
 \operatorname{rank} H^0(Q,O_Q(6))|_{2P_7}=7d+6
 \quad\Longrightarrow\quad
 \forall x\notin P_7\ \exists F_x\in H^0(Q,I_{2P_7}(6)):
 F_x|_{2x}\ne0. \tag{1}
\]

The eight-factor hyperplane construction of B281 has degree eight and
does not descend to degree six. S085 does not supply an emptiness
theorem here: seven supports lie beyond the degree-six Veronese
threshold. A proof must use the additional B260/B264 data—six
independent double blocks, exact residual rank \(d\), and the selected
edge-image equality—not merely the cardinality of \(P_7\).

G202 is falsifiable by one exact-rank cubic configuration with one
absorbed eighth tangent osculator. No such classification or separator
is yet proved. It is EXPLORATORY and active inside G200. It constructs
no ODP package, rational detector,
specified pairing, cycle, proof, or disproof of HC.
