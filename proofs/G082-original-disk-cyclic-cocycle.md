---
brick_id: G082
status: EXPLORATORY
base_field: C with all chain, local-system, and monodromy data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, the original plane-net incidence family, and one marked algebraic collision curve through a clean nodal target
smoothness: X and the original incidence total space smooth; the punctured disk fibers smooth; target fiber clean nodal
projectivity: X, plane net, original incidence family, and algebraic curve base change projective
dimension: dim_C X = 2n; hyperplane fibers 2n-1; plane base dimension 2; collision disk dimension 1
codimension: middle cycle codimension n; target has disk codimension one
coefficient_field: Q
cohomology_theory: selected relative thimble chains, B022 quotient local systems, original disk nearby cycles, cyclic monodromy, and local invariant cycles
hodge_type: no type requirement on the total disk-nearby class or lift; only a separately proved relation-filtered lift enters conditional B119
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022-B023, B057-B059, B084-B085, B090-B091, B110-B123, G050-G051, G073-G081, NG059-NG063, NG087, NG095-NG099, S022, S037
claim: As an optional stronger chain-level mechanism, compute and kill the raw selected thimble cocycle on one original disk while retaining both B022 quotients and the pairing; B122/NG098 prove this is unnecessary for ordinary liftability, and B123/NG099 prove it cannot imply a nonzero relation-filtered lift.
falsifier: undefined chain-to-disk-nearby map, zero B022 quotient image, nonzero cyclic obstruction for every admissible original disk, failure of J to be monodromy-stable, loss of the prescribed pairing under every kernel adjustment, or use of an exceptional altered class in place of the original class
---

# G082 — Kill the selected cocycle on one original collision disk

**Status:** EXPLORATORY

**Optional stronger mechanism; not an active gate.**

Choose one marked algebraic collision curve as in B120 and restrict the
original incidence family to its disk germ \(\Delta\). Realize the selected
B058 chain as

\[
 t\in A_\Delta,
\]

where \(A_\Delta\) is the exact boundary-zero thimble/nearby local system
before the two B022 quotients. Let \(J_\Delta\) be the combined kernel of
the equator-extension and base-locus quotient maps. The construction must
first prove that

\[
 q(t)=c\ne0
\]

is the prescribed primitive ambient detector and retains its nonzero pairing
with \(\zeta\).

For the cyclic disk monodromy \(M_\Delta\), compute

\[
 d=(M_\Delta-I)t\in J_\Delta.
\]

B085 makes the exact falsifiable condition

\[
 [d]=0
 \quad\text{in}\quad
 \operatorname{coker}(M_\Delta-I:J_\Delta\to J_\Delta).
\]

Equivalently, print a rational \(k\in J_\Delta\) satisfying

\[
 d+(M_\Delta-I)k=0.
\]

Then \(t_\Delta=t+k\) is nonzero because its quotient remains \(c\ne0\),
is cyclically invariant, and has the same prescribed pairing. This is a
valid stronger chain-level certificate, but B122/NG098 show it is not needed
for an ordinary special lift of the actual nearby target class and it does
not imply B107 filtered liftability.

## Current obstruction

If this optional route is pursued, its missing calculation is the matrix of
one actual original-disk monodromy on:

1. the selected distributed B057 coefficient vector;
2. the equator-extension subspace;
3. the base-locus kernel; and
4. their topology-changing comparison at the clean nodal endpoint.

G050 is the abstract cyclic cocycle parent and G051 its semistable
nilpotent-residue form. G082 insists that the final invariant vector live in
the original disk object and survive downstairs; a class supported only on
an alteration's exceptional locus does not pass the gate. B090-B091 prevent
replacing this computation by the positive nodal-boundary Hurwitz word.
The active gate is G065's boundary-marked relative comparison; this optional
cocycle calculation does not discharge it.
