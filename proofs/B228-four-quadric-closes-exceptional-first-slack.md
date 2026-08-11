---
brick_id: B228
status: PROVED
base_field: C
variety: the smooth four-dimensional quadric X=Q^4 in P^5 with primitive rational middle class zeta=a-b
smoothness: Q^4 is smooth; all marked points are distinct; no nodal divisor or incidence smoothness is constructed
projectivity: Q^4, every very ample O_Q(k)-embedding, secant lines, maximal isotropic planes, and quartic evaluation systems are projective
dimension: dim X=4; c_4=15; a first-slack degree-five configuration would have N=32 and H^2 point rank c_4+1=16
codimension: every standard-polarization two-triple defect clique lies in a maximal isotropic P^2, where quartics have dimension 15, one below the required rank
coefficient_field: Q for zeta and the cycle-class input; C for the quadratic form, isotropic spans, jets, and evaluation ranks
cohomology_theory: rational singular cohomology for zeta and coherent restriction to finite schemes for the obstruction
hodge_type: zeta=a-b is nonzero primitive rational type (2,2); the obstruction constructs no detector of type (0,0)
cycle_class_map: CH^2(Q^4)_Q -> H^4(Q^4,Q(2)); zeta is the difference of the two ruling-plane classes
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221, B226-B227, S081
claim: On the legitimate primitive input (Q^4,zeta), no very ample A admits a first-slack configuration whose A^4 point span has dimension 16 and contains all full second osculators. For A=O_Q(k), k>=2, the two-triple defect locus is empty; for A=O_Q(1), every defect clique lies in an isotropic P^2 and therefore has A^4 evaluation rank at most 15.
falsifier: a very ample polarization outside O_Q(k), a powered-polarization defect pair, a standard-polarization defect pair not joined by a line on Q, a pairwise orthogonal set spanning more than an isotropic P^2, or quartic rank at least 16 on P^2
---

# B228 — The four-quadric closes exceptional first slack

B221 supplies the legitimate primitive input

\[
 (X,\zeta)=(Q^4,a-b), \tag{1}
\]

and proves that every very ample line bundle is \(A=O_Q(k)\), \(k\ge1\).

If \(k\ge2\), B226 makes the \(A^4\) two-triple defect locus empty, so
no first-slack marked set exists. It remains to test \(A=O_Q(1)\).

Suppose a pair \(p\ne q\) is defective for \(O_Q(4)\). By B227, the
line \(L=\overline{pq}\) has contact order at least three with \(Q\) at
an endpoint. The restriction of the defining quadratic form to \(L\)
has degree two, so this is possible only when \(L\subset Q\).

Write \(B\) for the nondegenerate polar form of the quadric. A complete
defect clique \(Z=\{[v_i]\}\) therefore satisfies

\[
 B(v_i,v_j)=0\qquad\text{for all }i,j. \tag{2}
\]

Its vector span is totally isotropic in a six-dimensional nondegenerate
quadratic space, hence has dimension at most three. Thus

\[
 Z\subset\mathbf P^2\subset Q^4. \tag{3}
\]

But the first-slack rank required by B222-B225 is

\[
 h_Z(A^4)=c_4+1=\binom{6}{2}+1=16, \tag{4}
\]

whereas (3) gives

\[
 h_Z(A^4)\le h^0(\mathbf P^2,O(4))=\binom{6}{2}=15. \tag{5}
\]

This contradiction covers the last polarization. Hence no choice of
very ample \(A\) on \(Q^4\) realizes exceptional first slack. The
argument falsifies that sufficient mechanism, not the Hodge Conjecture.
