---
brick_id: B047
status: PROVED
base_field: C
variety: a five-dimensional nodal smoothing slice with eleven central discriminant hyperplanes whose nontrivial connected-flat building set is a three-level chain, together with its wonderful resolution
smoothness: the parameter fivefold and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber has only ordinary double points and nearby fibers are smooth
projectivity: the wonderful blow-up morphisms and exceptional strata are projective over their centers, and the fiber Z is projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 5, exceptional fiber dimension 4, nested-flat dimensions 3, 2, and 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the three proper connected flats have codimensions 2, 3, and 4; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B015, B041-B046, G019, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: For the explicit rank-five arrangement whose nontrivial connected flats form one chain of ranks 2, 3, 4, and 5, the wonderful-resolution degree-one IC channel is canonically the full rational vanishing-cycle relation kernel and is pure type (0,0) after Q(n).
falsifier: an unintended connected flat in the explicit realization, a nontriangular four-class residue equation, a non-full-support summand contributing in ordinary degree one, or a non-(0,0) kernel component after Q(n)
---

# B047 - Three-level nested-chain channel

This is the first G019 test with three proper nested exceptional flats.

## Exact realizable arrangement

Let the eleven hyperplanes in \(\mathbf C^5\) have coefficient columns

\[
\begin{array}{c|rrrrrrrrrrr}
 i&1&2&3&4&5&6&7&8&9&10&11\\ \hline
 x_1&1&0&1&0&1&0&7&3&2&3&9\\
 x_2&0&1&1&0&2&0&5&3&4&1&6\\
 x_3&0&0&0&1&3&0&2&7&8&7&5\\
 x_4&0&0&0&0&0&1&2&5&2&5&4\\
 x_5&0&0&0&0&0&0&0&8&7&1&5.
\end{array}
\]

Put

\[
 S=\{1,2,3\}\subset T=\{1,\ldots,5\}
 \subset U=\{1,\ldots,7\}\subset E=\{1,\ldots,11\}.
\]

Exact rational rank enumeration gives ranks \(2,3,4,5\), respectively,
and proves that these four sets are the only connected flats with at least
two elements. Here connectedness is checked directly by the absence of a
partition \(A\sqcup B\) with
\(r(A)+r(B)=r(A\sqcup B)\), exactly the absence of a direct-sum
decomposition of the normal arrangement. Thus the only nontrivial members
of the minimal building set
are the flats \(F_S\supset F_T\supset F_U\supset\{0\}\). The same exact
enumeration verifies the independent-block partition

\[
 \{1,2,4,6\}\sqcup\{3,5,7,8\}\sqcup\{9,10,11\}.
\]

This is therefore a realizable three-block smoothing arrangement, not a
formal incidence poset.

## Projective realization guard

The matrix can occur in an actual projective nodal family. Fix eleven
general points of \(\mathbf P^{2n}\). For sufficiently large degree \(d\),
Serre vanishing makes the restriction map from
\(H^0(\mathbf P^{2n},\mathcal O(d))\) to their finite union of second-order
neighborhoods surjective. Choose a section whose first jets vanish and whose
quadratic terms are nondegenerate at all eleven points. Nondegeneracy is
open, and Bertini away from the base scheme gives a hypersurface with exactly
those eleven ordinary double points after a general choice.

The same jet surjectivity makes the local map from the hypersurface parameter
space to the product smoothing space \(\mathbf C^{11}\) a submersion. In
analytic coordinates it is a projection. Pulling the universal projective
family back along the explicit linear map \(\mathbf C^5\to\mathbf C^{11}\)
defined by the matrix therefore gives an analytic fivefold base with exactly
those discriminant hyperplanes and projective fibers. This realization is
used only to validate the geometric local model. Its ambient projective space
has no non-tautological primitive detector supplied by the construction.

## Wonderful fiber and divisor classes

Li's Theorems 1.2 and 1.3 (S038) justify the inclusion-compatible sequence
of smooth blow-ups and its SNC boundary. Blow up the origin, followed by the
dominant transforms of \(F_U,F_T,F_S\). If

