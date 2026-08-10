---
brick_id: G005
status: EXPLORATORY
base_field: C
variety: arbitrary polarized smooth projective X with a specified primitive middle Hodge class
smoothness: X smooth; the detecting hyperplane fiber is necessarily singular and may be resolved
projectivity: X projective and L very ample
dimension: even dimension 2n
codimension: middle codimension n
coefficient_field: Q, or a non-torsion integral multiple
cohomology_theory: singular Betti cohomology H^{2n}(-,Q(n)) and the local intersection-cohomology singularity of an admissible normal function
hodge_type: primitive (n,n), equivalently (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007; BFNP Proposition 5.11 and Corollary 5.15 (S009)
claim: Every nonzero primitive rational middle Hodge class is detected by restriction to some sufficiently high-degree singular hyperplane section.
falsifier: a smooth projective even-dimensional X, polarization L, and nonzero primitive rational Hodge class whose restriction vanishes on every member of every |L^m|
---

# G005 - Singular-hyperplane detection gate

## Falsifiable theorem sought

For every smooth projective \(X/\mathbf C\) of dimension \(2n\), every very
ample \(L\), and every nonzero primitive

\[
 \zeta\in H^{2n}(X,\mathbf Q(n))\cap H^{0,0},
\]

there are \(m>0\) and a necessarily singular divisor
\(D=X_{m,p}\in|L^m|\) such that

\[
 \zeta|_D\ne0\quad\text{in }H^{2n}(D,\mathbf Q(n)).
\]

By B007 this theorem is equivalent to the standard rational Hodge
Conjecture. It is now the active terminal-equivalent gate. Unlike G001/G004,
it does not assume an algebraic anchor.

## Attempt: high degree plus monodromy

1. For \(m\gg0\), BFNP Proposition 5.11 proves that Lefschetz pencils in
   \(|L^m|\) have nontrivial vanishing cycles.
2. The discriminant therefore contains genuine singular fibers, and global
   monodromy relates the vanishing cycles.
3. To finish, one would need a point \(p\) for which the *specified* class
   \(\zeta\) has nonzero local restriction.

Step 3 does not follow from steps 1-2. Corollary 5.15 says precisely
\(\sigma_p=\zeta|_{X_{m,p}}\); it computes a singularity if present but does
not force one. Any universal argument forcing step 3 already proves HC by
B007. This attempt is therefore closed as NG-008.

## Nodal refinement and its obstruction

Thomas proves a stronger equivalent formulation: one may ask for a divisor
with only ordinary double points whose middle homology carries the Poincare
dual of \(\zeta\). His constructive direction first assumes \(\zeta\) is
algebraic, chooses a smooth cycle \(Z\), and places \(Z\) in a nodal
hypersurface. Reusing that construction without \(Z\) would assume the desired
conclusion.

Thomas also tests deformation of such nodal divisors. If their nodes are
\(p_i\), the obstruction lies in \(H^1(I_{\{p_i\}}(NH))\); for a divisor
constructed around \(Z\), a Koszul resolution gives an injection

\[
 H^1(N_{Z/X})\hookrightarrow H^1(I_{\{p_i\}}(NH)).
\]

Increasing \(N\) therefore does not erase the embedded-cycle deformation
obstruction. This supplies a precise geometric reason that “take degree very
large and deform the nodes” is not a proof of G005.

## Next justified subgate

By B008, a smooth point of the discriminant has zero rational local
intersection-cohomology target and is excluded. By B009, a transverse nodal
stratum has a concrete target: the rational relation space among its
vanishing cycles. The next subgate is therefore G006.

Construct, directly from the rational Hodge tensor \(\zeta\) and the polarized
variation over \(|L^m|\setminus X^\vee\), a nodal discriminant point \(p\), a
nonzero relation among its vanishing cycles, and a corresponding new middle
cycle on which \(\zeta\) pairs nontrivially. Equivalently, produce a provably
nonzero class in

\[
 IH^1_p\bigl(R^{2n-1}\pi_{m,*}\mathbf Q(n)\bigr),
\]

without using an algebraic representative of \(\zeta\). A candidate must give
a class-specific nonvanishing theorem; ambient monodromy size or positive
nodal defect is insufficient.
