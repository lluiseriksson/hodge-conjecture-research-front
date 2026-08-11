from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
d = 22
for r in range(2):
    target = 160 + r
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_three = (d - 4) + (d - 5) + (d - 6)
    assert q == 51 + r
    assert residual == 114 + r < 148
    assert budget == 53 + r
    assert first_three == 51
    assert budget - first_three == 2 + r < d - 7 == 15
    assert 36 < target


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require("proofs/B285-standard-dimension-twenty-two-two-rank-band.md", ("brick_id: B285", "status: PROVED", "114+r", "h_Z(1)\\ge162", "disproof of HC"))
require("proofs/NG242-standard-dimension-twenty-two-two-rank-band.md", ("brick_id: NG242", "status: NO-GO", "G206", "160 and 161"))
require("proofs/G205-nonstandard-four-row-boundary.md", ("brick_id: G205", "status: NO-GO", "B285", "G206"))
require("proofs/G207-uniform-nonstandard-refinement.md", ("brick_id: G207", "status: EXPLORATORY", "AG(d)=7d+7", "active"))

print("PASS: B285 Q22 standard band, G205 no-go, and G206 uniform boundary")
