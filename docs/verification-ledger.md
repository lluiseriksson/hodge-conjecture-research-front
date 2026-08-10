# Verification ledger

| ID | Claim | Label | Evidence | Remaining risk |
|---|---|---|---|---|
| D001 | exact official rational statement is fixed | PROVED | Deligne/Clay pp. 1-2; `problem-statement.md` | none beyond convention checks |
| L001 | algebraic cycle classes are of Hodge type | PROVED | standard cycle-class theorem; Deligne p. 1 | formalization absent |
| K001 | \(p=1\), \(p=n-1\), and \(n\le3\) cases | PROVED | Lefschetz (1,1), hard Lefschetz | primary-source audit can be expanded |
| B001 | universal HC iff universal middle HC | PROVED | `proofs/B001-middle-degree-reduction.md` | proof-assistant formalization absent |
| RC0 | a dominating relative cycle with fixed class gives fiberwise algebraicity | PROVED | functoriality/proper base change; encoded in G002 attempt | family singularities/base change must stay explicit |
| G001 | every middle class has an algebraic anchor in a connected Hodge locus | EXPLORATORY | no proof | may be as hard as HC |
| G002 | anchored Hodge locus is dominated by relative cycle space | CONDITIONAL | sufficient theorem formulated; proof only when dominance is assumed | dominance is the open content |
| NG-001 | CDK algebraicity alone implies G002 | NO-GO | logical audit in `no-go-ledger.md` | none; route requires a new input |

## Promotion rule

A claim moves to `PROVED` only when all dependencies are theorems with matching
fields, coefficients, cohomology, and scope. It moves to `FORMALLY VERIFIED`
only with a reproducible kernel-checked theorem and no project-local axiom for
the decisive content.

