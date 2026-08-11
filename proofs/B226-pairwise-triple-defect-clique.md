---
brick_id: B226
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X with very ample A, H=A^2, and a reduced marked scheme Z whose H^2 point span has dimension c_d+1 and contains every full second osculator
smoothness: X and the reduced marked scheme Z are smooth; triple neighborhoods are infinitesimal and no ODP divisor is constructed
projectivity: X, the A^4 evaluation system, all marked triple neighborhoods, and the second-osculating spans are projective
dimension: dim X=d; each full second osculator has vector dimension c_d=binom(d+2,2), while their common point span has dimension c_d+1
codimension: every pair of marked points lies in the failure locus for A^4 interpolation on the disjoint union of their two triple neighborhoods
coefficient_field: C for sections, jets, osculators, and evaluation ranks
cohomology_theory: coherent restriction to length-c_d triple neighborhoods and finite-dimensional duality
hodge_type: none asserted; pairwise jet defect supplies no rational Hodge detector
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B214-B215
claim: If the H^2 point span S_Z has dimension c_d+1 and contains the c_d-dimensional full second osculator at every marked point, then for all distinct p,q in Z the restriction H^0(X,A^4)->H^0(3p union 3q,A^4) is not surjective. Hence Z is a complete clique in the pairwise two-triple defect locus. If A=B^ell with B very ample and ell>=2, that defect locus is empty.
falsifier: such a marked span containing a pair whose two triple neighborhoods impose independent conditions on A^4, or a powered A=B^ell with ell>=2 whose A^4 system fails B215's two-triple interpolation
---

# B226 — First slack is a clique of two-triple defects

Assume a reduced marked scheme \(Z\subset X\) satisfies

\[
S=S_{2,Z}^{(0)}\subset H^0(X,H^2)^*,\qquad
\dim S=c_d+1.
\]

By hypothesis, for every \(p\in Z\) the full second osculator

\[
O_p=\widehat O_p^{(2)}(H^2),\qquad \dim O_p=c_d,
\]

inside \(S\). Fix distinct \(p,q\in Z\). If

\[
H^0(X,H^2)\longrightarrow
H^0(3p\sqcup3q,H^2) \tag{1}
\]

were surjective, its dual would embed the two local dual jet spaces as
a direct sum. Thus

\[
\dim(O_p+O_q)=2c_d. \tag{2}
\]

But both osculators lie in \(S\), so (2) would give
\(2c_d\le c_d+1\), impossible for \(d\ge1\). Therefore (1) fails for
every pair. Since \(H^2=A^4\), the marked set is a complete clique in

\[
\mathfrak D_A^{(2,2)}
=\{(p,q):p\ne q,
H^0(A^4)\to H^0(3p\sqcup3q,A^4)\text{ is not onto}\}. \tag{3}
\]

This defect is destroyed by powers. If \(A=B^\ell\), with \(B\) very
ample and \(\ell\ge2\), then

\[
A^4=B^{4\ell},\qquad 4\ell\ge8.
\]

B215 interpolates two triple neighborhoods in degree \(5\) relative to
\(B\), and in every higher degree after multiplication by a section
nonzero at both supports. Hence \(\mathfrak D_A^{(2,2)}=\varnothing\).

The lemma now applies to the first-slack hypotheses of G149-G151 via
B222-B225. It also applies to a valid primitive input. On
\(X=\mathbf P^n\times\mathbf P^n\), \(n\ge2\), let
\(B=O(1,1)\) and \(A=B^2\). The one-dimensional middle primitive
subspace is rational and algebraic, and primitivity is unchanged by
passing from \(B\) to \(A\). Thus the universal fixed-\(A\) formulations
G149-G151 are false.

B226 constructs no defect clique for an exceptional polarization and
no detector or cycle.
