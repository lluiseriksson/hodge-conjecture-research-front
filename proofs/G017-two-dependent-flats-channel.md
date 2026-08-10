---
brick_id: G017
status: PROVED
base_field: C
variety: a three-dimensional nodal smoothing slice with seven central discriminant hyperplanes and exactly two dependent triples sharing one branch
smoothness: the parameter threefold is smooth; the central projective fiber has seven ordinary double points and nearby fibers are smooth; the projectivized arrangement has exactly two triple points
projectivity: the wonderful blow-ups and exceptional strata are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 3, dependent flats dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the origin has codimension 3, each dependent flat has codimension 2, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and mixed Hodge modules
hodge_type: the sought downstairs degree-one relation channel must be pure of type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B043-B045, G015-G016
claim: For seven rank-three branches with dependent triples {1,2,3} and {1,4,5} and no others, the wonderful-resolution degree-one IC channel is the full rational relation kernel of pure type (0,0) after Q(n).
falsifier: interaction between the two exceptional-flat residue equations kills a relation, creates a class, or introduces an ordinary-degree-one non-full-support summand
---

# G017 - Two-dependent-flat channel

Let the projective branch lines have exactly two triple points,
\(p_{123}\) and \(p_{145}\), lying on the common branch \(L_1\). After
blowing up the origin, the strict transforms of the two dependent flats are
disjoint, although their exceptional residue data share the coefficient
\(\delta_1\).

The falsifiable theorem is that the two-stage exceptional fiber

\[
 \operatorname{Bl}_{\{p_{123},p_{145}\}}\mathbf P^2
\]

has residue kernel canonically equal to
\(\ker(\mathbf Q^7\to\operatorname{span}\{\delta_i\})\), with no additional
ordinary-degree-one strict-support contribution and pure type \((0,0)\).

The first obligation is to write the three divisor-class components
\(h,e_{123},e_{145}\). Each exceptional coefficient should be forced to the
partial sum on its dependent triple. The shared branch tests whether those
two equations remain compatible rather than silently double-counting
\(\delta_1\).

B045 proves that the residue equations are

\[
 \sum_i a_i\delta_i=0,
 \quad
 w_A=\sum_{i\in\{1,2,3\}}a_i\delta_i,
 \quad
 w_B=\sum_{i\in\{1,4,5\}}a_i\delta_i.
\]

The exceptional classes are independent, so the shared branch creates no
compatibility obstruction. Projection to \((a_i)\) is the full relation
kernel. Flat- and point-supported direct-image summands begin in ordinary
degree two, and the downstairs group is pure type \((0,0)\).

G017 constructs no algebraic cycle and does not cover nested flats.
