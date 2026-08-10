---
brick_id: G012
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective X of dimension 2n, a specified primitive rational Hodge class, a global detector, and a sought nodal high-degree hypersurface whose nodes admit a quasi-local partition
smoothness: X and nearby fibers are smooth; the sought member has only ordinary double points; each part of the node partition satisfies the required independence condition although the full node set is dependent
projectivity: X and the hypersurface family are projective
dimension: dim_C X = 2n and the nodal hypersurface has dimension 2n-1
codimension: middle codimension n on X; the partitioned nodal stratum has higher codimension in the hyperplane parameter space
coefficient_field: Q for Hodge, homology, and relation data; C for adjoint coherent-cohomology defects
cohomology_theory: primitive Betti homology and cohomology, monodromy tubes, quotiented thimbles, nodal vanishing cycles, local intersection cohomology, mixed Hodge structures, and adjoint node-evaluation cohomology
hodge_type: the input and sought relation have rational type (0,0) after Tate twist; ordinary double points supply the local type statement
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B009-B013, B016, and B022-B028
claim: Every specified primitive rational Hodge class with a nonzero global detector admits a high-degree nodal member whose nodes partition into independently controlled subsets but have a nonzero cross-part relation whose Saito ambient class retains nonzero pairing with the specified class.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class for which every quasi-local partitioned nodal relation at every sufficiently high power has zero Saito pairing
---

# G012 - Partitioned nodal-defect realization

## Falsifiable theorem sought

Let

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}.
\]

Starting from a nonzero global detector, construct a high-degree nodal member
\(Y_0\) with node set \(\Delta=J\sqcup K\) such that:

1. the nodes in \(J\) and in \(K\) separately satisfy the independence
   conditions needed for the quasi-local B009 calculation;
2. the full set \(\Delta\) has a nonzero adjoint evaluation defect and hence
   a nonzero relation \(\beta\) crossing the partition;
3. \(\beta\) survives the B022 ambient quotients and
   \(\langle\zeta,\gamma_\beta\rangle\ne0\).

B009 then computes the local relation channel without imposing the fatal
full-independence hypothesis. B010 gives type \((0,0)\) and the pairing, and
B007 propagates the universally quantified statement to the rational Hodge
Conjecture.

## Why the partition is forced

B027 proves that, for \(n\ge2\) in sufficiently high powers, full
independence on the defining system implies zero adjoint defect and zero
relation space. Thus G009-G011 cannot be repaired while retaining their full
independence hypothesis. A viable nodal target must allow a global dependence
while preserving enough local independence to keep the intersection-
cohomology channel computable. Green-Griffiths' partition variant in B009 is
the narrowest audited model with exactly that shape.

## Attempt 1 - Use an arbitrary positive defect

B026 turns a positive adjoint defect into the correct relation dimension,
but an arbitrary defect subspace may lie in \(\zeta^\perp\). It also need not
admit a two-part independence decomposition compatible with the local
discriminant calculation. Positivity alone is NG-023.

## Attempt 2 - Choose a smoothing circuit

A circuit of the \(A\)-evaluation matroid automatically partitions into two
independent subsets. B028 shows that dependence may disappear in the larger
adjoint evaluation system \(K_X\otimes A^n\), leaving zero nodal defect and
zero relation space. Thus circuit selection alone is NG-025. G013 records
the exact simultaneous rank conditions required of both matroids.

## Re-entry condition

Construct an incidence correspondence of node partitions over the
high-degree linear system, prove that the global detector induces a rational
section of its cross-part defect local system, and establish nonzero pairing
at one fiber. No step may select the incidence using an algebraic
representative of \(\zeta\).
