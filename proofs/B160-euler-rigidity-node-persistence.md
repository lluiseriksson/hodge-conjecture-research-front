---
brick_id: B160
status: PROVED
base_field: C
variety: a proper analytic family of projective hypersurfaces of complex dimension r in a fixed linear system, with N disjoint tracked ordinary-double-point charts and no other singularities
smoothness: the ambient variety is smooth; every tracked critical point has nondegenerate Hessian; a nearby reference hypersurface is smooth
projectivity: the hypersurfaces are projective and lie in one complete linear system; the proof uses properness and local Milnor balls
dimension: hypersurface dimension r, equal to 2n-1 in the rational Hodge application; N tracked critical-point charts
codimension: a basis-node germ has codimension R; Euler rigidity forces all N-R extra node branches to contain it
coefficient_field: Z for Euler characteristics and Milnor numbers; C for analytic deformations; Q only downstream
cohomology_theory: singular cohomology with compact finite CW type, Milnor fibers, Ehresmann fibration outside Milnor balls, and analytic critical-value deformation theory
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B025, B157-B159, S030, Milnor-ball excision, and Ehresmann's theorem
claim: In a sufficiently small proper hypersurface family whose only possible singularities are the unique Morse critical points in N disjoint tracked charts, the Euler–Milnor formula is chi(Y_t)=chi(Y_sm)-(-1)^r times the number of nodal fibers among those charts. Consequently, on any connected basis-node germ through a central N-node member, local constancy of chi(Y_t) is equivalent to persistence of all N nodes and therefore implies B158's all-order factorization.
falsifier: an incorrect Euler–Milnor sign, a fiber with the same Euler characteristic but fewer tracked nodes under the no-other-singularity hypotheses, or an inference without properness, isolated Milnor balls, or control of all singularities
---

# B160 — Euler rigidity forces every tracked node to persist

Let \(\mathcal Y\to(T,0)\) be a proper analytic family of projective
hypersurfaces of complex dimension \(r\). Assume, after shrinking \(T\),
that:

1. the central fiber \(Y_0\) has exactly \(N\) ordinary double points;
2. there are disjoint Milnor balls \(U_1,\ldots,U_N\), each carrying one
   analytic critical-point section with nondegenerate spatial Hessian;
3. no fiber has a singularity outside the \(U_i\);
4. inside each \(U_i\), a fiber is singular exactly when its tracked
   critical value \(\tau_i\) is zero.

Let \(Y_{\mathrm{sm}}\) be a smooth member obtained by simultaneously
smoothing the tracked critical values.

## Euler–Milnor formula

For any \(t\), remove the interiors of the Milnor balls. Ehresmann's
theorem identifies the complements in \(Y_t\) and \(Y_{\mathrm{sm}}\).
Inside a ball containing an isolated hypersurface singularity of Milnor
number \(\mu\), the singular piece is contractible and has Euler
characteristic \(1\). S030 gives the Milnor fiber the homotopy type of a
bouquet of \(\mu\) spheres of real dimension \(r\), hence

\[
 \chi(F_{\mathrm{Milnor}})=1+(-1)^r\mu.
\]

Additivity of Euler characteristic under the common boundary gluing gives

\[
 \chi(Y_t)=
 \chi(Y_{\mathrm{sm}})
 -(-1)^r\sum_{p\in\operatorname{Sing}Y_t}\mu_p. \tag{1}
\]

Every tracked singularity is an ordinary double point, so \(\mu_p=1\). If
\(\nu(t)\) is the number of zero critical values, equation (1) becomes

\[
 \chi(Y_t)=\chi(Y_{\mathrm{sm}})-(-1)^r\nu(t). \tag{2}
\]

For the Hodge-conjecture hyperplane sections, \(r=2n-1\) is odd and
\(\chi(Y_t)=\chi(Y_{\mathrm{sm}})+\nu(t)\).

## Equivalence with basis-node persistence

Let \(F_B\subset T\) be a connected basis-node germ through \(0\). At the
central point, \(\nu(0)=N\). Since there are exactly \(N\) tracked charts
and each contains at most one singular point, \(\nu(t)\le N\).

If \(\chi(Y_t)\) is locally constant on \(F_B\), equation (2) forces
\(\nu(t)=N\) for every \(t\in F_B\). Hence every \(\tau_i\) vanishes on
\(F_B\): all extra nodes persist. Conversely, if all nodes persist then
\(\nu(t)=N\) and equation (2) makes \(\chi\) constant.

Thus, under the stated exhaustive-singularity hypotheses,

\[
 \chi(Y_t)\text{ constant on }F_B
 \quad\Longleftrightarrow\quad
 F_B\subseteq\{\tau_i=0\}\text{ for all }i. \tag{3}
\]

B158 turns (3) into \(H_\tau=0\), analytic syzygy lifting, and the
rank-\(R\) factorization. Euler rigidity is therefore a genuine global
all-order certificate, not a finite-jet test.

## Scope guard

Equation (3) fails as a persistence criterion if singularities may enter
or leave the tracked balls in compensating pairs, if worse singularities
with other Milnor numbers occur, or if the family is not proper enough for
the complement comparison. G102 must verify these hypotheses for the actual
full-linear-system germ.
