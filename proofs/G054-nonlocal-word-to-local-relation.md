---
brick_id: G054
status: EXPLORATORY
base_field: C with all detector data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, a B058 nonlocal detector word, and a B089 marked collision through a clean nodal target
smoothness: ambient and marked reference fiber smooth; target has only ordinary double points; nearby collision fibers meet the stated Lefschetz locus
projectivity: ambient hyperplane system, plane net, and collision family projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision parameter one inside a plane net
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: relative thimble homology, Picard-Lefschetz monodromy, nearby and vanishing cycles, local intersection cohomology, B022 quotients, and Saito pairing
hodge_type: the specialized local relation must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B052-B059, B082-B090, G029-G032, NG065-NG066
claim: For every prescribed nonzero primitive rational Hodge class, choose a nonlocal B058 detector word and a topology-changing marked collision whose nearby extension specializes to a nonzero clean-nodal local relation, survives both B022 quotients, is rational type (0,0), and retains nonzero prescribed pairing.
falsifier: a primitive Hodge class for which every such nonlocal-to-local comparison vanishes, lands in a B022 kernel or wrong Hodge type, or becomes orthogonal to the class
---

# G054 — Transport a nonlocal word to a local nodal relation

**Status:** EXPLORATORY

B090 rules out replacing the detector by the positive total boundary of the
target nodal cluster. The remaining falsifiable comparison must instead keep
the genuinely distributed B057 word selected by B058 and prove, across a
topology-changing collision, that its nearby chain has a special value
$r_H$ satisfying all of:

1. $r_H$ is a nonzero element of B009/B052's local relation channel;
2. $r_H$ is rational type $(0,0)$ after the middle Tate twist;
3. its thimble class survives the equator-extension and base-locus kernels;
4. its ambient image pairs nontrivially with the prescribed class; and
5. the comparison uses a marked reference fiber but does not identify the
   detector word with the positive total local boundary.

This is narrower than exact ambient-class preservation, but it still contains
the terminal class-specific support problem. No existing degeneration brick
proves the comparison.
