#!/usr/bin/env python3
"""Integer sign/count guards for B160-B161; not a topological proof or HC."""


def singular_euler(smooth_euler, hypersurface_dimension, milnor_sum):
    return smooth_euler - ((-1) ** hypersurface_dimension) * milnor_sum


for dimension in range(1, 10):
    for smooth_euler in range(-20, 21):
        for node_count in range(0, 15):
            value = singular_euler(smooth_euler, dimension, node_count)
            recovered = (
                (smooth_euler - value) * ((-1) ** dimension)
            )
            assert recovered == node_count


# Losing exactly one node always changes Euler characteristic by one with
# the dimension-dependent sign, including odd Hodge hyperplane dimension.
for dimension in range(1, 10):
    for central_nodes in range(1, 15):
        central = singular_euler(7, dimension, central_nodes)
        escaped = singular_euler(7, dimension, central_nodes - 1)
        assert central - escaped == -((-1) ** dimension)
        assert central != escaped

for n in range(1, 10):
    odd_dimension = 2 * n - 1
    assert singular_euler(11, odd_dimension, 5) == 16

print("PASS: B160 Euler-Milnor sign and B161 one-node escape")
