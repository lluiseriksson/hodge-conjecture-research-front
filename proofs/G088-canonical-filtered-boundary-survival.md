---
brick_id: G088
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2r-fold X and its universal sufficiently high hyperplane incidence over the full parameter space P
smoothness: X is smooth; the coefficient variation is smooth on P_sm and minimally extended across the discriminant
projectivity: X and P are projective
dimension: dim_C X=2r with r at least 2; hyperplane dimension 2r-1; dim P=d
codimension: middle codimension r on X; required parameter support has codimension at least two
coefficient_field: Q, with complexification for filtered de Rham calculations
cohomology_theory: rational intersection cohomology, Hodge modules, filtered D-modules, stalk spectral sequences, and the B128 hypercohomology edge map
hodge_type: primitive rational type (r,r), normalized to (0,0) after Q(r)
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no algebraic representative may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B009, B012, B026-B028, B128, B130-B145, G008, G013, G086-G087, G089-G091, NG103-NG116, S009, S021-S024, S037, S053, S055-S060
claim: For every nonzero primitive rational Hodge class zeta, for some sufficiently high power and some discriminant point p, the canonical projective filtered section h_m(zeta) survives the filtered stalk spectral sequence to the nonzero rational ordinary class e_m(s_m(zeta))_p in H^(-d+1)(IC(V_m))_p; at a clean nodal point this class is the dual relation functional beta |-> <zeta,gamma_beta>.
falsifier: a smooth projective complex 2r-fold and nonzero primitive rational Hodge class for which the canonical section is killed in every discriminant stalk for every sufficiently high power
---

# G088 — Canonical filtered boundary survival

**Status:** EXPLORATORY — exact residual mechanism for G086

B131 proves that the rational first-Leray incidence class is nonzero. B132
then constructs, on the full projective parameter space and without any
splitting choice, its nonzero filtered realization

\[
 h_m(\zeta)\in
 H^0\!\left(P_m,
 \mathcal H^{-d_m+1}
 \operatorname{gr}_{-r}^F\operatorname{DR}(M_m)\right).
\]

Prove that for some \(m\gg0\) and \(p\) on the discriminant, this specified
class is not killed by the filtered stalk differentials and yields

\[
 0\ne e_m(s_m(\zeta))_p
 \in \mathcal H^{-d_m+1}(IC(V_m))_p.
\]

The survivor must be checked in the rational realization after the Tate
twist and in the full-support minimal-extension constituent. A complex
associated-graded survivor in a proper-support summand is not sufficient.

## Exact obstruction

On \(P_m^{\rm sm}\), B130 proves

\[
 \mathcal H^{-d_m+1}\operatorname{DR}(M_m)=0,
\]

so cancellation of \(h_m(\zeta)\) is mandatory there. At a generic smooth
point of the discriminant, B008 gives a zero rational local IC channel. Any
survivor must therefore occur on a support stratum of codimension at least
two, consistently with B012.

B133-B134 compute the minimal clean nodal case. At a quasi-local
normal-crossing point with vanishing cycles \(\delta_i\), put

\[
 R_p=\ker\!\left(\mathbf Q^r\longrightarrow
 H_{2r-1}(X_s,\mathbf Q(r))\right).
\]

The ordinary cohomological target is \(R_p^\vee\), and the specified class
is

\[
 \lambda_{\zeta,p}(\beta)=\langle\zeta,\gamma_\beta\rangle.
\]

For two branches this target is nonzero only when the two nonzero vanishing
cycles are proportional. NG106 therefore closes the generic transverse
double-node shortcut. G088 may still use a class-directed two-cycle relation
or a higher multipart relation, but it must prove
\(\lambda_{\zeta,p}(\beta)\ne0\) for an actual relation. NG107 forbids
replacing this functional by a canonically selected relation vector.

B135 resolves the filtered local class into logarithmic-residue coordinates.
If the residues of a local normal-function lift are \(a_i\delta_i\), then

\[
 e_m(s_m(\zeta))_p
 =[a]\in\operatorname{coker}\Delta^\ast
 \simeq(\ker\Delta)^\vee.
\]

At a proportional two-branch point \(\delta_2=c\delta_1\), the exact
survival condition is

\[
 c a_1-a_2\ne0.
\]

NG108 shows why nonzero individual residues do not suffice: \(q(1,c)\) is a
nonzero residue vector but a Koszul coboundary. G089 isolated construction
of a two-branch residue mismatch as the smallest clean restricted attack.
B136 now proves that every fixed bound on the number of nodes has zero
relation target in all sufficiently high powers. Consequently G089 is
NO-GO as a scalable route, NG109 excludes every bounded-node replacement,
and G013 is the next clean-nodal construction gate: its multipart node count
must grow and its B135 residue-cokernel class must be nonzero. B137/NG110
quantify the first condition: for \(A_m=H^m\), isolated nodal defect requires
a node count superlinear in \(mn-c\) once \(K_X\otimes H^c\) is globally generated.

Thus G088 requires an actual codimension-two-or-higher calculation of the
minimal-extension filtered differentials. Global nonvanishing, Nori
connectivity, projective strictness, and the existence of the Higgs section
do not decide it. NG115 makes the last warning geometric: the Higgs section
is constant and nonzero, so neither its zero locus nor its as-yet-unproved
ordinary survival locus constructs G090's saturated nodal stratum.

By B128, a nonzero survivor is exactly \(e_m(s_m(\zeta))\ne0\), hence G086
and G008. Under universal quantification B007 shows that this remains
terminal-equivalent to the rational Hodge Conjecture; G088 is not counted as
partial resolution of the terminal conjecture.
