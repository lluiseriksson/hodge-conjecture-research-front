---
brick_id: B229
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X with H=A^2 for a very ample A and a hypothetical G144 configuration at m=2 and second slack
smoothness: X and the reduced marked scheme Z are smooth; the central H^2 divisor and all retained incidence clauses are hypotheses, not constructions
projectivity: X, the complete A and H embeddings, tangent spaces, secant lines, double neighborhoods, and degree-one evaluation code are projective
dimension: dim X=d; N=D_d(2)+2=2d+4; h_Z(1)=d+2; the degree-one code has length 2d+4 and dimension d+2
codimension: the full-support degree-two relation makes the degree-one code self-dual; every tangent space is a hyperplane in its point span and every pair fails H=A^2 interpolation on two double neighborhoods
coefficient_field: C for sections, tangent jets, codes, and diagonal pairings; Q remains required for the Hodge detector
cohomology_theory: coherent restriction to double neighborhoods, graded section multiplication, and finite-dimensional orthogonal duality
hodge_type: none asserted; self-association over C does not supply a rational type-(0,0) detector
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B213-B215, B220, B222, B227
claim: Every injective-Gauss G144 candidate with m=2 and slack s=2 has N=2d+4, h_Z(1)=d+2, and an isomorphic relation transport. Its degree-one evaluation code is diagonally self-dual and its columns are self-associated in P^(d+1). Every pair p,q fails H^0(X,A^2)->H^0(2p union 2q,A^2), so its A-secant is tangent to X at both endpoints. If A=B^ell with ell>=2, no such pair exists.
falsifier: a second-slack m=2 candidate with another rank, a non-self-dual degree-one code, a pair imposing independent double-jet conditions, a defect pair whose A-secant is not bitangent, or a powered A=B^ell with a defect pair
---

# B229 — Second slack reopens at degree two

For \(m=2\), B222 writes

\[
 N=D_d(2)+s,\qquad
 \delta_1=h_Z(1)-(d+1),\qquad 2\delta_1\le s. \tag{1}
\]

Injective Gauss forces \(\delta_1\ge1\). At the first viable value
\(s=2\), therefore,

\[
 N=2d+4,\qquad h_Z(1)=d+2, \tag{2}
\]

and \(M_{\lambda,1}:E_1\to\mathcal R_1\) is an isomorphism. For
\(u,v\in E_1\), the full-support degree-two relation gives

\[
 \sum_{p\in Z}\lambda_pu_pv_p=0. \tag{3}
\]

Thus \(E_1\subset E_1^{\perp_\lambda}\). Both spaces have dimension
\(d+2=N/2\), so equality holds. The degree-one columns are a
self-associated configuration in \(\mathbf P^{d+1}\).

Every full tangent osculator has vector dimension \(d+1\) and lies in
the common \((d+2)\)-dimensional point span. If the restriction

\[
 H^0(X,H)\longrightarrow H^0(2p\sqcup2q,H) \tag{4}
\]

were surjective, the two tangent-jet duals would form a direct sum of
dimension \(2d+2>d+2\) inside that span. Hence (4) fails for every pair.

The quadratic analogue of B227 is immediate in secant coordinates:
ambient quadrics on two ambient double points have a single relation,
because \(X_0X_1\) represents both chord-direction linear jets. Its
functional descends to \(X\) only if the chord direction lies in both
tangent spaces. Therefore every marked A-secant is bitangent.

Finally, if \(A=B^\ell\), \(\ell\ge2\), then
\(A^2=B^{2\ell}\) has exponent at least four. B215 interpolates two
double neighborhoods from exponent three onward, contradicting (4).
Thus this second-slack branch must again use an exceptional low
polarization.

B229 constructs no bitangent clique, ODP profile, rational detector,
specified pairing, or cycle.
