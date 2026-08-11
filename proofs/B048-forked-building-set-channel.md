---
brick_id: B048
status: PROVED
base_field: C
variety: a five-dimensional nodal smoothing slice with eleven central discriminant hyperplanes whose nontrivial connected-flat building set is a fork with two rank-two children inside one rank-four parent, together with its wonderful resolution
smoothness: the parameter fivefold and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber has only ordinary double points and nearby fibers are smooth
projectivity: the wonderful blow-up morphisms and exceptional strata are projective over their centers, and the fiber Z is projective; the parameter calculation is local analytic, while the realizing hypersurface family is projective
dimension: parameter dimension 5, exceptional fiber dimension 4, parent-flat dimension 1, child-flat dimensions 3, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the two children have codimension 2, their connected parent has codimension 4, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B015, B045-B047, B134, G019-G020, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: For the explicit rank-five fork arrangement, both blow-up orders give the same channel; its polarized homological model is the full rational relation kernel, its cohomological stalk is the dual, and both are pure type (0,0) after Q(n).
falsifier: an unintended connected flat, intersecting child centers after the parent blow-up, different divisor or residue matrices for the two orders, a non-full-support contribution in ordinary degree one, or a non-(0,0) component after Q(n)
---

# B048 - Forked building-set channel

This brick proves G020 for its explicit fork.

## Arrangement and multipart realization

Use the eleven coefficient columns displayed in G020 and set

\[
 A=\{1,2,3\},\qquad B=\{4,5,6\},\qquad
 U=\{1,\ldots,7\},\qquad E=\{1,\ldots,11\}.
\]

Exact rank and partition enumeration gives

\[
 r(A)=r(B)=2,\qquad r(U)=4,\qquad r(E)=5,
\]

and proves that these are the only connected flats with at least two
elements. Connectedness is tested by excluding every rank-additive
decomposition. The eleven branches partition into the independent blocks

\[
 \{1,2,4,5\}\sqcup\{3,6,7,8\}\sqcup\{9,10,11\}.
\]

The jet-separation and analytic-submersion construction in B047 applies to
this matrix verbatim: for a sufficiently high-degree hypersurface family it
realizes the fork as an actual projective analytic nodal slice. This validates
the local model but supplies no primitive detector.

## The two child blow-ups commute

The geometric flats satisfy

\[
 F_U=F_A\cap F_B,qquad
 \dim F_A=\dim F_B=3,qquad \dim F_U=1,qquad
 F_A+F_B=\mathbf C^5.
\]

After blowing up the origin, write

\[
 p=\mathbf P(F_U),\qquad
 \Pi_A=\mathbf P(F_A),\qquad
 \Pi_B=\mathbf P(F_B)\subset\mathbf P^4.
\]

The two planes meet only at \(p\). In the exceptional
\(\mathbf P(T_p\mathbf P^4)\simeq\mathbf P^3\) of
\(\operatorname{Bl}_p\mathbf P^4\), their strict transforms meet the
exceptional divisor in the disjoint lines
\(\mathbf P(F_A/F_U)\) and \(\mathbf P(F_B/F_U)\). Hence
\(\widetilde\Pi_A\cap\widetilde\Pi_B=\varnothing\).

Blow-ups along disjoint centers commute canonically, so both permissible
orders give

\[
 Z\simeq
 \operatorname{Bl}_{\widetilde\Pi_B}
 \operatorname{Bl}_{\widetilde\Pi_A}
 \operatorname{Bl}_p\mathbf P^4
 \simeq
 \operatorname{Bl}_{\widetilde\Pi_A}
 \operatorname{Bl}_{\widetilde\Pi_B}
 \operatorname{Bl}_p\mathbf P^4.
\]

Li S038 supplies the smooth/SNC wonderful-model statement; the displayed
disjointness proves order independence in this particular fiber.

## Divisor classes and residue kernel

Let \(h,e_U,e_A,e_B\) be the pullback hyperplane and exceptional classes.
For either child order,

\[
 [M_i]=
 \begin{cases}
 h-e_U-e_A,&i\in A,\\
 h-e_U-e_B,&i\in B,\\
 h-e_U,&i\in U\setminus(A\cup B),\\
 h,&i\notin U.
 \end{cases}
\]

The four classes are independent. Put
\(W_C=\operatorname{span}_{\mathbf Q}\{\delta_i:i\in C\}\). The same
Picard-Lefschetz lift calculation as in B042-B047 gives the residue
transgression

\[
\begin{aligned}
 h&\otimes\sum_i a_i\delta_i\\
 {}+e_U&\otimes\left(w_U-\sum_{i\in U}a_i\delta_i\right)\\
 {}+e_A&\otimes\left(w_A-\sum_{i\in A}a_i\delta_i\right)\\
 {}+e_B&\otimes\left(w_B-\sum_{i\in B}a_i\delta_i\right).
\end{aligned}
\]

There is no \(e_Ae_B\) incidence row because the child exceptional
divisors are disjoint. The common-parent equation is independent of the two
child equations. Projection to \((a_i)\) is therefore canonically the full
relation kernel, with inverse assigning the three partial sums. Since both
orders identify the same named exceptional classes over the same centers,
this isomorphism is order independent.

## Strict-support and Hodge audits

The possible connected strict supports are \(F_A,F_B,F_U\), and the origin.

- Each codimension-two child has the semismall rank-two normal model, so its
  lower-support summands begin in ordinary degree two.
- Over generic \(F_U\), the normal fiber dimension is at most three. The
  perverse defect is at most \(2\), and a codimension-four support begins in
  ordinary degree \(4-2=2\).
- Over the origin, the projective fiber has dimension four. Point-supported
  perverse degrees lie in \([-3,3]\), hence ordinary degrees \(2\) through
  \(8\).
- Every disconnected arrangement stratum is a transverse product of these
  connected normal models with SNC coordinate factors, which cannot lower
  the ordinary degree.

Thus no non-full support contributes in degree one. Saito's rational
projective direct-image and strict-support decomposition identifies the
resolved kernel with \(H^1(IC_B(L_{\mathbf Q})_0)\).

After \(\mathbf Q(n)\), all branch and exceptional coefficients are sums of
\(\mathbf Q(0)\), and the residue differential is a morphism of rational
mixed Hodge structures. The kernel is therefore pure type \((0,0)\).

## Scope guard

B048 proves one fork and no arbitrary-building-set induction. It produces no
algebraic cycle and no class-specific extra-to-primitive pairing. G019,
G015, and the standard rational Hodge Conjecture remain open.
