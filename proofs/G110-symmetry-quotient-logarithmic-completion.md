---
brick_id: G110
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex variety X with a very ample polarization, its full linear-system germ, an ordered class-directed nodal member, and the connected polarized-automorphism action
smoothness: X and the parameter germ are smooth; central spatial singularities are ODPs; smoothness of the simultaneous-node germ is the intended consequence
projectivity: X and the hypersurface family are projective; the logarithmic completion is analytic on the affine germ of the full projective linear system
dimension: parameter dimension d; critical-value rank R; automorphism-orbit rank r_A; construct d-R-r_A residual directions
codimension: complete the symmetry tangent to all of ker(d tau_0), thereby forcing a smooth reduced codimension-R simultaneous-node germ
coefficient_field: C for analytic derivations and group actions; Q for the specified primitive Hodge class and detector
cohomology_theory: ideal-preserving logarithmic derivations, polarized automorphism actions, ODP deformation theory, vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained relation must be rational type (0,0) and pair nontrivially with the specified primitive rational Hodge class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); the input Hodge class is not assumed algebraic
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B177, G013, G088-G109, NG106-NG141
claim: After inserting every fundamental vector field supplied by the connected polarized-automorphism orbit, construct d-R-r_A further analytic derivations preserving I_tau whose values span the residual quotient Q_A, while retaining every nodal matroid and class-specific detector clause.
falsifier: fewer residual directions than dim Q_A, failure of ideal preservation, use of reduced-discriminant invariance only, or loss of the uniform matroid, adjoint defect, primitive ambient image, rational type, or specified pairing
---

# G110 — Complete the symmetry quotient

Let \(A\) be the connected polarized-automorphism group acting on the full
linear-system germ \((P,s_0)\), and assume its local action preserves the
labelled ideal \(I_\tau\). B177 supplies the valid logarithmic subspace

\[
 T_{s_0}(A\cdot s_0)
 \subseteq\ker d\tau_{s_0}.
\]

Write

\[
 r_A=\dim T_{s_0}(A\cdot s_0),
 \qquad
 Q_A=\ker d\tau_{s_0}/T_{s_0}(A\cdot s_0).
\]

The exact residual obligation is to construct

\[
 d-R-r_A=\dim Q_A
\]

analytic ideal-preserving vector fields whose values form a basis of
\(Q_A\). Together with the fundamental fields they satisfy B176 and close
\(H_\tau\).

This is narrower than G109 only on varieties and members with a nonzero
polarized-automorphism orbit. For varieties with \(r_A=0\), G110 is
identical to G109. It therefore cannot count as general Hodge progress
unless the residual construction works uniformly for arbitrary smooth
projective complex varieties and retains:

1. the required superlinear uniform node matroid;
2. positive adjoint defect and nonzero primitive ambient image;
3. rational type \((0,0)\);
4. the specified nonzero Saito pairing.

No residual fields are currently constructed.
