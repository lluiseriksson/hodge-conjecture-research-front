---
brick_id: NG136
status: NO-GO
base_field: C
variety: a one-parameter affine polynomial Morse family on A^1, serving only as an exact test of the proposed Jacobi-residue mechanism
smoothness: the parameter line is smooth and the three critical points are fixed, distinct, and Morse
projectivity: the model is affine; its failure is the polynomial degree and residue-at-infinity obstruction that any projective compactification must explicitly repair
dimension: one spatial variable; two tracked critical points; one auxiliary critical point; tracked central rank R=1<N=2
codimension: the tracked simultaneous-zero germ is the reduced divisor (t=0), and its one linear relation already lifts analytically
coefficient_field: C
cohomology_theory: one-variable Grothendieck residues, Jacobi's degree bound, and analytic syzygies
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no Hodge class or algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156, B172, G100, S069
claim: A global Jacobi residue identity automatically supplies admissible numerators that isolate the tracked critical values and lift their complete central relation space.
falsifier: f_t(z)=(z^2-1)^2+t has the exact tracked syzygy tau_-=tau_+=t, but every nonzero numerator f_t A exceeds Jacobi's allowed degree; the would-be critical-value residue has a nonzero residue at infinity
---

# NG136 — Global residues do not automatically isolate tracked nodes

Consider

\[
 f_t(z)=(z^2-1)^2+t.
\]

Its critical points are \(-1,0,1\). Track \(-1\) and \(1\), and treat \(0\)
as auxiliary. Their critical values and Hessians are

\[
 \tau_-(t)=t,\quad \nu_0(t)=1+t,\quad \tau_+(t)=t,
 \qquad
 f_t''(-1)=8,\quad f_t''(0)=-4,\quad f_t''(1)=8.
\]

The tracked value map has rank one and the unique central relation already
lifts:

\[
 \tau_- - \tau_+=0.
\]

Nevertheless \(P_t=f_t'=4z(z^2-1)\) has degree three, so Jacobi's bound in
one variable is

\[
 \deg Q\le 3-1-1=1.
\]

Every nonzero polynomial numerator of the selector form \(Q=f_tA\) has
degree at least four. It is therefore outside the vanishing theorem. The
failed substitution is visible symbolically:

\[
 \sum_{f_t'(p)=0}\frac{f_t(p)}{f_t''(p)}
 =\frac t8-\frac{1+t}{4}+\frac t8=-\frac14.
\]

The missing \(1/4\) is the contribution at infinity. By contrast, the
admissible constant numerator gives

\[
 \frac18-\frac14+\frac18=0,
\]

but contains no critical values and yields no tracked-value syzygy.

This example does not obstruct all possible residue constructions and is
not a Hodge counterexample. It falsifies only the automatic step from a
global residue theorem to the selectors required in B172. Re-entry requires
an explicit bounded-degree selector/interpolation theorem for the complete
critical configuration, plus control of auxiliary and infinity terms and
all detector clauses.
