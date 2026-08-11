---
brick_id: G109
status: EXPLORATORY
base_field: C
variety: the full affine complete-linear-system germ of hypersurfaces on an arbitrary smooth projective complex variety X, with an ordered class-directed N-node member
smoothness: X and the parameter germ are smooth; the central spatial singularities are ODPs; smoothness of the simultaneous-node germ is the desired consequence
projectivity: X and the hypersurface family are projective; logarithmic vector fields live on the affine parameter germ of the full complete linear system
dimension: X has the dimension required by the middle Hodge reduction; parameter dimension d; N nodes; central critical-value rank R; construct d-R independent logarithmic directions
codimension: force the labelled simultaneous-node ideal I_tau to define a smooth reduced codimension-R germ
coefficient_field: C analytically and Q for the retained Hodge class, vanishing-cycle relation, and detector pairing
cohomology_theory: ODP deformation theory, ideal-preserving logarithmic derivations, vanishing cycles, primitive rational cohomology, and Saito's type-(0,0) relation pairing
hodge_type: the retained detector relation must be rational type (0,0) and pair nontrivially with the specified primitive rational Hodge class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the input Hodge class may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B176, G013, G088-G100, NG106-NG140, S071
claim: Construct d-R analytic vector fields on the full complete-linear-system germ that preserve the labelled simultaneous critical-value ideal I_tau and have independent values spanning ker(d tau_0), while retaining the uniform superlinear node matroid, positive adjoint defect, nonzero primitive ambient image, rational type (0,0), and specified nonzero Saito pairing.
falsifier: failure of ideal preservation, logarithmic evaluation rank below d-R, use only of the reduced product discriminant, loss of any detector clause, restriction to a special family without a proved general reduction, or assumption of algebraicity of the input Hodge class
---

# G109 — Construct a labelled logarithmic orbit

B176 converts the exact active local obstruction into the following
falsifiable construction problem. On the full affine germ \((P,s_0)\) of
the complete linear system, let

\[
 I_\tau=(\tau_1,\ldots,\tau_N),
 \qquad \operatorname{rank}d\tau_{s_0}=R,
 \qquad d=\dim P.
\]

Construct analytic vector fields

\[
 \delta_1,\ldots,\delta_{d-R}
 \in\Theta_P(-\log I_\tau)
\]

such that

\[
 \delta_1(s_0),\ldots,\delta_{d-R}(s_0)
\]

are linearly independent. Equivalently, their values span
\(\ker d\tau_{s_0}\).

By B176 this is equivalent to \(H_\tau=0\), hence to B155's analytic
rank-\(R\) factorization and the exact G100 syzygy lifting. The advantage
is operational rather than logical: a successful proof may try to build
flows from global incidence symmetries, correspondences, or deformation
vector fields while checking ideal preservation directly.

## Detector clauses that must remain attached

The orbit does not count toward the Hodge Conjecture unless the same nodal
configuration also retains:

1. the uniform superlinear evaluation matroid required after B141;
2. positive adjoint defect and a nonzero primitive ambient image;
3. a rational type-\((0,0)\) local relation;
4. nonzero pairing with the specified primitive rational Hodge class.

No theorem for a special family propagates upward without an explicit
proved reduction from arbitrary smooth projective complex varieties.

## Current status

No such logarithmic frame is known in the full system. NG139 excludes
deriving it from freeness of the reduced discriminant. NG140 excludes
integrating the central Zariski tangent kernel without a separate
ideal-preservation theorem. Thus G109 is an equivalent attack form of
G100, not evidence that G100 has been solved.
