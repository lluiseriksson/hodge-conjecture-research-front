---
brick_id: G052
status: EXPLORATORY
base_field: C with all marked homology data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 plane-net detector, and a marked proper one-parameter collision family
smoothness: reference fiber and generic detector fibers smooth; endpoint singular; semistable replacement regular
projectivity: ambient, hyperplane, and collision families projective
dimension: ambient 2n, hyperplane fibers 2n-1, plane-net base 2, and collision parameter 1
codimension: middle codimension n; collision endpoint has positive parameter codimension
coefficient_field: Q
cohomology_theory: marked Picard-Lefschetz fibrations, relative thimble homology, Gauss-Manin transport, nearby cycles, and B022 quotient homology
hodge_type: the fixed B058 ambient class is rational type (0,0) after Q(n); no algebraic cycle is assumed
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022-B023, B057-B059, B084-B088, G051, NG061-NG064
claim: Construct a proper topology-changing collision family with a marked smooth reference fiber such that collision monodromy acts on the detector factorization purely by Hurwitz moves and returns the exact composite loop g and class alpha; B088 then gives Nt=0 for the specified B057 chain.
falsifier: every admissible collision necessarily conjugates the detector loop, changes the reference class, crosses the reference fiber discriminant, or fails to preserve the B022 quotient identifications
---

# G052 — A marked Hurwitz collision fixing the detector datum

**Status:** EXPLORATORY  
**Parent gate:** G051

Starting from the B058 pair $(g,\alpha)$, construct a pointed algebraic
collision curve together with:

1. a smooth reference hyperplane fiber disjoint from the moving collision;
2. a rational Gauss-Manin trivialization of its middle homology;
3. a moving meridian factorization of $g$ whose collision monodromy is a
   sequence of Hurwitz moves;
4. exact return of the marked data

   \[
   g\longmapsto g,
   \qquad
   \alpha\longmapsto\alpha;
   \]

5. compatibility of the induced relative chain transport with both B022
   quotient maps.

B088 then proves

\[
 M_{\mathrm{coll}}\tau_g(\alpha)=\tau_g(\alpha),
 \qquad N\tau_g(\alpha)=0.
\]

This closes G051's residue obstruction for that marked collision model.
The construction must cross the topology-changing boundary; a loop wholly
inside one fixed Morse fibration supplies only B023 and does not create the
needed special relation.
