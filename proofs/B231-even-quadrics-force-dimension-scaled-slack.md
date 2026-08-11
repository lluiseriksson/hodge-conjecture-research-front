---
brick_id: B231
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive rational middle class zeta=a-b, and an arbitrary very ample A=O_Q(k), with H=A^2
smoothness: Q^d and every reduced marked scheme are smooth; central ODP and incidence conditions are only inherited hypotheses and are not constructed
projectivity: Q^d, every complete O_Q(k)-embedding, finite double and triple neighborhoods, point spans, tangent and second osculators, secant lines, and maximal isotropic spaces are projective
dimension: dim X=d=2n; for m=2 no candidate exists when s<2d+2; for m>=3 no candidate exists when s<c_d=binom(d+2,2)
codimension: the ruling difference a-b is a valid primitive codimension-n input; the obstruction forces any universal strict-slack mechanism to use slack growing with dimension
coefficient_field: Q for zeta and C for sections, jets, quadratic forms, osculators, and ranks
cohomology_theory: rational singular cohomology for the primitive input and coherent restriction to finite jet schemes
hodge_type: zeta is nonzero primitive rational type (n,n); the obstruction constructs no rational type-(0,0) detector
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies a legitimate universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B230, S081, S083
claim: On (Q^d,a-b), every m=2 G144 candidate has slack s>=2d+2 and every m>=3 candidate has slack s>=c_d. At the m=2 boundary s=2d+2, any hypothetical candidate necessarily has delta_1=d+1, N=4d+4, h_Z(1)=2d+2=N/2, and an isomorphic degree-one relation transport. Consequently no dimension-independent finite slack bound can realize G148 universally.
falsifier: a candidate below either displayed threshold, failure of the forced pairwise jet defect, a quadric defect clique not spanning a totally isotropic space, containment of v odot v-perp in Sym^2(W), containment of the O_Q(4) second osculator in Sym^4(W), or a different threshold rank signature
---

# B231 — Even quadrics force dimension-scaled slack

Fix the valid input

\[
 (X,\zeta)=(Q^d,a-b),\qquad d=2n\ge4. \tag{1}
\]

By B221, every very ample line bundle on \(Q^d\) is
\(A=O_Q(k)\), \(k\ge1\). Put \(H=A^2\) and write
\(N=D_d(m)+s\).

## Degree two

For \(m=2\), B222 gives

\[
 h_Z(1)=d+1+\delta_1,\qquad
 2\delta_1\le s. \tag{2}
\]

Suppose \(s<2d+2\). Then \(\delta_1\le d\), hence

\[
 h_Z(1)\le2d+1<2(d+1). \tag{3}
\]

If the restriction to \(2p\sqcup2q\) were surjective for some marked
pair, its two dual tangent-jet spaces, each of vector dimension \(d+1\),
would form a direct sum inside the degree-one point span. Equation (3)
makes this impossible. Thus every marked pair is defective.

When \(k\ge2\), \(A^2=O_Q(2k)\) has exponent at least four, whereas
B215 separates two double neighborhoods from exponent three onward.
Therefore \(k=1\). The quadratic secant criterion of B229 then says
that every marked chord is tangent at both endpoints. If \(v_i,v_j\)
represent two marked points and \(B\) is the polar form of the quadric,
this is

\[
 B(v_i,v_j)=0. \tag{4}
\]

Hence the vector span \(W=\langle v_i\rangle\) is totally isotropic and
\(\dim W\le n+1\). The \(O_Q(2)\) point span lies in
\(\operatorname{Sym}^2W\). At \(p=[v]\), however, the full tangent
osculator is

\[
 v\mathbin{\odot}v^\perp. \tag{5}
\]

Because \(\dim v^\perp=2n+1>n+1\ge\dim W\), choose
\(u\in v^\perp\setminus W\). Then
\(v\mathbin{\odot}u\notin\operatorname{Sym}^2W\), contradicting the
lower tangent-osculator absorption required by G144. Thus

\[
 m=2\quad\Longrightarrow\quad s\ge2d+2. \tag{6}
\]

## Every degree at least three

Let \(m\ge3\) and \(c_d=\binom{d+2}{2}\). B222 gives

\[
 h_Z(2)=c_d+\delta_2,\qquad 0\le\delta_2\le s. \tag{7}
\]

If \(s<c_d\), then \(h_Z(2)<2c_d\), so the same direct-sum argument
forces failure of the \(A^4\) restriction to \(3p\sqcup3q\) for every
marked pair. When \(k\ge2\), B215 separates those two triple
neighborhoods because \(A^4=O_Q(4k)\) has exponent at least eight.
Thus \(k=1\).

B227 makes every defect chord have contact order at least three at both
endpoints. In particular it is tangent at both endpoints; on a quadric,
(4) follows and the entire chord lies on \(Q\). Again all marked
representatives lie in a totally isotropic \(W\).

Now the \(O_Q(4)\) point span lies in \(\operatorname{Sym}^4W\). The
full second osculator at \([v]\) contains its tangent directions

\[
 v^3\mathbin{\odot}v^\perp. \tag{8}
\]

For \(u\in v^\perp\setminus W\), the tensor
\(v^3\mathbin{\odot}u\) is not in \(\operatorname{Sym}^4W\). This
contradicts G144's lower second-osculator absorption. Therefore

\[
 m\ge3\quad\Longrightarrow\quad s\ge c_d. \tag{9}
\]

## Consequences and next threshold

For \(d\ge4\), \(c_d>2d+2\). Given any fixed finite slack bound \(S\),
choose an even \(d\ge4\) with \(S<2d+2\). Equations (6) and (9) then
exclude every degree on the valid input \(Q^d\). Thus no slack bound
independent of dimension can realize the universal G148 mechanism.

At the first value not excluded by the preceding argument, \(s=2d+2\),
the quadric argument
still excludes \(\delta_1<d+1\), while (2) forces
\(\delta_1\le d+1\). Hence

\[
 \delta_1=d+1,\qquad N=4d+4,\qquad
 h_Z(1)=2d+2=N/2,\qquad s-2\delta_1=0. \tag{10}
\]

The relation transport is therefore an isomorphism and the degree-one
code is diagonally self-dual. B232 later excludes this boundary signature.
B231 proves only a necessary dimension-scaled floor and its conditional
threshold ranks. It constructs no
marked scheme, ODP profile, rational detector, specified pairing, cycle,
proof, or disproof of the Hodge Conjecture.
