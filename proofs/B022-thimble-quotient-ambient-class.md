---
brick_id: B022
status: PROVED
base_field: C
variety: a smooth projective hypersurface X with a generic hyperplane pencil, its blowup pi:Y->X along the smooth base locus X', and a smooth reference hyperplane section X_b
smoothness: X, X', and X_b are smooth; the pencil is Lefschetz with isolated Morse critical points
projectivity: X and Y are projective
dimension: dim_C X = n; the middle group is H_n(X) and X_b has dimension n-1
codimension: middle codimension n/2 when n is even; the topological theorem is stated for every n
coefficient_field: Z in the cited exact sequences and Q after extension for the Hodge application
cohomology_theory: singular and relative homology, Lefschetz thimbles, vanishing cycles, long exact sequences, and primitive homology
hodge_type: no Hodge type is asserted; a rational type-(0,0) test is an additional obligation for the Hodge application
cycle_class_map: CH^{n/2}(X)_Q -> H^n(X,Q(n/2)) when n is even; no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Lairez-Pichon-Pharabod-Vanhove Section 2.1.4, Lemma 1, and Theorem 2 (S029)
claim: In the audited Lefschetz-pencil setting, thimbles freely generate the middle relative homology and boundary to the vanishing cycles, but an ambient middle class is obtained only after quotienting zero-boundary thimble combinations by equator extensions and then by the base-locus kernel under projection to X.
falsifier: a pencil satisfying the cited hypotheses for which the thimbles do not form the stated relative basis, boundary(Delta_i) differs from delta_i, or either exact sequence in Theorem 2 fails
---

# B022 - Thimble quotient before ambient class

Let \(X\) be a smooth projective hypersurface of complex dimension \(n\),
let \(f:Y\to\mathbf P^1\) be the blowup of a generic hyperplane pencil, and
let \(X_b\) be a smooth reference fiber. Choose a hemisphere \(D_+\)
containing all critical values and put \(Y_+=f^{-1}(D_+)\).

Lairez, Pichon-Pharabod, and Vanhove prove that

\[
 H_q(Y_+,X_b)=0\quad(q\ne n),
 \qquad
 H_n(Y_+,X_b)=\bigoplus_i\mathbf Z\Delta_i,
\]

where \(\Delta_i\) are the Lefschetz thimbles and

\[
 \partial\Delta_i=\delta_i
\]

for the corresponding vanishing cycles. Thus a coefficient vector
\((a_i)\) gives a relative chain with homologically zero boundary exactly
when \(\sum_i a_i\delta_i=0\).

That kernel is not yet the ambient homology. If \(\tau_\infty\) denotes
extension around the equator, the correct intermediate group is

\[
 \mathcal T(Y)=
 \frac{\ker(\partial:H_n(Y_+,X_b)\to H_{n-1}(X_b))}
      {\operatorname{im}(\tau_\infty:H_{n-1}(X_b)\to H_n(Y_+,X_b))}.
\]

Theorem 2 gives exact sequences

\[
 0\to\mathcal T(Y)\to
 \frac{H_n(Y)}{\iota_*H_n(X_b)}
 \to H_{n-2}(X_b)\to0
\]

and

\[
 0\to K\to\mathcal T(Y)\to
 \frac{H_n(X)}{\iota_*H_n(X_b)}\to0,
\]

where

\[
 K=\ker\bigl(H_{n-2}(X')\to H_{n-2}(X_b)\bigr)
\]

comes from the pencil base locus.

When \(X\) is a smooth projective complete intersection, the reference-fiber
image is precisely the nonprimitive linear-section summand. Equation (19) of
the cited paper therefore reads

\[
 0\to K\to\mathcal T(Y)\to PH_n(X)\to0.
\]

Thus \(\mathcal T(Y)\) surjects onto primitive middle homology, while its
kernel is still the base-locus contribution \(K\).

## Consequence for G007

There are two independent ways for a thimble relation to fail as an ambient
detector:

1. it can vanish already in \(\mathcal T(Y)\) because it is an equator
   extension;
2. its nonzero class in \(\mathcal T(Y)\) can lie in \(K\) and therefore
   project to zero in ambient middle homology.

Consequently, preserving a kernel vector or even a nonzero relative cycle
through collision is insufficient. A valid bridge must preserve its class
after both quotients and then verify rational type \((0,0)\) and nonzero
pairing with the specified Hodge class.

## Scope guard

The theorem is an exact topological reconstruction for generic pencils on
smooth projective hypersurfaces. It is not a cycle-construction theorem and
does not prove that a surviving ambient class is Hodge or algebraic. It is
used here as an auditable model of the data any proposed general
specialization must control.
