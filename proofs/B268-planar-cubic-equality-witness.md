---
brick_id: B268
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22 containing an isotropic plane Pi, primitive ruling difference zeta=a-b, cubic A=O_Q(3), H=O_Q(6), and seven specified reduced supports
smoothness: Q^d, Pi, and the seven distinct reduced supports are smooth; no central ODP divisor or incidence package is asserted
projectivity: the split quadric, isotropic plane, two generator lines through u, complete sextic embedding, and restrictions to double finite schemes are projective
dimension: dim X=d=2n>=22; six double supports have rank 6d+6, their union with 2u has rank exactly 7d+5, and the residual restriction to 2u has rank exactly d-1
codimension: the primitive codimension-n ruling difference supplies a valid universal test input; the configuration realizes G190's cubic equality rank but none of its relation, ODP, Kuranishi, rational-type, or pairing obligations
coefficient_field: Q for the explicit affine coordinates and exact rank matrices, Q for zeta, and C for global sections and tangent jets
cohomology_theory: rational singular cohomology and coherent restriction to the seven double neighborhoods
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B247, B256, B260-B267, G190, S081
claim: On every split even Q^d with d>=22, choose an isotropic plane Pi, u in Pi, and three points on each of two distinct generator lines through u with affine parameters 1,2,3. For H=O_Q(6), the six double neighborhoods are independent of rank 6d+6, while adding 2u contributes exactly d-1, so the seven-double evaluation rank is exactly 7d+5. Thus B261's cubic floor is sharp at the coherent rank level on this explicit planar configuration.
falsifier: plane degree-six double-jet rank below 18, degree-five value rank below six on P6 or below seven on P6 union {u}, failure of the d-2 normal-jet decomposition, residual plane rank different from one, residual total rank different from d-1, or seven-double rank different from 7d+5
---

# B268 — A planar cubic equality witness

Let \(Q^d\) be split and contain an isotropic plane
\(\Pi\simeq\mathbf P^2\). In the affine chart of \(\Pi\) centered at
\(u=(0,0)\), choose

\[
 p_i=(i,0),\qquad q_i=(0,i),\qquad i=1,2,3. \tag{1}
\]

The \(p_i\) lie on one generator line through \(u\), the \(q_i\) on
another, and the first four supports may be ordered with two from each
line, so no three of those four are collinear.

## The six double neighborhoods are independent

The plane part of a sextic first jet is represented by polynomials in
two affine variables of total degree at most six. Exact rational
Gaussian elimination on the value and two derivative rows at the six
points (1) gives

\[
 \operatorname{rank}\bigl(O_\Pi(6)\to O_{2P_6}(6)\bigr)=18. \tag{2}
\]

The calculation is reproduced without floating point arithmetic in
verification/verify_B268_planar_cubic_equality.py.

At every support, the tangent space of \(Q\) has two directions along
\(\Pi\) and \(d-2\) normal directions. The conormal sequence is

\[
 O_\Pi(-2)\longrightarrow O_\Pi(-1)^{\oplus(d-1)}
 \longrightarrow N^*_{\Pi/Q}\longrightarrow0. \tag{3}
\]

After tensoring by \(O_\Pi(6)\), ambient linear equations of \(\Pi\)
multiplied by plane quintics map onto every normal first-jet fiber.
The degree-five value map at the six points has exact rank six, so its
direct sum in the \(d-1\) ambient conormal generators surjects onto the
six fibers of the rank-\((d-2)\) quotient \(N^*_{\Pi/Q}(6)\). These
sections vanish along \(\Pi\), hence contribute no plane jet. Therefore

\[
 18+6(d-2)=6d+6. \tag{4}
\]

## Every residual plane jet is determined by its value

Let \(F\) be a plane sextic vanishing doubly at all six points. Its
restriction to the first generator line is a degree-six polynomial
with double zeros at parameters \(1,2,3\), hence is a scalar multiple
of

\[
 (t-1)^2(t-2)^2(t-3)^2. \tag{5}
\]

The same holds on the second line. The two scalars are determined by
the common value \(F(u)\). Consequently both directional derivatives
at \(u\) are fixed by that value. If \(F(u)=0\), both line restrictions
vanish identically and both plane derivatives vanish. Thus

\[
 \operatorname{rank}\bigl(I_{2P_6,\Pi}(6)\to O_{2u,\Pi}(6)\bigr)=1. \tag{6}
\]

Existence of a unit is explicit: take the square of the cubic formed
by three good cross-secants pairing the two triples.

## Normal residual jets and exact equality

Degree-five plane polynomials have value rank seven on
\(P_6\cup\{u\}\). Hence, after forcing zero normal derivative at the
six supports, each of the \(d-2\) normal directions at \(u\) remains
arbitrary. Combining this with (6),

\[
 \operatorname{rank}\bigl(I_{2P_6,Q}(6)\to O_{2u,Q}(6)\bigr)
 =1+(d-2)=d-1. \tag{7}
\]

Equations (4) and (7) give the exact seven-double rank

\[
 6d+6+(d-1)=7d+5. \tag{8}
\]

This is an exact coherent-rank witness, not a numerical approximation.
It proves that B261's cubic floor is sharp for this configuration and
that sextic interpolation alone cannot close G190. It supplies no
degree-one relation transport, ODP divisor, Kuranishi vanishing,
rational type-(0,0) detector, specified pairing, algebraic cycle, proof,
or disproof of HC.
