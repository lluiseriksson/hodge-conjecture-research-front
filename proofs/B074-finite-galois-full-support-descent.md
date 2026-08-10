---
brick_id: B074
status: PROVED
base_field: C
variety: a finite Galois cover q_U of a dense smooth open U and a finite extension q of a compactifying base, with a rational Hodge local system on U
smoothness: U and its cover are smooth; compactifications may be singular but the application uses B071's regular stack
projectivity: q is finite and hence proper/projective; later semistable modifications are projective
dimension: arbitrary
codimension: arbitrary boundary codimension; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: perverse rational mixed Hodge modules, intermediate extension, finite proper pushforward, and finite-group invariants
hodge_type: invariant direct summands remain rational Hodge subobjects; no detector class is produced
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative
dependencies: B072
claim: For a finite Galois cover q_U:U'->U with group Gamma extending finitely across the boundary, the Gamma-invariant part of q_* j'_{!*} q_U^* L is canonically j_{!*} L for every rational Hodge local system L on U.
falsifier: failure of finite pushforward exactness, failure of invariants to be exact over Q, or a boundary subquotient in the invariant image contradicting intermediate-extension uniqueness
---

# B074 — Finite-Galois descent of the full-support summand

**Status:** PROVED

Let \(j:U\hookrightarrow B\) be a dense open immersion and let
\(q_U:U'\to U\) be a finite étale Galois cover with group \(\Gamma\),
extending to a finite map \(q:B'\to B\). Write
\(j':U'\hookrightarrow B'\). For a rational Hodge local system \(L\) on
\(U\), set

\[
M'=j'_{!*}q_U^*L.
\]

Finite pushforward is exact for the perverse t-structure. It also commutes
with the open-extension functors in the two squares. Therefore

\[
q_*M'
=\operatorname{im}\bigl(q_*j'_!q_U^*L\to q_*j'_*q_U^*L\bigr)
=j_{!*}(q_{U*}q_U^*L).
\]

Because the coefficient field is \(\mathbf Q\), the Reynolds projector

\[
e_\Gamma=|\Gamma|^{-1}\sum_{g\in\Gamma}g
\]

splits and taking invariants is exact. On the Galois open,

\[
(q_{U*}q_U^*L)^\Gamma\simeq L.
\]

Taking the invariant direct summand in the displayed intermediate extension
therefore gives the canonical isomorphism

\[
(q_*M')^\Gamma\simeq j_{!*}L.
\]

B072 puts every functor and projector in rational mixed Hodge modules on the
quotient stack, so this is an isomorphism of Hodge objects, not merely of
complex perverse sheaves.

## Exact boundary

B074 guarantees a trivial full-support constituent. It does not show that a
particular boundary or nearby-cycle class has a nonzero component in that
constituent. B073 shows that a class lying in the local \(A_2\) standard
constituent averages to zero even though B074's global trivial summand exists.
G042 isolates the missing class-level landing statement.
