---
brick_id: G111
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system germ on an arbitrary smooth projective complex variety X, with a class-directed ordered nodal member and a chosen rank-R basis-node germ F_B
smoothness: X, the parameter germ, and F_B are smooth; the full simultaneous-node germ is not assumed smooth
projectivity: X and the hypersurface family are projective; K_B and its tangent derivations are analytic on the full linear-system germ
dimension: parameter dimension d; basis-node dimension d-R; N-R escape functions; arbitrary middle Hodge dimension downstream
codimension: prove the escape ideal is a differential ideal on F_B, forcing it to vanish and giving smooth codimension-R simultaneous persistence
coefficient_field: C for analytic differential ideals and Gauss-Manin connections; Q for the specified Hodge class, vanishing cycles, and Saito detector
cohomology_theory: variation of Hodge structure, Gauss-Manin connection, ODP vanishing cycles, analytic differential ideals, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) and pair nontrivially with the specified primitive rational Hodge class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the specified Hodge class may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B178, G013, G088-G110, NG106-NG142
claim: Construct a canonical connection-compatible map from the relevant Gauss-Manin or vanishing-cycle object to the escape ideal K_B that proves theta(K_B) is contained in K_B for a tangent frame on F_B, then retain every nodal and class-specific detector clause.
falsifier: a connection acting only on cohomology with no map to K_B, failure of differential stability for one tangent direction, use of a nonlinear special base as general evidence, or loss of any detector clause
---

# G111 — Transfer a connection to the escape ideal

On the full complete-linear-system germ, choose a rank-\(R\) basis of
tracked node branches and form B178's escape ideal

\[
 K_B=(\tau_i|_{F_B}:i\notin B)
 \subset\mathcal O_{F_B,0}.
\]

B178 makes the next falsifiable theorem:

> Construct, from the actual Gauss--Manin/vanishing-cycle geometry of the
> full universal family, a canonical connection-compatible structure on
> \(K_B\) such that a local tangent frame
> \(\theta_1,\ldots,\theta_{d-R}\) satisfies
> \(\theta_j(K_B)\subseteq K_B\).

If proved, differential-ideal rigidity forces \(K_B=0\), hence
\(H_\tau=0\), B155's factorization, and the G100/G109 logarithmic frame.

## Required comparison, not notation

The Gauss--Manin connection naturally acts on a cohomology bundle or
local system. The escape ideal is an ideal of analytic scalar functions.
G111 therefore requires an explicit map intertwining the connection with
ordinary differentiation of critical values. Naming both structures
“flat” or using constant nodewise Milnor lattices is not such a map.

The same configuration must retain the superlinear uniform matroid,
positive adjoint defect, nonzero primitive ambient image, rational type
\((0,0)\), and specified nonzero pairing. No comparison satisfying these
requirements is currently known.
