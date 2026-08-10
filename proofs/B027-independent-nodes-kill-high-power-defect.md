---
brick_id: B027
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n with n at least 2, a sufficiently high power A of an ample line bundle, a finite reduced node scheme Delta imposing independent conditions on A, and a nodal member Y_0 in |A|
smoothness: X is smooth; Y_0 has only ordinary double points; Delta is reduced
projectivity: X and Y_0 are projective
dimension: dim_C X = 2n with n >= 2; dim_C Y_0 = 2n-1
codimension: Y_0 has codimension 1; the Hodge application has middle codimension n
coefficient_field: C for coherent evaluation maps and Q for vanishing-cycle relations
cohomology_theory: coherent sheaf cohomology, singular homology, nodal vanishing cycles, and local intersection cohomology
hodge_type: every nodal rational relation would have type (0,0) after Tate twist, but the proved relation space is zero
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026, global generation and Serre vanishing for high powers, and the elementary evaluation-map argument below
claim: For n at least 2 and A sufficiently ample, if the nodes of a nodal member impose independent conditions on A, then the adjoint defect H^1(I_Delta tensor K_X tensor A^n) and hence the nodal vanishing-cycle relation space are zero; therefore fully independent-node members cannot generate nonzero high-power Saito detectors.
falsifier: data satisfying H^1(I_Delta tensor A)=0, global generation of K_X tensor A^(n-1), and H^1(K_X tensor A^n)=0 but with H^1(I_Delta tensor K_X tensor A^n) nonzero
---

# B027 - Independent nodes kill the high-power defect

Let \(A\) be a line bundle on a smooth projective \(2n\)-fold \(X\), with
\(n\ge2\), and let \(\Delta\subset X\) be finite and reduced. Assume

\[
 H^1(X,I_\Delta\otimes A)=0,
 \qquad
 M:=K_X\otimes A^{n-1}\text{ is globally generated},
 \qquad
 H^1(X,K_X\otimes A^n)=0.
\]

The first condition makes the evaluation map

\[
 H^0(X,A)\longrightarrow H^0(\Delta,A|_\Delta)
\]

surjective. Since \(M\) is globally generated and \(\Delta\) is finite, a
section \(t\in H^0(X,M)\) can be chosen nonzero at every point of \(\Delta\):
the sections vanishing at a fixed point form a proper hyperplane, and a
finite union of proper hyperplanes cannot cover \(H^0(X,M)\) over
\(\mathbf C\).

Given arbitrary values
\(u_p\in(K_X\otimes A^n)|_p=(A\otimes M)|_p\), divide by \(t(p)\) to obtain
values in \(A|_p\). Choose \(s\in H^0(X,A)\) interpolating them. Then
\(s\otimes t\) interpolates the original adjoint values. Hence

\[
 H^0(X,K_X\otimes A^n)
 \longrightarrow H^0(\Delta,(K_X\otimes A^n)|_\Delta)
\]

is surjective. The ideal-sheaf exact sequence and the last vanishing
hypothesis give

\[
 H^1(X,I_\Delta\otimes K_X\otimes A^n)=0.
\]

If \(Y_0\in|A|\) is nodal with node scheme \(\Delta\) and lies in the
high-ampleness scope of B026, the defect-number equality now gives

\[
 \operatorname{Rel}(\delta_p)=0.
\]

For \(A=L^m\) with \(L\) ample and \(m\gg0\), global generation of
\(K_X\otimes A^{n-1}\) and the required coherent vanishing hold because
\(n-1>0\). Thus the conclusion applies throughout the high-power regime of
G009 whenever the full node set satisfies B015's independence condition.

## Explicit falsifier for G009

Take \(X=\mathbf P^2\times\mathbf P^2\), let \(h_1,h_2\) be the two
hyperplane classes, and polarize by \(L=\mathcal O(1,1)\). The rational
algebraic Hodge class

\[
 \gamma=h_1^2-h_1h_2+h_2^2
\]

is nonzero and primitive because
\((h_1+h_2)\gamma=0\). For every sufficiently high \(A=L^m\), however, every
fully independent-node member has zero relation space by the preceding
argument. Its Saito detector span is therefore zero and cannot span the
nonzero primitive Hodge line containing \(\gamma\). This disproves G009 as a
universal sufficient theorem. It does not disprove the Hodge Conjecture;
\(\gamma\) is visibly algebraic.

## Re-entry condition

Use a nodal configuration whose **full** node set is dependent while smaller
parts retain enough independence to give a quasi-local normal-crossing
calculation. B009 already permits a partition \(\Delta=J\sqcup K\) with each
part independent. The required relation must cross the partition; demanding
full independence destroys it.
