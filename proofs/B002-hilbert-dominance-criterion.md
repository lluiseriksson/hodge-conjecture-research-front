---
brick_id: B002
status: PROVED
base_field: C
variety: smooth projective family f:Y->T with relative Hilbert scheme
smoothness: T smooth and irreducible; Hilbert component smooth at the anchor point
projectivity: f projective; relative Hilbert scheme projective over T
dimension: arbitrary relative dimension, specialized to 2m for Hodge use
codimension: fixed m for the universal subscheme
coefficient_field: Q
cohomology_theory: relative singular Betti cohomology R^{2m}f_*Q
hodge_type: prescribed flat section fiberwise of type (m,m)
cycle_class_map: fiberwise CH^m(-)_Q -> H^{2m}(-,Q(m))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Jacobian smoothness criterion in characteristic zero; openness of smooth morphisms; properness of relative Hilbert schemes (S014); flat-family cycle-class rigidity
claim: A smooth anchor point with surjective Hilbert-to-base tangent map lies on a component that surjects onto the base and carries the prescribed fiberwise class.
falsifier: failure of smoothness/openness from the stated tangent hypotheses or a jump of the Betti class in the universal flat family
---

# B002 - Hilbert dominance criterion

## Statement

Let \(T\) be a smooth irreducible complex algebraic variety and
\(f:\mathcal Y\to T\) a smooth projective morphism. Fix a Hilbert polynomial
and let \(\pi:H=\operatorname{Hilb}(\mathcal Y/T)\to T\). Let \(h\in H\) lie
over \(t\), representing a codimension-\(m\) subscheme \(Z_t\subset Y_t\).
Assume:

1. \(H\) is smooth at \(h\);
2. the differential \(d\pi_h:T_hH\to T_tT\) is surjective; and
3. a flat section \(\alpha\) of \(R^{2m}f_*\mathbf Q(m)\) has
   \(\operatorname{cl}(Z_t)=\alpha_t\).

Then the irreducible component \(H_0\) through \(h\) maps surjectively to
\(T\). The universal subscheme over \(H_0\) has fiberwise Betti class
\(\pi^*\alpha\). Consequently every fiber \(Y_s\) has an algebraic cycle with
class \(\alpha_s\).

## Proof

Because source and target are smooth at \(h,t\) and \(d\pi_h\) is surjective,
the characteristic-zero Jacobian criterion makes \(\pi\) smooth at \(h\).
After shrinking around \(h\), a smooth morphism is open, so the image of the
unique local irreducible component through \(h\) contains a nonempty Zariski
open subset of \(T\). Its global closure \(H_0\) therefore dominates \(T\).

The relative Hilbert scheme is projective over \(T\); hence
\(\pi(H_0)\) is closed. Since it contains a nonempty open subset and \(T\) is
irreducible, \(\pi(H_0)=T\).

The universal subscheme is flat over \(H_0\). Its Betti cycle class is a flat
section of the pullback local system. On the connected complex space
\(H_0^{an}\), it agrees at \(h\) with the flat section \(\pi^*\alpha\), hence
agrees everywhere. For any \(s\in T\), choose a point of \(H_0\) above \(s\);
the corresponding fiber subscheme is an algebraic cycle of class \(\alpha_s\).
QED.

## Scope audit

- The theorem does not assert that hypotheses 1-3 hold for arbitrary Hodge
  classes. G003 records that open obligation.
- It supplies a surjective projective parameter base \(H_0\to T\), not
  automatically a generically finite base change.
- It begins with an anchor cycle; it cannot create the G001 anchor.
- Smoothness of \(H\) and tangent surjectivity are independent requirements;
  a Hodge-locus tangent calculation alone does not give either one.
