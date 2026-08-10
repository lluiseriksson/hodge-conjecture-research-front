---
brick_id: G029
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold, a global monodromy-tube detector, and a one-parameter degeneration to a clean multipart nodal hyperplane member
smoothness: X and the general hyperplane fibers are smooth; the target fiber has only ordinary double points; its discriminant strata satisfy the B054 clean-arrangement hypothesis
projectivity: X, the hyperplane family, and the one-parameter degeneration are projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1
codimension: middle codimension n; the degeneration crosses a higher-codimension nodal incidence boundary
coefficient_field: Q
cohomology_theory: global tube maps, Lefschetz thimbles, B022 quotient homology, nodal vanishing-cycle relations, nearby cycles, and Saito mixed Hodge modules
hodge_type: the terminal nodal relation must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the input class may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010-B013, B022-B025, B054-B055, G007, NG023, and NG037
claim: Every nonzero global tube detector pairing with a specified primitive rational Hodge class admits a topology-changing algebraic specialization to one clean q-block nodal member and a rational relation whose B022 quotient-level ambient image preserves a nonzero pairing with that class.
falsifier: a global tube detector for which every clean multipart nodal boundary specialization either has zero relation, dies in an equator or base-locus quotient, loses rational type (0,0), or has ambient image in the class annihilator
---

# G029 - Boundary transport from a tube to one nodal relation

Fix

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}
\]

and choose a global tube detector supplied by B011, or by B024 in the
complete-intersection case, whose ambient class pairs nontrivially with
\(\zeta\).

The sought theorem must construct an algebraic one-parameter approach to a
single clean \(q\)-block nodal member \(Y_0\), together with a rational
vanishing-cycle relation \(\beta\), such that:

1. the thimble combination has zero boundary and survives both B022
   quotients;
2. specialization identifies its ambient class with
   \(\gamma_\beta\), up to a term pairing trivially with \(\zeta\), so the
   chosen nonzero pairing is preserved;
3. \(\beta\) has type \((0,0)\) after the Tate twist;
4. the clean arrangement and dimension-scaled matroid hypotheses of
   B054/G028 hold at \(Y_0\).

B055 and NG037 show why motion inside one equisingular component cannot do
this: a topology-changing boundary map is essential. B023 also excludes an
invertible Hurwitz basis change as the missing operation. The unresolved
object is therefore a non-invertible specialization comparison between the
global thimble quotient and one local nodal relation space.

No audited theorem currently supplies that comparison with rational Hodge
type and class-pairing preservation. This gate would supply G028's
class-directed part once the target incidence ranks exist; it does not itself
prove those ranks, assume an algebraic representative of \(\zeta\), or
construct one.
