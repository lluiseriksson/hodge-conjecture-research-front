---
brick_id: B139
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X with fixed very ample H and nodal members of |H^m|
smoothness: X is smooth; hypersurface members have isolated ordinary double points; auxiliary carrier curves may be singular or reducible and are treated through their reduced components and normalizations
projectivity: X, its H-embedding, bounded Hilbert families of curves of H-degree at most three, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1; carrier dimension one
codimension: middle codimension n on X; nodes have codimension 2n and carrier curves have codimension 2n-1
coefficient_field: C for coherent evaluation and first jets; Q for vanishing-cycle relations, with Q(n) after Hodge normalization
cohomology_theory: coherent adjoint cohomology, Cayley-Bacharach postulation, bounded vector bundles on normalized carrier curves, nodal vanishing homology, and local intersection cohomology
hodge_type: every potential nodal relation has rational type (0,0) after Q(n), but the theorem excludes all supports below the stated floor
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B138, S058 Picoco Theorem 3.2, and the bounded-carrier first-jet lemma below
claim: Choose c at least zero such that K_X tensor H^c is globally generated and set t_m=mn-c. For all sufficiently large m, every B026-admissible member of |H^m| with isolated nodes and nonzero adjoint defect or vanishing-cycle relation has at least 4t_m-4=4mn-4c-4 nodes.
falsifier: a sequence m tending to infinity of isolated-nodal members with nonzero adjoint defect and at most 4(mn-c)-5 nodes
---

# B139 — A quartic-linear floor for isolated nodal relations

**Status:** PROVED

Let

\[
 t=t_m=mn-c,\qquad
 F_m=K_X\otimes H^{mn}=(K_X\otimes H^c)\otimes H^t.
\]

B138 shows that a nonzero B026 adjoint defect produces an
inclusion-minimal dependent subset
\(\Gamma\subseteq\Delta_m\) of ambient degree-\(t\) evaluation
functionals. Every coefficient of its unique relation is nonzero, so
\(\Gamma\) is \(\mathrm{CB}(t)\).

Assume toward contradiction that

\[
 |\Delta_m|\le4t-5.
\]

Then \(|\Gamma|\le4(t-1)-1\). Picoco's Theorem 3.2, the \(h=4\) case of
Theorem A, places \(\Gamma\) on a projective curve of degree at most three.

## Uniform first-jet bound for bounded carriers

We first isolate the geometric estimate used for every irreducible carrier.

For each \(e\in\{1,2,3\}\), there is a constant \(b_e=b_e(X,H)\) with the
following property. Let \(D\subset X\) be a reduced irreducible curve of
\(H\)-degree \(e\), let \(\nu:\widetilde D\to D\) be its normalization, and
let a section of \(H^m\) vanish identically on \(D\). If its conormal first
term is not generically zero on \(D\), it can vanish at no more than

\[
 em+b_e
\]

distinct smooth points of \(D\).

Indeed, reduced integral curves of \(H\)-degree at most three form a bounded
union of projective Hilbert strata. Their normalizations have genus zero or
one: the possibilities are lines, conics, twisted cubics, and integral plane
cubics. After a finite stratification, the normalization maps and the vector
bundles \(\nu^\ast\Omega_X\) form bounded families. Hence the maximum degree
of a line subbundle of \(\nu^\ast\Omega_X\) is uniformly bounded by some
\(b_e\).

On the smooth locus, the conormal sheaf injects into \(\Omega_X|_D\).
A generically nonzero first term therefore yields, after pullback and
saturation, a line subbundle

\[
 M\subset\nu^\ast\Omega_X\otimes\nu^\ast H^m.
\]

If the first term vanishes at \(q\) smooth points, its induced nonzero
section of \(M\) has at least \(q\) zeros, so

\[
 q\le\deg M
 \le b_e+m\deg(\nu^\ast H)
 =b_e+em.
\]

The bounded number of singular or component-intersection points is absorbed
by increasing \(b_e\). This proves the uniform estimate without assuming
that the carrier itself is smooth.

