---
brick_id: B164
status: PROVED
base_field: C
variety: the smooth-total-space flat projective escape family of B161 and, independently, the universal hypersurface family of a basepoint-free complete linear system
smoothness: the B161 total space is smooth because every critical-value differential is nonzero; the universal hypersurface incidence is a smooth projective bundle over the ambient variety
projectivity: both family maps are projective
dimension: arbitrary hypersurface dimension r; arbitrary uniform value rank R<N in the B161 model
codimension: one node escapes along the codimension-R basis germ despite projective direct-image decomposition
coefficient_field: Q
cohomology_theory: proper direct images, decomposition theorem, semisimple perverse sheaves, proper base change, and microsupport
hodge_type: pure direct-image summands exist, but no specified detector type or pairing is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not resolved; decomposition alone does not make a specified Hodge class algebraic
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B159-B163, S037, S052, and S066
claim: The B161 node-escape family can be chosen with smooth total space, so the projective decomposition theorem applies to its rational direct image, yet after restriction to the basis germ the direct image is not locally constant and has nonzero microsupport. Likewise the smooth universal hypersurface total space has a decomposed direct image with discriminant microsupport. Therefore projective decomposition and semisimplicity do not imply B163's zero-microsupport condition.
falsifier: a singular point of the B161 total space under nonzero d tau_i, failure of projective decomposition for its smooth total space, local constancy on the escaping basis germ, or a theorem turning arbitrary semisimple IC summands into zero-section support
---

# B164 — Decomposition does not remove discriminant microsupport

## Smooth total space in the escape family

In B161, near the \(i\)-th tracked critical point the total hypersurface is

\[
 q_i(z)+\tau_i(t)=0.
\]

B159 uses nonzero linear forms \(d\tau_i(0)=\ell_i\). For the perturbed last
branch, \(d(\ell_N(x)+y^m)_0=\ell_N\ne0\). Hence the gradient of the total
equation is nonzero even where the spatial gradient vanishes. The total
space is smooth near every tracked node; it is smooth elsewhere after
shrinking because the central hypersurface was chosen smooth there.

The map \(g:\mathcal Y\to T\) is projective. S037's projective
decomposition theorem therefore decomposes

\[
 Rg_*\mathbf Q_{\mathcal Y}[\dim\mathcal Y]
\]

into shifted semisimple intersection-complex summands.

Nevertheless, on \(F_B=\{x=0\}\) the last node escapes by \(y^m\). B160
shows that fiber Euler characteristic jumps, and B163 gives

\[
 SS\!\left(Li^*Rg_*\mathbf Q_{\mathcal Y}\right)
 \not\subseteq T^*_{F_B}F_B.
\]

Here \(i:F_B\hookrightarrow T\), and proper base change identifies the
displayed derived restriction with the direct image of the base-changed
family.

Thus semisimple decomposition permits nonzero conormal support.

## Universal-family check

For a basepoint-free complete linear system \(P=|L|\), the universal
hypersurface

\[
 \mathcal U=\{(x,[s])\in X\times P:s(x)=0\}
\]

is the projectivization of the kernel of the evaluation bundle map over
\(X\), hence is smooth when \(X\) is smooth. The projection
\(\mathcal U\to P\) is projective, so its direct image also satisfies the
decomposition theorem. S052's transverse Lefschetz-disk calculation still
has a nonzero rank-one vanishing cycle at a nodal discriminant point.
Therefore the decomposed universal direct image itself has discriminant
microsupport.

## Consequence

The decomposition theorem controls purity, semisimplicity, shifts, and
strict supports. It does not say that every strict support is the whole
base or that every intersection complex is a local system. G104 must prove
the much stronger zero-section statement after restriction to its special
class-directed \(F_B\).
