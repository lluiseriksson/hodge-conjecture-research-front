---
brick_id: G032
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold, one detecting singular hyperplane section, and algebraic deformations of that section inside a high-power hyperplane family
smoothness: X is smooth; the source hyperplane is arbitrary singular and the sought target has only ordinary double points with a Li-clean discriminant arrangement
projectivity: X, the hyperplane family, and the deformation are projective
dimension: dim_C X = 2n and hyperplane fibers have dimension 2n-1
codimension: middle codimension n; deformation occurs inside the dual discriminant and its higher strata
coefficient_field: Q
cohomology_theory: singular and intersection cohomology, nearby and vanishing cycles, limit mixed Hodge structures, local Saito relations, and primitive homology
hodge_type: primitive rational type (0,0) input and rational type-(0,0) local relation after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B022, B025, B054, B064, B125-B126, G008, G031, G084, NG040, and NG101
claim: Every singular hyperplane section detecting a primitive rational Hodge class can be connected through an algebraic topology-changing deformation to a Li-clean multipart nodal member carrying a Saito relation that retains nonzero pairing with that class.
falsifier: a detecting singular hyperplane for which every accessible Li-clean multipart nodal deformation has zero relation space, loses the class through specialization, or has ambient detector image orthogonal to the specified Hodge class
---

# G032 - Pairing-preserving nodalization of a detector

## Falsifiable cleanup theorem

Let \(Y_0\) be a singular hyperplane section of a smooth projective
\(X/\mathbf C\), and suppose

\[
 \zeta|_{Y_0}\ne0
\]

for a nonzero primitive rational Hodge class \(\zeta\). Construct an
algebraic deformation inside a sufficiently high hyperplane system to a
Li-clean multipart nodal member \(Y_1\), together with

\[
 \beta_1\in R(Y_1)_1^{(0,0)},\qquad
 \langle\zeta,\Phi_{Y_1}(\beta_1)\rangle\ne0.
\]

If G032 were proved, B007/G008 would supply the source detector under HC and
G032 would upgrade it to G031's controlled locus. Conversely, G031 already
implies HC. Thus G032 is exactly the missing cleanup mechanism needed before
the clean-nodal restriction can be treated as equivalent rather than merely
sufficient.

## Attempt 1 - Generic morsification

For an isolated hypersurface singularity, a morsification replaces the
critical point by \(\mu\) Morse critical points. B025 proves that the
distinguished vanishing cycles form an integral basis of the local Milnor
lattice. They therefore carry no internal relation. Moreover, each separate
Morse critical value is a smooth point of the discriminant, and B008 gives
zero rational degree-one local intersection-cohomology channel there.

Consequently, generic morsification destroys the one-point higher-stratum
configuration instead of producing a Saito relation at one nodal member.
NG040 records this failed inference.

The suspended $A_2$ chart makes the failure sharper. B126 proves its local
miniversal discriminant has exactly one singular point on every fiber: one
node away from the cusp and one $A_2$ point at the cusp. There is no local
two-node target to recollide. NG101 therefore requires any cleanup theorem
to leave the single local versal germ and use global incidence geometry.

## Attempt 2 - Recollide the Morse points

Recolliding several Morse values into a multipart nodal member can create the
geometric format used by B054, but a nonzero relation must then occur in the
global kernel

\[
 \bigoplus_y H_{2n-1}(Z_{y,\infty},\mathbf Q(n))
 \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n)),
\]

not inside any local Milnor lattice. Neither morsification nor conservation
of Milnor number supplies this dependence. Even a produced relation must
retain a nonzero primitive ambient image and the specified pairing; B022
shows that an extension chain can die in two quotient kernels before that
test.

## Precise obstruction

No audited specialization theorem gives an injective or pairing-preserving
map from the source local intersection-cohomology class to the relation
channel of a different, cleaner discriminant stratum. Rank, Milnor number,
and adjacency of singularity types do not determine the global
local-to-nearby kernel or its primitive ambient image.

## Re-entry condition

Construct the comparison on the full nearby-cycle complex across the
topology-changing family and prove: rationality; type \((0,0)\) after the
Tate twist; survival through both B022 quotients; and nonzero pairing with
\(\zeta\). A list of Morse critical points or a conserved Milnor number is
insufficient.
