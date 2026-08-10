# Mathematical brick contract

Every Markdown file under `proofs/` begins with a YAML front matter record
containing all fields below. `not-applicable` is allowed only with a written
reason in the body.

| Key | Required meaning |
|---|---|
| `brick_id` | stable identifier (`B...`, `G...`, or `NG...`) |
| `status` | one allowed result label |
| `base_field` | field over which the variety is defined |
| `variety` | exact object or quantified class of objects |
| `smoothness` | smoothness assumptions |
| `projectivity` | projectivity/properness assumptions |
| `dimension` | fixed dimension or quantified range |
| `codimension` | cycle codimension |
| `coefficient_field` | coefficients on cycles and cohomology |
| `cohomology_theory` | Betti, de Rham, etale, etc. |
| `hodge_type` | exact bidegree/Tate-twisted type |
| `cycle_class_map` | domain, codomain, and normalization |
| `cycle_equivalence` | equivalence used in the cycle group |
| `scope` | `absolute`, `relative`, `generic`, or `fiberwise` |
| `dependencies` | prior bricks and external theorems |
| `claim` | one-sentence falsifiable claim |
| `falsifier` | concrete observation that refutes or blocks the claim |

## Status semantics

- `EXPLORATORY`: candidate statement or route, not established.
- `NUMERICAL`: computational evidence only.
- `CONDITIONAL`: proved only from enumerated hypotheses.
- `PROVED`: complete conventional proof included and audited locally.
- `FORMALLY VERIFIED`: kernel-checked with toolchain and theorem identifier.
- `NO-GO`: route fails; the exact failed inference is recorded.

`PROVED` never means “proved modulo the Hodge Conjecture,” and `FORMALLY
VERIFIED` never applies to a theorem whose decisive content is stored as an
axiom or opaque hypothesis.

