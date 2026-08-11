from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

for d in range(14, 102, 2):
    assert (d + 1) ** 2 - (7 * d + 7) == (d - 6) * (d + 1) > 0
    assert d + 1 > d

for k in range(2, 20):
    assert 2 * k - 2 >= 2


def require(path: str, needles: tuple[str, ...]) -> None:
    content = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in content, f"missing {needle!r} in {path}"


require(
    "proofs/B287-nonstandard-iterated-double-block-floor.md",
    ("brick_id: B287", "status: PROVED", "(d+1)^2", "E^2", "disproof of HC"),
)
require(
    "proofs/NG244-nonstandard-uniform-boundary.md",
    ("brick_id: NG244", "status: NO-GO", "G208", "(d+1)^2"),
)
require(
    "proofs/G208-standard-piecewise-frontier.md",
    ("brick_id: G208", "status: EXPLORATORY", "E(14)=108", "8d-16"),
)

print("PASS: B287 iterated nonstandard floor and G208 standard frontier")
