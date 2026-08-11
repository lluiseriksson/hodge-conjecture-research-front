---
brick_id: G013
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective X of dimension 2n, a specified primitive rational Hodge class, a global detector, and a sought high-degree nodal member with node scheme Delta
smoothness: X and nearby fibers are smooth; the sought member has only ordinary double points; its node scheme satisfies the two-part smoothing-matroid inequalities
projectivity: X and the hypersurface family are projective
dimension: dim_C X = 2n and the nodal hypersurface has dimension 2n-1
codimension: middle codimension n on X; nodes have codimension 2n in X and define a higher-codimension incidence condition
coefficient_field: Q for Hodge, homology, and Saito relation data; C for smoothing and adjoint evaluation matroids
cohomology_theory: primitive Betti homology and cohomology, monodromy tubes, nodal vanishing cycles, local intersection cohomology, mixed Hodge structures, and coherent node-evaluation cohomology
hodge_type: the specified class and sought Saito relation have rational type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B009-B013, B016, B022-B032, B135-B142, NG109-NG114, and S056-S060
claim: Every specified primitive rational Hodge class with a nonzero global detector admits a high-degree nodal member whose node scheme satisfies the two-part smoothing-matroid inequalities, has positive adjoint evaluation defect, and contains a rational Saito relation whose ambient class retains nonzero pairing with the specified class.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class for which every nodal node scheme satisfying the two-part matroid inequalities either has zero adjoint defect or has detector image contained in the class annihilator
---

# G013 - Class-paired two-matroid incidence

## Falsifiable theorem sought

For

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0},
\]

construct a sufficiently high line bundle \(A\), a nodal member
\(Y_0\in|A|\) with node scheme \(\Delta\), and a relation \(\beta\) such
that:

1. \(|S|\le2r_A(S)\) for every \(S\subseteq\Delta\), so Edmonds' theorem
   partitions \(\Delta\) into two independently smoothable parts;
2. \(r_F(\Delta)<|\Delta|\) for
   \(F=K_X\otimes A^n\), so B026 supplies a nonzero nodal relation space;
3. the canonical map
   \(\Phi_{Y_0}:E^\vee(Y_0)\to
   H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\) has positive rank;
4. \(\beta\) is rational and its Saito ambient class survives the B022
   quotients with \(\langle\zeta,\gamma_\beta\rangle\ne0\).

B135 rewrites the last condition at a normal-crossing nodal point. If the
canonical logarithmic residues are \(a_i\delta_i\), require

\[
 [a]\ne0\ \text{in}\
 \operatorname{coker}\Delta^\ast,
\]

equivalently \(\sum_i b_i a_i\ne0\) for some
\(b\in\ker\Delta\). B136 first shows that the number of nodes cannot remain
bounded. B137 makes the requirement quantitative. After fixing a very ample
\(H\), choosing \(c\ge0\) with \(K_X\otimes H^c\) globally generated, and
putting \(A_m=H^m\), B141 now requires every viable isolated-nodal sequence to
satisfy

\[
 \frac{|\Delta_m|}{mn-c}\longrightarrow\infty.
\]

This is an exact rank-function version of G012. B028 removes the ambiguity
from “partitioned independence,” while B009 and B010 supply the local channel,
Hodge type, and pairing once the incidence is constructed. Universal G013
implies G012, G008, and hence the standard rational Hodge Conjecture through
B007.

## Attempt 1 - Choose a smoothing circuit

Every circuit of the smoothing evaluation matroid admits the required
two-part partition. B028 gives an explicit high-power configuration on
\(\mathbf P^2\times\mathbf P^2\) where such a circuit becomes independent in
the adjoint evaluation matroid. Thus a smoothing circuit does not force the
strict inequality \(r_F(\Delta)<|\Delta|\). This shortcut is NG-025.

## Attempt 2 - Force adjoint dependence on one line

On the line \(C=\mathbf P^1\times\{q\}\subset\mathbf P^2\times\mathbf P^2\),
choose enough points to exceed the rank \(2m-2\) of
\(F|_C=\mathcal O_C(2m-3)\). Their \(A|_C=\mathcal O_C(m)\) matroid still
partitions into two independent sets for the smallest such cardinalities, so
the configuration satisfies the two abstract rank requirements.

B029 proves that it cannot be a nodal node scheme. A section of
\(\mathcal O(m,m)\) singular at more than \(m\) points of \(C\) vanishes to
second order along \(C\); the whole line lies in its singular locus. Thus
overloading this low-degree carrier trades adjoint dependence for
nonisolated singularities. This route is NG-026.

## Attempt 3 - Use a zero-dimensional plane complete intersection

B030 gives a positive compatibility witness. A quintic threefold in
\(\mathbf P^4\) containing a plane can have \(16\) nodes forming a
\((4,4)\) complete intersection on that plane. Factoring one quartic into two
conics partitions the nodes into two \((2,4)\) eight-point sets; each half
imposes independent conditions on \(\mathcal O(5)\), while the union has
defect one for

\[
 K_{\mathbf P^4}\otimes\mathcal O(5)^2=\mathcal O(5).
\]

Thus the two rank systems and isolated nodality are compatible. This does
not advance the class-specific gate: \(\mathbf P^4\) has zero primitive
middle cohomology, and the contained plane is an algebraic anchor built into
the construction. Importing that anchor for an arbitrary \(\zeta\) would
repeat NG-013.

## Re-entry condition

Construct an algebraic incidence component on which the Edmonds inequalities
hold fiberwise, the adjoint corank is positive, and the first-jet conditions
still have isolated nodal solutions. Its node count must meet B141's
superlinear floor, not merely escape every fixed bound or cross one linear
threshold. The support must be
distributed or use
a genuinely zero-dimensional Cayley-Bacharach mechanism rather than
overloading one low-degree carrier. Then build a rational comparison from its
adjoint cokernel to the Saito relation local system and prove that the global
detector gives a residue-cokernel section not everywhere annihilated by
\(\zeta\). The
incidence must be defined without an algebraic representative of \(\zeta\).
B030 shows that this package is not geometrically empty, but its built-in
plane cannot supply the required class-selection mechanism. B031 sharpens
the failure: the extra-to-primitive map is zero in that witness. A viable
incidence must control this third rank independently of both evaluation
matroids. B032 supplies the complementary positive-rank witness and even a
nonzero pairing, but obtains both from a divisor forced to contain the
algebraic diagonal. NG-029 shows that the remaining requirement is not
finite-rank compatibility; it is non-circular construction from the input
class or global detector.

B142 strengthens the compatibility evidence at the quantitative boundary
left by B141. On \(\mathbf P^n\times\mathbf P^n\), a divisor containing a
product fiber has \(m^n=\omega(m)\) isolated nodes, an optimal
\(n!\)-block uniform smoothing matroid, defect one, ambient rank one, and a
nonzero primitive pairing. It does not satisfy this gate's two-block
condition for \(n\ge3\), and its pairing comes from the preselected
algebraic fiber. Thus the dimension-scaled successor is G028; neither
version has the required unanchored class-selection mechanism.
