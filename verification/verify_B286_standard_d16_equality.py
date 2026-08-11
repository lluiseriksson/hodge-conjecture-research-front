from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
d = 16
target = 119
q = target - (5 * d - 1)
budget = q + 2
residual = 3 * d - 3 + q
first_three = (d - 4) + (d - 5) + (d - 6)
fourth = d - 7
assert q == 40
assert residual == 85 < 108
assert budget == 42
assert first_three == 33
assert budget - first_three == fourth == 9
assert (8 + 2) * (8 + 1) // 2 == 45 < target


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require("proofs/B286-standard-dimension-sixteen-fourth-escape-equality.md", ("brick_id: B286", "status: PROVED", "45<119", "floor", "disproof of HC"))
require("proofs/NG243-standard-tie-at-uniform-boundary.md", ("brick_id: NG243", "status: NO-GO", "G207", "rank 119"))
require("proofs/G206-uniform-nonstandard-boundary.md", ("brick_id: G206", "status: EXPLORATORY", "B286", "nonstandard"))
require("proofs/G207-uniform-nonstandard-refinement.md", ("brick_id: G207", "status: EXPLORATORY", "AG(d)=7d+7", "active"))

print("PASS: B286 Q16 fourth-escape equality and G207 refinement")
