---
brick_id: G055
status: EXPLORATORY
base_field: C with all comparison data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, a B058 distributed detector, and a one-parameter marked collision to a clean nodal target
smoothness: ambient and marked reference fibers smooth; generic collision fiber lies in the Lefschetz locus; target has only ordinary double points
projectivity: ambient hyperplane family, plane net, and one-parameter collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational relative thimble complexes, nearby and vanishing cycles, local intersection cohomology, B022 quotients, perverse filtration, and Saito pairing
hodge_type: the correction must define a rational type-(0,0) local relation after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B052-B059, B081-B091, G048-G054, NG065-NG067
claim: Construct a rational chain-level nearby-to-special comparison for the specified B058 thimble word whose difference from every marked pure-Hurwitz comparison induces a nonzero type-(0,0) class in the target local relation channel, surviving both B022 quotients and retaining nonzero prescribed pairing.
falsifier: every rational comparison is chain-homotopic on the detector to a pure-Hurwitz map, or every resulting correction vanishes, has wrong Hodge type, dies in B022, or loses the prescribed pairing
---

# G055 — Construct the topology-changing specialization correction

**Status:** EXPLORATORY

Let $C_{\mathrm{dist}}$ denote the relative thimble/vanishing-cycle complex
carrying B058's distributed class $t$, and let $C_H$ denote the local
monodromy complex at the clean nodal target. The first concrete obligation is
to construct, from an algebraic one-parameter collision, a rational comparison

\[
 \operatorname{sp}_C:C_{\mathrm{dist}}\longrightarrow C_H
\]

compatible with the nearby-cycle triangle and the relative boundary maps.
After choosing the common B089 marking, compare it with the pure-Hurwitz
reference map $H_C$. B091 proves that $H_C$ sends the detector to zero in the
positive local-boundary realization. The required excess class is therefore

\[
 q_H=H^1(\operatorname{sp}_C-H_C)([t])
     =H^1(\operatorname{sp}_C)([t])
 \in H^1(C_H).
\]

The gate is passed only if the construction proves, rather than assumes:

1. $\operatorname{can}(t_\psi)=0$ in B083's vanishing-cycle term;
2. $q_H\ne0$ in B009/B052's local relation group;
3. $q_H$ is rational type $(0,0)$ after $\mathbf Q(n)$;
4. its image survives both B022 kernels; and
5. its ambient image pairs nontrivially with the prescribed Hodge class.

The displayed difference is not asserted to be canonical before the
collision and reference comparison are constructed. Treating it as an
already-defined specialization map would repeat NG059-NG060. Universally
quantified, the nonzero pairing remains terminal-level content.

B102 proves that isolated target singularities separately admit local
vanishing-polyhedron collapses. NG078 shows this does not construct
$\operatorname{sp}_C$: the distributed detector must first be localized and
the local maps glued to the exterior family. G066 isolates that realization.
