---
brick_id: B196
status: PROVED
base_field: C
variety: a smooth projective complex variety with a very ample line bundle A and a finite set Z of distinct points, applied degree by degree to A=H^k
smoothness: the variety and point supports are smooth; no nodal divisor or incidence smoothness is inferred by the projective criterion
projectivity: the complete linear system embeds the projective variety and the point span and embedded tangent spaces are projective linear spaces
dimension: dim X=d; the affine embedded tangent space has dimension d+1; the point-value span has vector dimension r_A
codimension: vanishing of the conditional-gradient quotient is equivalent to the point span containing every affine embedded tangent space
coefficient_field: C for sections, projective embeddings, tangent spaces, and annihilators; Q remains required separately for Hodge detectors
cohomology_theory: coherent first jets, very ample embeddings, projective duality, and finite-dimensional linear algebra
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B195, G123-G126, and the first-jet interpretation of a very ample embedding
claim: For a very ample A and point set Z, H0(I_Z A)=H0(I_2Z A) exactly when the vector span of the embedded point lines contains the affine embedded tangent space at every point of Z. If the point span is proper, its projectivization is tangent to X at every point of Z; if it is full, the equality is vacuous. In the proper case its value rank is at least d+1.
falsifier: a value-zero section with nonzero node derivative while every tangent space lies in the point span, a tangent direction outside the span when all value-zero sections have zero derivatives, or a proper absorbing span of vector dimension at most d
---

# B196 — Lower jet extinction is tangent-span absorption

Let \(A\) be very ample and write

\[
 \phi_A:X\hookrightarrow\mathbf P(W^*),\qquad W=H^0(X,A). \tag{1}
\]

For \(p_i\in Z\), let \(\ell_i\subset W^*\) be the embedded point line and
let

\[
 \widehat T_i\subset W^* \tag{2}
\]

be the affine embedded tangent space, of vector dimension
\(d+1\) for \(d=\dim X\). It contains \(\ell_i\). Put

\[
 S_Z=\operatorname{span}(\ell_1,\ldots,\ell_N)\subset W^*. \tag{3}
\]

Its dimension is the rank of value evaluation on \(Z\).

## Exact annihilator criterion

A section \(s\in W\) vanishes on \(Z\) exactly when the corresponding
linear functional on \(W^*\) annihilates \(S_Z\):

\[
 H^0(X,I_Z\otimes A)=S_Z^\perp. \tag{4}
\]

For a value-zero section, the derivative at \(p_i\) vanishes exactly when
its hyperplane contains the embedded tangent space, equivalently when the
functional annihilates \(\widehat T_i\). Hence

\[
 H^0(X,I_{2Z}\otimes A)
 =\left(S_Z+\sum_i\widehat T_i\right)^\perp. \tag{5}
\]

Combining (4), (5) and taking double annihilators gives

\[
 H^0(I_Z A)=H^0(I_{2Z}A)
 \quad\Longleftrightarrow\quad
 \widehat T_i\subset S_Z\quad\text{for every }i. \tag{6}
\]

This is the exact projective form of a zero conditional-gradient quotient.

## Full-span and contact branches

If \(S_Z=W^*\), (6) is automatic because no nonzero hyperplane section
contains all of \(Z\). This is the **full-span branch**; it carries no
tangency information.

If \(S_Z\subsetneq W^*\), put \(L_Z=\mathbf P(S_Z)\). Equation (6) says

\[
 T_{X,p_i}\subset L_Z\quad(1\le i\le N). \tag{7}
\]

Thus the proper secant span of the points contains the entire embedded
tangent space at each of its marked points. Its tangential contact locus

\[
 \{x\in X:T_{X,x}\subset L_Z\} \tag{8}
\]

contains \(Z\). Since \(\widehat T_i\) has dimension \(d+1\), a proper
absorbing span must satisfy

\[
 \dim S_Z\ge d+1. \tag{9}
\]

For G125, take \(A=H^k\) for every \(1\le k<m\). B194's extinction is
equivalent to requiring (6) simultaneously in every lower embedding. B196
does not construct such a configuration, prove that its contact locus is
zero-dimensional, produce ODPs, or supply a Hodge detector.
