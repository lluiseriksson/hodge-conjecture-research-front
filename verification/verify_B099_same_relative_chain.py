#!/usr/bin/env python3
"""Finite boundary/pushforward model for B099's same-chain statement."""

from fractions import Fraction

# Relative class coordinates: local boundary, equator, base, ambient.
gamma_prime = (Fraction(2), Fraction(7), Fraction(-3), Fraction(5))
b057_chain = gamma_prime

boundary = lambda value: value[0]
ambient = lambda value: value[3]

assert boundary(gamma_prime) == boundary(b057_chain) == Fraction(2)
assert ambient(gamma_prime) == ambient(b057_chain) == Fraction(5)
print("PASS: B099 same relative chain has the same boundary and ambient image")
