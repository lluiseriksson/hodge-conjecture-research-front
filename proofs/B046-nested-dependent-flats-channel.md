---
brick_id: B046
status: PROVED
base_field: C
variety: a four-dimensional nodal smoothing slice with a dependent codimension-three flat contained in a dependent codimension-two flat, and its wonderful resolution
smoothness: the parameter fourfold and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber is nodal and nearby fibers are smooth
projectivity: all blow-ups and exceptional strata are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 4, exceptional fiber dimension 3, dependent-flat dimensions 1 and 2, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the nested flats have codimensions 3 and 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B043-B045, G018, Green-Griffiths S021, and Saito S022/S037
claim: For the rank-four nested-flat model with three branches through F_S and five through F_T contained in F_S, the wonderful-resolution degree-one IC channel is canonically the full rational relation kernel and is pure type (0,0) after Q(n).
falsifier: a nontriangular nested residue equation, a strict-support summand on F_S, F_T, or the origin contributing in ordinary degree one, or a non-(0,0) kernel component after Q(n)
---

# B046 - Nested-dependent-flat relation channel

This brick proves G018 for an explicit minimal nested model.

## Realizable arrangement and building set

In coordinates \(x_1,\ldots,x_4\), take the first five branch forms

\[
 x_1,\quad x_2,\quad x_1+x_2,\quad x_3,
 \quad x_1+2x_2+3x_3.
\]

The set \(S=\{1,2,3\}\) cuts out the codimension-two flat
\(F_S=\{x_1=x_2=0\}\). The set \(T=\{1,2,3,4,5\}\) cuts out the contained
codimension-three flat \(F_T=\{x_1=x_2=x_3=0\}\subset F_S\). Add four
sufficiently general forms with nonzero \(x_4\)-coefficient, so there are no
other non-SNC positive-dimensional flats. They may be chosen so that
\(\{1,4,6\}\), \(\{2,5,7\}\), and \(\{3,8,9\}\) are three independent
smoothing blocks. The coefficient vectors of the first five forms have rank
three, and every triple among them other than \(S\) has rank three; thus the
only proper dependent flat inside \(T\) is the stated \(F_S\).

Blow up the origin, then the strict transform of \(F_T\), then that of
\(F_S\). The fiber over the origin is

\[
 Z=\operatorname{Bl}_{\widetilde\ell}
   \operatorname{Bl}_{p}\mathbf P^3,
 \qquad
 p=\mathbf P(F_T)\in\ell=\mathbf P(F_S).
\]

Here \(\widetilde\ell\) is the strict transform of \(\ell\).

## Divisor classes and coefficient spaces

Let \(h\) be the pullback hyperplane class and let \(e_T,e_S\) be the
classes of the exceptional divisors over \(p\) and \(\widetilde\ell\).
The strict branch divisors have classes

\[
 [M_i]=
 \begin{cases}
 h-e_T-e_S,&i\in S,\\
 h-e_T,&i\in T\setminus S,\\
 h,&i\notin T.
 \end{cases}
\]

The earlier exceptional divisor is not blown up along a contained center:
\(\widetilde\ell\) meets it transversely at one point. Its strict-transform
class remains \(e_T\); the new exceptional class is \(e_S\).

Put

\[
 W_S=\operatorname{span}\{\delta_i:i\in S\},
 \qquad
 W_T=\operatorname{span}\{\delta_i:i\in T\},
 \qquad W_S\subseteq W_T\subseteq W.
\]

All products of branch and exceptional logarithms vanish. The degree-one
exceptional cohomology sheaf is the direct sum of the branch coefficient
lines, the \(W_T\)-sheaf on the first flat-exceptional divisor, and the
\(W_S\)-sheaf on the second. Nested incidence adds simultaneous stalks but
no new quotient.

## Triangular residue kernel

In the divisor basis \(h,e_T,e_S\), the residue transgression sends
\((w_T,w_S,(a_i))\) to

\[
\begin{aligned}
 h&\otimes\sum_i a_i\delta_i\\
 {}+e_T&\otimes\left(w_T-\sum_{i\in T}a_i\delta_i\right)\\
 {}+e_S&\otimes\left(w_S-\sum_{i\in S}a_i\delta_i\right).
\end{aligned}
\]

Its kernel conditions are triangular:

\[
 \sum_i a_i\delta_i=0,
 \qquad
 w_T=\sum_{i\in T}a_i\delta_i,
 \qquad
 w_S=\sum_{i\in S}a_i\delta_i.
\]

The containment \(W_S\subset W_T\) produces no extra equation because
\(e_S,e_T\) are independent divisor classes. Projection onto the \(a_i\)
is a canonical isomorphism from the resolved kernel to the full global
vanishing-cycle relation space.

## Strict-support audit

The proper map has possible non-full strict supports on \(F_S\), \(F_T\),
and the origin.

- Generically on the codimension-two flat \(F_S\), the normal resolution is
  rank two and semismall; its summands begin in ordinary degree two.
- Generically on the codimension-three flat \(F_T\), the normal resolution
  has perverse amplitude \([-1,1]\). A perverse summand supported on the
  one-dimensional \(F_T\) in degree \(j\ge-1\) appears after the ambient
  shift in ordinary degree \(3+j\ge2\).
- At the origin, the exceptional fiber has dimension three. Its two-row
  complex has ordinary hypercohomology through degree six, so after the
  dimension-four shift the point-supported perverse range is contained in
  \([-2,2]\), giving ordinary degrees \(2\) through \(6\).

Thus no non-full-support summand appears in ordinary degree one. Proper base
change and Saito strict-support decomposition transfer the resolved kernel
canonically to \(H^1(IC_B(L_{\mathbf Q})_0)\).

## Hodge type

After \(\mathbf Q(n)\), all branch, \(W_S\), and \(W_T\) coefficients are
sums of \(\mathbf Q(0)\). The SNC residue differential is a morphism of
rational mixed Hodge structures, so its kernel and the downstairs IC stalk
are pure type \((0,0)\).

## Scope guard

B046 proves one nested pair. It does not yet prove a building-set theorem
for arbitrary arrangements, construct a class-paired nodal incidence, or
produce an algebraic cycle. The rational Hodge Conjecture and G015 remain
open.
