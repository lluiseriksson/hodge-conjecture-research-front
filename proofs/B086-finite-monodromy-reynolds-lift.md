---
brick_id: B086
status: PROVED
base_field: C in the collision application; the representation argument is over Q
variety: a finite root-cover or deck-group stage of a proper collision family
smoothness: generic fibers smooth; no special-fiber smoothness is required for the representation lemma
projectivity: collision family projective in the application; the finite-group lemma is linear
dimension: arbitrary; ambient dimension 2n in the Hodge application
codimension: middle codimension n; no new support codimension
coefficient_field: Q
cohomology_theory: finite-group representations, rational local systems, Reynolds averaging, and B022 quotient homology
hodge_type: averaging is a rational Hodge morphism when the sequence is one of Hodge structures, but no algebraic cycle is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the downstream application
scope: relative and fiberwise
dependencies: B022, B074-B076, B085
claim: For an exact sequence 0 -> J -> A -> V -> 0 of rational representations of a finite group Gamma, every invariant quotient class c in V has a Gamma-invariant lift obtained by Reynolds averaging; hence the finite-monodromy part of B085's obstruction always vanishes.
falsifier: an invariant rational quotient class whose every lift has nonzero finite-group cohomology obstruction after averaging
---

# B086 — Finite collision monodromy has an invariant rational lift

**Status:** PROVED

Let

\[
0\longrightarrow J\longrightarrow A\xrightarrow{q}V\longrightarrow0
\]

be an exact sequence of rational $\Gamma$-representations with $\Gamma$
finite. Let $c\in V^\Gamma$ and choose any lift $t\in A$. Define

\[
 \overline t=\frac1{|\Gamma|}\sum_{\gamma\in\Gamma}\gamma t.
\]

Then $\overline t\in A^\Gamma$ and

\[
 q(\overline t)
 =\frac1{|\Gamma|}\sum_\gamma\gamma c=c.
\]

Thus every invariant quotient class has an invariant rational lift. The
adjustment $\overline t-t$ lies in $J$, so it preserves the B022 ambient
class and its prescribed pairing.

For the $A_2$ root construction, this kills the finite $S_3$ deck component
of G050's obstruction. It is the class-level Reynolds argument underlying
the exactness of invariants used in B074.

## Boundary

Semistable reduction leaves a generally nontrivial unipotent local
monodromy after the finite root cover. Averaging the finite deck group does
not make a lift invariant under that infinite cyclic action. B087/G051
isolate the remaining nilpotent-residue obstruction.
