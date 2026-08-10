---
brick_id: G014
status: EXPLORATORY
base_field: C
variety: arbitrary smooth projective complex variety X of even dimension 2n with a very ample line bundle L
smoothness: X is smooth; detector divisors are required to have only isolated ordinary double points with the stated transverse local model
projectivity: X and every detector divisor are projective
dimension: dim_C X = 2n and detector divisors have dimension 2n-1
codimension: target cycles have middle codimension n; detector divisors have codimension 1
coefficient_field: Q for cycles, vanishing relations, homology, cohomology, and Hodge classes
cohomology_theory: Betti cohomology and homology, polarized rational Hodge structures, vanishing cycles, local intersection cohomology, and coherent adjoint defect
hodge_type: primitive middle type (n,n), equivalently type (0,0) after Tate twist; local relations must also have rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B001, B007, B009-B010, B016-B017, B026-B028, B031-B033, and G013
claim: Canonical primitive images of unanchored high-power two-part nodal relations span primitive rational Hodge homology for every X.
falsifier: a smooth projective X and a nonzero primitive rational middle Hodge class zeta pairing trivially with every canonical image from every unanchored high-power nodal member satisfying the B028 two-part conditions
---

# G014 - Unanchored nodal detector spanning

## Falsifiable theorem

Fix a smooth projective complex \(2n\)-fold \(X\) and a very ample line
bundle \(L\). For all powers \(m\), consider nodal members
\(Y\in|L^m|\) whose node set \(\Delta\) satisfies

\[
 |\Delta'|\le2r_{L^m}(\Delta')\quad(\Delta'\subseteq\Delta)
\]

and has positive adjoint defect

\[
 r_{K_X\otimes L^{mn}}(\Delta)<|\Delta|.
\]

Take the union over **all** such members; no fixed middle-dimensional
carrier is part of the definition of the collection. For every rational
type-\((0,0)\) relation \(\beta\) in such a member, let

\[
 \gamma_\beta=
 \Phi_Y(\beta)\in
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}^{(0,0)}
\]

be Saito's canonical primitive ambient image. “Unanchored” means precisely
that this detector collection is defined intrinsically from the complete
linear systems and the two rank conditions, not as the subfamily containing
a preselected algebraic cycle. This makes the statement a property of
\((X,L)\), independent of proof provenance.

The gate asserts

\[
 \operatorname{span}_{\mathbf Q}\{\gamma_\beta\}
 =
 H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}^{(0,0)}.
\]

## Why this propagates to the terminal theorem

B016 proves that a detector collection pairs nontrivially with every
nonzero primitive rational Hodge class exactly when its canonical images
span primitive rational Hodge homology. B010 turns such a nonzero pairing
into singular-hyperplane detection. B007 identifies universal detection with
the standard rational Hodge Conjecture after B001's middle-degree reduction.
Thus G014 is sufficient, and its universal content is still
terminal-equivalent rather than an easier known theorem.

## First proof attempt: scale the diagonal witness

B033 proves all finite geometric requirements at every power in
\(\mathbf P^2\times\mathbf P^2\):

- the nodes have a uniform smoothing evaluation matroid and split into two
  independent blocks;
- the adjoint defect and relation space are one-dimensional;
- the canonical extra-to-primitive map has rank one;
- its image pairs nontrivially with the primitive diagonal component.

This attempt fails the unanchored hypothesis. Every member is required to
contain the diagonal, and the canonical image is computed from the
already-algebraic class

\[
 [\Delta_{\mathbf P^2}]_{\mathrm{prim}}
 =\frac13(h_1^2-h_1h_2+h_2^2).
\]

Varying \(m\), the node partition, or the section of
\(\Omega^1_{\mathbf P^2}(2m)\) does not vary this primitive direction.
Full symmetric monodromy acts on the nodes and proves uniform postulation;
it supplies no monodromy theorem for the image of \(\Phi_Y\) in ambient
primitive homology.

## Precise unresolved obstruction

The missing map is class-directed and vector-valued. Starting from a
nonzero primitive rational Hodge class \(\zeta\), or from B011's global tube
detector, one must construct an unanchored nodal relation \(\beta\) and prove

\[
 \langle\zeta,\Phi_Y(\beta)\rangle\ne0.
\]

Positive coherent defect controls only the source dimension (B026);
positive ambient rank is independent (B031); and even a positive image may
lie in \(\zeta^\perp\) (NG-023). No audited source provides the required
global-tube-to-unanchored-incidence comparison.

## Next justified attack

Construct a parameter space of two-part nodal members without a fixed
middle-dimensional carrier and compute the monodromy representation of the
local system \(\operatorname{im}\Phi\), not merely the permutation
representation on nodes. A successful brick must prove that its invariant
span is the full primitive rational Hodge substructure or exhibit a
specific nonzero annihilator. Numerical node configurations, defect
dimensions, and special-family monodromy do not decide this gate.
