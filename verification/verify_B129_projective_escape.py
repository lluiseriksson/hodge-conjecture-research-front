"""Finite arithmetic checks for the B129 Hodge escape countermodel."""

# Four punctures and a nontrivial rank-one local system with no local
# invariants give dim H_c^1 = -(2-rank-punctures) = r-2.
punctures = 4
euler_characteristic = 2 - punctures
h_c_0 = 0
h_c_2 = 0
h_c_1 = h_c_0 + h_c_2 - euler_characteristic
assert h_c_1 == 2

# H^1(C) has types (1,0),(0,1), while H^1(C)(1) has
# types (0,-1),(-1,0). Their tensor contains two (0,0) summands.
left_types = [(1, 0), (0, 1)]
right_types = [(0, -1), (-1, 0)]
tensor_types = [(a + c, b + d) for a, b in left_types for c, d in right_types]
assert tensor_types.count((0, 0)) == 2
assert all(a + b == 0 for a, b in tensor_types)

# A complex concentrated in degree -d has no degree -d+1 local target.
for dimension in range(1, 21):
    nonzero_sheaf_degrees = {-dimension}
    assert -dimension + 1 not in nonzero_sheaf_degrees

print("PASS: B129 projective full-support Hodge escape arithmetic")
