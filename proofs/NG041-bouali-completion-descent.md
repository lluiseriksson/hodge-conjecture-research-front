---
brick_id: NG041
status: NO-GO
base_field: C for the terminal Hodge claim; finitely generated characteristic-zero fields and p-adic completions in the claimed Tate reduction
variety: arbitrary smooth projective complex varieties, reduced in the cited argument to hypersurfaces and normal-crossing degeneration components
smoothness: the terminal variety and the selected resolution component are smooth; the degeneration has a normal-crossing special fiber
projectivity: all terminal varieties, hypersurfaces, and degeneration components are projective
dimension: arbitrary
codimension: arbitrary
coefficient_field: Q for Hodge classes and Qp for the intermediate Tate classes
cohomology_theory: Betti and de Rham cohomology, p-adic etale cohomology, crystalline comparison, and nearby cycles
hodge_type: rational (p,p), equivalently type (0,0) after Q(p)
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p)), with the cited intermediate map Z^p(X)_Qp -> H^(2p)_et(X_kbar,Qp(p))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B060 and primary-source audit S040
claim: The Bouali 2023-2024 preprint chain cannot be accepted as an unconditional proof of the rational Hodge Conjecture because its decisive Tate theorem descends a completion-valued cycle by an undefined finite Galois average.
falsifier: a missing argument in the cited versions proving that the constructed cycle over the p-adic completion is defined over a finite algebraic extension of k and that its average has the asserted class
---

# NG041 - Completion-to-algebraic descent gap in a claimed proof

## Route audited

Bouali's *Degeneration of families of projective hypersurfaces and Hodge
conjecture* (arXiv:2401.03465v13) claims the general Hodge Conjecture by
combining a degeneration with two earlier preprints. On pp. 14-15 it invokes
Theorem 4 of *De Rham logarithmic classes and Tate conjecture*
(arXiv:2303.09932v16) to turn Galois-stable Hodge-locus data into algebraic
cycles.

Theorem 4 depends on Corollary 2(ii), which depends on the claimed universal
Tate Theorem 3. In the proof of Theorem 3(i), pp. 34-35, the argument first
constructs

\[
 Z\in Z^d(X_{\widehat{k}_{\sigma_p}})\otimes\mathbf Q_p.
\]

It then writes \(\alpha=[Z]\) in cohomology over \(\bar k\) and defines an
average of \(gZ\) over \(G_k/G_Z\) to obtain a cycle on \(X/k\).

## Precise failure

No descent of \(Z\) from the completion
\(\widehat{k}_{\sigma_p}\) to \(\bar k\), much less to a finite extension of
\(k\), is proved. Therefore \(G_k\) has no stated action on \(Z\), the
stabilizer \(G_Z\) and finite orbit are unavailable, and the displayed
average is undefined. B060 gives an elementary exact type counterexample to
this inference using a transcendental \(\mathbf Q_p\)-point of
\(\mathbf P^1\).

Invariance of \([Z]\) cannot repair the step: cycle-class maps are not known
to be injective, and invariant cohomology does not control the field of
definition of a chosen cycle representative.

## Consequence

The cited Theorem 3 is not established by the written proof. Consequently
Corollary 2(ii), Theorem 4, the hypersurface-to-general degeneration step,
and the claimed general Hodge theorem cannot be promoted in this repository.
This is a proof audit, not a disproof of any theorem statement and not a
counterexample to the Hodge or Tate conjectures.

## Re-entry condition

Provide a valid theorem that replaces the completion-valued representative
by a cycle defined over a finite algebraic extension of \(k\), with equality
of the required \(p\)-adic class, before taking a trace or Galois average.
That theorem must not assume the Tate conjecture or the desired algebraicity.
