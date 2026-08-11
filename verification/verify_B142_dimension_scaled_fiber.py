#!/usr/bin/env python3
"""Lightweight exact arithmetic guards for B142; not a proof of HC."""

from math import comb, factorial


def evaluation_rank(n: int, m: int) -> int:
    return comb(m + n, n) - n


for n in range(2, 9):
    q = factorial(n)
    for m in range(2, 41):
        nodes = m**n
        rank = evaluation_rank(n, m)
        adjoint_degree = n * m - n - 1

        assert rank == comb(m + n, n) - n
        assert q * rank >= nodes
        assert adjoint_degree == n * (m - 1) - 1

    # B141 normalization is genuinely superlinear for every n >= 2.
    ratios = [m**n / (n * m - n - 1) for m in (20, 40, 80)]
    assert ratios[0] < ratios[1] < ratios[2]

    # (h1+h2) gamma_n telescopes; all interior coefficients cancel.
    gamma = [(-1) ** i for i in range(n + 1)]
    product = [0] * (n + 2)
    for i, coefficient in enumerate(gamma):
        product[i] += coefficient
        product[i + 1] += coefficient
    assert all(coefficient == 0 for coefficient in product[1:-1])
    # Endpoint monomials vanish in H*(P^n x P^n); the fiber pairing is
    # the h2^n coefficient of gamma_n.
    assert gamma[-1] == (-1) ** n
    assert gamma[-1] != 0
    self_pairing = sum(gamma[i] * gamma[n - i] for i in range(n + 1))
    assert self_pairing == (-1) ** n * (n + 1)
    assert self_pairing != 0

print("PASS: B142 node, rank, factorial-block, adjoint, and primitive guards")
