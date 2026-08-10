---
brick_id: B031
status: PROVED
base_field: C
variety: X = P^4, a general degree-d hypersurface Y containing a plane, and a nearby smooth degree-d hypersurface Y_infinity
smoothness: X and Y_infinity are smooth; for d at least 3, a general Y containing the plane has exactly (d-1)^2 ordinary double points
projectivity: X, Y, and Y_infinity are projective
dimension: dim_C X = 4 and dim_C Y = dim_C Y_infinity = 3
codimension: Y has codimension 1 in X; the contained plane has middle codimension 2 in X
coefficient_field: Q for homology and vanishing-cycle relations; C for the node-evaluation calculation
cohomology_theory: singular homology and cohomology, limit mixed Hodge structures, vanishing cycles, and coherent node-defect cohomology
hodge_type: nodal rational relations have type (0,0) after Tate twist, but their primitive ambient image is zero in this family
cycle_class_map: CH^2(P^4)_Q -> H^4(P^4,Q(2)); the primitive target is zero
cycle_equivalence: rational equivalence
scope: generic
dependencies: B010, B030 for the d=5 split witness, Kloosterman Proposition 3.3 and Proposition 3.7 (S032), and Saito Proposition 1 and Theorem 1 (S022)
claim: In arbitrarily high degree, a nodal hypersurface can have a one-dimensional relation and extra-homology space while the canonical map to primitive ambient homology is zero; hence positive adjoint defect does not imply a nonzero primitive detector.
falsifier: failure of the plane-containing general member to be nodal with defect one, nonzero primitive middle homology of P^4, or injectivity of a map from its nonzero extra homology into the zero primitive target
---

# B031 - The extra-to-primitive map can have a kernel

Fix \(d\ge3\). Let \(P\simeq\mathbf P^2\subset\mathbf P^4=X\), and take a
general degree-\(d\) hypersurface

\[
 Y=V(\ell_1f_1+\ell_2f_2)
\]

containing \(P=V(\ell_1,\ell_2)\). Kloosterman records that the general
member is nodal. Its nodes on \(P\) form the reduced complete intersection

\[
 \Delta=V_P(f_1|_P,f_2|_P)
\]

of type \((d-1,d-1)\), so \(|\Delta|=(d-1)^2\).

## Defect and extra homology

For a degree-\(d\) hypersurface in \(\mathbf P^4\), Kloosterman
Proposition 3.7 computes the topological defect from evaluation on the nodes
in degree \(2d-5\). The Koszul resolution on \(P\), twisted by \(2d-5\), is

\[
 0\longrightarrow\mathcal O_P(-3)
 \longrightarrow\mathcal O_P(d-4)^{\oplus2}
 \longrightarrow I_{\Delta/P}(2d-5)\longrightarrow0.
\]

Since \(H^1(\mathbf P^2,\mathcal O(k))=0\) for every \(k\) and
\(H^2(\mathbf P^2,\mathcal O(d-4))=0\) for \(d\ge3\),

\[
 h^1(P,I_{\Delta/P}(2d-5))
 =h^2(P,\mathcal O_P(-3))=1.
\]

The exact Hilbert-function identity underlying this calculation is reproduced
for \(3\le d\le200\) by the B031 plane-family verification script. The
script is a finite arithmetic check, not a substitute for the cohomological
proof.

The Koszul resolution of the plane ideal in \(\mathbf P^4\) has no
intermediate cohomology after this positive twist. The sequence
\(0\to I_P(2d-5)\to I_\Delta(2d-5)\to
I_{\Delta/P}(2d-5)\to0\) therefore gives the same \(H^1\) in
\(\mathbf P^4\).

Thus Kloosterman's defect
\(\delta(Y)=h^4(Y)-h^2(Y)\) equals one. Proposition 3.3 gives
\(h^2(Y)=1\), so \(h^4(Y)=2\). A nearby smooth hypersurface has
\(h^4(Y_\infty)=1\). For an ordinary-double-point smoothing, the next local
vanishing group is zero, so the specialization map in Saito's sequence is
surjective in cohomology and injective after dualizing. Hence

\[
 \dim E^\vee(Y)
 =\dim\operatorname{coker}\!\left(
 H_4(Y_\infty,\mathbf Q(2))\to H_4(Y,\mathbf Q(2))\right)=1.
\]

Saito's canonical isomorphism identifies \(E^\vee(Y)^{(0,0)}\) with the
one-dimensional rational relation space among the nodal vanishing cycles.

For \(d=5\), B030 gives the more structured instance in which the sixteen
nodes split into two eight-point subsets independently imposing conditions
on \(\mathcal O_{\mathbf P^4}(5)\).

## The canonical ambient map is zero

For every \(d\),

\[
 H_4(\mathbf P^4,\mathbf Q(2))_{\mathrm{prim}}=0.
\]

Therefore Saito's canonical map

\[
 \Phi_Y:E^\vee(Y)\longrightarrow
 H_4(\mathbf P^4,\mathbf Q(2))_{\mathrm{prim}}
\]

is the zero map from a one-dimensional source. Every relation \(\beta\) in
this family has \(\gamma_\beta=0\).

Because \(d\) is arbitrary, increasing the hypersurface degree does not
restore injectivity.

## Consequence and source conflict

The following conditions do not imply a nonzero primitive ambient detector:

1. isolated nodality;
2. positive adjoint evaluation defect;
3. a nonzero rational vanishing-cycle relation;
4. nonzero extra homology.

A separate vector-level condition \(\operatorname{rank}\Phi_Y>0\) is
indispensable, followed by the stronger class-specific requirement
\(\operatorname{im}\Phi_Y\not\subseteq\zeta^\perp\).

Green–Griffiths Section 4.2.4 explicitly defines its printed
\(\rho(ii)\) as the dimension of the primitive ambient image and then prints
\(\rho(i)=\rho(ii)\). Under the literal reading, this family has
\(\rho(i)=1\) and \(\rho(ii)=0\) for arbitrarily large \(d\). The repository
therefore quarantines that component of the printed six-invariant equality
as NG-028. No undocumented reinterpretation of \(\rho(ii)\) is used.

## Scope guard

This is a counterexample to an intermediate implication and to the literal
printed equality just identified, not a counterexample to the rational
Hodge Conjecture. The ambient primitive target is zero, so the family
contains no nonzero primitive Hodge class to disprove.
