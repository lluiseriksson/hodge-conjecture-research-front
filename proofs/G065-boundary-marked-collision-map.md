---
brick_id: G065
status: EXPLORATORY
base_field: C with all comparison maps and homology classes defined over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its B058 detector in a plane net, and the actual isolated clean nodal collision
smoothness: X and nearby fibers smooth; detector critical points Morse; target singularities ordinary double points; local Milnor neighborhoods disjoint
projectivity: ambient hyperplane family, plane net, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target singular support finite
coefficient_field: Q
cohomology_theory: marked relative singular homology, Lefschetz thimbles, Milnor neighborhoods, good retraction, and primitive ambient homology
hodge_type: target relation and ambient class rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081-B083, B093-B103, B123-B124, G030-G031, G047-G063, G066-G067, NG069-NG079, NG099-NG100, S022, S049-S050
claim: Construct in the actual collision a map of pairs F:(A,B)->(Y_c,Z_c) carrying a marked relative representative of the B057 detector to Saito's nearby pair, send its marked boundary vector to r_H(beta_sp), and construct a chain homotopy between the B057 closure/quotient realization and Saito's good-retraction ambient realization on that class.
falsifier: no continuous comparison of pairs compatible with the collision, collision of marked boundary components with the wrong local vanishing spheres or signs, or failure of chain-homotopy compatibility between the two ambient realizations
---

# G065 — Construct the boundary-marked collision map

**Status:** EXPLORATORY — sufficient exact-target mechanism, not the active minimum

Choose a relative pair $(A,B)$ retaining the individual boundary spheres of
the B057 distributed thimbles and a representative
$\widetilde t\in H_{2n}(A,B;\mathbf Q(n))$. Construct from the actual
collision a map of pairs

\[
 F:(A,B)\longrightarrow(Y_c,Z_c)
\]

such that

\[
 (F|_B)_*(\partial\widetilde t)
 =r_H(\beta_{\mathrm{sp}}).
\]

The markings must record every vanishing sphere and its orientation; an
unmarked equality after inclusion into the smooth fiber is insufficient by
NG077. Finally construct a chain homotopy identifying B057/B098's closed
ambient realization with Saito's good-retraction/pushforward realization on
$\widetilde t$. Maps of the underlying relative spaces into $X$ alone are
not enough, because a relative chain is not automatically an absolute cycle.

B101 then proves both conclusions of G064, and B100 removes all remaining
dependence on the choice of Saito relative lift. The unresolved content is
now a concrete geometric construction, not an equality inside an abstract
quotient.

B102 supplies the local collapsing map at each isolated singularity, but
NG078 blocks treating those separate local maps as a globalization of the
distributed detector. G066 is the remaining constructive subgate: localize
the detector into the Milnor tubes, glue the local collapses to the exterior
trivialization, and compare the two closed ambient chains.

B103/NG079 sharpen this further: Saito's good retraction already supplies
the global local/exterior map. G067 retains only the missing single-fiber
realization of the distributed detector and its two class-specific
identities.

B123/NG099 close the opposite special-to-nearby filtered-lift direction:
$u_\Delta(S_0)=0$. Thus G065 has the correct relative-boundary direction.
However B124/NG100 prove that its ambient compatibility clause already
contains G030's exact equality $\Phi_{Y_0}(\beta)=c$; relative-lift ambiguity
cannot tune that value. G065 remains a valid sufficient construction, but
G031's nonzero-pairing obligation is narrower, and B125 isolates G084 as its
active exact subgate.