\[
 p=\mathbf P(F_U)\subset\ell=\mathbf P(F_T)
 \subset\Pi=\mathbf P(F_S)\subset\mathbf P^4,
\]

the fiber over the origin is

\[
 Z=\operatorname{Bl}_{\widetilde\Pi}
   \operatorname{Bl}_{\widetilde\ell}
   \operatorname{Bl}_p\mathbf P^4.
\]

Let \(h\) be the pullback hyperplane class and \(e_U,e_T,e_S\) the three
exceptional divisor classes. Successive total-transform calculations give

\[
 [M_i]=
 \begin{cases}
 h-e_U-e_T-e_S,&i\in S,\\
 h-e_U-e_T,&i\in T\setminus S,\\
 h-e_U,&i\in U\setminus T,\\
 h,&i\notin U.
 \end{cases}
\]

The later centers meet, but are not contained in, the earlier exceptional
divisors. Hence their strict transforms retain classes \(e_U,e_T\), and
\(h,e_U,e_T,e_S\) are independent in \(H^2(Z,\mathbf Q)\).

## Four-component residue calculation

Write

\[
 W_S\subset W_T\subset W_U\subset W,
 \qquad
 W_A=\operatorname{span}_{\mathbf Q}\{\delta_i:i\in A\}.
\]

Every product of two Picard-Lefschetz logarithms is zero. The lift argument
of B042-B046 therefore identifies the degree-one coefficient sheaf with the
branch lines together with \(W_U,W_T,W_S\) on their exceptional divisors;
triple exceptional incidence adds simultaneous stalks, not a new quotient.
In the displayed divisor basis the residue transgression is

\[
\begin{aligned}
 h&\otimes\sum_i a_i\delta_i\\
 {}+e_U&\otimes\left(w_U-\sum_{i\in U}a_i\delta_i\right)\\
 {}+e_T&\otimes\left(w_T-\sum_{i\in T}a_i\delta_i\right)\\
 {}+e_S&\otimes\left(w_S-\sum_{i\in S}a_i\delta_i\right).
\end{aligned}
\]

Independence of the four divisor classes makes the kernel equations
triangular. Projection to \((a_i)\) is an isomorphism onto

\[
 \ker\!\left(\mathbf Q^{11}\longrightarrow W,
 (a_i)\longmapsto\sum_i a_i\delta_i\right),
\]

with inverse assigning the three indicated partial sums.

## Complete strict-support audit

The possible connected strict supports are \(F_S,F_T,F_U\), and the origin.

- Over a generic point of the codimension-two \(F_S\), the normal map is the
  semismall rank-two model, so lower-support terms begin in ordinary degree
  two.
- Over a generic point of codimension-three \(F_T\), the normal fiber has
  dimension at most two and perverse defect at most one. Its lowest possible
  ordinary degree is \(3-1=2\).
- Over a generic point of codimension-four \(F_U\), the normal fiber has
  dimension at most three and perverse defect at most two. Its lowest
  possible ordinary degree is \(4-2=2\).
- Over the origin, \(Z\) has dimension four. The shifted direct image has
  point-supported perverse amplitude contained in \([-3,3]\), giving
  ordinary degrees \(2\) through \(8\).

Every other arrangement stratum is a transverse product of one of these
connected normal models with coordinate hyperplanes. Such an SNC factor
does not lower the ordinary degree. Hence no non-full strict support can
contribute in degree one. Saito's projective direct-image and strict-support
decomposition (S037) transfers the resolved kernel to
\(H^1(IC_B(L_{\mathbf Q})_0)\).

## Rational Hodge type and scope

After \(\mathbf Q(n)\), the branch and exceptional coefficient spaces are
sums of \(\mathbf Q(0)\). The SNC residue map is a morphism of rational
mixed Hodge structures, so its kernel and the downstairs IC stalk are pure
type \((0,0)\).

B047 proves only one three-level chain. It does not prove G019 for arbitrary
building sets, establish order independence of the residue identification,
construct a class-paired nodal incidence, or produce an algebraic cycle.
The standard rational Hodge Conjecture and G015 remain open.
