---
brick_id: B081
status: PROVED
base_field: C
variety: a proper map from a smooth finite-stabilizer Deligne-Mumford stack to the plane-net base, including the B071 pushdown
smoothness: source stack smooth/regular; target base smooth of dimension two
projectivity: morphism proper/projective
dimension: total space 2n+1, base 2, and fiber 2n-1
codimension: full, divisor, and point supports on the base; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, perverse truncation, perverse spectral sequence, decomposition theorem, and strict-support decomposition
hodge_type: all canonical filtrations and strict-support summands are Hodge subquotients; no class-specific type is inferred
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B077, B080, S037, S047
claim: The derived decomposition into shifted perverse cohomology objects is noncanonical, whereas the perverse filtration and strict-support decomposition inside each perverse cohomology object are canonical; in total degree -1 the complete positions are full-support constant E2^(-2,1), relation/divisor E2^(-1,0), and point E2^(0,-1).
falsifier: a canonical derived splitting supplied by the cited theorems, a noncanonical perverse filtration, or a different E2 position for either B080 support shift
---

# B081 — Canonical perverse grade before strict-support projection

**Status:** PROVED

Let

\[
 K=f_*\mathbf Q_{\mathcal Y}[2n+1]
\]

for the B071 proper pushdown. Purity gives an isomorphism

\[
 K\simeq\bigoplus_s {}^pH^s(K)[-s],
\]

but this isomorphism is not canonical. De Cataldo–Migliorini Remarks 1.4.2
and 1.6.2 explicitly warn that decomposition-theorem splittings are not
uniquely determined.

Two structures are canonical:

1. the perverse truncations and their induced perverse filtration;
2. the unique strict-support decomposition of each semisimple pure perverse
   Hodge module ${}^pH^s(K)$.

Consequently there is no canonical total-object morphism
$K\to K_{\mathrm{fs}}$ obtained merely by choosing a decomposition-theorem
splitting. A class must first be passed to a canonical associated-graded
piece of the perverse filtration; only there may one use strict support.
We name the relevant grade by its spectral-sequence position, avoiding any
choice between increasing and decreasing filtration-index conventions.

## The two detector positions

At a collision point $p$, the perverse spectral sequence is

\[
 E_2^{r,s}=H^r\!\left(i_p^*{}^pH^s(K)\right)
 \Longrightarrow H^{r+s}(i_p^*K).
\]

The detector has total degree $-1$. B080/B121 give:

- the full-base $b=1$ term lies in ${}^pH^1(K)$ and contributes at
  $E_2^{-2,1}$; this is the constant ambient $R^{d+1}$ grade;
- a full-support or divisor-support term with $b=0$ lies in
  ${}^pH^0(K)$ and contributes at $E_2^{-1,0}$;
- a point-support term with $b=-1$ lies in
  ${}^pH^{-1}(K)$ and contributes at $E_2^{0,-1}$.

The decomposition theorem makes this spectral sequence degenerate, but it
does not canonically split the resulting filtration on
$H^{-1}(i_p^*K)$. Therefore the point term is a different canonical
perverse grade, not a coordinate that can be subtracted from a total class
using an arbitrary derived splitting.

Inside $E_2^{-1,0}$, the strict-support decomposition of
${}^pH^0(K)$ canonically separates the full-support and divisor-support
parts. This is the invariant class test used in G046.

## Erratum and boundary

The first version of B081 listed only the latter two positions and silently
omitted $E_\infty^{-2,1}$. B121 gives the exact correction and proves that
the omitted term is generally nonzero. B081 does not prove that the B058
class lies in B107's relation filtration step, has a nonzero
$E_\infty^{-1,0}$ grade, or has a nonzero full-support component inside that
grade.
