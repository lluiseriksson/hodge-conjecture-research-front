---
brick_id: B010
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n, a high-power hyperplane family, and a one-parameter degeneration f:Y->C through a singular member Y_0
smoothness: X and the nearby fiber Y_c are smooth; Y_0 may be singular, with a separate explicit isolated-singularity and nodal specialization
projectivity: X projective, L ample with L^k very ample, and f projective after base change
dimension: dim X = 2n and dim Y_c = 2n-1
codimension: middle codimension n on X
coefficient_field: Q
cohomology_theory: singular Betti cohomology and homology with Tate twist, limit mixed Hodge structures, vanishing cohomology, and local intersection cohomology
hodge_type: primitive (n,n) input; type (0,0) unipotent vanishing-cycle relations and extra Hodge cycles after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); the local theorem does not assume surjectivity
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Saito Theorems 1-3 and Proposition 1 (S022); B007 and B009
claim: A singular hyperplane Y_0 detects a primitive rational Hodge class zeta exactly when zeta pairs nontrivially with the primitive Hodge class gamma_beta attached to some type-(0,0) unipotent relation beta among its vanishing cycles.
falsifier: data satisfying Saito's hypotheses for which zeta restricts nontrivially to Y_0 but pairs trivially with every gamma_beta, or conversely
---

# B010 - Saito local relation-pairing criterion

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L^k\)
be very ample, and let \(Y_0\in|L^k|\) be singular. Choose an irreducible
analytic curve germ through its parameter, normalize it to a disk \(C\), and
write \(f:Y\to C\) for the induced one-parameter degeneration. Let \(Y_\infty\)
carry the limit mixed Hodge structure.

For isolated singularities, Saito's Proposition 1 gives an exact sequence of
mixed Hodge structures

\[
 H^{2n-1}(Y_\infty)
 \longrightarrow \bigoplus_{y\in\operatorname{Sing}Y_0}
 H^{2n-1}(Z_{y,\infty})
 \longrightarrow H^{2n}(Y_0)
 \longrightarrow H^{2n}(Y_\infty).
\]

Define the extra cohomology and the relation space by

\[
\begin{aligned}
 E(Y_0)&=\ker\!\left(H^{2n}(Y_0,\mathbf Q(n))
             \to H^{2n}(Y_\infty,\mathbf Q(n))\right),\\
 R(Y_0)&=\ker\!\left(
   \bigoplus_y H_{2n-1}(Z_{y,\infty},\mathbf Q(n))
   \to H_{2n-1}(Y_\infty,\mathbf Q(n))\right).
\end{aligned}
\]

Write \(R(Y_0)_1^{(0,0)}\) for the type-\((0,0)\) part of the unipotent
monodromy summand. Saito Theorem 1 supplies a canonical isomorphism

\[
 R(Y_0)_1^{(0,0)}\simeq E^\vee(Y_0)^{(0,0)}.
\]

For \(\beta\) in this relation space, the canonical map from extra homology to
the primitive part of \(H_{2n}(X,\mathbf Q(n))\) gives a primitive rational
Hodge class \(\gamma_\beta\). For every primitive rational Hodge class
\(\zeta\) on \(X\),

\[
 \zeta|_{Y_0}\ne0
 \quad\Longleftrightarrow\quad
 \langle\zeta,\gamma_\beta\rangle\ne0
 \text{ for some }\beta\in R(Y_0)_1^{(0,0)}.
\]

Theorem 2 replaces the sum of isolated local Milnor groups by the vanishing
cycle functor and retains the statement for non-isolated singularities.

## Explicit topological construction

In the isolated case, choose a good retraction
\(\rho:Y_c\to Y_0\) and small vanishing neighborhoods \(Z_c\). A relation
\(\beta\) lifts to a relative cycle
\(\gamma'\in H_{2n}(Y_c,Z_c;\mathbf Q(n))\). Its retraction is a class in
\(H_{2n}(Y_0,\mathbf Q(n))\), and \(\gamma_\beta\) is the primitive part of
its pushforward to \(X\). The lift need not be unique, but its primitive
pushforward is the class used in the pairing criterion.

## Nodal specialization

For ordinary double points, Saito Theorem 3 proves that every local vanishing
group is \(\mathbf Q(-n)\) with unipotent monodromy. Thus every rational
relation among the nodal vanishing cycles has the required type \((0,0)\)
after the Tate twist. This supplies the precise mixed-Hodge justification
missing from a dimension-only defect argument.

## Scope guard

The theorem characterizes detection at a chosen singular member. It does not
produce that member or a nonzero relation for a specified \(\zeta\). Universal
existence remains equivalent to the rational Hodge Conjecture.
