---
brick_id: B137
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X with a fixed very ample line bundle H and nodal members of |H^m|
smoothness: X is smooth; the tested hypersurface members have only isolated ordinary double points with reduced node scheme Delta
projectivity: X, its H-embedding, the Fano scheme of H-lines, and the hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1
codimension: middle codimension n on X; every node has codimension 2n and the quantitative bound concerns the total node count
coefficient_field: C for evaluation maps and Q for vanishing-cycle relations, with Q(n) after Hodge normalization
cohomology_theory: coherent cohomology, projective postulation, nodal vanishing homology, and local intersection cohomology
hodge_type: every potential nodal relation has rational type (0,0) after Q(n), but the theorem forces its node support above a linear floor
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B027, B029, B136, S056 Eisenbud-Green-Harris Proposition 1, and the projective arguments below
claim: Choose c at least zero such that K_X tensor H^c is globally generated and put t_m=mn-c. For all sufficiently large m, every nodal member of |H^m| with isolated nodes and nonzero adjoint defect, equivalently a nonzero B026 vanishing-cycle relation, has at least 2t_m+2=2mn-2c+2 nodes.
falsifier: a sequence m tending to infinity of isolated-nodal members with nonzero adjoint defect and at most 2(mn-c)+1 nodes
---

# B137 — A linear floor for high-power nodal relations

**Status:** PROVED

Fix a very ample line bundle \(H\) and use it to embed
\(X\hookrightarrow\mathbf P^N\). Choose \(c\ge0\) such that

\[
 B:=K_X\otimes H^c
\]

is globally generated. Put

\[
 A_m=H^m,\qquad F_m=K_X\otimes A_m^n,\qquad t_m=mn-c,
\]

so that \(F_m=B\otimes H^{t_m}\).

## From adjoint defect to projective postulation

Let \(Y_m\in|A_m|\) have reduced node set \(\Delta_m\) of cardinality \(r\).
For \(m\gg0\), Serre vanishing gives \(H^1(X,F_m)=0\). If the B026 adjoint
defect is nonzero, the evaluation map

\[
 H^0(X,F_m)\longrightarrow H^0(\Delta_m,F_m|_{\Delta_m})
\]

is not surjective.

Global generation of \(B\) permits a section \(u\in H^0(X,B)\) nonzero at
every point of \(\Delta_m\): avoid the finite union of evaluation
hyperplanes. Multiplication by \(u\) embeds the degree-\(t_m\) ambient
polynomial evaluations, up to invertible diagonal rescaling, in the
\(F_m\)-evaluation map. Hence

\[
 H^0(\mathbf P^N,\mathcal O(t_m))\longrightarrow\mathbf C^{\Delta_m}
\]

also fails to be surjective.

## Small dependent sets contain a long line

We use the following consequence of Eisenbud-Green-Harris Proposition 1.

> If \(r\le2t+1\) distinct points of \(\mathbf P^N\) fail to impose
> independent conditions on degree-\(t\) forms, at least \(t+2\) of them are
> collinear.

For completeness, project generically to \(\mathbf P^2\), injectively on the
finite set. Pullback of plane forms shows that every such projection still
fails degree-\(t\) independence. Proposition 1 gives \(t+2\) collinear
projected points; its exceptional conic case requires exactly \(2t+2\)
points and is absent here. There are only finitely many subsets of size
\(t+2\). If no original subset were collinear, each subset would remain
noncollinear for a nonempty open set of projections, and the intersection of
these finitely many opens would contradict the plane theorem.

Assume now, toward contradiction, that \(r\le2t_m+1\). A line
\(\ell\subset\mathbf P^N\) contains at least \(t_m+2\) nodes. Fix a degree
bound \(g_X\) for homogeneous generators of \(I_X\). Once \(t_m+2>g_X\),
each generator restricts to a polynomial on \(\ell\) with more zeros than its
degree. Thus every generator vanishes identically on \(\ell\), so

\[
 C:=\ell\subset X,\qquad H|_C=\mathcal O_{\mathbf P^1}(1).
\]

## Too many singular points force the whole line to be singular

There is a constant \(b_X\) uniform over all \(H\)-lines \(C\subset X\)
such that, if

\[
 N_{C/X}\simeq\bigoplus_{j=1}^{2n-1}\mathcal O_{\mathbf P^1}(a_j),
\]

then \(-a_j\le b_X\). Indeed,
\(N_{C/X}\hookrightarrow N_{C/\mathbf P^N}\simeq
\mathcal O(1)^{\oplus(N-1)}\), so \(a_j\le1\). The degree
\(\sum a_j=-K_X\cdot C-2\) takes only finitely many values on the finitely
many components of the projective Fano scheme of \(H\)-lines, giving the
uniform lower bound.

Let \(s_m\) define \(Y_m\). Since \(t_m+2>m\), its restriction
\(s_m|_C\in H^0(C,\mathcal O_C(m))\) is zero. Its first normal term is then

\[
 \overline{d s_m}\in
 H^0\!\left(C,N_{C/X}^{\vee}\otimes\mathcal O_C(m)\right)
 =\bigoplus_j H^0(C,\mathcal O_C(m-a_j)).
\]

All components vanish at the \(t_m+2\) selected nodes. For \(m\gg0\),

\[
 t_m+2=mn-c+2>m+b_X,
\]

so every component is identically zero. Therefore both \(s_m\) and its
first derivative vanish along \(C\), and

\[
 C\subset\operatorname{Sing}(Y_m).
\]

This contradicts isolated nodality. Consequently

\[
 |\Delta_m|\ge2t_m+2=2mn-2c+2.
\]

## Scope guard

The constant \(c\), and the threshold hidden in \(m\gg0\), depend on
\((X,H)\). The theorem does not exclude the boundary cardinality
\(2t_m+2\): Eisenbud-Green-Harris has a conic alternative exactly there.
It constructs no nodal member, no residue class, and no algebraic cycle.
It strengthens B136 only by giving a necessary linear node floor. B138
subsequently resolves the conic boundary and strengthens the floor to
\(3t_m\).
