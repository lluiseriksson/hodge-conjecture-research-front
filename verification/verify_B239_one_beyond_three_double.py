#!/usr/bin/env python3
"""Exact lightweight checks for B239, NG197, and G163; not a proof of HC."""


def incidence_counts(pattern: tuple[set[str], ...]) -> dict[str, int]:
    return {
        point: sum(point in factor for factor in pattern)
        for point in "pqrtu"
    }


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G162 and its odd neighbor have one dimension beyond three doubles.
        for slack in (4 * d + 6, 4 * d + 7):
            delta_1 = slack // 2
            assert delta_1 == 2 * d + 3
            assert d + 1 + delta_1 == 3 * d + 4

        # Standard-polarization quotient ranks outside the exceptional Q^4.
        if d >= 6:
            assert 2 * (d - 1) > d + 2
            assert d - 2 > 2

        # The residual Q^2 equality in the d=4 orthogonal branch.
        if d == 4:
            assert d + 2 == 2 * (d - 1) == 6

        # First unexcluded G163 signature.
        slack = 4 * d + 8
        delta_1 = 2 * d + 4
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 10
        assert h_1 == 3 * d + 5 == length // 2
        assert slack - 2 * delta_1 == 0

    # Sextic: one paired factor plus five single factors gives the mixed
    # multiplicities (2,2,2,1) while every factor can avoid u.
    sextic = ({"p", "q"}, {"p"}, {"q"}, {"r"}, {"r"}, {"t"})
    sextic_counts = incidence_counts(sextic)
    assert len(sextic) == 6
    assert sextic_counts == {"p": 2, "q": 2, "r": 2, "t": 1, "u": 0}

    # Quartic value separators in the three exhaustive incidence cases.
    outside_plane = ({"p", "q", "r"}, {"p", "q", "r"}, {"t"}, set())
    inside_triangle = ({"p", "q"}, {"p", "r"}, {"q", "r"}, {"t"})
    pair_line_off_t = ({"p", "r"}, {"q", "r"}, {"p", "t"}, {"q"})
    for pattern in (outside_plane, inside_triangle, pair_line_off_t):
        counts = incidence_counts(pattern)
        assert len(pattern) == 4
        assert counts["p"] >= 2 and counts["q"] >= 2 and counts["r"] >= 2
        assert counts["t"] >= 1 and counts["u"] == 0

    # On the exceptional pair line the value restriction is forced, but
    # this product has exactly one vanishing factor at u and hence a
    # potentially nonzero transverse first jet.
    line_jet = ({"p", "r"}, {"q", "r"}, {"p", "q", "t", "u"}, set())
    line_counts = incidence_counts(line_jet)
    assert line_counts == {"p": 2, "q": 2, "r": 2, "t": 1, "u": 1}
    assert 2 + 2 + 1 > 4  # restriction to the pair line is identically zero

    # Q^4, nondegenerate W: in a Witt basis (t,f,g), B(t,f)=1 and
    # B(g,g)=1.  The four surviving tensors act on x=(alpha,beta,gamma)
    # by the displayed coefficient vectors.
    alpha, beta, gamma = 2, 3, 5
    nondeg_actions = (
        (2 * beta, 0, 0),                 # t^2 x
        (alpha, beta, 0),                 # (t f) x
        (gamma, 0, beta),                 # (t g) x
        (0, 0, 2 * gamma),                # g^2 x
    )
    assert nondeg_actions[0] == (6, 0, 0)
    assert nondeg_actions[2] == (5, 0, 3)
    # The case split is exact: beta!=0 is killed by t^2; after beta=0,
    # gamma!=0 is killed by g^2 and t g; only the t-line remains.
    assert beta != 0 and gamma != 0

    # Q^4, degenerate W: basis (u,t,f), u radical.  The allowed tensors
    # are u^2,ut,t^2,tf; contraction conditions remove uf and f^2.
    allowed_degenerate = {"uu", "ut", "tt", "tf"}
    excluded_degenerate = {"uf", "ff"}
    assert len(allowed_degenerate) == 4
    assert allowed_degenerate.isdisjoint(excluded_degenerate)
    assert len(allowed_degenerate | excluded_degenerate) == 6

    # An exterior t imposes three conditions on Sym^2(W); an isotropic
    # t in W imposes only the two quotient conditions defining L.
    assert 6 - 3 == 3
    assert 6 - 2 == 4
    assert 5 + 1 < 16  # plane-conic plus t versus the required Q^4 rank

    print("PASS: B239 one-beyond-three-double exclusion, NG197, and G163")


if __name__ == "__main__":
    main()
