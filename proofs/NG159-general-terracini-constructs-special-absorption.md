---
brick_id: NG159
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold in its lower H^k embeddings and a special class-directed finite point scheme Z
smoothness: the embedded variety and marked points are smooth; isolated ODPs at the birth degree remain an independent requirement
projectivity: the embeddings, secant varieties, point spans, tangent spaces, and contact loci are projective
dimension: dim X=2n; arbitrary N; generic secant results concern general points, while G127 requires one special point scheme simultaneously across many embeddings
codimension: Terracini identifies the tangent to a secant variety with the span of tangent spaces at general points; it does not force each tangent space into the span of the points themselves
coefficient_field: C, matching S073; Q detector data are absent from the secant theorem
cohomology_theory: secant varieties, embedded tangent spaces, tangential contact loci, and coherent first jets
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: generic
dependencies: B194-B196, G125-G127, S073
claim: Apply Terracini's lemma or generic contact-locus theory directly to construct G127's special simultaneous tangent-span absorption and its rational detector.
falsifier: S073 Theorem 3.1 assumes general points and identifies the tangent to the secant variety with the span of their tangent spaces, whereas G127 fixes special points and requires the point span to contain those tangent spaces in every lower embedding
---

# NG159 — Generic Terracini theory does not construct the special absorbing span

- **Route:** invoke Terracini's lemma, tangential defect, or generic contact-
  locus classifications to assert the existence of G127's lower absorbing
  spans.
- **Valid input:** S073 Theorem 3.1 states, for general points
  \(p_0,\ldots,p_k\) and a general point of their span,
  \[
  T_{S^k(X),x}=\langle T_{X,p_0},\ldots,T_{X,p_k}\rangle. \tag{1}
  \]
  S073 Definition 3.4 then studies the locus of points whose tangent spaces
  lie in this **tangent-space span**.
- **Invalid inference:** equation (1) forces
  \[
  T_{X,p_i}\subset\langle p_0,\ldots,p_k\rangle, \tag{2}
  \]
  or produces points satisfying (2).

The containments run in different ambient spaces: Terracini builds the span
of tangent spaces from general points; B196/G127 require the much smaller
point span itself to absorb every tangent. Moreover G127's \(Z\) is highly
special, class-directed, and fixed simultaneously in all embeddings
\(H^k\), while S073's theorem and contact loci use general points in one
fixed embedding.

- **Precise obstruction:** neither generality, containment direction, nor
  polarization scope matches. S073 contains no ODP construction, doubled-
  scheme birth, Hessian holonomy, rational Hodge type, or specified pairing.
- **Re-entry condition:** prove a theorem for the actual special incidence
  locus of point spans satisfying (2) in every lower embedding, then verify
  the degree-m primitive birth and detector separately.
