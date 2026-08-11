---
brick_id: B045
status: PROVED
base_field: C
variety: a three-dimensional nodal smoothing slice with seven central discriminant hyperplanes and exactly two dependent triples sharing one branch, together with its wonderful resolution
smoothness: the parameter threefold and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber has seven ordinary double points and nearby fibers are smooth
projectivity: all blow-ups and exceptional strata are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 3, exceptional fiber dimension 2, dependent flats dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the origin has codimension 3, each dependent flat has codimension 2, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure of type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B043-B044, B134, G017, Green-Griffiths S021, and Saito S022/S037
claim: For seven rank-three branches with dependent triples {1,2,3} and {1,4,5}, the polarized homological model dual to the downstairs cohomological IC channel is the full rational relation kernel, and both are pure type (0,0) after Q(n).
falsifier: incompatibility of the two exceptional partial-sum equations, an ordinary-degree-one summand supported on either dependent flat or the origin, or a non-(0,0) kernel component after Q(n)
---

# B045 - Two-dependent-flat relation channel

This brick proves G017.

## Exceptional fiber and divisor classes

Let \(F_A=H_1\cap H_2\cap H_3\) and
\(F_B=H_1\cap H_4\cap H_5\). After blowing up the origin, their strict
transforms meet the exceptional plane at distinct points \(p_A,p_B\in L_1\)
and are disjoint. Blow up both curves. The fiber over the origin is

\[
 Z=\operatorname{Bl}_{\{p_A,p_B\}}\mathbf P^2.
\]

Write \(C_A,C_B\) for the exceptional curves and \(e_A,e_B\) for their
classes. With \(h\) the pullback hyperplane class, the branch curves satisfy

\[
\begin{aligned}
 [M_1]&=h-e_A-e_B,\\
 [M_2]=[M_3]&=h-e_A,\\
 [M_4]=[M_5]&=h-e_B,\\
 [M_6]=[M_7]&=h.
\end{aligned}
\]

The curves \(C_A,C_B,M_1,\ldots,M_7\) form an SNC divisor. Although \(M_1\)
meets both exceptional curves, \(C_A\cap C_B=\varnothing\).

## Exceptional cohomology sheaf

Put

\[
 W_A=\operatorname{span}\{\delta_1,\delta_2,\delta_3\},
 \qquad
 W_B=\operatorname{span}\{\delta_1,\delta_4,\delta_5\}.
\]

All products of the branch and exceptional logarithms vanish. The lift
calculation of B044 therefore gives

\[
 \mathcal H^0(A|_Z)=K_Z,
 \qquad
 \mathcal H^1(A|_Z)=
 (W_A)_{C_A}\oplus(W_B)_{C_B}
 \oplus\bigoplus_{i=1}^7\mathbf Q_{M_i},
 \qquad
 \mathcal H^{\ge2}(A|_Z)=0.
\]

## Three-component residue kernel

In the basis \(h,e_A,e_B\), the residue transgression sends
\((w_A,w_B,a_1,\ldots,a_7)\) to

\[
\begin{aligned}
 h&\otimes\sum_{i=1}^7a_i\delta_i\\
 {}+e_A&\otimes
 \left(w_A-a_1\delta_1-a_2\delta_2-a_3\delta_3\right)\\
 {}+e_B&\otimes
 \left(w_B-a_1\delta_1-a_4\delta_4-a_5\delta_5\right).
\end{aligned}
\]

Thus its kernel is defined by

\[
 \sum_{i=1}^7a_i\delta_i=0,
 \quad
 w_A=a_1\delta_1+a_2\delta_2+a_3\delta_3,
 \quad
 w_B=a_1\delta_1+a_4\delta_4+a_5\delta_5.
\]

The shared coefficient \(a_1\delta_1\) causes no conflict: the last two
equations occupy the independent divisor classes \(e_A,e_B\), and their
right sides lie automatically in \(W_A,W_B\). Projection to
\((a_1,\ldots,a_7)\) is therefore a canonical isomorphism onto the full
vanishing-cycle relation kernel.

## Supports and Hodge type

Away from the origin, each dependent-flat resolution is locally the product
of its smooth flat with B041's semismall rank-two resolution. The two strict
transforms are disjoint, so possible strict supports \(F_A,F_B\) occur only
in perverse degree zero. At the origin the exceptional fiber is a surface,
giving total perverse amplitude \([-1,1]\), as in B044.

After undoing the ambient shift, the flat-supported IC summands and the
lowest point-supported summands begin in ordinary degree two. None affects
degree one. Proper base change and strict-support decomposition identify the
resolved kernel with the downstairs full-support IC stalk.

After \(\mathbf Q(n)\), \(W_A,W_B\) and every branch coefficient are Tate
type \((0,0)\). The residue kernel and its downstairs image have the same
pure type.

## Scope guard

B045 proves compatibility for two non-nested dependent flats in rank three.
It does not prove the wonderful-model theorem for arbitrarily many flats or
for nested flats, and it constructs no algebraic cycle. The rational Hodge
Conjecture and G015 remain open.
