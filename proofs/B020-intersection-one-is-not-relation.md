---
brick_id: B020
status: PROVED
base_field: C
variety: a smooth projective embedded variety X of even dimension with nonzero vanishing cohomology and its smooth and singular hyperplane sections
smoothness: X is smooth; smooth reference hyperplane sections are used; singular sections in the audited plane slice have either ordinary double points or one cusp-type singularity of Milnor number two
projectivity: X is projective with a fixed projective embedding
dimension: dim X = d = 2n; a hyperplane section has dimension 2n-1
codimension: middle codimension n on X; the discriminant is a hypersurface and its node/cusp strata have codimension two in a general plane slice
coefficient_field: Z for the vanishing lattice and Q for the independence and Hodge comparison
cohomology_theory: singular homology and cohomology, vanishing homology, Milnor fibers, intersection pairing, and Picard-Lefschetz monodromy
hodge_type: no type-(0,0) relation is produced; the audited vanishing cycles are topological classes in the odd-dimensional hyperplane fiber
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraic cycle or detector class is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Schnell Lemma 6 and its proof in Section 3.4 (S023), plus elementary linear algebra
claim: Schnell's intersection-one pair of vanishing cycles is rationally linearly independent and therefore cannot itself be the desired two-term local relation; the adjacent dual-plane node statement supplies a two-ODP hyperplane but no relation or type-(0,0) detector theorem.
falsifier: vanishing cycles delta_1 and delta_2 with intersection number one that satisfy a nontrivial rational linear relation, or a relation/type-(0,0) conclusion in the cited dual-plane node argument
---

# B020 - Intersection one is not a relation

Let \(X\) be as in Schnell's Section 3.4, with even complex dimension
\(d=2n\) and nonzero vanishing cohomology. Lemma 6 produces vanishing cycles
\(\delta_1,\delta_2\) satisfying

\[
 (\delta_1,\delta_2)=1.
\]

They are linearly independent over \(\mathbf Q\). Indeed, if
\(a\delta_1+b\delta_2=0\), pairing with \(\delta_1\) and \(\delta_2\), and
using skew-symmetry and \((\delta_i,\delta_i)=0\), gives
\(b=0\) and \(a=0\). In particular, \(\delta_1-\delta_2\ne0\); this pair
does not define a nonzero element of the kernel of a two-generator
vanishing-cycle map.

Schnell proves existence by taking a general plane section of the dual
variety. In that plane curve:

- a node corresponds to a hyperplane section of \(X\) with two ordinary
  double points;
- a cusp corresponds to one isolated singularity of Milnor number two.

The cusp supplies the intersection-one pair. Its two cycles are independent,
not a relation. The statement about a node supplies a simultaneous two-ODP
member, but the cited argument does not assert that its two vanishing cycles
are dependent, that any relation has rational type \((0,0)\), or that its
Saito ambient class is nonzero.

## Consequence for G009

Nontrivial vanishing lattices and codimension-two discriminant singularities
are insufficient. The local detector needs an actual kernel element
\(\beta\), its type-\((0,0)\) property, and nonzero ambient pushforward
\(\gamma_\beta\). Intersection number one certifies the opposite of the
first requirement for the particular pair constructed in Lemma 6.

