---
brick_id: G008
status: EXPLORATORY
base_field: C
variety: arbitrary polarized smooth projective X of dimension 2n, its universal high-power hyperplane family, and a specified nonzero primitive rational Hodge class
smoothness: X is smooth; fibers over the smooth locus are smooth and a sought detecting fiber is singular
projectivity: X is projective and L is ample, with the family embedded by mL for m sufficiently large
dimension: dim X = 2n; hyperplane fibers have dimension 2n-1; a generic two-parameter net is used only after support nonemptiness is proved
codimension: middle codimension n on X; the sought local support lies in parameter-space codimension at least 2
coefficient_field: Q
cohomology_theory: singular Betti and intersection cohomology, perverse sheaves, decomposition theorem, variation of Hodge structure, monodromy, and vanishing cycles
hodge_type: primitive (n,n) input; local Green-Griffiths invariant and Saito relation of type (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007, B010-B012, B014-B015, B127-B130, G084-G087, NG102-NG104, and the attempted mechanisms B011 and B013
claim: For every nonzero primitive rational Hodge class zeta, there is a sufficiently high embedding for which the associated local Green-Griffiths invariant is nonzero at some discriminant point, equivalently Sing(zeta) is nonempty for that embedding.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class whose local Green-Griffiths invariant vanishes at every parameter point for every sufficiently high power
---

# G008 - Codimension-two support realization

**Status:** EXPLORATORY — active terminal-equivalent gate

## Falsifiable theorem sought

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L\) be
ample, and let

\[
 0\ne\zeta\in H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}.
\]

For some sufficiently high embedding by \(|mL|\), prove

\[
 s(\zeta)\ne0
 \quad\Longrightarrow\quad
 \operatorname{Sing}(\zeta)=\{p:s(\zeta)_p\ne0\}\ne\varnothing.
\]

The premise is already a theorem for every \(\zeta\ne0\) by B012. The
conclusion is equivalent, again by B012, to finding a singular hyperplane
\(X_p\) with \(\zeta|_{X_p}\ne0\). Hence B007 propagates the universal theorem
to the standard rational Hodge Conjecture. G008 is therefore an exact
terminal gate, not partial algebraicity progress.

B127/NG102 restore this as the active minimum after auditing the stronger
clean-nodal program: G084 equals G008 plus the independent conditional
cleanup G085.

## Attempt 1 - Restrict the global class to a generic pencil

This fails on support dimension. B012 proves that every possible local
singularity lies in parameter-space codimension at least two. A generic
complex curve avoids such a locus. If a point of the locus were already
known, one could choose a curve through it, but that choice assumes the
desired conclusion.

## Attempt 2 - Pass to a generic net

A generic projective plane can meet a nonempty codimension-two component, so
a net is the first generic slice capable of seeing such support. It does not
prove nonemptiness: the global intersection-cohomology class \(s(\zeta)\) may
be nonzero while every associated local class \(s(\zeta)_p\) is zero
unless a new global-to-local support theorem is supplied. Merely increasing
the parameter dimension therefore does not close the implication. B014
proves with an elliptic-curve intersection complex that no theorem of this
form follows from abstract perversity and hypercohomology alone.

## Attempt 3 - Use the boundary of a tube filling

B013 turns a Picard-Lefschetz factorization of a Schnell loop into an exact
distributed relation. The separate meridians meet smooth discriminant
points, while B008 says that every such point has zero rational local
intersection-cohomology channel. Colliding them into a codimension-two
stratum would require a geometric incidence theorem plus a specialization
argument preserving the nonzero pairing and Hodge type. Neither B011 nor
B013 provides it. B015 supplies the normal-crossing and partial-smoothing
geometry after an independent-node hyperplane is already chosen, but does not
construct that hyperplane from \(\zeta\) or the tube.

## Attempt 4 - Force localization from the formal Hodge package

B128 computes the exact two-row hypercohomology edge sequence. The global
class has empty local support precisely when it lies in

\[
 H^1(P_m,\mathcal H^{-d_m}K_m)\subset IH^1(P_m,K_m).
\]

It is tempting to exclude this escape row using the projective-space base,
full strict support, geometric origin, polarizability, purity, hard Lefschetz,
and the rational type-\((0,0)\) of \(s_m(\zeta)\). B129/NG103 disprove that
formal implication on every \(\mathbf P^d\): a geometric weight-\(-1\)
full-support IC can carry a nonzero rational \((0,0)\) class entirely in the
escape row while its local target sheaf vanishes everywhere.

The surviving input must therefore be the exact universal-incidence origin
\(s_m(\zeta)=[q_m^*\zeta]_{00}\). G086 records the resulting edge-survival
obligation. It is an operational form of G008, not a smaller terminal gate.

## Attempt 5 - Apply Nori connectivity to the universal incidence

B130 specializes Nori's theorem and Brogan's filtered \(D\)-module formula
to the exact middle Hodge component. It produces

\[
H^{r,r}_{\rm prim}(X)\otimes\mathcal O_P
\simeq
\mathcal H^{-d+1}\operatorname{gr}^{F}_{-r}\operatorname{DR}(M).
\]

NG104 closes the direct inference to local support. On the smooth locus,
\(\operatorname{DR}(M)\simeq V_{\mathbf C}[d]\), so its ordinary
degree-(-d+1\) cohomology sheaf is zero: filtered differentials cancel the
nonzero Higgs class. Brogan also explicitly leaves the comparison between
the Leray-incidence map and the abstract Corollary 4.1 map unchecked. G087
therefore requires both canonical map identification and failure of that
cancellation at a discriminant stalk.

## Smallest concrete obligation

Construct, directly from \((X,L,\zeta)\) and without an algebraic
representative of \(\zeta\), a codimension-two discriminant stratum \(Z\) and
a point \(p\in Z\) for which the associated local class is nonzero:

\[
 s(\zeta)_p\ne0.
\]

After that point is obtained, a transverse curve through \(p\), B010, and
Saito's vanishing-cycle exact sequence reduce the remaining work to a local
type-\((0,0)\) relation. The unsupported step is precisely the production of
the point \(p\); a generic slice or a global tube cannot substitute for it.

Equivalently by B128, prove that the incidence class avoids the bottom-row
escape space for some high power. This is G086.

## Re-entry condition

Prove a support theorem that forces a primitive rational Hodge class with
nonzero \(s(\zeta)\in IH^1(\mathbf P^d,IC(R^{2n-1}))\) to have nonzero
associated local invariant \(s(\zeta)_p\) somewhere, or construct an
equivalent Hodge-adapted net and verify the local stalk nonvanishing. The
theorem must use no algebraic representative of \(\zeta\).
