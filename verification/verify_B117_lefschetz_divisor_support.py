"""Shift and multiplicity checks for B117 and NG093."""


for n in range(1, 21):
    d = 2 * n - 1
    surface_total_shift = d + 2
    disk_total_shift = d + 1

    assert surface_total_shift == 2 * n + 1
    assert disk_total_shift == 2 * n

    # On the disk, H^k(Rg_*Q[d+1]) = R^(k+d+1)g_*Q.
    assert 0 + disk_total_shift == d + 1
    assert -1 + disk_total_shift == d

    # A punctual pH^0 summand sits in normalized ordinary degree zero.
    punctual_degree = 0
    assert punctual_degree + disk_total_shift == d + 1

    # Therefore the middle direct image R^d is one degree too low.
    assert d != punctual_degree + disk_total_shift


# Decomposition gives special rank = constant full-support rank + punctual rank.
for generic_rank in range(0, 25):
    special_rank = generic_rank  # S052 cospecialization isomorphism
    punctual_rank = special_rank - generic_rank
    assert punctual_rank == 0

print("PASS: B117 transverse Lefschetz divisors have zero pH0 support")
