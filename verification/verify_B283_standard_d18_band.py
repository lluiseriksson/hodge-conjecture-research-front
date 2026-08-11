from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
d = 18
for r in range(6):
    target = 128 + r
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_three = (d - 4) + (d - 5) + (d - 6)
    assert q == 39 + r
    assert residual == 90 + r < 119
    assert budget == 41 + r
    assert first_three == 39
    assert budget - first_three == 2 + r < d - 7 == 11
    assert 36 < target


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require("proofs/B283-standard-dimension-eighteen-six-rank-band.md", ("brick_id: B283", "status: PROVED", "90+r", "h_Z(1)\\ge134", "disproof of HC"))
require("proofs/NG240-standard-dimension-eighteen-six-rank-band.md", ("brick_id: NG240", "status: NO-GO", "G204", "128 through 133"))
require("proofs/G203-all-nonstandard-next-boundary.md", ("brick_id: G203", "status: NO-GO", "B283", "G204"))
require("proofs/G204-nonstandard-three-row-boundary.md", ("brick_id: G204", "status: NO-GO", "AC(18)=133", "B284"))

print("PASS: B283 Q18 standard band, G203 no-go, and G204 boundary")
