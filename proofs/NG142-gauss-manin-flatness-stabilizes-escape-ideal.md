---
brick_id: NG142
status: NO-GO
base_field: C
variety: a projectively realizable family of fixed ODP charts with constant nodewise Milnor lattices and arbitrary analytic critical-value germ
smoothness: X is smooth, the ODP Hessians stay nondegenerate, and the basis-node germ is smooth
projectivity: B157 realizes the model after sufficient twisting on a smooth projective variety, but generally over a nonlinear analytic pullback of the full linear system
dimension: two-parameter model with N=2, R=1, one-dimensional basis-node germ, and one escape function
codimension: the escape ideal (y^2) is not stable under the tangent derivation partial_y and therefore does not vanish
coefficient_field: C for critical values and Gauss-Manin connections; Q for the constant local A1 Milnor lattices
cohomology_theory: local ODP Milnor fibrations, nodewise Gauss-Manin transport, analytic differential ideals, and critical-value deformation theory
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B158, B176-B178, G111
claim: Constancy or flatness of the nodewise Milnor/Gauss-Manin local systems automatically makes the scalar escape ideal K_B stable under tangent differentiation.
falsifier: tau=(x,x+y^2) has fixed ODP Hessians and constant A1 Milnor lattices, but K_B=(y^2) and partial_y(y^2)=2y is not in K_B
---

# NG142 — Gauss–Manin flatness does not stabilize critical values

B157 realizes arbitrary analytic critical values while fixing every local
ODP quadratic form, Milnor lattice, and individual Picard--Lefschetz
operator. Apply it to

\[
 \tau=(x,x+y^2).
\]

Choose the first branch as the basis. Then

\[
 F_B=\{x=0\},
 \qquad
 K_B=(\tau_2|_{F_B})=(y^2)
 \subset\mathbf C\{y\}. \tag{1}
\]

The tangent frame on \(F_B\) is \(\partial_y\), but

\[
 \partial_y(y^2)=2y\notin(y^2). \tag{2}
\]

Thus the escape ideal is not differential even though all nodewise local
Milnor and Picard--Lefschetz data are constant.

## Precise mismatch

Gauss--Manin transport acts on local cohomology or vanishing homology.
The ideal \(K_B\) consists of scalar critical-value functions. There is no
automatic connection-compatible morphism from the former to the latter.
B157 shows that any theorem using only the fixed local systems would have
to hold for arbitrary \(K_B\), which (1)--(2) refute.

## Re-entry condition

G111 must construct a new comparison using global full-linear-system
incidence geometry, prove differential stability of the actual escape
ideal, and retain all rational Hodge and detector clauses. A nonlinear
projective pullback or constant nodewise VHS cannot substitute for that
theorem.
