---
brick_id: B216
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a reduced marked point scheme Z, and the complete G143 package at the minimal B215 node count
smoothness: X and Z are smooth; the central divisor and incidence smoothness are only those separately required by G143
projectivity: X, all powers H^k through m, the marked point spans, affine first and second osculating spaces, and relation transports are projective
dimension: dim X=d; for m=2 the saturated rank is d+1, while for m>=3 the saturated degree-two rank is c_d=binom(d+2,2); the Hodge branch has d=2n
codimension: equality N=D_d(m) saturates B215's complementary-rank inequality and forces common marked tangent spaces for m=2 or common marked second osculating spaces for m>=3
coefficient_field: C for sections, values, osculating spaces, relations, and transport isomorphisms; Q remains separately required for the Hodge class and detector
cohomology_theory: coherent restriction to finite schemes, principal parts through order two, graded section multiplication, and finite-dimensional annihilator duality
hodge_type: none asserted; the rational type-(0,0) detector and specified pairing remain separate G143 clauses
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B213-B215, G143
claim: If a G143 configuration has N=D_d(m), then for m=2 its degree-one point span has dimension d+1 and equals every marked affine tangent space, and M_(lambda,1):E_1->R_1 is an isomorphism. If m>=3, h_Z(2)=c_d, h_Z(m-2)=L_d(m-2), the degree-two point span equals every marked affine second osculating space, and M_(lambda,2):E_2->R_(m-2) and M_(lambda,m-2):E_(m-2)->R_2 are isomorphisms.
falsifier: a minimal-window G143 configuration with a strict lower-rank inequality, two unequal marked osculating spaces of the stated order, or a nonsurjective displayed transport map
---

# B216 — Equality saturates the simultaneous-jet window

Put

\[
 c_d=\binom{d+2}{2}.
\]

Assume the complete hypotheses of G143 and the extremal equality

\[
 N=D_d(m).
\]

## Birth degree two

When \(m=2\), B213 and B215 give

\[
 2h_Z(1)\le N=2(d+1),\qquad h_Z(1)\ge d+1.
\]

Thus \(h_Z(1)=d+1\). Lower extinction and B196 place every marked
affine embedded tangent space, each of vector dimension \(d+1\), inside
the degree-one point span. Equal dimensions force

\[
 S^{(0)}_{1,Z}=\widehat T_{p_i}X
 \quad\text{for every }p_i\in Z. \tag{1}
\]

The full-support relation transport
\(M_{\lambda,1}:E_1\hookrightarrow\mathcal R_1\) is between two
\((d+1)\)-dimensional spaces, hence is an isomorphism.

## Birth degree at least three

For \(m\ge3\), use the complementary split \((2,m-2)\). The corrected
B215 formula satisfies the exact identity

\[
 D_d(m)=L_d(2)+L_d(m-2)=c_d+L_d(m-2). \tag{2}
\]

B213 and B215 therefore give

\[
 c_d+L_d(m-2)
 \le h_Z(2)+h_Z(m-2)
 \le N
 =c_d+L_d(m-2). \tag{3}
\]

Every inequality in (3) is an equality:

\[
 h_Z(2)=c_d,\qquad h_Z(m-2)=L_d(m-2). \tag{4}
\]

B214 and lower two-layer extinction place the full affine second
osculating space at each marked point inside \(S^{(0)}_{2,Z}\). Both
spaces have vector dimension \(c_d\), so

\[
 S^{(0)}_{2,Z}=\widehat O^{(2)}_{p_i}(H^2)
 \quad\text{for every }p_i\in Z. \tag{5}
\]

Finally, B213 supplies injections

\[
 M_{\lambda,2}:E_2\hookrightarrow\mathcal R_{m-2},
 \qquad
 M_{\lambda,m-2}:E_{m-2}\hookrightarrow\mathcal R_2. \tag{6}
\]

Equations (3)-(4) identify the source and target dimensions in each
map, so both maps are isomorphisms.

This is rigidity, not existence. It constructs no extremal marked
scheme, central nondegenerate profile, holonomy, rational detector,
specified pairing, algebraic cycle, or proof of the Hodge Conjecture.
