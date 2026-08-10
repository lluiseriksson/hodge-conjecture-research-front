---
brick_id: B089
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold, an independent-node hyperplane section H, a suitably general smooth reference hyperplane H0, and a plane net through both parameter points
smoothness: X and H0 smooth; H has only independent ordinary double points; the local Severi strata are smooth by B015
projectivity: X, the hyperplane system, and the plane net are projective
dimension: ambient 2n; hyperplane fibers 2n-1; parameter plane 2; full parameter space dimension at least 3
codimension: middle codimension n; delta-node stratum codimension delta
coefficient_field: Q for downstream homology; the plane-slice construction is over C
cohomology_theory: local discriminant topology, Picard-Lefschetz meridians, and relative thimble homology
hodge_type: no class-specific Hodge conclusion; this is a marked geometric slicing theorem
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the downstream application
scope: relative and fiberwise
dependencies: B008, B015, B023, B088
claim: Given an independent-node hyperplane H and a smooth reference H0 whose direction at H avoids every pairwise intersection of discriminant-branch tangent hyperplanes, a general parameter plane through H and H0 cuts the local discriminant in distinct smooth branches, keeps H0 literally fixed, and admits a collision disk whose boundary loop is fixed by all braids supported inside the disk.
falsifier: a normal-crossing discriminant germ and admissible reference direction for which every plane through the two marked points identifies two branch tangents or moves the reference fiber
---

# B089 — A marked plane net through a nodal target

**Status:** PROVED

Let $P=|L^m|\simeq\mathbf P^N$, with $N\ge3$, and let $H\in P$ be a
$\delta$-node hyperplane satisfying B015's independent-condition
hypothesis. In local coordinates at $H$, the discriminant has smooth
normal-crossing branches with independent defining differentials

\[
 \lambda_1,\ldots,\lambda_\delta.
\]

Choose a smooth reference point $H_0\in P\setminus D$ so that its tangent
direction $v_0$ from $H$ satisfies

\[
 v_0\notin\ker\lambda_i\cap\ker\lambda_j
 \qquad(i\ne j).
\]

This excludes finitely many proper linear subspaces and is therefore a
generic condition.

A plane through $H$ and $H_0$ has tangent space
$\langle v_0,w\rangle$ at $H$. The restrictions of branches $i$ and $j$
have the same tangent line precisely when

\[
 \lambda_i(v_0)\lambda_j(w)
 -\lambda_j(v_0)\lambda_i(w)=0.
\]

For each pair this is a nonzero linear condition on $w$, by the choice of
$v_0$. Avoiding the finite union of these hyperplanes gives a plane net in
which all $\delta$ restricted branches are smooth and have distinct tangent
lines at $H$.

Choose a sufficiently small disk $\Delta$ in this plane centered at $H$ and
disjoint from $H_0$. Its boundary loop $g_H=\partial\Delta$ is based using
a fixed path to $H_0$. A braid supported in the interior changes the ordered
meridian factorization by Hurwitz moves but fixes the boundary loop and the
reference hyperplane literally. Hence B088 applies to any marked class
$\alpha_H$ fixed by $g_H$.

## Boundary

B089 constructs the marked collision geometry only after $H$ and a local
detector class are supplied. It does not turn the arbitrary global B058
pair $(g,\alpha)$ into $(g_H,\alpha_H)$ or preserve its prescribed Hodge
pairing. NG065 closes that inference; G053 is the class-specific localization
gate. The disk must also remain a proper local cluster inside the global net:
B089 does not prove that its extension survives either B022 quotient.
