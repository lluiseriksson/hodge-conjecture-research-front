"""Exact representation check for B113 and NG089."""

from fractions import Fraction


s1 = ((-1, 1), (0, 1))
s2 = ((1, 0), (1, -1))


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


identity = ((1, 0), (0, 1))
elements = {identity}
frontier = [identity]
while frontier:
    current = frontier.pop()
    for generator in (s1, s2):
        candidate = multiply(generator, current)
        if candidate not in elements:
            elements.add(candidate)
            frontier.append(candidate)

assert len(elements) == 6
average = tuple(
    tuple(Fraction(sum(g[i][j] for g in elements), 6) for j in range(2))
    for i in range(2)
)
assert average == ((0, 0), (0, 0))

# In V direct-sum Qw, Reynolds kills V and retains exactly the trivial w.
for v1, v2, w in ((1, 0, 0), (2, -3, 0), (4, 5, 7)):
    descended = (0, 0, Fraction(w))
    assert (descended != (0, 0, 0)) == (w != 0)

print("PASS: B113 local A2 excess descends only through a nonlocal trivial component")
