---
brick_id: B141
status: PROVED
base_field: C
variety: a fixed smooth projective complex 2n-fold X with fixed very ample H and a sequence of nodal members of |H^m|
smoothness: X is smooth; hypersurface members have isolated ordinary double points; bounded-degree carrier curves are reduced before component analysis and may otherwise be singular or reducible
projectivity: X, its H-embedding, carrier curves, Hilbert strata, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1; carrier dimension one
codimension: middle codimension n on X; nodes have codimension 2n and carrier curves have codimension 2n-1
coefficient_field: C for coherent evaluation, curve separation, and first jets; Q for vanishing-cycle relations, with Q(n) after Hodge normalization
cohomology_theory: coherent adjoint cohomology, Cayley-Bacharach postulation, Hilbert-family regularity, Serre duality on curves, nodal vanishing homology, and local intersection cohomology
hodge_type: every potential nodal relation has rational type (0,0) after Q(n), but the theorem only excludes supports of at most linear growth
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B140, S055, S060 Banerjee Theorem 1.13, and the bounded-component lemma in B140
claim: Choose c at least zero such that K_X tensor H^c is globally generated and put t_m=mn-c. For every sequence of B026-admissible isolated-nodal members of |H^m| with nonzero adjoint defect or vanishing-cycle relation, |Delta_m|/t_m tends to infinity. Equivalently, for every fixed integer E at least one there are constants f_N(E) and M_E such that |Delta_m| is at least E t_m-f_N(E) for all m at least M_E.
falsifier: a sequence m tending to infinity of isolated-nodal members with nonzero adjoint defect and |Delta_m| bounded above by C(mn-c)+D for fixed C,D
---

# B141 — Every isolated nodal relation has superlinear support

**Status:** PROVED

Fix the very ample embedding \(X\subset\mathbf P^N\), choose
\(c\ge0\) with \(K_X\otimes H^c\) globally generated, and write

\[
 t=t_m=mn-c.
\]

Let \(Y_m\in|H^m|\) be B026-admissible with isolated nodes
\(\Delta_m\) and nonzero adjoint defect. B138 extracts an
inclusion-minimal dependent subset
\(\Gamma_m\subseteq\Delta_m\) of ambient degree-\(t\) evaluation
functionals. It is an intrinsic \(\mathrm{CB}(t)\) set.

## The arbitrary fixed-degree carrier theorem

Fix an integer \(E\ge1\). Banerjee's Theorem 1.13 gives a positive
increasing function \(f_N\), depending on the ambient dimension \(N\) but
not on \(t\), such that for \(t\gg E\), every
\(\mathrm{CB}(t)\) set \(Z\subset\mathbf P^N\) satisfying

\[
 |Z|<Et-f_N(E)
\]

lies on a projective curve of degree at most \(E\). The theorem is not a
special-family statement: its proof projects a general reduced point set to
lower-dimensional projective spaces, applies the plane result, intersects
the resulting cones, and removes the bounded residual set. Its only
asymptotic hypothesis is \(t\gg E\).

Assume for contradiction that

\[
 |\Delta_m|<Et-f_N(E).
\]

Then the same strict inequality holds for \(\Gamma_m\), so S060 supplies a
carrier \(C_m\) of degree at most \(E\).

## Uniform exclusion of every fixed carrier degree

The bounded-component lemma in B140 was proved for an arbitrary fixed
degree bound, not only for quartics. Applied with this \(E\), it finds an
integral component \(D_m\subset(C_m)_{\mathrm{red}}\) of degree \(e\) and
a constant \(a_E\), independent of \(m\), such that at least

\[
 et-a_E
\]

points of \(\Gamma_m\) lie on the smooth single-component locus of \(D_m\).
The existence of such a component uses the elementary lower bound
\(|\Gamma_m|\ge t+2\); all singular, intersection, and multiplier-zero
points contribute only a constant depending on \(E,N\).

For high \(m\), those points force \(D_m\subset X\): each fixed homogeneous
generator of \(I_X\) has bounded degree, whereas its restriction to
\(D_m\) has more distinct zeros than its degree. They then force the
defining section \(s_m\in H^0(X,H^m)\) to vanish identically on \(D_m\),
because

\[
 et-a_E=e(mn-c)-a_E>em.
\]

Finally, integral curves of degree at most \(E\) form bounded families.
The degrees of line subbundles of their normalized pullbacks of
\(\Omega_X\) have a uniform upper bound \(b_E\). A generically nonzero
conormal first term of \(s_m\) can therefore vanish at no more than
\(em+b_E\) smooth points. But

\[
 et-a_E>em+b_E
\]

for \(m\gg0\), while nodality makes it vanish at every selected point.
Thus the first term vanishes generically, and
\(D_m\subset\operatorname{Sing}(Y_m)\), contradicting isolated nodality.

We have proved that for every fixed \(E\), after a threshold depending on
\((X,H,E)\),

\[
 |\Delta_m|\ge Et_m-f_N(E).
\]

## Superlinear conclusion and scope guard

Divide by \(t_m\) and let \(m\to\infty\). For each fixed \(E\),

\[
 \liminf_{m\to\infty}\frac{|\Delta_m|}{t_m}\ge E.
\]

Since \(E\) is arbitrary,

\[
 \frac{|\Delta_m|}{mn-c}\longrightarrow\infty.
\]

In particular, no \(O(m)\) node-count model can close G013. The theorem does
not provide any effective common threshold as \(E\) varies, exclude
superlinear or polynomially larger node counts, construct a G013 incidence,
prove its ambient rank, evaluate B135, or construct an algebraic cycle. It
is a necessary asymptotic obstruction only. B142 subsequently realizes the
superlinear scale in an anchored product family; it does not weaken this
scope guard for arbitrary varieties or classes.
