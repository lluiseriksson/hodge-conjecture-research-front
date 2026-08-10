---
brick_id: B024
status: PROVED
base_field: C
variety: a smooth projective complete intersection X with a generic Lefschetz hyperplane pencil and blowup Y along its smooth base locus
smoothness: X, the pencil base locus, and the reference hyperplane section are smooth; the pencil has only Lefschetz critical points
projectivity: X and Y are projective
dimension: dim_C X = 2n for the Hodge application; the cited exact sequence holds in every dimension
codimension: middle codimension n on X
coefficient_field: Q
cohomology_theory: singular and relative Betti homology, primitive homology, Lefschetz thimbles, vanishing-cycle boundary maps, and Poincare duality
hodge_type: the input may be any nonzero primitive class; for the Hodge application it is rational type (n,n), or type (0,0) after Tate twist; the thimble lift has no asserted Hodge type
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B022, Lairez-Pichon-Pharabod-Vanhove equation (19) (S029), and nondegeneracy of the primitive Poincare pairing
claim: For a smooth projective complete intersection of even dimension, every nonzero primitive rational middle cohomology class pairs nontrivially with the ambient image of some class in the quotiented thimble group T(Y); this detector is global and topological, not a local Saito relation or algebraic cycle.
falsifier: a nonzero primitive rational middle cohomology class annihilating the image of every class in T(Y) despite the surjection T(Y)->PH_{2n}(X,Q)
---

# B024 - Complete-intersection thimble detection

For a smooth projective complete intersection \(X\), equation (19) of
Lairez, Pichon-Pharabod, and Vanhove specializes B022 to

\[
 0\longrightarrow K\longrightarrow\mathcal T(Y)
 \overset{q}{\longrightarrow}PH_{2n}(X,\mathbf Q)
 \longrightarrow0.
\]

Let

\[
 0\ne\zeta\in H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n)).
\]

The primitive Poincare pairing is nondegenerate, so there is
\(c\in PH_{2n}(X,\mathbf Q)\) with
\(\langle\zeta,c\rangle\ne0\). Surjectivity of \(q\) gives
\(t\in\mathcal T(Y)\) with \(q(t)=c\). Therefore

\[
 \langle\zeta,q(t)\rangle\ne0.
\]

By B022, \(t\) is represented by a linear combination of Lefschetz
thimbles whose vanishing-cycle boundary is zero, modulo equator extensions;
its image is nonzero modulo the base-locus kernel because it pairs
nontrivially with \(\zeta\).

## Exact gain

For complete intersections, the global quotient-level detector required by
the thimble route always exists for every nonzero primitive class. This is an
explicit counterpart of the more general global tube surjectivity in B011.
It proves that, in this special geometric setting, neither the
equator-extension quotient nor the base-locus quotient blocks **all**
detectors.

## Scope guard

The class \(t\) is a global topological thimble combination. The argument
does not:

- concentrate it at one singular fiber;
- identify it with a Saito relation class \(\gamma_\beta\);
- prove rational type \((0,0)\) for a local relation; or
- put \(q(t)\) in the image of the algebraic cycle-class map.

Consequently B024 is not a Hodge theorem even for complete intersections,
and a fortiori is not progress for arbitrary smooth projective varieties.

