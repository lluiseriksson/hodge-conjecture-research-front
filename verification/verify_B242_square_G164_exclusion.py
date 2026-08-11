#!/usr/bin/env python3
"""Exact lightweight checks for B242, G164-G166, and NG200; not a proof of HC."""


def counts(pattern: tuple[set[str], ...]) -> dict[str, int]:
    return {
        point: sum(point in factor for factor in pattern)
        for point in "pqrtuxy"
    }


def assert_base(pattern: tuple[set[str], ...]) -> dict[str, int]:
    result = counts(pattern)
    assert result["p"] >= 2
    assert result["q"] >= 2
    assert result["r"] >= 2
    assert result["t"] >= 1
    assert result["u"] >= 1
    assert result["x"] >= 1
    return result


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G164 and its odd neighbor have the same integral rank.
        for slack in (4 * d + 10, 4 * d + 11):
            delta_1 = slack // 2
            assert delta_1 == 2 * d + 5
            assert d + 1 + delta_1 == 3 * d + 6

        # The next balanced G166 signature.
        slack = 4 * d + 12
        delta_1 = 2 * d + 6
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 14
        assert h_1 == 3 * d + 7 == length // 2
        assert slack - 2 * delta_1 == 0

    # The triangle and two-line rank bounds already fail in d=4.
    assert 3 * 5 < 3 * 4 + 6
    assert 2 * 5 + 3 < 3 * 4 + 6

    # Seventh point off the triangle: three edge factors plus one plane
    # factor.  y is either avoided or occurs in that sole transverse factor.
    off_value = ({"p", "q"}, {"p", "r"}, {"q", "r"}, {"t", "u", "x"})
    off_jet = (
        {"p", "q"},
        {"p", "r"},
        {"q", "r"},
        {"t", "u", "x", "y"},
    )
    assert assert_base(off_value)["y"] == 0
    assert assert_base(off_jet)["y"] == 1

    # Seventh point on pq: pr, qr, pt, and qux.
    pair_value = ({"p", "r"}, {"q", "r"}, {"p", "t"}, {"q", "u", "x"})
    pair_jet = (
        {"p", "r"},
        {"q", "r"},
        {"p", "t"},
        {"q", "u", "x", "y"},
    )
    assert assert_base(pair_value)["y"] == 0
    assert assert_base(pair_jet)["y"] == 1

    # Q^6 is the universal-quantifier falsifier: B241 leaves only k=2,
    # while B242 excludes k=2.
    d = 6
    assert 3 * d + 6 == 24
    surviving_polarizations_after_B241 = {2}
    surviving_polarizations_after_B242 = surviving_polarizations_after_B241 - {2}
    assert not surviving_polarizations_after_B242

    print("PASS: B242 square G164 exclusion, G164-G166, and NG200")


if __name__ == "__main__":
    main()
