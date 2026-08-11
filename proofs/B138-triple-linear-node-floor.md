---
brick_id: B138
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X with a fixed very ample line bundle H and nodal members of |H^m|
smoothness: X is smooth; the tested hypersurface members have only isolated ordinary double points with reduced node scheme Delta
projectivity: X, its H-embedding, the Hilbert schemes of H-lines and H-conics, and the hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1
codimension: middle codimension n on X; nodes have codimension 2n and the theorem bounds their total cardinality
coefficient_field: C for evaluation maps and Q for vanishing-cycle relations, with Q(n) after Hodge normalization
cohomology_theory: coherent adjoint cohomology, projective Cayley-Bacharach postulation, nodal vanishing homology, and local intersection cohomology
hodge_type: any surviving nodal relation has rational type (0,0) after Q(n), but the theorem forces its support above the stated cardinality floor
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B137, S057 Picoco Theorem 3.1, and the carrier first-jet argument below
claim: Choose c at least zero such that K_X tensor H^c is globally generated and put t_m=mn-c. For all sufficiently large m, every B026-admissible member of |H^m| with isolated nodes and nonzero adjoint defect or vanishing-cycle relation has at least 3t_m=3mn-3c nodes.
falsifier: a sequence m tending to infinity of isolated-nodal members with nonzero adjoint defect and at most 3(mn-c)-1 nodes
---

# B138 — A triple-linear floor for isolated nodal relations

**Status:** PROVED

Retain B137's notation

\[
 A_m=H^m,\qquad F_m=K_X\otimes A_m^n
 =(K_X\otimes H^c)\otimes H^{t_m},\qquad t_m=mn-c,
\]

where \(K_X\otimes H^c\) is globally generated.

## Extract the intrinsic Cayley-Bacharach circuit

For \(m\gg0\), a nonzero B026 adjoint defect makes the
\(F_m\)-evaluation map on the reduced node set \(\Delta_m\) nonsurjective.
Exactly as in B137, multiplication by a section of
\(K_X\otimes H^c\) nonzero at every node shows that the ambient evaluation

\[
 H^0(\mathbf P^N,\mathcal O(t_m))
 \longrightarrow \mathbf C^{\Delta_m}
\]

is not surjective.

Choose an inclusion-minimal dependent subset
\(\Gamma_m\subseteq\Delta_m\). Its evaluation functionals have a unique
relation up to scale,

\[
 \sum_{p\in\Gamma_m}\lambda_p\operatorname{ev}_p=0,
 \qquad \lambda_p\ne0.
\]

Therefore \(\Gamma_m\) is \(\mathrm{CB}(t_m)\): if a degree-\(t_m\) form
vanishes on \(\Gamma_m\setminus\{p\}\), the displayed relation forces it to
vanish at \(p\) as well.

Suppose

\[
 |\Delta_m|\le3t_m-1.
\]

Then \(|\Gamma_m|\le3t_m-1\), and Picoco's Theorem 3.1, the \(h=3\)
case of Theorem A, places \(\Gamma_m\) on a projective curve of degree at
most two.

## Degree-one carriers

If \(\Gamma_m\) is supported on a line \(\ell\), the elementary
Cayley-Bacharach lower bound gives

\[
 |\Gamma_m|\ge t_m+2.
\]

For high \(m\), these points force \(\ell\subset X\): every fixed
homogeneous generator of \(I_X\) has more zeros on \(\ell\) than its degree.
B137's uniform normal-bundle constant \(b_1\) for \(H\)-lines then gives

\[
 t_m+2>m+b_1.
\]

The restriction of the hypersurface section and all its conormal first
derivatives vanish identically along \(\ell\). Thus
\(\ell\subset\operatorname{Sing}(Y_m)\), contradicting isolated nodality.

The same conclusion handles a nonreduced degree-two carrier supported on a
line.

## Reducible degree-two carriers

Suppose the reduced carrier is \(L_1\cup L_2\), with the lines either
intersecting or skew, and \(\Gamma_m\) meets both away from their possible
intersection. Put

\[
 \Gamma_i=\Gamma_m\cap(L_i\setminus L_{3-i}).
\]

If \(0<|\Gamma_i|\le t_m\), choose \(p\in\Gamma_i\). A hyperplane through
\(L_{3-i}\) but not \(p\), multiplied by
\(|\Gamma_i|-1\) hyperplanes through the other points of \(\Gamma_i\) but
not \(p\), and then by general hyperplanes to reach degree \(t_m\), vanishes
on \(\Gamma_m\setminus\{p\}\) but not at \(p\). This contradicts
\(\mathrm{CB}(t_m)\). Hence

\[
 |\Gamma_i|\ge t_m+1
\]

for every occupied component. One such line contains at least \(t_m+1\)
nodes. Since \(t_m+1>m+b_1\) for \(n\ge2\) and \(m\gg0\), the line is again
contained in the singular locus.

## Irreducible conic carrier

The remaining carrier is a smooth plane conic
\(C\simeq\mathbf P^1\) with

\[
 H|_C\simeq\mathcal O_{\mathbf P^1}(2).
\]

Conics are projectively normal, so degree-\(t_m\) ambient forms restrict to
the complete system \(H^0(\mathbf P^1,\mathcal O(2t_m))\).
The Cayley-Bacharach property therefore requires

\[
 |\Gamma_m|\ge2t_m+2.
\]

For high \(m\), this exceeds twice the generator-degree bound for \(I_X\),
so \(C\subset X\).

There is a uniform constant \(b_2\) for smooth \(H\)-conics in \(X\) such
that every summand \(\mathcal O(a_j)\) of \(N_{C/X}\) has
\(-a_j\le b_2\). Indeed, the conics form a bounded projective Hilbert
family,

\[
 N_{C/X}\hookrightarrow N_{C/\mathbf P^N}
 \simeq\mathcal O_{\mathbf P^1}(4)
 \oplus\mathcal O_{\mathbf P^1}(2)^{\oplus(N-2)},
\]

and \(\deg N_{C/X}=-K_X\cdot C-2\) takes finitely many values on that
family.

The hypersurface restriction has degree \(2m\), and its conormal first
derivative has summands of degree at most \(2m+b_2\). But

\[
 2t_m+2=2mn-2c+2>2m+b_2
\]

for \(n\ge2\) and \(m\gg0\). Thus both vanish identically on \(C\), forcing
\(C\subset\operatorname{Sing}(Y_m)\), again impossible.

## Conclusion and scope guard

Every degree-at-most-two carrier supplied by S057 contradicts isolated
nodality. Hence

\[
 |\Delta_m|\ge3t_m=3mn-3c.
\]

The constants and the high-power threshold depend on \((X,H)\). B138 does
not treat the boundary \(3t_m\), construct any such node scheme, prove the
two-matroid inequalities, evaluate the B135 quotient, or construct an
algebraic cycle. It is a necessary cardinality theorem, not progress toward
algebraicity by itself.
