---
brick_id: G028
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective 2n-fold and a high-power nodal hyperplane member with node-smoothing evaluation matroid
smoothness: the ambient variety and nearby hyperplane sections are smooth; the selected central member has only ordinary double points and the sought incidence strata form a clean arrangement
projectivity: the ambient variety and hyperplane family are projective
dimension: ambient dimension 2n, with a number q of smoothing blocks allowed to scale with n
codimension: middle codimension n; node conditions have their standard first-jet codimension
coefficient_field: Q
cohomology_theory: node-smoothing evaluation matroids, adjoint defect, rational vanishing-cycle relations, and Saito detector classes
hodge_type: the selected relation must have type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B010, B016, B028, B034, B054-B055, B142-B146, G012-G015, G019, G092, NG037, and NG115-NG117
claim: For every specified nonzero primitive rational Hodge class, some high-power nodal member has a clean node incidence whose smoothing matroid partitions into a dimension-scaled number q of independent blocks, has positive adjoint defect and positive extra-to-primitive rank, and contains a rational type-(0,0) relation pairing nontrivially with the class.
falsifier: a polarized smooth projective variety and primitive rational Hodge class for which every clean q-block nodal relation at every high power either violates the q-matroid partition inequalities, has zero adjoint/ambient rank, or has zero class pairing
---

# G028 - Dimension-scaled class-paired nodal incidence

B054 removes the multipart local-topology obstruction. The next gate returns
to geometry and the specified Hodge class.

For a node set \(\Delta\) with smoothing-evaluation rank function \(r_A\),
Edmonds' \(q\)-matroid partition criterion requires

\[
 |S|\le q\,r_A(S)\qquad(S\subseteq\Delta).
\]

The sought member must satisfy these inequalities for some \(q=q(n)\), have
positive adjoint corank, and have a relation whose canonical
extra-to-primitive image pairs nontrivially with the specified class. Its
discriminant intersections must satisfy B054's clean-arrangement hypothesis.

B034 shows why \(q\) must scale at least factorially in the fixed-carrier
model. B054 proves that increasing \(q\) causes no further local IC loss. It
does not supply the member, the positive ambient map, or the class-specific
pairing. Choosing an algebraic carrier with the desired class would be
circular and remains forbidden.

## Attempt 1 - Sweep one positive image by equisingular monodromy

One might construct a single unanchored component with
\(\operatorname{rank}\Phi_Y>0\), prove large monodromy on its nodes or
relation space, and try to span the primitive Hodge homology by monodromy
translates.

B055 proves that this cannot work on one connected equisingular component.
The canonical ambient maps, when they form the required morphism to the
constant local system \(H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\), have one
fixed image subspace throughout the component. Domain monodromy acts only
inside its fibers and kernel. This failed route is NG037.

The next justified gate is G029: cross a topology-changing incidence
boundary and prove that a chosen global tube or quotient-level thimble class
specializes to one clean nodal relation while retaining rational Hodge type
and nonzero pairing. This is not supplied by equisingular transport.

## Attempt 2 - Realize the factorial scale on a product fiber

B142 takes

\[
 X=\mathbf P^n\times\mathbf P^n,\qquad
 W=\{p\}\times\mathbf P^n,\qquad
 A_m=\mathcal O(m,m).
\]

A general member containing \(W\) has \(m^n\) isolated nodes. Their
smoothing matroid is the uniform matroid of rank
\(\binom{m+n}{n}-n\), so they partition into \(n!\) independent blocks,
exactly matching B034's asymptotic lower bound. The adjoint defect is one,
the extra-to-primitive map has rank one, and the fiber class pairs
nontrivially with the one-dimensional primitive Hodge line. Since
\(m^n/(mn-n-1)\to\infty\), this is the first witness that also crosses
B141's superlinear floor in every middle dimension.

B143 proves the missing nonlinear statement: the moving-fiber incidence is
a smooth codimension-\(R_m\) germ contained in all node branches, and the
uniform rank calculation forces every deeper intersection to equal that
germ. Thus the discriminant is Li clean. B054 applies, and B142's nonzero
unique primitive pairing makes the B134/B135 local functional nonzero.

This proves the complete G028 package for the special product family, but
not universal G028. The fiber \(W\) is an explicit algebraic anchor, and no
construction starts from an arbitrary \((X,\zeta)\). The surviving narrow
gate is therefore no longer node count, block capacity, clean geometry, or
local nonvanishing in this model: it is an unanchored class-directed
incidence theorem for arbitrary varieties.

B144 abstracts the successful clean step: a uniform branch-conormal
matroid becomes Li clean as soon as an actual smooth codimension-rank germ
is contained in every branch. G090 is the resulting explicit unanchored
gate. NG115 closes the first attempted source for that germ: B132's
filtered section is constant and nonzero, while its ordinary survival locus
is precisely the unresolved G088 support.

B145/G091 sharpen the saturated germ into a smooth excess component of the
ordered-node incidence. NG116 excludes the generic expected-codimension
component: its first jets and node values are independent, so B027-B028
force zero relation space.

B146/G092 further require any uniform excess component to carry a common
Hessian-isotropic conditional-gradient image of corank at least
\(n(R+1)\). NG117 blocks using value-rank degeneracy without this second
geometric failure and its higher-order integration.
