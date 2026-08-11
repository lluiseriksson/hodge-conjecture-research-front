from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
d = 20
for r in range(4):
    target = 144 + r
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_three = (d - 4) + (d - 5) + (d - 6)
    assert q == 45 + r
    assert residual == 102 + r < 134
    assert budget == 47 + r
    assert first_three == 45
    assert budget - first_three == 2 + r < d - 7 == 13
    assert 36 < target


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require("proofs/B284-standard-dimension-twenty-four-rank-band.md", ("brick_id: B284", "status: PROVED", "102+r", "h_Z(1)\\ge148", "disproof of HC"))
require("proofs/NG241-standard-dimension-twenty-four-rank-band.md", ("brick_id: NG241", "status: NO-GO", "G205", "144 through 147"))
require("proofs/G204-nonstandard-three-row-boundary.md", ("brick_id: G204", "status: NO-GO", "B284", "G205"))
require("proofs/G205-nonstandard-four-row-boundary.md", ("brick_id: G205", "status: NO-GO", "AD(20)=147", "B285"))

print("PASS: B284 Q20 standard band, G204 no-go, and G205 boundary")
