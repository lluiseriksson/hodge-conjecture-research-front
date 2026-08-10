# Verification ledger

| ID | Claim | Label | Evidence | Remaining risk |
|---|---|---|---|---|
| D001 | exact official rational statement is fixed | PROVED | Deligne/Clay pp. 1-2; `problem-statement.md` | none beyond convention checks |
| L001 | algebraic cycle classes are of Hodge type | PROVED | standard cycle-class theorem; Deligne p. 1 | formalization absent |
| K001 | \(p=1\), \(p=n-1\), and \(n\le3\) cases | PROVED | Lefschetz (1,1), hard Lefschetz | primary-source audit can be expanded |
| B001 | universal HC iff universal middle HC | PROVED | `proofs/B001-middle-degree-reduction.md` | proof-assistant formalization absent |
| RC0 | a dominating relative cycle with fixed class gives fiberwise algebraicity | PROVED | functoriality/proper base change; encoded in G002 attempt | family singularities/base change must stay explicit |
| B002 | smooth Hilbert point plus tangent surjectivity forces component dominance and fiberwise cycles | PROVED | `proofs/B002-hilbert-dominance-criterion.md` | exact formalization absent |
| B003 | semiregular lci cycles lift along first-order Hodge-preserving deformations | PROVED | Bloch theorem 7.1; `proofs/B003-semiregular-infinitesimal-bridge.md` | first-order only; exact original-page audit incomplete |
| B004 | injectively combined semiregular lci presentations propagate over an irreducible Hodge base | PROVED | Ran Theorem 0(ii), BF 5.2/7.8-7.10, B002; `proofs/B004-semiregular-presentation-propagation.md` | conventional proof only; tuple-linearity not formalized |
| G001 | every middle class has an algebraic anchor in a connected Hodge locus | EXPLORATORY | no proof | may be as hard as HC |
| G002 | anchored Hodge locus is dominated by relative cycle space | CONDITIONAL | sufficient theorem formulated; proof only when dominance is assumed | dominance is the open content |
| G003 | every anchored class has a B002-good cycle representative | EXPLORATORY | no proof; semiregularity source seeded | likely fails without strong lci/obstruction hypotheses |
| G004 | every algebraic anchor has an injectively combined semiregular lci presentation | EXPLORATORY | no proof; precise falsifier recorded | moving and K-theory generation do not control injectivity |
| NG-001 | CDK algebraicity alone implies G002 | NO-GO | logical audit in `no-go-ledger.md` | none; route requires a new input |
| NG-004 | Bloch semiregularity is automatic for arbitrary anchor cycles | NO-GO | hypothesis audit in `no-go-ledger.md` | exact positive scope still needs deep source audit |
| NG-005 | moving/K-theory generation supplies a G004 presentation | NO-GO | logical obstruction in `no-go-ledger.md` | requires a new stabilization theorem |

## Promotion rule

A claim moves to `PROVED` only when all dependencies are theorems with matching
fields, coefficients, cohomology, and scope. It moves to `FORMALLY VERIFIED`
only with a reproducible kernel-checked theorem and no project-local axiom for
the decisive content.
