---
brick_id: G201
status: EXPLORATORY
base_field: C
variety: the smooth split even-dimensional quadric Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) for k=3,4, H=A^2, six independent double supports P6, and a seventh support u in the nonplanar exact-rank branch of G200
smoothness: Q^d and the seven reduced supports are smooth and distinct; no central ODP package is assumed or constructed
projectivity: the complete sextic or octic embedding, double-support span, tangent osculators, variable-edge product spaces, and absorbed-support locus are projective
dimension: dim X=d=2n>=14; rank H0(O_Q(2k)) to H0(O_(2(P6 union {u}))(2k)) equals 7d+6; the residual rank at u is exactly d; N=2(7d+6)>7
codimension: classify the exact-rank-d nonplanar branch inside the G200 cubic/quartic boundary and prove that its seven-support tangent span absorbs no eighth distinct tangent osculator
coefficient_field: Q for zeta and C for sections, first jets, tangent osculators, endpoint-plane graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is assumed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B272, B278, G200, NG237, S081, S084
claim: For k=3 and k=4, every nonplanar seven-support configuration on Q^d with double-support rank exactly 7d+6 admits, for each x outside the seven supports, a section F_x in H0(Q,I_(2P7)(2k)) whose restriction to 2x is nonzero. Consequently its tangent span cannot absorb the N=2(7d+6) distinct supports required by G200.
falsifier: a nonplanar exact-rank-d residual configuration with an eighth distinct tangent osculator contained in the seven-support span, or a failure of the separator criterion
---

# G201 — Nonplanar exact-rank separation gate

Let \(P_7=P_6\cup\{u\}\) be a nonplanar cubic or quartic branch with

\[
 \operatorname{rank}\!\left(
 H^0(Q,O_Q(2k))\longrightarrow H^0(2P_7,O_{2P_7}(2k))
 \right)=7d+6. \tag{1}
\]

The smallest sufficient statement is the following separator theorem:
for every \(x\notin P_7\), construct

\[
 F_x\in H^0(Q,I_{2P_7}(2k)),
 \qquad F_x|_{2x}\ne0. \tag{2}
\]

Equation (2) is equivalent to saying that the tangent osculator at
\(x\) is not contained in the span of the seven tangent osculators.
Since G200 requires \(N=2(7d+6)>7\) distinct marked supports and lower
profile extinction absorbs every one of their tangent osculators, (2)
would exclude the nonplanar branch. The already-audited planar
classification could then be treated separately.

G201 is falsifiable by one explicit exact-rank configuration and one
eighth absorbed support. No such classification or separator is yet
proved. It constructs no ODP package, rational detector, specified
pairing, cycle, proof, or disproof of HC.

B281 subsequently proves (2) for \(k=4\) without a planar assumption.
The unresolved cubic clause is isolated as G202.
