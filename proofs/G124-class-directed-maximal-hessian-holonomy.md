---
brick_id: G124
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system ordered-node incidence of an arbitrary polarized smooth projective complex 2n-fold with a specified primitive rational middle Hodge class
smoothness: the ambient variety and tracked singularities are smooth/ODP; the final simultaneous-node germ must be reduced and smooth
projectivity: the line bundle, reduced and doubled node schemes, complete linear system, and detector family are projective
dimension: N nodes, value rank R<N, and maximal one-node-determined conditional-gradient quotient q=2n
codimension: construct unique dual relation completion and a conformal Hessian transition cocycle whose full-support multiplier lies in the value image
coefficient_field: C for coherent jets, dual relations, and Hessian holonomy; Q for the Hodge class, vanishing-cycle detector, and specified pairing
cohomology_theory: coherent first-jet interpolation, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B193, G013, G090-G123, and NG106-NG156
claim: Construct from arbitrary (X,zeta) full-incidence ordered ODP data in the q=2n branch of B193, with all one-node relation-completion isomorphisms, conformal Hessian cocycle, full-support multiplier vector in a rank-R no-coloop value image, positive adjoint defect, nonzero primitive image, rational type-(0,0) detector, and nonzero specified Saito pairing.
falsifier: q<2n or q>2n in this branch, nonunique punctured relation completion, a nonconformal transition, multiplier outside im(E), a zero multiplier coordinate, a value coloop, use of a restricted subfamily, or failure of any detector clause
---

# G124 — Construct maximal conformal Hessian holonomy

G124 is a sufficient branch of G123, not a replacement for it. Require the
largest possible one-node-determined quotient

\[
 q=\dim H^0(I_ZL)/H^0(I_{2Z}L)=2n. \tag{1}
\]

Then B193 turns every node gradient map into an isomorphism. The
class-directed construction must provide jointly:

1. a rank-\(R\) no-coloop value image \(S\), with \(R<N\);
2. every one-node kernel equality of B191;
3. the unique dual relation-completion isomorphisms (6) of B193;
4. a conformal Hessian cocycle \(T_{ji}\) and nonzero multiplier vector
   \(\lambda\in S\); maximality automatically forces every \(\lambda_i\ne0\);
5. positive adjoint defect, nonzero primitive ambient image, a rational
   type-\((0,0)\) detector, and nonzero specified Saito pairing with
   \(\zeta\).

These conditions imply B191's rank-one tensor criterion and hence G123,
G122, and B190's vanishing of the complete quadratic relation-Hessian
tensor. They make the prospective mechanism falsifiable through exact
coherent ranks, linear relation completion, and pairwise similitude
identities.

When \(H^1(X,L)=0\), this branch has the exact defect

\[
 h^1(X,I_{2Z}L)=(2n+1)N-R-2n
 \ge2n(N-1)+1. \tag{2}
\]

Equation (2) measures the required superabundance but does not construct
it. Even success at G124 would leave cubic and higher Kuranishi rungs,
smooth integration, and the terminal algebraic-cycle construction open.
