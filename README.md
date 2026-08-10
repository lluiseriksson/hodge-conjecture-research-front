# Rational Hodge Conjecture Research Front

> **Status (2026-08-10): EXPLORATORY research programme. This repository does not prove or disprove the Hodge Conjecture.**

This is an independent, audit-first repository devoted exclusively to the
standard **rational** Hodge Conjecture for arbitrary smooth projective complex
varieties. Its terminal target is an unconditional, complete, non-circular,
auditable proof or disproof.

The strongest result is now an exact, primary-source-audited vertical
equivalence: the universal rational conjecture holds if and only if every
nonzero primitive rational middle Hodge class restricts nontrivially to some
high-degree singular hyperplane section, equivalently its admissible normal
function has a nonzero boundary singularity. The repository also contains a
proved middle-degree reduction and semiregular deformation lemmas. The
class-specific nonvanishing and the general cycle construction remain
completely open. See [STATUS.md](STATUS.md).

## Official target

For every smooth projective algebraic variety \(X/\mathbf C\) and every
integer \(p\ge 0\), the Betti cycle-class map

\[
  \operatorname{cl}_{B,\mathbf Q}:CH^p(X)_{\mathbf Q}
  \longrightarrow H^{2p}(X^{an},\mathbf Q(p))
\]

is surjective onto the rational Hodge classes
\(H^{2p}(X,\mathbf Q(p))\cap H^{0,0}\), equivalently onto
\(H^{2p}(X,\mathbf Q)\cap H^{p,p}(X)\) before the Tate twist.

Read the exact quantifiers and conventions in
[docs/problem-statement.md](docs/problem-statement.md).

## Non-claims

This programme never substitutes any of the following for the terminal target:

- the integral Hodge conjecture (false in general);
- a compact Kahler analogue (false in general);
- a low-dimensional or special-family theorem;
- numerical or algebraic equivalence in place of the Betti class-map image;
- a period computation, dimension count, or Hodge-locus calculation;
- a theorem whose hypotheses already assume the desired class is algebraic.

## Research loop

Every cycle is:

```text
brick -> source audit -> adversarial verification -> commit -> ledger update -> next gate
```

Every result is labeled exactly one of `EXPLORATORY`, `NUMERICAL`,
`CONDITIONAL`, `PROVED`, `FORMALLY VERIFIED`, or `NO-GO`. Every mathematical
brick carries the metadata required by [docs/brick-schema.md](docs/brick-schema.md).

## Vertical dependency

```text
standard rational Hodge Conjecture
  <=> primitive singular-hyperplane detection                    [B007, PROVED]
  <= class-specific local nonvanishing                           [G005, OPEN]

secondary route:
  <=> universal middle-degree cycle construction                 [B001, PROVED]
  <= algebraic-anchor access + semiregular presentation          [G001/G004, OPEN]
  <= all-order semiregular propagation                           [B004, PROVED]
```

The active gate is **G005**: given arbitrary
\((X,L,\zeta)\), construct a discriminant point \(p\) at which the local
intersection-cohomology singularity of \(\zeta\)'s normal function is nonzero,
without assuming an algebraic representative. High degree provides
nontrivial ambient vanishing cycles but not this class-specific projection.
The anchored G001/G004 route remains open as an independent secondary route.

## Repository map

| Path | Purpose |
|---|---|
| `docs/problem-statement.md` | exact official rational statement and exclusions |
| `docs/landscape.md` | known cases, mechanisms, obstructions, and open scope |
| `docs/vertical-map.md` | implication graph and current gate |
| `docs/verification-ledger.md` | claim-by-claim status and evidence |
| `docs/no-go-ledger.md` | failed routes with precise failure points |
| `docs/source-citations/` | primary-source audit records |
| `proofs/` | statement-first proof bricks and failed attempts |
| `experiments/` | diagnostics that can never be promoted without proof |
| `formal/` | formalization boundary and future kernel-checked work |
| `verification/` | deterministic repository audits |
| `artifacts/` | machine-readable research state and generated outputs |

## Verify

```bash
python verification/verify_repository.py
```

The verifier checks the required directory topology, result labels, metadata
keys on proof bricks, ledger identifiers, and the explicit non-claim banner.
A green check certifies repository consistency only; it is not evidence for
the conjecture.
