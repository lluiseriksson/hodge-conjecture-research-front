---
brick_id: B140
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X with fixed very ample H and nodal members of |H^m|
smoothness: X is smooth; hypersurface members have isolated ordinary double points; auxiliary carrier curves are reduced after discarding nilpotents and their integral components may be singular
projectivity: X, its H-embedding, the bounded Hilbert families of curves of H-degree at most four, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1; carrier dimension one
codimension: middle codimension n on X; nodes have codimension 2n and carrier curves have codimension 2n-1
coefficient_field: C for coherent evaluation, curve separation, and first jets; Q for vanishing-cycle relations, with Q(n) after Hodge normalization
cohomology_theory: coherent adjoint cohomology, Cayley-Bacharach postulation, Hilbert-family regularity, Serre duality on integral curves, nodal vanishing homology, and local intersection cohomology
hodge_type: every potential nodal relation has rational type (0,0) after Q(n), but the theorem excludes all supports below the stated floor
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B139, S055, S059 Picoco Theorem A with h=5, and the bounded-component lemma proved below
claim: Choose c at least zero such that K_X tensor H^c is globally generated and set t_m=mn-c. For all sufficiently large m, every B026-admissible member of |H^m| with isolated nodes and nonzero adjoint defect or vanishing-cycle relation has at least 5t_m-10=5mn-5c-10 nodes.
falsifier: a sequence m tending to infinity of isolated-nodal members with nonzero adjoint defect and at most 5(mn-c)-11 nodes
---

# B140 — A quintic-linear floor for isolated nodal relations

**Status:** PROVED

Put

\[
 t=t_m=mn-c,
 \qquad
 F_m=K_X\otimes H^{mn}
     =(K_X\otimes H^c)\otimes H^t.
\]

By B138, a nonzero B026 adjoint defect contains an inclusion-minimal
dependent set \(\Gamma\subseteq\Delta_m\) of ambient degree-\(t\)
evaluation functionals. Its unique relation has full support, so
\(\Gamma\) is intrinsically \(\mathrm{CB}(t)\).

Assume

\[
 |\Delta_m|\le5t-11.
\]

Then \(|\Gamma|\le5(t-5+3)-1\). The \(h=5\) case of Picoco's
Theorem A places \(\Gamma\) on a projective curve of degree at most four.

## Uniform bounded-component lemma

Fix \(E\). For every reduced projective curve
\(C\subset\mathbf P^N\) of degree at most \(E\), every integral component
\(D\subset C\) of degree \(e\), and every sufficiently large \(t\), a
\(\mathrm{CB}(t)\) set \(\Gamma\subset C\) has the following alternative:

1. no point of \(\Gamma\) lies on the smooth single-component locus of
   \(D\); or
2. at least

   \[
    et-a_E
   \]

   points of \(\Gamma\) lie there, where \(a_E\) is independent of
   \(C,D,t\), and \(\Gamma\).

Here is a proof, including the uniformity. Reduced curves of bounded degree
in fixed \(\mathbf P^N\), their integral components, their finite singular
and intersection loci, and their incidence pairs form finitely many
projective Hilbert strata. Uniform Castelnuovo-Mumford regularity on these
strata gives integers \(Q,R\) with both properties below.

- There is a form \(P_D\) of degree \(q\le Q\) which vanishes on every
  other component and on the finite singular/intersection locus, but does
  not vanish identically on \(D\).
- The restriction
  \(H^0(\mathbf P^N,\mathcal O(k))\to H^0(D,\mathcal O_D(k))\)
  is surjective for \(k\ge R\).

The first assertion can also be read directly from bounded regularity:
the closed subscheme consisting of the other components and the finite bad
locus does not contain \(D\), so its bounded-degree ideal contains a form
nonzero on \(D\). The zero divisor of \(P_D|_D\) has degree at most \(eQ\).

Let \(S_D\) be the points of \(\Gamma\cap D\) at which \(P_D\ne0\).
They are smooth points belonging only to \(D\). If \(S_D\ne\varnothing\),
fix \(p\in S_D\), put \(Z=S_D\setminus\{p\}\), and set \(k=t-q\).
For \(t\) large, restriction in degree \(k\) is complete. If
\(g=p_a(D)\) and

\[
 |S_D|\le ek-2g+1,
\]

then

\[
 \deg\mathcal O_D(k)(-Z-p)=ek-|S_D|>2g-2.
\]

Serre duality on the integral projective curve therefore gives

\[
 H^1\!\left(D,\mathcal O_D(k)(-Z-p)\right)=0.
\]

Consequently an ambient degree-\(k\) form \(G\) vanishes on \(Z\) but not
at \(p\). The degree-\(t\) form \(P_DG\) vanishes on
\(\Gamma\setminus\{p\}\) but not at \(p\), contradicting
\(\mathrm{CB}(t)\). Hence

\[
 |S_D|\ge e(t-q)-2g+2\ge et-a_E.
\]

Degree bounds give uniform bounds for \(g\) and \(q\), proving the lemma.

Finally, a \(\mathrm{CB}(t)\) set has at least \(t+2\) points: if it had at
most \(t+1\), a product of hyperplanes through all points but one would
separate the last point. Since a degree-at-most-\(E\) reduced curve has at
most \(E\) components and only uniformly many bad points, the second
alternative occurs for at least one component when \(t\) is large.

## Application to the quartic carrier

Apply the lemma with \(E=4\), and choose a component \(D\) of degree \(e\)
with at least

\[
 et-a_4
\]

points of \(\Gamma\) on its smooth single-component locus. A nonreduced
degree-at-most-four carrier has reduced degree at most three unless it was
reduced already. Nilpotents do not alter the point set, so the former case
is excluded by B139 and the latter is covered here.

For \(m\gg0\), the component lies in \(X\). Indeed, take fixed homogeneous
generators of \(I_X\). A generator of degree \(d\) restricts to a section of
degree \(ed\) on \(D\), but it vanishes at \(et-a_4>ed\) distinct smooth
points. Thus every generator vanishes identically on \(D\).

The defining section \(s_m\in H^0(X,H^m)\) likewise restricts to degree
\(em\) on \(D\) and vanishes at all these nodes. Since \(n\ge2\),

\[
 et-a_4=e(mn-c)-a_4>em,
\]

so \(s_m|_D=0\).

It remains to audit first jets uniformly. Integral components of
degree at most four form bounded Hilbert families. After normalization and
finite stratification, the bundles \(\nu^*\Omega_X\) are bounded; hence the
degrees of their line subbundles have a common upper bound \(b_e\). If the
conormal first term of \(s_m\) is generically nonzero on \(D\), saturation
on the normalization gives a line subbundle of

\[
 \nu^*\Omega_X\otimes\nu^*H^m
\]

of degree at most \(b_e+em\). Its section cannot vanish at more than that
many distinct smooth points. But nodality makes the first term vanish at
at least \(et-a_4\) points, and

\[
 et-a_4=e(mn-c)-a_4>em+b_e
\]

for high \(m\). The first term is therefore generically zero. Together with
\(s_m|_D=0\), this puts the positive-dimensional curve \(D\) inside
\(\operatorname{Sing}(Y_m)\), contradicting isolated nodality.

## Conclusion and scope guard

Every degree-at-most-four carrier supplied by S059 is incompatible with the
assumed isolated-nodal defect. Therefore

\[
 |\Delta_m|\ge5t_m-10=5mn-5c-10.
\]

This theorem does not treat the boundary \(5t_m-10\), construct a node
scheme, establish either G013 matroid/rank condition, evaluate the B135
residue quotient, or construct an algebraic cycle. It is only a necessary
high-power incidence bound.
