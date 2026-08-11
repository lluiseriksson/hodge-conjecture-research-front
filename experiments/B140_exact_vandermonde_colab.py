"""Colab-only exact-Q stress test for B140; do not run on the local workstation.

This intentionally reproduces the rational SymPy rank calculation that
exceeded the local 30-second resource ceiling.  The repository verifier uses
a bounded modular certificate instead.  Run this file only on the designated
Colab Pro+ CPU/high-RAM runtime.
"""

from fractions import Fraction
from time import perf_counter

import sympy as sp


started = perf_counter()
for t in range(5, 10):
    count = 4 * t + 2
    points = [Fraction(i + 1, i + 2) for i in range(count)]
    matrix = sp.Matrix(
        [
            [sp.Rational(p.numerator, p.denominator) ** j for j in range(4 * t + 1)]
            for p in points
        ]
    )
    rank = matrix.rank()
    assert rank == 4 * t + 1
    assert count - rank == 1
    print(f"t={t}: rank={rank}, nullity={count-rank}")

print(f"COLAB PASS: exact rational ranks in {perf_counter()-started:.3f}s")
