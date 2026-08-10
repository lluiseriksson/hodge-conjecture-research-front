---
brick_id: B035
status: PROVED
base_field: C
variety: a two-dimensional local smoothing-parameter slice whose reduced discriminant is a simple central arrangement of distinct complex lines, modeling a nodal hyperplane-section degeneration
smoothness: the parameter surface is smooth; its discriminant branches are smooth away from the common origin; the nearby projective fibers are smooth and the central fiber has ordinary double points
projectivity: the parameter calculation is analytic and local; the motivating hyperplane-section family is projective
dimension: parameter dimension 2; ambient projective variety dimension 2n; nearby fiber dimension 2n-1
codimension: the discriminant branches have codimension 1 in the parameter surface; the original common stratum has codimension 2; downstream algebraic cycles have middle codimension n
coefficient_field: Q for the Picard-Lefschetz representation and relation space; C for local coordinates
cohomology_theory: Picard-Lefschetz vanishing homology, unipotent monodromy logarithms, normal-crossing local systems, and intersection-complex direct images
hodge_type: no Hodge-type comparison is proved; the unresolved G015 output would have to be rational of type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009, G015, elementary blow-up geometry, Picard-Lefschetz formula, and proper base change
claim: The smallest simple central arrangement not coverable by two independent smoothing blocks is U_(2,5); one blow-up resolves it to an exceptional P^1 with five marked crossings, with N_E equal to the sum of the five nodal logarithms and all crossingwise degree-two products zero, leaving a global exceptional-divisor IC gluing computation not determined by the individual crossing complexes.
falsifier: a simple central arrangement with at most four branches requiring three independent blocks, a non-star reduced total transform of five distinct lines after blowing up the origin, or a disjoint-ODP Picard-Lefschetz representation in which N_E differs from the sum of the branch logarithms or N_E N_i is nonzero
---

# B035 - Minimal multipart arrangement

This brick takes G015 at its smallest genuinely multipart local model. It
proves the arrangement and monodromy reduction, but **does not** compute the
intersection-complex stalk or prove G015.

## 1. Minimality

Let \(A=\{H_1,\ldots,H_r\}\) be a simple central arrangement of distinct
lines in \(\mathbf C^2\). Every one- or two-element subset of \(A\) is
independent, while every subset of size at least three is dependent. Thus
its smoothing matroid is the uniform matroid \(U_{2,r}\), and one independent
block contains at most two branches. Its block-covering number is

\[
 \chi(U_{2,r})=\left\lceil\frac r2\right\rceil.
\]

Consequently \(r=5\) is the smallest simple central arrangement that cannot
be covered by two independent blocks. It has the genuine three-block
partition

\[
 \{1,2\}\sqcup\{3,4\}\sqcup\{5\}.
\]

For \(r\le4\), pairing the branches gives a two-block cover. Rank-one
examples with three proportional smoothing forms do not qualify: they
describe one reduced hyperplane with multiplicity, not three distinct
discriminant branches.

## 2. One blow-up and the exceptional star

Choose pairwise nonproportional linear forms
\(\ell_i(x,y)=a_ix+b_iy\) and put

\[
 D=\bigcup_{i=1}^5\{\ell_i=0\}\subset\mathbf C^2.
\]

Let \(\pi:\widetilde{\mathbf C^2}\to\mathbf C^2\) be the blow-up of the
origin, with exceptional divisor \(E\simeq\mathbf P^1\). In the chart
\(x=u, y=uv\),

\[
 \pi^*\ell_i=u(a_i+b_iv).
\]

Hence the reduced total transform is

\[
 \widetilde D_{\rm red}=E\cup\widetilde H_1\cup\cdots\cup\widetilde H_5.
\]

The strict transforms are pairwise disjoint. Each \(\widetilde H_i\) meets
\(E\) transversely at the point \([x:y]=[-b_i:a_i]\), and these five points
are distinct. Thus one blow-up produces a simple-normal-crossing star: a
single compact exceptional \(\mathbf P^1\) with five marked crossings.

## 3. Resolved monodromy

Let \(T_i=\exp N_i\) be the local monodromy about \(H_i\). A positive loop
around a generic point of \(E\) winds once around every original branch, so

\[
 T_E=T_1T_2T_3T_4T_5.
\]

For simultaneous ordinary double points the vanishing spheres can be chosen
in disjoint Milnor balls. Their pairings vanish. Since the nearby fiber has
odd complex dimension, the middle pairing is alternating and each
vanishing cycle also has self-pairing zero. The Picard-Lefschetz formula
therefore gives

\[
 N_i^2=0,\qquad N_iN_j=0\quad(i\ne j).
\]

The logarithms commute, so

\[
 N_E=\log T_E=\sum_{i=1}^5N_i,
 \qquad N_EN_i=0.
\]

At every resolved crossing \(E\cap\widetilde H_i\), the degree-two Koszul
term \(N_EN_iV\) is consequently zero. The obstruction to G015 is not a
nonzero local product at one crossing.

## 4. What remains after resolution

Let \(U=\mathbf C^2\setminus D\), let \(\mathbb V\) be the rational
Picard-Lefschetz local system on \(U\), and write
\(\widetilde j:U\hookrightarrow\widetilde{\mathbf C^2}\). Proper base change
shows that the stalk at the origin of any resolution-based direct-image
calculation is obtained from hypercohomology over the complete exceptional
fiber:

\[
 \left(R\pi_*\widetilde j_{!*}\mathbb V[2]\right)_0
 \simeq
 R\Gamma\!\left(E,
   i_E^*\widetilde j_{!*}\mathbb V[2]
 \right).
\]

This is a global gluing problem on \(E\simeq\mathbf P^1\) with the five
marked points \(E\cap\widetilde H_i\). Individual two-branch crossing
complexes do not compute that hypercohomology. Moreover, identifying the
desired \(j_{!*}\mathbb V[2]\) stalk downstairs requires isolating it from
any point-supported summands in the proper direct image; equality with the
entire direct image is not automatic.

Accordingly, the smallest unresolved instance of G015 is now explicit:

1. compute the intermediate-extension/quiver complex on this marked
   exceptional \(\mathbf P^1\) for the Picard-Lefschetz representation;
2. isolate the downstairs intermediate-extension summand;
3. compare its degree-one rational group with
   \(\ker(\mathbf Q^5\to H_{2n-1}(Y_t,\mathbf Q))\);
4. verify the required type-\((0,0)\) limit-Hodge comparison.

## Scope guard

B035 proves a local geometric and monodromy reduction only. The
\(U_{2,5}\) arrangement has not been realized here by a global projective
hyperplane family, and its exceptional hypercohomology has not been
computed. No vanishing-cycle relation is promoted to an algebraic cycle,
and no special-family statement is counted as progress toward the general
Hodge Conjecture.
