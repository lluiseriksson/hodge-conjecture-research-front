---
brick_id: B120
status: PROVED
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X, a generic plane-net incidence family h:Y->B, a clean nodal collision point p, and one marked algebraic curve transverse to every local discriminant branch at p
smoothness: X, Y, and the transverse curve pullback Y_Delta smooth; the marked punctured disk has smooth hyperplane fibers; the special fiber has finitely many isolated ordinary double points
projectivity: X, Y, B, h, and the algebraic curve base change projective; the local disk is analytic inside that curve
dimension: dim_C X = 2n; hyperplane fibers d=2n-1; plane base dimension 2; marked disk dimension 1
codimension: middle cycle codimension n; p has plane-base codimension two and disk codimension one
coefficient_field: Q
cohomology_theory: rational proper direct image, normal-slice shift, nearby cycles on a disk, cyclic local monodromy, and local invariant cycles
hodge_type: no type condition on the total nearby class or special lift; B119 controls the relevant clean-nodal grade after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B080-B084, B089, B121-B122, S037
claim: To obtain the ordinary special-stalk lift required by G080, it is enough to realize the selected class on one marked original collision disk and prove invariance under that disk's cyclic monodromy; full invariance under the local fundamental group of the punctured plane neighborhood is unnecessary.
falsifier: a cyclic-invariant class in the original disk nearby group that local invariant cycles does not lift, or a failure of the disk special group H^0(i^*K_Delta) to identify with the required plane-normalized group H^(-1)(i^*K_B)
---

# B120 — One original collision disk suffices for the ordinary lift

**Status:** PROVED

Let

\[
 d=2n-1,
 \qquad
 K_B=Rh_*\mathbf Q_Y[d+2]
\]

for the original incidence family over the plane net \(B\). Choose an
algebraic curve through the collision point \(p\) with generic tangent, and
let

\[
 a:\Delta\hookrightarrow B
\]

be a sufficiently small analytic disk germ in that curve. Genericity makes
\(\Delta^*=\Delta\setminus\{p\}\) lie in the smooth-fiber locus. Choose its
direction transverse to every one of the finitely many smooth local
discriminant branches. At the critical point belonging to each nodal branch,
this transversality makes the hypersurface pullback \(Y_\Delta\) smooth; away
from those points smoothness follows from smooth base change. If
\(g:Y_\Delta\to\Delta\) is the proper base change, its perverse-normalized
direct image is

\[
 K_\Delta=Rg_*\mathbf Q_{Y_\Delta}[d+1]
          =a^*K_B[-1].
\]

The shift gives a canonical identification

\[
 H^0(i_p^*K_\Delta)
 \simeq
 H^{-1}(i_p^*K_B)
 \simeq
 H^{d+1}(Y_p,\mathbf Q).
\]

## Cyclic invariance produces the required plane-stalk class

Let

\[
 t_\Delta\in H^0(i_p^*\Psi K_\Delta)
\]

be rational and fixed by the monodromy \(M_\Delta\) of the punctured disk.
Applied to the proper map \(g\), the local invariant-cycle theorem B084
gives a rational class

\[
 \widetilde\beta\in H^0(i_p^*K_\Delta)
\]

mapping to \(t_\Delta\). Through the displayed shift, this is exactly a
rational

\[
 \beta\in H^{-1}(i_p^*K_B),
\]

the ordinary special lift required by G080. If \(t_\Delta\ne0\), then
\(\beta\ne0\). B122 strengthens this conclusion in the isolated-singularity
setting by proving that every class in this nearby degree lifts, without
first checking monodromy invariance.

Nothing in this argument requires \(t_\Delta\) to be fixed under every loop
in a punctured two-dimensional neighborhood of \(p\). The local invariant
cycle theorem is applied after proper base change to the chosen curve, whose
local fundamental group is cyclic.

## Scope guard

The disk must be transverse enough that \(Y_\Delta\) is smooth, so that
\(IC_{Y_\Delta}=\mathbf Q_{Y_\Delta}[d+1]\). It must also be a base change
of the original incidence family, not a
semistable alteration whose exceptional class is substituted for the
downstairs class. B120 does not construct \(t_\Delta\), prove it survives
the B022 quotients, or place a lift in B107's filtration step \(S_0\).
B090-B091 still
exclude obtaining the selected nonzero class from the pure positive nodal
boundary by Hurwitz relabelling alone. B121 corrects the earlier claim that
B117-B119 leave only one grade: the constant
\(E_\infty^{-2,1}\) term survives. Therefore B108's filtered-lift
obstruction remains mandatory.
