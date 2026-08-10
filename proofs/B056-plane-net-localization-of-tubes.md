---
brick_id: B056
status: PROVED
base_field: C
variety: an arbitrary smooth projective complex 2n-fold in a sufficiently high projective embedding, its dual hypersurface, and a generic projective plane net through the reference hyperplane
smoothness: X is smooth; all hyperplane fibers over the complement of the plane discriminant curve are smooth
projectivity: X, the full hyperplane parameter space, and the plane net are projective
dimension: dim_C X = 2n; the parameter reduction is from projective dimension N at least 3 to a projective plane
codimension: middle codimension n; the dual discriminant is a hypersurface and cuts a curve in the net
coefficient_field: Q
cohomology_theory: primitive singular Betti homology and cohomology, vanishing-homology local systems, monodromy, and tube classes
hodge_type: none created by the reduction; the specified input class may be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B011, Schnell Lemma 3 and Section 3.4 (S023), and the Zariski fundamental-group plane-section theorem (S039)
claim: Every Schnell tube detector for a high-power embedding with nonzero vanishing homology can be represented by the restriction of the hyperplane family to one generic projective plane net, without changing its monodromy-fixed vanishing class or its primitive ambient tube class.
falsifier: a detector pair (g,alpha) whose class in the full smooth hyperplane locus has no representative in a generic plane-section complement or whose tube class changes after applying the inclusion-induced fundamental-group isomorphism
---

# B056 - Every tube detector lives in a plane net

Let \(P\) be the projective space parametrizing hyperplanes and
\(P^{\mathrm{sm}}\subset P\) the smooth-hyperplane locus. Fix a base point
\(H_0\). For the high-power embeddings used in B011, the rational vanishing
homology is nonzero. Schnell's Lemma 3 then proves that

\[
 X^\vee=P\setminus P^{\mathrm{sm}}
\]

is an irreducible hypersurface.

Choose a generic projective plane \(A\simeq\mathbf P^2\) through \(H_0\) and
put \(C=A\cap X^\vee\). The Zariski fundamental-group theorem, used in this
exact setting in Schnell Section 3.4, gives

\[
 \pi_1(A\setminus C,H_0)
 \xrightarrow{\;\sim\;}
 \pi_1(P^{\mathrm{sm}},H_0).
\]

Let \((g,\alpha)\) be any Schnell detector pair, with

\[
 \alpha\in H_{2n-1}^{\mathrm{van}}(X\cap H_0,\mathbf Q),
 \qquad g\alpha=\alpha.
\]

Choose the unique class \(\widetilde g\) in the plane complement mapping to
\(g\). The vanishing local system on \(A\setminus C\) is the pullback of the
full local system, so \(\widetilde g\alpha=\alpha\). The two loops represent
the same class in the full parameter complement. Flat transport in the
pulled-back universal family is therefore the same transport, and the traced
\(2n\)-cycle is unchanged modulo the reference-fiber ambiguity in Schnell's
definition. Hence

\[
 \tau_{\widetilde g}(\alpha)=\tau_g(\alpha)
 \quad\text{in}\quad
 H_{2n}(X,\mathbf Q)/H_{2n}(X\cap H_0,\mathbf Q).
\]

Thus a detector pairing nontrivially with a specified primitive class may be
placed in a two-parameter linear net. This is a parameter-space reduction,
not a collision theorem: it does not put the loop in one pencil, produce a
single singular member, or give a type-\((0,0)\) local relation.
