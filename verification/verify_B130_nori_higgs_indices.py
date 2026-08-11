"""Index and filtration checks for B130/NG104."""

for middle_codimension in range(2, 21):
    r = middle_codimension
    brogan_n = 2 * r - 1
    k = 2 * r
    b = r

    # Nori/Brogan range and Corollary 4.1 range.
    assert k < 2 * brogan_n
    assert k - b < brogan_n

    # Specialization k=n+1 has one primitive summand of type (r,r)
    # and lands in ordinary complex degree -d+1.
    assert k == brogan_n + 1
    assert (b, brogan_n + 1 - b) == (r, r)
    degree_offset_from_minus_d = -brogan_n + k
    assert degree_offset_from_minus_d == 1

    # On the smooth locus DR(V)=V[d], so only degree -d survives;
    # the degree -d+1 Higgs cohomology cannot be read as Betti cohomology.
    ordinary_offset_degrees = {0}
    assert degree_offset_from_minus_d not in ordinary_offset_degrees

print("PASS: B130 Nori-Brogan indices and NG104 filtration guard")
