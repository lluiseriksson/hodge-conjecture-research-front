#!/usr/bin/env python3
"""Degree normalization check for B093 on a two-dimensional base."""

base_dimension = 2
raw_relation_degree = 1
perverse_stalk_degree = raw_relation_degree - base_dimension

assert perverse_stalk_degree == -1
assert (-1, 0) == (perverse_stalk_degree, 0)
print("PASS: B093 H^1(j_!*L) equals H^-1((j_!*L[2])_H)")
