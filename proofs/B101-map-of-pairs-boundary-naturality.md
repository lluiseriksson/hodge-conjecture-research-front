---
brick_id: B101
status: PROVED
base_field: C with rational singular homology
variety: a B057 marked thimble detector pair, a Saito nearby-fiber pair (Y_c,Z_c), and a fixed smooth projective complex 2n-fold X
smoothness: X and Y_c smooth; the source thimble pair is taken over smooth paths with Morse endpoints; Z_c is a disjoint union of local Milnor neighborhoods
projectivity: X and the hyperplane family projective; the comparison theorem itself is topological
dimension: ambient 2n; hyperplane fibers 2n-1; relative chains 2n-dimensional
codimension: middle codimension n; local singular support finite
coefficient_field: Q
cohomology_theory: singular relative homology, long exact sequences of pairs, homotopy invariance, and primitive Lefschetz projection
hodge_type: no Hodge type is created; the selected ambient target c is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B022, B057-B058, B098-B100, S022 Sections 2.4-2.5, S029 Section 2.1.4
claim: A boundary-marked map of pairs from a relative representative of the B057 detector to Saito's pair (Y_c,Z_c) automatically carries the marked boundary to the Saito local relation; if the B057 closure/quotient realization and Saito good-retraction realization are chain-homotopy compatible, it also carries the primitive ambient image to B058's class c.
falsifier: a map of pairs for which the relative boundary square fails to commute, or chain-homotopy-compatible ambient realization maps whose primitive homology maps disagree
---

# B101 — A marked map of pairs makes the two required squares formal

**Status:** PROVED

Let $(A,B)$ be a relative model of the distributed B057 thimbles in which
the individual boundary spheres remain marked, and let

\[
 F:(A,B)\longrightarrow(Y_c,Z_c)
\]

be a continuous map of pairs. For
$\widetilde t\in H_{2n}(A,B;\mathbf Q(n))$, naturality of the long exact
sequence of a pair gives the commutative square

\[
\begin{array}{ccc}
H_{2n}(A,B) & \xrightarrow{F_*} & H_{2n}(Y_c,Z_c)\\
\partial\downarrow && \downarrow\partial\\
H_{2n-1}(B) & \xrightarrow{(F|_B)_*} & H_{2n-1}(Z_c).
\end{array}
\]

Consequently, if the marked boundary satisfies

\[
 (F|_B)_*(\partial\widetilde t)=r_H(\beta_{\mathrm{sp}}),
\]

then $\gamma_t=F_*\widetilde t$ satisfies G064's boundary identity.

For the ambient statement, let $q_A$ denote B057/B098's closure-and-quotient
realization on the globally boundary-zero source class, and let $q_S$ denote
Saito's good-retraction, pushforward, and primitive projection. Suppose the
actual collision supplies chain maps and a chain homotopy proving

\[
 q_S F_*(\widetilde t)=q_A(\widetilde t).
\]

This is a compatibility of the two ambient *realization maps*; it is not
inferred merely from maps of the underlying spaces to $X$. B098 identifies
the right-hand side with B058's selected class $c$, so the primitive ambient
image of $\gamma_t$ is also $c$.

Thus both algebraic equalities in G064 follow formally from a
boundary-marked comparison of pairs and its ambient chain homotopy. The
remaining content is geometric: construct that comparison in the actual
topology-changing collision and prove what it does to every marked boundary
sphere.

## Scope guard

The theorem does not infer the marked local boundary from the fact that the
sum of the B057 boundaries vanishes in the smooth reference fiber. It also
does not construct the collision, the map $F$, or an algebraic cycle.
