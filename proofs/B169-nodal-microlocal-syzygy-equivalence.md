---
brick_id: B169
status: PROVED
base_field: C
variety: a smooth complete-linear-system parameter germ P, the smooth projective universal hypersurface incidence h:U->P, and a smooth basis-node germ i:F_B->P through a fiber with N tracked ordinary double points
smoothness: P, U, F_B, and every labeled nodal discriminant branch D_j are smooth; after shrinking, every singularity is one of the N tracked ODPs and all spatial Hessians remain nondegenerate
projectivity: h is projective; the branchwise microlocal calculation is local analytic
dimension: arbitrary smooth base dimension d; hypersurface dimension 2n-1 in the Hodge application; value rank R<N and dim F_B=d-R
codimension: every D_j is a divisor; F_B is the transverse intersection of R basis branches; the simultaneous-node germ has desired codimension R
coefficient_field: Q for constructible sheaves and C for analytic critical-value equations
cohomology_theory: rational proper direct images, constructible functions, microsupport, microlocal inverse image, higher-discriminant envelopes, ODP vanishing cycles, and convergent analytic local algebra
hodge_type: none asserted; the rational type-(0,0) specified Saito pairing remains a separate downstream obligation
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic representative of a Hodge class is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B168, S030, S066-S068
claim: In an exhaustive tracked-ODP neighborhood, the ambient characteristic envelope is the zero section together with the conormals of the labeled nodal divisors. For a basis-node germ F_B, zero microlocal normal-cone image of either the actual proper-direct-image microsupport or the full envelope is equivalent to persistence of every tracked node, hence to H_tau=0 and analytic lifting of every linear critical-value relation.
falsifier: an additional envelope covector not arising from a tracked critical point, a nodal conormal absent from the actual sheaf microsupport, a branch not containing F_B but having zero i-sharp image, or a branch containing F_B with nonzero i-sharp image
---

# B169 — Nodal microlocal absorption is exactly analytic syzygy lifting

Let \(h:\mathcal U\to P\) be the universal hypersurface map near a member
with \(N\) labeled ordinary double points. Shrink \(P\) so that there are
disjoint spatial Morse charts, no singularities outside them, and one
analytic critical-value function

\[
 \tau_j:(P,0)\longrightarrow(\mathbf C,0)
\]

for each chart. Assume \(d\tau_j(0)\ne0\), as in the uniform-matroid
application, and put \(D_j=\{\tau_j=0\}\).

## The ambient envelope has only the nodal conormals

At a smooth point of \(h\), the differential is surjective and contributes
only the zero covector to \(h^\dagger(0_{\mathcal U})\). At the unique
critical point in the \(j\)-th Morse chart over \(t\in D_j\), the image of
\(dh\) is

\[
 \ker d\tau_j(t)\subset T_tP.
\]

Its annihilator is the line spanned by \(d\tau_j(t)\). Consequently, on
this exhaustive neighborhood,

\[
 h^\dagger(0_{\mathcal U})
 =0_P\cup\bigcup_{j=1}^N T^*_{D_j}P. \tag{1}
\]

This also follows from the tangent description behind
Migliorini--Shende Theorem C, but (1) is stronger bookkeeping than merely
listing possible higher-discriminant supports: distinct critical points
give a union of annihilator lines, not their linear span.

Every nodal conormal actually occurs in the sheaf microsupport. Group
coincident divisor germs, if any, and take a generic point of one distinct
reduced component away from all the others. The fiber there acquires
\(k\ge1\) tracked ODPs, where \(k\) is the multiplicity of that component
in the labeled list. The Euler--Milnor jump is the same nonzero signed
multiple \(k\), so the pushed-forward constructible function has the
component conormal in its singular support. Migliorini--Shende equation
(2.6) then gives

\[
 \bigcup_jT^*_{D_j}P
 \subseteq SS(Rh_*\mathbf Q_{\mathcal U})
 \subseteq h^\dagger(0_{\mathcal U}). \tag{2}
\]

There is no alternating-cancellation inference here: the generic jump
along each distinct branch component is a nonzero positive multiple of
the one-ODP jump.

## Exact branchwise pullback criterion

Let \(i:F\hookrightarrow P\) be any smooth closed germ through the central
point and let \(D\subset P\) be one of the smooth divisors above. Then

\[
 i^\#T^*_DP\subseteq0_F
 \quad\Longleftrightarrow\quad
 F\subseteq D\text{ as an analytic set germ}. \tag{3}
\]

If \(F\subseteq D\), simultaneous submanifold coordinates may be chosen
so that

\[
 F=\{x_1=\cdots=x_r=0\},\qquad D=\{x_1=0\}.
\]

The conormal to \(D\) is spanned by \(dx_1\), with zero component in the
cotangent directions of \(F\). Kashiwara--Schapira's coordinate
description of \(i^\#\) therefore gives only the zero section.

Conversely, suppose \(F\not\subset D\). The restriction of a defining
equation of \(D\) is then a nonzero analytic function on the smooth germ
\(F\), and its zero set has a dense smooth divisor locus. Regard
\(\mathbf Q_D\) as a sheaf on \(P\). Locally at a smooth point of that
reduced pullback divisor,

\[
 SS(\mathbf Q_D)=T^*_DP,
 \qquad
 SS(i^{-1}\mathbf Q_D)
 =SS(\mathbf Q_{D\cap F})
 \supset T^*_{(D\cap F)_{\mathrm{red}}}F.
\]

Kashiwara--Schapira Corollary 6.4.4 puts the nonzero conormal on the right
inside \(i^\#T^*_DP\). This proves (3), including nonreduced contacts such
as \(y^m=0\).

## Collapse to the hidden-generator gate

Choose a value-matroid basis \(B\) and set

\[
 F_B=\bigcap_{b\in B}D_b.
\]

It is smooth of codimension \(R\). Combining (1)--(3) gives

\[
 \begin{aligned}
 i^\#SS(Rh_*\mathbf Q_{\mathcal U})\subseteq0_{F_B}
 &\Longleftrightarrow
 i^\#h^\dagger(0_{\mathcal U})\subseteq0_{F_B}\\
 &\Longleftrightarrow
 F_B\subseteq D_j\quad\text{for every }j. \tag{4}
 \end{aligned}
\]

For the first equivalence, the forward implication uses the left
inclusion in (2), while the reverse implication uses the right inclusion.
B158 identifies the last condition with vanishing of every escape germ.
B155--B156 identify it further with

\[
 H_\tau=0,
\]

equivalently analytic lifting of every linear relation among the
\(d\tau_j(0)\).

Thus G106's microlocal clause is not a weaker route around G100/G101 in
the exact tracked-ODP setting. It is the same all-order analytic syzygy
obligation in cotangent language. The uniform matroid, rational Hodge
type, nonzero primitive image, and specified Saito pairing remain
unproved.
