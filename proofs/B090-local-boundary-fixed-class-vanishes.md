---
brick_id: B090
status: PROVED
base_field: C
variety: a local family of odd-dimensional hyperplane sections of a smooth projective complex 2n-fold around one normal-crossing independent-node parameter
smoothness: ambient and nearby fibers smooth; the central fiber has only ordinary double points with independently smoothable local branches
projectivity: the ambient hyperplane family is projective; the proof is local topological linear algebra
dimension: ambient 2n; smooth and central hyperplane fibers 2n-1
codimension: middle codimension n; the nodal stratum has codimension equal to the number of branches
coefficient_field: Q
cohomology_theory: singular homology, Picard-Lefschetz monodromy, vanishing cycles, and relative thimble homology
hodge_type: unrestricted topological vanishing; no algebraicity conclusion
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B009, B013, B015, B057, B089
claim: For the positively oriented total boundary loop around a normal-crossing cluster of simultaneous nodes, every monodromy-fixed rational fiber class has zero B057 Picard-Lefschetz coefficient vector and hence zero ordered thimble-extension chain.
falsifier: a fixed rational class for such a positive local boundary whose B057 coefficient vector is nonzero
---

# B090 — A fixed class gives no detector on the total nodal boundary

**Status:** PROVED

Let the local vanishing cycles in the marked reference fiber be
$\delta_1,\ldots,\delta_r$. Because the nodes have disjoint Milnor balls,
their pairwise intersection numbers vanish. The positive local meridians
therefore commute, and B057 gives

\[
 T_i(x)=x+\varepsilon\langle x,\delta_i\rangle\delta_i,
 \qquad
 c_i=\varepsilon\langle\alpha,\delta_i\rangle,
\]

with one dimension-dependent sign $\varepsilon\in\{\pm1\}$. No successive
correction occurs because every $T_j$ fixes every $\delta_i$ for $i\ne j$.

If the positive total boundary monodromy $g=T_r\cdots T_1$ fixes $\alpha$,
then

\[
 0=(g-I)\alpha=\sum_i c_i\delta_i.
\]

Pair this relation with $\alpha$. Since
$\langle\alpha,\delta_i\rangle=\varepsilon c_i$, one obtains

\[
 0=\left\langle\alpha,\sum_i c_i\delta_i\right\rangle
  =\varepsilon\sum_i c_i^2.
\]

The coefficients are rational, so the sum of their real squares vanishes
only when every $c_i=0$. B057's ordered thimble expression
$\tau_g(\alpha)=\sum_i c_i\Delta_i$ is consequently zero.

## Boundary

This does not annihilate B009's local relation space. It proves instead that
a nonzero relation there cannot be obtained by taking an arbitrary class
fixed by the positive total boundary of the same normal-crossing nodal
cluster. A successful route must transport a genuinely nonlocal distributed
word through a topology-changing comparison; G054 records that obligation.
