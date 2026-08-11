---
brick_id: G130
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G129's class-directed reduced node scheme
smoothness: X and Z are smooth; F has isolated ODPs and the full simultaneous-node incidence germ must be reduced and smooth
projectivity: X, H^m, H^(2m), the third infinitesimal neighborhood 3Z, generator spaces, and detector family are projective
dimension: dim X=2n; one double generator F; a 2n-dimensional jet-generator complement U; one nondegenerate Q in Sym^2 U
codimension: construct the global congruence tF=mu_2(Q) modulo I_Z^3 while retaining minimality, adjacent extinction, and all higher obligations
coefficient_field: C for sections, generators, quadratic jets, and Hessians; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent third-neighborhood interpolation, graded ideals, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B200, G013, G090-G129, NG106-NG162, and S065-S073
claim: Construct from arbitrary (X,zeta) G129's minimal augmented generator package together with t in H0(H^m), nowhere zero on Z, and nondegenerate Q in Sym^2 U satisfying tF-mu_2(Q) in H0(I_Z^3 H^(2m)), then close every higher Kuranishi rung and retain the complete rational detector.
falsifier: failure of generator minimality or adjacent extinction, a zero value of t, degenerate Q, failure of the third-neighborhood congruence, extra conditional jets, a nonzero higher Kuranishi obstruction, or failure of any detector clause
---

# G130 — Construct the class-directed quadratic congruence

Starting from arbitrary \((X,\zeta)\), construct the G129 data

\[
 F\in K_m,\qquad
 U\subset J_m,\quad \dim U=2n,\qquad
 J_m/(R_+J)_m=D_m\oplus U
\]

with \(D_m=\mathbf C[F]\), adjacent extinction \(V_{m-1}=0\), and every
node derivative \(U\to G_i\) an isomorphism.

B200 makes the quadratic holonomy and value-image multiplier obligations
equivalent to constructing

\[
 t\in H^0(X,H^m),\qquad t|_Z\ne0,\qquad
 Q\in\operatorname{Sym}^2U\ \text{nondegenerate},
\]

such that

\[
 tF-\mu_2(Q)\in H^0(X,I_Z^3\otimes H^{2m}). \tag{1}
\]

Equation (1) is a finite algebraic condition on the third neighborhood of
\(Z\). It must hold in the full complete system, not merely after deleting
global sections or choosing an analytic slice. The same package must close
G126's cubic and higher Kuranishi ladder and retain the rational
type-\((0,0)\) detector with nonzero specified pairing.

G130 is the current smallest algebraic construction gate inside G129. It
does not claim that the quadratic congruence implies any higher rung or
produces an algebraic cycle.
B201 decomposes the next cubic rung into a pure \(U^3\) tensor and a mixed
\(\overline K\,U^2\) Hessian filter. G131 records their simultaneous
vanishing as the next operational gate; NG163 prevents replacing it by
formal normalization of the central member alone.
B202 identifies the construction of \(F\) itself with a selective
third-neighborhood lift. G132 isolates the required nondegenerate kernel
element, while NG164 excludes making the connecting map vanish wholesale.
