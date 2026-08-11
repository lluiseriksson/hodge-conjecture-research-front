---
brick_id: B143
status: PROVED
base_field: C
variety: X=P^n x P^n, the B142 fiber W={p} x P^n, a general Y_m in |I_W tensor O(m,m)|, and the germ of the full (m,m) linear system at Y_m
smoothness: X and W are smooth; Y_m has m^n isolated ordinary double points; every labeled discriminant branch and every intersection stratum in the asserted germ is smooth
projectivity: X, W, Y_m, the linear system, and the moving-fiber incidence are projective; the clean-arrangement assertion is local analytic
dimension: dim_C X=2n, dim_C W=n, dim_C Y_m=2n-1, and the smoothing-tangent rank is R_m=binomial(m+n,n)-n
codimension: W has middle codimension n; a subset of s labeled node branches has intersection codimension min(s,R_m) in the linear-system germ
coefficient_field: C for analytic deformation germs and tangent matroids; Q for the resulting vanishing-cycle relation functional
cohomology_theory: local A1 deformation theory, evaluation matroids, clean discriminant arrangements, rational local intersection cohomology, and Saito's nodal relation pairing
hodge_type: B054 gives the clean local relation channel pure type (0,0) after Q(n); B142's unique relation has a nonzero functional on the primitive Hodge line
cycle_class_map: CH^n(P^n x P^n)_Q -> H^(2n)(P^n x P^n,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B015, B054, B134-B135, B142, and the local A1 discriminant model
claim: At a general B142 divisor, the m^n labeled nodal discriminant branches form a Li clean arrangement with uniform intersection codimension min(s,R_m); every intersection of more than R_m branches is the smooth moving-fiber incidence germ. Consequently B054 applies and the unique local relation functional is nonzero on the primitive Hodge line.
falsifier: a labeled branch that is singular, a subset of at most R_m branches with dependent conormals, a subset of more than R_m branches whose germ differs from the moving-fiber incidence, a nonclean tangent intersection, or vanishing of the resulting unique primitive relation functional
---

# B143 — The fiber witness has a clean nonlinear discriminant

Retain the notation of B142:

\[
 X=\mathbf P^n\times\mathbf P^n,\qquad
 W_p=\{p\}\times\mathbf P^n,\qquad
 A_m=\mathcal O_X(m,m),
\]

and let \(Y=Y_m\) be a general member containing \(W_p\). Its node set
\(Z=\{z_1,\ldots,z_N\}\) has

\[
 N=m^n,\qquad R=\binom{m+n}{n}-n.
\]

B142 proves that the \(A_m\)-evaluation matroid on \(Z\) is the uniform
matroid \(U_{R,N}\). This brick promotes that tangent statement to the
actual nonlinear labeled discriminant germ.

## The labeled nodal branches

Let \(P=|A_m|\), and work in a sufficiently small analytic neighborhood of
\([Y]\). The local deformation of an ordinary double point has one
smoothing coordinate. For each labeled node \(z_i\), the locus \(D_i\)
where its continuation remains singular is therefore a smooth hypersurface
germ. Its conormal at \([Y]\) is the evaluation functional

\[
 \operatorname{ev}_{z_i}:T_{[Y]}P\longrightarrow A_m|_{z_i}.
\]

For a subset \(S\subseteq\{1,\ldots,N\}\) with \(|S|\le R\), uniformity of
the evaluation matroid makes these conormals independent. Hence

\[
 D_S:=\bigcap_{i\in S}D_i
\]

is smooth of codimension \(|S|\), with the branches meeting transversely.

## The moving-fiber incidence

Consider the incidence

\[
 \mathcal F_m=
 \{(p',[Y'])\in\mathbf P^n\times P:
       W_{p'}\subset Y'\}.
\]

Restriction to \(W_{p'}\) is surjective, so \(\mathcal F_m\) is a smooth
projective bundle over \(\mathbf P^n\). Its image in \(P\) has codimension

\[
 h^0(\mathbf P^n,\mathcal O(m))-n
 =\binom{m+n}{n}-n
 =R.
\]

At \((p,[Y])\), a tangent vector \(v\in T_p\mathbf P^n\) lies in the kernel
of the projection differential precisely when contraction of the normal
derivative

\[
 (f_1,\ldots,f_n)\in
 H^0(\mathbf P^n,\mathcal O(m))^{\oplus n}
\]

with \(v\) vanishes identically. The general forms \(f_1,\ldots,f_n\) are
linearly independent, so \(v=0\). The projection is an immersion there,
and its image defines a smooth codimension-\(R\) germ \(F\subset P\).

Every nearby divisor represented by \(F\) contains a nearby fiber and has,
on the open regular-normal-derivative locus, \(N\) nodes labeled by
continuation from \(Z\). Therefore

\[
 F\subseteq D_i\qquad(1\le i\le N).
\]

## All large intersections equal the fiber germ

Let \(S\) have more than \(R\) elements and choose
\(T\subset S\) with \(|T|=R\). The preceding transversality proves that
\(D_T\) is a smooth codimension-\(R\) germ. It contains the smooth
codimension-\(R\) germ \(F\). Inclusion between two smooth analytic germs of
the same dimension is equality, so

\[
 D_T=F.
\]

Since \(F\subseteq D_i\) for every \(i\), it follows that

\[
 D_S=F\qquad(|S|>R).
\]

Thus every labeled intersection is smooth and

\[
 \operatorname{codim}_P D_S=\min\{|S|,R\}.
\]

The same uniform-rank calculation gives

\[
 T_{[Y]}D_S=\bigcap_{i\in S}T_{[Y]}D_i.
\]

Consequently all intersections are clean, and the collection of its
intersection strata is closed under intersection. The nonlinear labeled
discriminant is a Li clean arrangement whose intersection lattice is the
uniform lattice of \(U_{R,N}\). For \(|S|>R\), all nominally different deep
intersections coincide with the moving-fiber stratum \(F\).

## Hodge consequence and scope

B054 now applies without an extra clean-arrangement assumption. It
identifies the degree-one local intersection-cohomology channel with the
dual of the rational vanishing-cycle relation kernel and preserves its pure
type \((0,0)\) after \(\mathbf Q(n)\).

B142 proves that this relation space is one-dimensional and that its
Saito ambient image pairs nontrivially with the one-dimensional primitive
Hodge line. By B134, the canonical local class is exactly that pairing
functional; by B135, its residue-cokernel class is therefore nonzero. This
proves the complete clean multipart detector package for this special
product family.

The proof still uses the moving algebraic fibers \(W_{p'}\) to identify the
deep stratum. It supplies no incidence for an arbitrary smooth projective
variety or a specified Hodge class without a known algebraic carrier.
Therefore it is not progress toward the general rational Hodge Conjecture.
It removes the nonlinear-clean and local-functional doubts from B142 and
isolates the sole remaining general obstruction: unanchored,
class-directed construction on arbitrary \((X,\zeta)\).
