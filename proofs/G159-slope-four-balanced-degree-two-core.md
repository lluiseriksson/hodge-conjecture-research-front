---
brick_id: G159
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=4d=8n; N=6d+2=12n+2; h_Z(1)=3d+1=6n+1=N/2
codimension: construct the complete G144 package with delta_1=2d and an isomorphic degree-one relation transport at the slope-four boundary forced by B235
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B236, G013, G090-G148, NG106-NG194, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=6d+2 points satisfying the complete G144 package with slack s=4d, h_Z(1)=3d+1, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the slope-four balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G159 — Construct the slope-four balanced degree-two core

B235 replaces the additive low-slack ladder by the necessary bound

\[
 m=2\quad\Longrightarrow\quad s\ge4d. \tag{1}
\]

At equality, its exact rank signature is

\[
 s=4d,\qquad \delta_1=2d,\qquad
 N=6d+2,\qquad h_Z(1)=3d+1=N/2. \tag{2}
\]

The relation transport has zero cokernel and the degree-one code is
diagonally self-dual.

G159 asks for this slope-four threshold on every primitive target,
together with the central ODP generator, adjacent profile, conformal
holonomy, finite Kuranishi closure, rational type-\((0,0)\) relation,
and specified nonzero pairing. On the even-quadric test, B235 shows that
only the standard polarization can occur at equality. On an arbitrary
variety this is a constraint to audit, not an existence theorem.

G159 is a sufficient specialization of G148. No marked configuration,
detector, pairing, algebraic cycle, proof, or disproof of HC is currently
constructed.

B236 attacks equality on \(Q^d\). It forces a third marked point
orthogonal to the initial nonorthogonal pair and makes the three tangent
osculators fill the point span. The symmetric-tensor decomposition then
shows that no fourth distinct point can have its full tangent absorbed.

Thus G159 and the adjacent odd layer \(4d+1\) are **NO-GO**. The next
gate is G160 at \(s=4d+2,\delta_1=2d+1\). G148 and HC remain open.
