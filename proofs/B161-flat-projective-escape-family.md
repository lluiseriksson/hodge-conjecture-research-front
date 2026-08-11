---
brick_id: B161
status: PROVED
base_field: C
variety: the projective realization of B159 on a connected smooth projective variety X using a sufficiently high power of an ample line bundle
smoothness: the central hypersurface has exactly the prescribed ordinary double points and is smooth elsewhere; nearby singularities remain confined to the tracked Morse charts
projectivity: every fiber is a projective effective Cartier divisor in one fixed linear system
dimension: arbitrary smooth projective ambient dimension d; hypersurface dimension r=d-1; base dimension R+1
codimension: the family is flat with fixed Hilbert polynomial, while one node escapes along the codimension-R basis germ
coefficient_field: C for the family and Z for Hilbert polynomial and Euler characteristic
cohomology_theory: coherent jet interpolation, relative effective Cartier divisors, flatness, Hilbert polynomials, and Euler–Milnor comparison
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no specified Hodge class is assumed algebraic
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B160 and S065
claim: The arbitrary-rank escaping germ of B159 can be realized as a flat projective hypersurface family with every fiber in one fixed linear system and hence with constant Hilbert polynomial, while the topological Euler characteristic changes by one signed Milnor contribution along the basis-node germ. Therefore projective flatness and Hilbert-polynomial constancy do not imply B160's Euler rigidity.
falsifier: failure of the B157 family to be a relative effective Cartier divisor after shrinking, variation of its Hilbert polynomial, an untracked singularity invalidating the Euler comparison, or constancy of Euler characteristic when exactly one node disappears
---

# B161 — Flat projective families still permit node escape

Apply B157 to B159's critical-value germ

\[
 \tau_i=\ell_i(x)\quad(i<N),\qquad
 \tau_N=\ell_N(x)+y^m.
\]

Work on the connected component of \(X\) containing the prescribed points;
the B159 base germ is smooth and connected. After shrinking it, the section
\(s(t)\) is nonzero on every fiber of \(X\times T\to T\). Its zero scheme

\[
 \mathcal Y=Z(s)\subset X\times T
\]

is a relative effective Cartier divisor: the ambient product is smooth,
the total section is a non-zero-divisor, and its restriction to every fiber
is a nonzero section of the same line bundle. Hence
\(\mathcal Y\to T\) is flat. All fibers lie in \(|L^k|\), so their Hilbert
polynomial is constant.

B157 chooses the central section smooth away from the prescribed nodes.
Properness of \(X\) and openness of smoothness allow the base to be shrunk
so that no new singularity occurs outside the disjoint tracked Morse
charts.

On the basis germ \(F_B=\{x=0\}\), the first \(N-1\) critical values vanish.
At \(y=0\), the last one vanishes as well, so the fiber has \(N\) nodes. At
\(y\ne0\), the last value is \(y^m\ne0\), so precisely that node disappears
and the fiber has \(N-1\) nodes. B160 therefore gives

\[
 \chi(Y_{(0,0)})-\chi(Y_{(0,y)})
 =-(-1)^r.
\]

The topological Euler characteristic is not constant although the family
is flat, projective, and Hilbert-polynomial constant. These algebraic
properties alone cannot close G101.