## Irreducible cubic carriers

Let \(D\) be an integral degree-three carrier.

If \(D\) is a twisted cubic, projective normality identifies the restricted
degree-\(t\) system with
\(H^0(\mathbf P^1,\mathcal O(3t))\). Thus
\(\mathrm{CB}(t)\) requires at least \(3t+2\) points.

Otherwise \(D\) is an integral plane cubic. It is Gorenstein of arithmetic
genus one with \(\omega_D\simeq\mathcal O_D\), and its plane embedding is
projectively normal. Suppose
\(|\Gamma|\le3t-1\), fix \(p\in\Gamma\), and put
\(Z=\Gamma\setminus\{p\}\). The line bundle

\[
 L=\mathcal O_D(t)(-Z)
\]

has degree at least two. Serre duality gives

\[
 H^1(D,L(-p))
 \simeq H^0(D,L^{-1}(p))^\vee=0,
\]

because \(L^{-1}(p)\) has negative degree. Hence a section of \(L\) can be
chosen nonzero at \(p\), contradicting \(\mathrm{CB}(t)\). Therefore

\[
 |\Gamma|\ge3t
\]

also for an integral plane cubic.

For \(m\gg0\), these points force \(D\subset X\): every fixed homogeneous
generator of \(I_X\) restricts to a section of degree three times its own
degree and has too many zeros. They also force the defining hypersurface
section to vanish on \(D\), because \(3t>3m\).

At all but a uniformly bounded number of singular points, its conormal first
term vanishes at at least \(3t-O(1)\) points. Since

\[
 3t-O(1)=3mn-3c-O(1)>3m+b_3,
\]

the bounded-carrier lemma makes that first term generically zero. Thus
\(D\subset\operatorname{Sing}(Y_m)\), contradicting isolated nodality.

## Reducible cubic carriers

Only the reduced degree partitions \(2+1\) and \(1+1+1\) are new; carriers
of smaller reduced degree were already excluded by B138.

Suppose first that \(C=Q\cup L\), where \(Q\) is a conic and \(L\) a line.
For a point \(p\in\Gamma\cap(L\setminus Q)\), multiply a quadratic
hypersurface containing \(Q\) but not \(p\) by degree-\((t-2)\) forms on
\(L\). The Cayley-Bacharach property forces

\[
 |\Gamma\cap(L\setminus Q)|\ge t.
\]

Similarly, a hyperplane containing \(L\) but not a chosen point of
\(Q\setminus L\), followed by degree-\((t-1)\) interpolation on the conic,
forces

\[
 |\Gamma\cap(Q\setminus L)|\ge2t.
\]

Every component containing a point away from the finite component
intersections therefore contains at least \(e t\) such points, where \(e\)
is its degree.

If the reduced support is three lines, use a degree-two product of
hyperplanes containing the other two lines. Degree-\((t-2)\) interpolation
on the chosen line shows that every occupied component away from the finite
intersection set contains at least \(t\) points.

At least one such component exists for large \(t\), since a reduced cubic
has only a uniformly bounded finite intersection locus while a
\(\mathrm{CB}(t)\) circuit has growing cardinality. For each such component
\(D\) of degree \(e\), high \(m\) gives

\[
 et-O(1)>em+b_e.
\]

The same generator-degree, restriction, and bounded first-jet argument
forces \(D\) into \(\operatorname{Sing}(Y_m)\). Nonreduced cubic carriers
have reduced support of one of the already treated types and give no new
case.

## Conclusion and scope guard

Every degree-at-most-three carrier supplied by S058 is incompatible with an
isolated-nodal member. Therefore

\[
 |\Delta_m|\ge4t_m-4=4mn-4c-4.
\]

The theorem does not treat the boundary \(4t_m-4\), construct its node
scheme, prove the G013 matroid inequalities or ambient rank, evaluate B135,
or construct an algebraic cycle. It is a necessary high-power incidence
bound only. B140 subsequently strengthens the necessary floor to
\(5t_m-10\).
