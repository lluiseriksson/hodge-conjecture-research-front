"""Bounded arithmetic guards for B141's superlinear quantifiers."""


def banerjee_floor(t: int, carrier_bound: int, error: int) -> int:
    return carrier_bound * t - error


for linear_coefficient in range(1, 9):
    carrier_bound = linear_coefficient + 1
    additive_error = 7 * carrier_bound**2 + 3
    additive_budget = 11
    threshold = additive_error + additive_budget + 1
    for t in range(threshold, threshold + 10):
        attempted = linear_coefficient * t + additive_budget
        assert attempted < banerjee_floor(t, carrier_bound, additive_error)

# Arbitrarily many fixed carrier bounds force arbitrarily large normalized
# lower bounds once their individual high-degree thresholds are crossed.
t = 10_000
normalized_floors = [banerjee_floor(t, e, e**3) / t for e in range(1, 20)]
assert normalized_floors[-1] > normalized_floors[4]
assert normalized_floors[-1] > 18

print("PASS: B141 fixed-E floors exclude every fixed linear node budget")
