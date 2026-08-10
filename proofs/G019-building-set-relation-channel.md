---
brick_id: G019
status: EXPLORATORY
base_field: C
variety: an arbitrary finite-dimensional nodal smoothing slice whose central discriminant is a representable hyperplane arrangement, together with a smooth wonderful resolution for a fixed building set
smoothness: the smoothing slice and resolved space are smooth; the resolved boundary is simple normal crossing; the central projective fiber has only ordinary double points and nearby fibers are smooth
projectivity: the wonderful blow-up morphisms and exceptional strata are projective over their centers, and fibers over the central point are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: arbitrary parameter rank d, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: arrangement flats have arbitrary codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: the sought downstairs degree-one relation channel must be pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B041-B050, G015-G018, G020-G023, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: For every representable central nodal arrangement and every wonderful building-set resolution, the degree-one downstairs IC stalk is canonically the full rational vanishing-cycle relation kernel and is pure type (0,0) after Q(n).
falsifier: a realizable building set for which exceptional-incidence residues impose an extra equation or create a class, a non-full strict-support summand contributes in ordinary degree one, or the resulting rational kernel has a non-(0,0) component after Q(n)
---

# G019 - Arbitrary building-set relation channel

This is the next falsifiable local gate after B046. Let \(\mathcal A\) be a
representable central arrangement in a smooth rank-\(d\) nodal smoothing
slice, let \(\mathcal G\) be a wonderful building set containing all
non-SNC dependent flats, and write

\[
 W_F=\operatorname{span}_{\mathbf Q}\{\delta_i:F\subset H_i\}
\]

for every exceptional flat \(F\in\mathcal G\). The proposed theorem is that
the resolved degree-one residue differential has, in the divisor-class
basis indexed by the ambient exceptional hyperplane and the members of
\(\mathcal G\), the triangular equations

\[
 \sum_i a_i\delta_i=0,
 \qquad
 w_F=\sum_{F\subset H_i}a_i\delta_i
 \quad(F\in\mathcal G).
\]

If these are all the equations, projection to \((a_i)\) identifies the
resolved kernel with the full vanishing-cycle relation space. A proof must
derive the matrix from the iterated total transforms, not assume independence
of exceptional coefficients. It must handle arbitrary nested sets and prove
that changing the permissible building-set order leaves the downstairs
identification canonical.

The second obligation is a uniform strict-support bound. For every flat of
codimension \(c\), every non-full-support summand created by its normal
wonderful resolution must begin in ordinary degree at least two after the
ambient shift, including summands supported on incidences of nested flats.
The third obligation is coefficient-sensitive: the residue complex and the
strict-support decomposition must be over \(\mathbf Q\), and the explicit
\(\mathbf Q(n)\) normalization must make the degree-one kernel pure type
\((0,0)\).

B041-B043 prove the simple uniform cases, B044 proves one dependent flat,
B045 proves two nonnested flats sharing a branch, and B046 proves one nested
pair. B047 proves the first three-level nested chain using a rank-five
eleven-branch realization whose connected flats are enumerated exactly.
These examples do not constitute an induction over a building set:
intersections among three or more exceptional divisors may introduce new
incidence rows, and an arbitrary normal arrangement need not have the
two-row form used in those bricks.

G020 replaces the chain by a fork: two
incomparable dependent flats have a common connected parent. Their strict
transforms become disjoint only after the parent blow-up, so the residue
calculation must simultaneously test the shared parent equation and
permissible-order independence. B048 proves that finite case.

B049 proves G021's geometric part for every building set and permissible
order: the intrinsic boundary classes form the expected Picard basis and
every strict branch has class \(h-\sum_{F\subset H_i}e_F\). NG035 records
why raw exceptional coordinates cannot be used in the arbitrary-order
induction. B050 then proves G022's coefficient-sheaf assertion by an anchored
SNC quotient valid at every nested stratum. G023 is now the active descent
gate: exclude ordinary-degree-one lower strict supports. Global residue
hypercohomology must also be assembled from B049-B050.

G019 constructs no algebraic cycle. Even a proof would close only the local
arrangement part of G015; an actual multipart nodal family and a nonzero
class-specific extra-to-primitive pairing would still be required upstream.
