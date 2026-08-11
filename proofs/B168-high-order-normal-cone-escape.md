---
brick_id: B168
status: PROVED
base_field: C
variety: the B159 smooth ambient ODP discriminant branch D_N in a projectively realizable analytic parameter germ P, restricted to its smooth basis germ F_B
smoothness: D_N and F_B are smooth; their scheme-theoretic pullback is the nonreduced divisor y^m=0
projectivity: B157 realizes the critical-value model after nonlinear analytic pullback in a projective hypersurface family
dimension: ambient base dimension R+1 or more; basis dimension at least one; arbitrary contact order m at least 2
codimension: D_N and the reduced internal escape locus y=0 are divisors; F_B has codimension R
coefficient_field: Q for the constructible direct image and C for analytic equations
cohomology_theory: ODP vanishing cycles, microsupport, microlocal inverse image, conormal geometry, and analytic critical-value germs
hodge_type: no specified detector type or pairing is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B167, S030, S052, S068
claim: In the B159 branch tau_N=ell_N(x)+y^m with F_B={x=0}, every ambient conormal over D_N intersect F_B is pointwise contained in N^*F_B, but the microlocal normal-cone inverse image contains the nonzero conormal to the reduced internal divisor {y=0}. Hence pointwise conormal quotient data miss the high-order escape detected by i-sharp.
falsifier: a nonzero restriction of d tau_N to T F_B on D_N intersect F_B, local constancy of the restricted ODP family across y=0, or exclusion of T^*_{y=0}F_B from i-sharp T^*_{D_N}P
---

# B168 — Higher-order contact survives in the microlocal normal cone

Use B159's coordinates

\[
 P=(x_1,\ldots,x_R,y),\qquad F_B=\{x_1=\cdots=x_R=0\},
\]

and its last discriminant branch

\[
 D_N=V(\tau_N),\qquad \tau_N=\ell_N(x)+y^m,\quad m\ge2.
\]

Because \(d\ell_N\ne0\), \(D_N\) is smooth. Its scheme-theoretic pullback
to \(F_B\) is \(y^m=0\), whose reduced support is the divisor
\(D_B=\{y=0\}\).

At every point of \(D_N\cap F_B\),

\[
 d\tau_N=d\ell_N+m y^{m-1}dy=d\ell_N,
\]

so

\[
 T^*_{D_N}P|_{D_N\cap F_B}\subseteq N^*_{F_B}P. \tag{1}
\]

The naive pointwise quotient of these ambient covectors in \(T^*F_B\) is
therefore zero.

Nevertheless, the restricted family has critical value \(y^m\). Its
special fiber has the tracked ODP and its nearby fibers are smooth. B162
gives a rank-one specialization group, and B166 gives

\[
 T^*_{D_B}F_B\subseteq SS(K_B). \tag{2}
\]

Disjoint spatial Milnor balls split the vanishing-cycle object by tracked
node, even when two base conormal directions coincide. Every other node
branch is independent of \(y\), so its base restriction is constant and
its normal-cone inverse image has no \(dy\) direction. The last Milnor ball
has rank one, and applying B167 to this localized contribution yields

\[
 T^*_{D_B}F_B
 \subseteq i^\#\overline{T^*_{D_N}P}. \tag{3}
\]

Equations (1)--(3) show that \(i^\#\) is strictly stronger than restricting
ambient covectors pointwise and quotienting by \(N^*F_B\). It records the
normal cone of the order-\(m\) contact. Since \(m\) is arbitrary, any fixed
jet-order test can miss this component.

## Scope guard

This is a nonlinear-base projective realization, not an impossibility
theorem for the full linear-system germ. It supplies no Hodge detector.
