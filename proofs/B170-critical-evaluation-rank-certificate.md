---
brick_id: B170
status: PROVED
base_field: C
variety: a smooth projective complex variety X, a line bundle L, an affine chart P of its complete linear system, and N disjoint tracked ODP critical-point sections in fixed local Morse gauges near a central nodal member
smoothness: X and P are smooth; the central singularities and all tracked spatial critical points have nondegenerate Hessian
projectivity: X and the hypersurface family are projective; the critical-point and rank calculations are local analytic
dimension: arbitrary parameter dimension; N critical values; central value-evaluation rank R<N; hypersurface dimension 2n-1 in the Hodge application
codimension: constant critical-evaluation rank R forces the simultaneous-node ideal to be reduced smooth of codimension R
coefficient_field: C for analytic critical values, evaluations, and ranks; Q only in downstream Hodge and vanishing-cycle applications
cohomology_theory: parameterized ODP deformation theory, principal-parts evaluation, analytic constant-rank theory, and convergent local algebra
hodge_type: none asserted; the rational type-(0,0) specified Saito pairing remains separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B169, G092, G100-G106, the analytic implicit-function and constant-rank theorems
claim: After fixing local frames that define the tracked critical-point sections, the differential of the ordered critical-value map at every nearby parameter is exactly evaluation of the parameter section at those moving critical points. If this chosen-gauge moving evaluation map has constant rank R near the central member, then the critical-value ideal has H_tau=0, admits the B155 rank-R factorization, and defines a reduced smooth codimension-R simultaneous-node germ.
falsifier: an extra critical-point-motion term in d tau, a constant-rank critical-value map with more than R minimal ideal generators, or failure of reduced smooth excess
---

# B170 — Constant critical-point evaluation rank kills \(H_\tau\)

Work in an affine chart of \(|L|\) through a section \(s_0\), written

\[
 s_t=s_0+t,\qquad t\in(W,0),
\]

where \(W\subset H^0(X,L)\) is a linear complement to \(\mathbf C s_0\).
Fix disjoint Morse charts around the \(N\) nodes. The implicit-function
theorem supplies a unique critical-point section

\[
 p_i:(W,0)\longrightarrow X
\]

in the \(i\)-th chart. In a local frame of \(L\), define

\[
 \tau_i(t)=s_t(p_i(t)).
\]

## Envelope identity

For \(v\in T_tW=W\), the chain rule gives

\[
 d\tau_i(t)(v)
 =v(p_i(t))
  +d_xs_t|_{p_i(t)}\bigl(dp_i(t)(v)\bigr).
\]

The second term is zero because \(p_i(t)\) is a spatial critical point.
Therefore

\[
 d\tau_i(t)(v)=v(p_i(t)). \tag{1}
\]

After choosing local frames at the moving points, the Jacobian

\[
 d\tau_t:W\longrightarrow\mathbf C^N
\]

is exactly the value-evaluation map at the moving critical configuration

\[
 Z(t)=(p_1(t),\ldots,p_N(t)). \tag{2}
\]

At fixed points, changing frames only rescales evaluation rows. However,
away from the discriminant it also changes which points solve the
critical-point equations. Thus (1)--(2) are identities in the fixed local
frames used to define \(p_i(t)\); constant rank of this extension is a
chosen-gauge sufficient certificate, not an intrinsic invariant of the
divisor germs.

## Constant-rank certificate

Assume

\[
 \operatorname{rank}d\tau_t=R
\quad\text{for every }t\text{ in a neighborhood of }0. \tag{3}
\]

The analytic constant-rank theorem gives source coordinates
\((u_1,\ldots,u_R,v)\) and a target coordinate change \(\psi\) such that

\[
 \psi\circ\tau=(u_1,\ldots,u_R,0,\ldots,0). \tag{4}
\]

Because \(\psi(0)=0\) and \(d\psi_0\) is invertible, the components of
\(\psi(\tau)\) and those of \(\tau\) generate the same analytic ideal.
Hence

\[
 I_\tau=(u_1,\ldots,u_R).
\]

It is reduced and smooth of codimension \(R\), has exactly \(R\) minimal
generators, and B155--B156 give

\[
 H_\tau=0
\]

together with the analytic rank-\(R\) factorization and syzygy lifts.

In these fixed gauges, let
\(\mathcal D_R\subset\operatorname{Conf}_N(X)\) be the
rank-at-most-\(R\) locus for value evaluation by \(W\). Since one
\(R\times R\) minor is nonzero at the central point, (3) holds exactly
when the critical-configuration map

\[
 p=(p_1,\ldots,p_N):(W,0)\longrightarrow\operatorname{Conf}_N(X)
\]

has image contained in \(\mathcal D_R\) as a germ.

## Strength guard

The criterion is sufficient, not necessary. For example,

\[
 \tau(x,y)=(x,(1+y)x)
\]

has \(I_\tau=(x)\) and \(H_\tau=0\), but \(d\tau\) has rank one on
\(x=0\) and rank two at points with \(x\ne0\). G100 only needs the ideal
factorization; G107 deliberately asks for the stronger determinantal
containment in a fixed gauge because it is a concrete target. A change of
local frame can alter the off-discriminant critical-point extension and
need not preserve this rank condition, although it preserves the
simultaneous-node ideal and \(H_\tau\). Neither condition produces the
specified Hodge pairing.
