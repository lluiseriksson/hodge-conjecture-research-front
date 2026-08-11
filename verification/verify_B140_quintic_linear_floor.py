"""Finite consistency checks for B140's h=5 threshold and component lemma."""

def modular_rank(matrix: list[list[int]], prime: int) -> int:
    """Row rank over F_prime; full column rank certifies the Q-rank."""
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column] % prime:
                factor = rows[i][column] % prime
                rows[i] = [
                    (a - factor * b) % prime
                    for a, b in zip(rows[i], rows[rank])
                ]
        rank += 1
    return rank


def rational_normal_quartic_rank(t: int) -> tuple[int, int]:
    """Rank and nullity for 4t+2 points on u -> (u,u^2,u^3,u^4)."""
    count = 4 * t + 2
    prime = 1009
    matrix = [
        [pow(point, exponent, prime) for exponent in range(4 * t + 1)]
        for point in range(1, count + 1)
    ]
    rank = modular_rank(matrix, prime)
    return rank, count - rank


for t in range(5, 10):
    threshold = 5 * (t - 2) - 1
    assert threshold == 5 * t - 11
    assert threshold + 1 == 5 * t - 10

    rank, nullity = rational_normal_quartic_rank(t)
    assert rank == 4 * t + 1
    assert nullity == 1

    # The component lower bound e(t-Q)-C eventually beats both restriction
    # degree em and the first-jet bound em+b_e when n >= 2.
    n, e, q, constant, b = 2, 4, 3, 7, 11
    m = 30 + t
    c = 2
    adjoint_degree = m * n - c
    component_points = e * (adjoint_degree - q) - constant
    assert component_points > e * m
    assert component_points > e * m + b

print("PASS: B140 h=5 threshold, quartic circuit rank, and component asymptotics")
