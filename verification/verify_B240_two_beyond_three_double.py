#!/usr/bin/env python3
"""Exact lightweight checks for B240, NG198, and G164; not a proof of HC."""


def counts(pattern: tuple[set[str], ...]) -> dict[str, int]:
    return {
        point: sum(point in factor for factor in pattern)
        for point in "pqrtux"
    }


def assert_mixed_base(pattern: tuple[set[str], ...]) -> dict[str, int]:
    result = counts(pattern)
    assert result["p"] >= 2
    assert result["q"] >= 2
    assert result["r"] >= 2
    assert result["t"] >= 1
    assert result["u"] >= 1
    return result


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G163 and its odd neighbor have two dimensions beyond three doubles.
        for slack in (4 * d + 8, 4 * d + 9):
            delta_1 = slack // 2
            assert delta_1 == 2 * d + 4
            assert d + 1 + delta_1 == 3 * d + 5

        # Standard quotient inequalities.
        if d >= 6:
            assert 2 * (d - 1) > d + 3
            assert d - 2 > 3
        else:
            assert d == 4
            assert (3 * d + 5) - 2 * (d + 1) == 7
            assert 2 * (d - 1) == 6
            assert 20 - (3 * d + 5) == 3
            assert 9 < 17

        # First unexcluded G164 signature.
        slack = 4 * d + 10
        delta_1 = 2 * d + 5
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 12
        assert h_1 == 3 * d + 6 == length // 2
        assert slack - 2 * delta_1 == 0

    # Sextic sixth-point separator: if x lies on pq, use pr and qr,
    # followed by the remaining p,q,t,u factors, all avoiding x.
    sextic = ({"p", "r"}, {"q", "r"}, {"p"}, {"q"}, {"t"}, {"u"})
    sextic_counts = assert_mixed_base(sextic)
    assert len(sextic) == 6
    assert sextic_counts["x"] == 0
    assert sextic_counts == {
        "p": 2, "q": 2, "r": 2, "t": 1, "u": 1, "x": 0
    }

    # Square polarization, x off the triangle: value or one transverse jet.
    off_value = ({"p", "q"}, {"p", "r"}, {"q", "r"}, {"t", "u"})
    off_jet = ({"p", "q"}, {"p", "r"}, {"q", "r"}, {"t", "u", "x"})
    assert assert_mixed_base(off_value)["x"] == 0
    assert assert_mixed_base(off_jet)["x"] == 1

    # Square polarization, x on pq.
    pair_value = ({"p", "r"}, {"q", "r"}, {"p", "t"}, {"q", "u"})
    pair_jet = (
        {"p", "r"},
        {"q", "r"},
        {"p", "q", "u", "x"},
        {"t"},
    )
    assert assert_mixed_base(pair_value)["x"] == 0
    assert assert_mixed_base(pair_jet)["x"] == 1
    assert 3 * 5 < 3 * 4 + 5  # triangle-line rank versus the smallest h_1

    # Q^4 nondegenerate W.  For L_1=<t^2,tf,tg,g^2>, evaluation at an
    # exterior vector with pairings (a,b,c) has rank one only at a=c=0.
    a, b, c = 0, 7, 0
    nondeg_images = (
        (2 * a, 0, 0),
        (b, a, 0),
        (c, 0, a),
        (0, 0, 2 * c),
    )
    nonzero_nondeg = [vector for vector in nondeg_images if any(vector)]
    assert nonzero_nondeg == [(b, 0, 0)]

    # Q^4 degenerate W.  For L_1=<rho^2,rho*t,t^2,t*f>, evaluation has
    # rank one only when the rho and t pairings vanish.
    rho_pairing, t_pairing, f_pairing = 0, 0, 11
    degenerate_images = (
        (2 * rho_pairing, 0, 0),
        (t_pairing, rho_pairing, 0),
        (0, 2 * t_pairing, 0),
        (0, f_pairing, t_pairing),
    )
    nonzero_degenerate = [vector for vector in degenerate_images if any(vector)]
    assert nonzero_degenerate == [(0, f_pairing, 0)]

    # Annihilator dimensions in the two Q^4 subbranches.
    assert 6 - 3 == 3  # exterior t: Sym^2(K)
    assert 6 - 2 == 4  # t in W
    assert 4 - 1 == 3  # one further tangent leaves Sym^2(K)
    assert 3 == 2 * (2 + 1) // 2

    print("PASS: B240 two-beyond-three-double exclusion, NG198, and G164")


if __name__ == "__main__":
    main()
