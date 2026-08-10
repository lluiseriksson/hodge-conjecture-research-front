---
brick_id: B078
status: PROVED
base_field: C
variety: proper toric morphisms between complex toric varieties; the strongest constant-sheaf form assumes simplicial source and target
smoothness: arbitrary toric varieties for the intersection-complex statement; smooth varieties are a special simplicial case
projectivity: proper for parity and fiber purity; projective for the relative-hard-Lefschetz monotonicity
dimension: arbitrary source and target dimensions
codimension: arbitrary torus-orbit support codimension; terminal cycles would have codimension n
coefficient_field: Q
cohomology_theory: rational intersection cohomology, decomposition theorem, fiber cohomology, and mixed Hodge structures
hodge_type: fibers of a proper toric map with simplicial source have pure Hodge-Tate cohomology and no odd cohomology
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: S048
claim: For a proper toric fibration, every support summand IC_V[-b] satisfies b+dim(X)-dim(V) even; for a general proper toric map the finite-factor version has the same parity with finite local-system coefficients, and with simplicial source every fiber has pure Hodge-Tate even cohomology.
falsifier: a support multiplicity with b+dim(X)-dim(V) odd, or odd cohomology in a fiber of a proper toric map with simplicial source
---

# B078 — Parity in the toric decomposition theorem

**Status:** PROVED (primary-source import)  
**Primary source:** S048

Let (f:X\to Y) be a proper toric fibration. De Cataldo, Migliorini, and
Mustaţă prove

\[
 Rf_*IC_X\simeq
 \bigoplus_{\tau\in\Delta_Y}\bigoplus_{b\in\mathbf Z}
 IC_{V(\tau)}[-b]^{\oplus s_{\tau,b}},
\]

with

\[
 s_{\tau,b}=0
 \quad\text{if}\quad
 b+\dim X-\dim V(\tau)\ \text{is odd}.
\]

Theorem 5.1 also gives (s_{\tau,b}=s_{\tau,-b}), and projectivity gives
the relative-hard-Lefschetz inequalities. Proposition 5.4 proves the fiber
intersection-cohomology parity from which the support parity follows.

For a general proper toric map, Remark 5.2 factors the map as a toric
fibration followed by a finite toric morphism. The same shifts and
multiplicities occur, but a finite local system can replace the constant
coefficient on the image orbit.

## Ordinary-degree normalization

If (X) and (Y) are smooth (more generally simplicial), then
(IC_X=\mathbf Q_X[\dim X]) and
(IC_V=\mathbf Q_V[\dim V]). Undoing the source normalization shows that a
summand indexed by ((V,b)) has its generic ordinary stalk in degree

\[
 q=\dim X-\dim V+b.
\]

The theorem therefore says exactly that (q) is even. Theorem 4.1 gives the
compatible fiber statement: if the source is simplicial, every fiber has
pure Hodge-Tate rational cohomology, hence no odd cohomology.

## Exact boundary

This is a theorem about globally toric maps and their constant/intersection-
complex input. It does not turn an arbitrary proper toroidal or semistable
family into a global toric map, compute coefficient local systems coming
from non-toric fibers, or identify the perverse degree occupied by the B058
tube specialization. Those are separated in NG055 and G044.
