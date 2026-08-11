---
brick_id: G125
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with a fixed very ample polarization H, a specified primitive rational middle Hodge class, and a full degree-m ordered-node incidence
smoothness: the ambient variety is smooth, all degree-m tracked singularities are ODPs, and the final simultaneous-node germ must be reduced and smooth
projectivity: the polarized variety, powers of H, reduced and doubled node schemes, complete linear system, and detector family are projective
dimension: N nodes, value rank R<N, lower conditional-gradient quotients zero, and first nonzero quotient V_m of maximal dimension 2n
codimension: construct a primitive degree-m first-jet birth together with B193 conformal Hessian holonomy and every detector clause
coefficient_field: C for graded coherent jets and Hessian holonomy; Q for the Hodge class, vanishing-cycle detector, and specified pairing
cohomology_theory: graded coherent first-jet interpolation, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B194, G013, G090-G124, and NG106-NG157
claim: Construct from arbitrary (X,zeta) a degree m and full-incidence ODP node scheme Z for which V_k=0 for every k<m but V_m has dimension 2n, satisfies every one-node determination equality and B193 conformal Hessian holonomy, has full-support multiplier in a no-coloop value image, and retains the complete rational detector package.
falsifier: a nonzero lower V_k, dim V_m other than 2n in this branch, failure of one-node determination or conformal holonomy, inherited jets from a selected lower-degree family, multiplier outside im(E), or failure of any detector clause
---

# G125 — Construct a primitive first-jet birth

B194 shows that every G123 candidate in a power \(L=H^m\) must satisfy

\[
 V_k:=H^0(I_ZH^k)/H^0(I_{2Z}H^k)=0
 \qquad(0\le k<m). \tag{1}
\]

G125 is the maximal sufficient branch in which

\[
 \dim V_m=2n. \tag{2}
\]

Starting from arbitrary \((X,\zeta)\), construct \(m\), a reduced node
scheme \(Z\), and a nodal member of \(|H^m|\) such that:

1. the extinction equalities (1) hold in the complete graded section ring;
2. \(V_m\) satisfies every one-node determination equality;
3. B193's unique dual relation completion and conformal Hessian cocycle
   hold, with full-support multiplier in the rank-\(R\) no-coloop value
   image \(R<N\);
4. positive adjoint defect, nonzero primitive ambient image, rational type-
   \((0,0)\), and nonzero specified Saito pairing with \(\zeta\) survive.

Items 1--3 say the full conditional first-jet space is born discontinuously
and primitively at degree \(m\); it is not the product of an earlier defect
with auxiliary polarization sections. This makes the multiplication audit
finite degree by degree.

G125 implies G124 and therefore the quadratic G119 rung. It remains only a
sufficient route: even success leaves every higher Kuranishi tensor, smooth
integration, and the terminal cycle construction open. B195/NG158 show
that the holonomy cannot persist after raising the power with \(Z\) fixed;
G126 therefore records the stronger requirement of closing the complete
finite Kuranishi ladder at this same birth degree. B196/G127 give the exact
projective form of every lower extinction equality: in each lower
embedding, the span of \(Z\) is full or absorbs every tangent space at its
marked points. NG159 prevents importing this special configuration from
generic Terracini theory.
