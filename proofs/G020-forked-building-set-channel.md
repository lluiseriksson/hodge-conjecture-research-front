---
brick_id: G020
status: PROVED
base_field: C
variety: a five-dimensional nodal smoothing slice with eleven central discriminant hyperplanes whose nontrivial connected-flat building set consists of two incomparable rank-two flats inside one rank-four parent and the rank-five origin
smoothness: the parameter fivefold is smooth; the central projective fiber has only ordinary double points and nearby fibers are smooth; a wonderful resolution is required
projectivity: the wonderful blow-up morphisms and exceptional strata are projective over their centers, and fibers over the central point are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 5, parent-flat dimension 1, child-flat dimensions 3, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the children have codimension 2, their connected parent has codimension 4, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: the sought downstairs degree-one relation channel must be pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B045-B048, G019, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: For the explicit rank-five fork arrangement, the wonderful-resolution degree-one IC channel is independent of the order of the two child blow-ups and is canonically the full rational type-(0,0) vanishing-cycle relation kernel.
falsifier: the common-parent exceptional equation couples the two child partial sums, the two permissible child orders give different kernels, a fork-incidence strict support contributes in ordinary degree one, or the kernel has a non-(0,0) component after Q(n)
---

# G020 - Forked building-set channel

Take coefficient columns

\[
\begin{array}{c|rrrrrrrrrrr}
 i&1&2&3&4&5&6&7&8&9&10&11\\ \hline
 x_1&1&0&1&0&0&0&2&3&5&2&6\\
 x_2&0&1&1&0&0&0&8&4&4&1&5\\
 x_3&0&0&0&1&0&1&8&5&6&5&7\\
 x_4&0&0&0&0&1&1&1&7&5&1&8\\
 x_5&0&0&0&0&0&0&0&2&3&7&2.
\end{array}
\]

The proposed exact audit must verify that the nontrivial connected flats are

\[
 A=\{1,2,3\},\qquad B=\{4,5,6\},\qquad
 U=\{1,\ldots,7\},\qquad E=\{1,\ldots,11\},
\]

with ranks \(2,2,4,5\). Geometrically,
\(F_U=F_A\cap F_B\) and the two children are incomparable. After blowing
the origin and \(F_U\), the dominant transforms of \(F_A\) and \(F_B\)
should be disjoint and hence blowable in either order.

The falsifiable residue prediction, in the basis \(h,e_U,e_A,e_B\), is

\[
 \sum_i a_i\delta_i=0,
 \quad w_U=\sum_{i\in U}a_i\delta_i,
 \quad w_A=\sum_{i\in A}a_i\delta_i,
 \quad w_B=\sum_{i\in B}a_i\delta_i.
\]

A proof must compute both permissible blow-up orders and the complete
strict-support list. It may not infer the result by combining B045 and B047:
B045 has no common connected parent, while B047 has no incomparable
children. G020 constructs no algebraic cycle and proves nothing about the
standard rational Hodge Conjecture unless the local result is subsequently
embedded in the still-open G015-G013 chain.

B048 performs that audit. Exact enumeration verifies the fork and its
three-block partition. After the parent blow-up the child planes are
disjoint, so their blow-ups commute. Both orders give the same classes

\[
 h-e_U-e_A,quad h-e_U-e_B,quad h-e_U,quad h
\]

on the four branch groups, hence the same global, parent, and two child
residue equations. All non-full supports begin in ordinary degree two, and
the downstairs relation kernel is pure type \((0,0)\). G020 is proved only
for this fork; the later B052 proves G019 in general.
